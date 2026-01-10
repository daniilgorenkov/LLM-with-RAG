import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(sys.path)
import json
from collections import defaultdict
import os
from config import Paths, LLMConfig

import random
import difflib
import re
from rag.generator.llm_client import LLMClient
from tqdm import tqdm
import pymorphy3
from utils.custom_logger import set_logger

logger = set_logger(Paths.LOG_FILE)


class QADatasetBuilder:

    OPEN_AI_ANSWER_RULES = """
    Вопрос:
    Недостаточно данных

    Ответ:
    Недостаточно данных

    ФОРМАТ ОТВЕТА (строго, без пояснений):

    Вопрос:
    ...

    Ответ:
    ...
    """

    OFFLINE_LLM_ANSWER_RULES = """
    На основе приведённого контекста сформулируй
    ОДИН КОНКРЕТНЫЙ технический вопрос, ответ на который
    ПРЯМО и ЯВНО содержится в тексте.

    Вопрос и ответ пометь как "Вопрос:" и "Ответ:"
    """
    PROMPT_TEMPLATE = """
    Ты — эксперт в области диагностики дефектов поверхности катания железнодорожных колес.

    Сформулируй ОДИН технический вопрос и ОДИН краткий ответ
    СТРОГО на основе приведённого контекста.

    Ключевые технические термины:
    - дефект поверхности катания
    - динамические напряжения
    - колесная пара
    - поверхность катания
    - модель машинного обучения
    - нейронная сеть
    - ползун
    - выщербина
    - неравномерный прокат
    - изношенный гребень
    - рельсы
    - тензометрические датчики
    - вертикальная сила в системе колесо-рельс
    - боковая сила в системе колесо-рельс

    Допустимые типы вопросов:
    - о числовых порогах и значениях
    - о классификации дефектов
    - о критериях принятия решения
    - о параметрах измерения
    - о ссылках на таблицы, нормы, стандарты

    Запрещено НИ В КОЕМ СЛУЧАЕ начинать вопрос со слов:
    какие, как, каким образом, каким, почему, зачем, в чём заключается, опиши, расскажи, объясни, в каких случаях

    Разрешены только вопросы вида:
    • Какое значение...?
    • Каков порог...?
    • При каком условии...?
    • Какой интервал считается...?
    • Чему равно максимально допустимое...?
    • Как классифицируется дефект при ... ?
    • Какой критерий используется для ... ?

    Примеры правильных пар:

    Вопрос: Какой интервал скорости является критическим для автоматической передачи данных?
    Ответ: От 45 до 50 м/с

    Вопрос: Какова предельная величина неравномерного проката для колес пассажирских вагонов?
    Ответ: 0,5 мм

    Вопрос: При каком значении вертикальной силы возникает риск выщербины?
    Ответ: Более 120 кН

    Вопрос: В каком документе указаны пороги вертикальной силы в системе колесо-рельс?
    Ответ: ГОСТ 34759-2021

    Вопрос: До какого значения вертикальной силы допускается эксплуатация колесной пары?
    Ответ: До 350кН, согласно ГОСТ 34759-2021

    ЕСЛИ информации недостаточно, напиши:

    {answer_rules}

    Контекст:
    {contexts}
    """

    N_SAMPLES: int = 2
    MAX_CONTEXT_CHARS = 1200

    def __init__(
        self,
        max_contexts: int = 3,
    ):
        self.max_contexts = max_contexts
        self.llm_asker = LLMClient(online=LLMConfig.ONLINE)
        self.morph = pymorphy3.MorphAnalyzer()

    def lemmatize_words(self, text: str):
        """
        Возвращает множество лемм слов длиной >=5 букв из текста.
        """

        words = re.findall(r"[а-яa-z]{5,}", text.lower())
        lemmas = set()
        for w in words:
            lemma = self.morph.parse(w)[0].normal_form  # берём наиболее вероятную лемму
            if len(lemma) >= 5:
                lemmas.add(lemma)
        return lemmas

    def is_good_qa(self, question: str, answer: str, context: str) -> bool:
        # 1. Пустые поля
        if not question or not answer:
            return False

        q = question.strip()
        a = answer.strip()
        c = context.strip()

        # 2. Слишком коротко / слишком длинно
        if len(q) < 10 or len(a) < 5:
            return False

        if len(a) > len(c) * 0.8:
            return False

        # 3. Ответ почти копия контекста
        ratio = difflib.SequenceMatcher(None, a.lower(), c.lower()).ratio()
        if ratio > 0.91 and len(a) / max(1, len(c)) > 0.75:
            return False

        # 4. Признаки обрезки
        if "..." in a:
            return False

        if re.search(r"[а-яa-z]{2,}$", a) is None:
            return False

        BAD_QUESTION_STARTS = [
            "какие методы",
            "как используются",
            "какие системы",
            "каким образом применяется",
        ]

        if any(q.lower().startswith(p) for p in BAD_QUESTION_STARTS):
            return False

        # 5. Эвристика: хотя бы часть ответа есть в контексте
        answer_lemmas = self.lemmatize_words(a)
        context_lemmas = self.lemmatize_words(c)

        overlap = answer_lemmas.intersection(context_lemmas)

        if len(overlap) < 2:
            return False

        return True

    def load_chunks(self, path: str):
        chunks = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                chunks.append(json.loads(line))
        return chunks

    def group_by_doc(self, chunks: list):
        grouped = defaultdict(list)
        for c in chunks:
            grouped[c["metadata"]["doc_id"]].append(c)
        return grouped

    def extarct_keywords(self, text: str, top_k=10):
        lemmas = self.lemmatize_words(text)
        return list(lemmas)[:top_k]

    def build_context(self, chunks):
        texts = []
        total_len = 0

        for c in chunks:
            text = c["text"].strip()
            if total_len + len(text) > self.MAX_CONTEXT_CHARS:
                break
            texts.append(text)
            total_len += len(text)

        return "\n\n".join(texts)

    def select_good_start_idx(self, doc_chunks, n_select=4):
        scores = []
        for i in range(len(doc_chunks)):
            text = doc_chunks[i]["text"]
            # Простая эвристика "ценности" чанка
            num_score = len(re.findall(r"\d+[,.]?\d*", text)) * 3
            key_score = sum(1 for kw in ["мм", "кН", "ГОСТ", "порог", "критическ", "допуск"] if kw in text.lower())
            length_score = len(text) / 300
            total = num_score + key_score + length_score
            scores.append((total, i))

        scores.sort(reverse=True)
        good_indices = [idx for _, idx in scores[:n_select]]

        if not good_indices:
            return random.randint(0, len(doc_chunks) - self.max_contexts)

        # Берём самый ценный и пытаемся взять соседние
        best = good_indices[0]
        start = max(0, best - random.randint(0, 2))
        return start

    def build_qa_samples(self, chunks: list):
        samples = []

        grouped = self.group_by_doc(chunks)

        for doc_id, doc_chunks in grouped.items():
            chunk_l = len(doc_chunks)
            if chunk_l < self.max_contexts:
                start_idx = 0
            else:
                start_idx = self.select_good_start_idx(doc_chunks)

            contexts = doc_chunks[start_idx : start_idx + self.max_contexts]
            texts = self.build_context(contexts)
            keywords = self.extarct_keywords(texts)
            texts = "Ключевые технические термины:\n" + ", ".join(keywords) + "\n\n" + texts

            if LLMConfig.ONLINE:
                prompt = self.PROMPT_TEMPLATE.format(answer_rules=self.OPEN_AI_ANSWER_RULES, contexts=texts)
            else:
                prompt = self.PROMPT_TEMPLATE.format(answer_rules=self.OFFLINE_LLM_ANSWER_RULES, contexts=texts)

            qa = self.llm_asker.ask_direct_llm(prompt)

            if isinstance(qa, dict):
                # del chineese chars
                qa["question"] = re.sub(r"[\u4e00-\u9fff]+", "", qa["question"])
                qa["answer"] = re.sub(r"[\u4e00-\u9fff]+", "", qa["answer"])

                if not self.is_good_qa(qa["question"], qa["answer"], texts):
                    logger.debug(f"Bad qa: question:{qa['question']}, answer: {qa['answer']}")
                    continue

                sample = {
                    "question": qa["question"],
                    "answer": qa["answer"],
                    "contexts": texts,
                    "sources": [doc_id],
                }

            elif qa is not None:
                sample = {
                    "text": qa,
                    "contexts": texts,
                    "sources": [doc_id],
                }
            else:
                sample = None

            if sample:
                samples.append(sample)

        return samples

    def save(self, samples: list, out_path: str):
        if not samples:
            return  # Nothing to save

        # Ensure directory exists
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        # Append new samples (creates file if missing)
        with open(out_path, "a", encoding="utf-8") as f:
            for s in samples:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")

    def build(self, num_samples: int = 100):

        for _ in tqdm(range(num_samples), desc="generating qa dataset"):
            chunks_list = os.listdir(Paths.CHUNKS)
            random_chunk = random.choice(chunks_list)
            sample_chunk = self.load_chunks(os.path.join(Paths.CHUNKS, random_chunk))
            samples_raw = self.build_qa_samples(sample_chunk)
            self.save(samples_raw, os.path.join(Paths.DATA, "qa_dataset.jsonl"))

    def qa_to_lora_format(self):

        with open(Paths.QA_DATASET, "r", encoding="utf-8") as fin, open(
            Paths.QA_LORA_DATASET, "w", encoding="utf-8"
        ) as fout:

            for line in fin:
                s = json.loads(line)

                instruction = (
                    "Ответь на вопрос строго на основе приведённого контекста. "
                    "Если информации недостаточно — напиши: Недостаточно данных."
                )

                input_text = f"Контекст:\n{s['contexts']}\n\nВопрос:\n{s['question']}"
                output_text = s["answer"]

                fout.write(
                    json.dumps(
                        {"instruction": instruction, "input": input_text, "output": output_text}, ensure_ascii=False
                    )
                    + "\n"
                )


if __name__ == "__main__":
    builder = QADatasetBuilder()
    builder.build(num_samples=20)
    builder.qa_to_lora_format()
