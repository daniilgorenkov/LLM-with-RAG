import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import json
from collections import defaultdict
import random
import difflib
import re
from tqdm import tqdm
from rag.generator.llm_client import LLMClient
from config import Paths, LLMConfig
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
    Ты — строгий эксперт в диагностике дефектов поверхности катания железнодорожных колес.
    Отвечай ТОЛЬКО на русском языке, ТОЛЬКО кириллицей (кроме названий стандартов и аббревиатур).

    СТРОГО СЛЕДУЙ ПРАВИЛАМ:

    1. Сформулируй РОВНО ОДИН технический вопрос и ОДИН краткий ответ.
    2. Вопрос ОБЯЗАТЕЛЬНО начинается с одного из вариантов:
       • Какое значение...?
       • Каков порог...?
       • При каком значении...?
       • Чему равно максимально допустимое...?
       • Как классифицируется дефект...?
       • В каком документе...?
       • Согласно какому ГОСТ...?
       ЗАПРЕЩЕНО начинать с: какие, как, каким образом, почему, зачем, опиши, расскажи и т.п.

    3. Ответ — максимум 1–2 предложения. Только факт из контекста.
    4. Никогда не придумывай числа, пороги, названия документов — только то, что явно есть в тексте.
    5. Если нужной информации нет — отвечай строго:
       Вопрос: Недостаточно данных
       Ответ: Недостаточно данных

    Примеры правильных пар (следуй этому стилю):

    Вопрос: Какой диапазон толщины гребня колеса в эксплуатации?
    Ответ: От 24 до 33 м.

    Вопрос: В каком документе указаны пороги вертикальной силы?
    Ответ: ГОСТ 34759-2021.

    Вопрос: До какого значения допускается вертикальная сила в системе колесо-рельс?
    Ответ: До 350 кН, согласно ГОСТ 34759-2021.

    Контекст:
    {contexts}
    """

    N_SAMPLES: int = 3
    MAX_CONTEXT_CHARS = 1200  # немного увеличили — современные модели нормально справляются

    def __init__(self, max_contexts: int = 3):
        self.max_contexts = max_contexts
        self.llm_asker = LLMClient(online=LLMConfig.ONLINE)
        self.morph = pymorphy3.MorphAnalyzer()

    def lemmatize_words(self, text: str):
        words = re.findall(r"[а-яa-z]{5,}", text.lower())
        lemmas = set()
        for w in words:
            lemma = self.morph.parse(w)[0].normal_form
            if len(lemma) >= 5:
                lemmas.add(lemma)
        return lemmas

    def is_good_qa(self, question: str, answer: str, context: str) -> bool:
        q = question.strip().lower()
        a = answer.strip()

        if not q or not a:
            return False

        # Запрещаем "плохие" начала только если ответ длинный/обобщающий
        bad_starts = [
            "какие методы",
            "какие технологии",
            "какие системы",
            "какие существуют",
            "какие данные",
            "какие параметры",
            "какие факторы",
        ]

        if any(q.startswith(b) for b in bad_starts) and len(a.split()) > 15:
            return False  # отсекаем только если ответ слишком длинный

        # Разрешаем "какие значения", "какие пороги", "какие единицы" и т.п.
        good_starts = ["какие значения", "какие пороги", "какие единицы", "какие документы", "какие размеры"]
        if any(q.startswith(b) for b in good_starts):
            # Дополнительно проверяем, что ответ содержит число/единицу/ГОСТ
            if re.search(r"\d|мм|кн|гост|м|кгс|нм", a.lower()):
                return True

        # Остальные правила (краткость, отсутствие ...)
        if "..." in a:
            return False

        if re.search(r"[а-яa-z]{2,}$", a) is None:
            return False

        # Если дошли сюда — пропускаем
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

    def extract_keywords(self, text: str, top_k=10):  # ← исправлена опечатка
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

    def chunk_density_score(self, text: str) -> float:
        """Оценка ценности чанка"""
        text_lower = text.lower()
        num_count = len(re.findall(r"\d+[,.]?\d*", text_lower))
        key_words = [
            "мм",
            "кн",
            "гост",
            "порог",
            "допуск",
            "критическ",
            "предельн",
            "выщербина",
            "прокат",
            "гребень",
            "износ",
            "дефект",
            "поверхност",
            "катания",
            "колесн",
            "пара",
            "рельс",
            "сила",
            "датчик",
            "модель",
        ]
        kw_count = sum(text_lower.count(kw) for kw in key_words)
        length_bonus = len(text) / 400.0
        return (num_count * 5) + (kw_count * 2) + length_bonus

    def select_best_start_idx(self, doc_chunks):
        if len(doc_chunks) <= self.max_contexts:
            return 0

        scores = [(self.chunk_density_score(c["text"]), i) for i, c in enumerate(doc_chunks)]
        scores.sort(reverse=True)

        top_indices = [idx for _, idx in scores[:8]]  # берём из топ-8

        if not top_indices:
            return random.randint(0, len(doc_chunks) - self.max_contexts)

        best = top_indices[0]
        # Берём начало окна так, чтобы захватить лучший чанк + немного соседей
        start = max(0, best - random.randint(0, 3))
        if start + self.max_contexts > len(doc_chunks):
            start = len(doc_chunks) - self.max_contexts

        return start

    def is_context_useful(self, text: str) -> bool:
        """Пропускаем совсем пустые/бесполезные контексты"""
        if len(text) < 400:
            return False
        num_count = len(re.findall(r"\d", text))
        kw_count = len(re.findall(r"(мм|кн|гост|порог|допуск|выщербина|прокат)", text.lower()))
        return num_count >= 1 or kw_count >= 2

    def build_qa_samples(self, chunks: list):
        samples = []

        grouped = self.group_by_doc(chunks)

        for doc_id, doc_chunks in grouped.items():
            if len(doc_chunks) == 0:
                continue

            start_idx = self.select_best_start_idx(doc_chunks)
            contexts = doc_chunks[start_idx : start_idx + self.max_contexts]
            texts = self.build_context(contexts)

            if not self.is_context_useful(texts):
                logger.debug(f"Context too weak for {doc_id} → skip")
                continue

            keywords = self.extract_keywords(texts)
            full_text = "Ключевые термины: " + ", ".join(keywords[:12]) + "\n\n" + texts

            QUESTION_TEMPLATES = [
                "Какое значение {topic}?",
                "Каков максимально допустимый {topic}?",
                "При каком значении {topic} возникает риск дефекта?",
                "Согласно какому документу устанавливается {topic}?",
                "Чему равен порог {topic}?",
            ]

            # В build_qa_samples перед формированием промпта:
            template = random.choice(QUESTION_TEMPLATES).format(
                topic="порог вертикальной силы / неравномерного проката"
            )
            texts = f"Предпочтительный шаблон вопроса: {template}\n\n" + texts

            if LLMConfig.ONLINE:
                prompt = self.PROMPT_TEMPLATE.format(answer_rules=self.OPEN_AI_ANSWER_RULES, contexts=full_text)
            else:
                prompt = self.PROMPT_TEMPLATE.format(answer_rules=self.OFFLINE_LLM_ANSWER_RULES, contexts=full_text)

            qa = self.llm_asker.ask_direct_llm(prompt)

            # Убираем китайские иероглифы сразу
            if isinstance(qa, dict):
                qa["question"] = re.sub(r"[\u4e00-\u9fff]+", "", qa["question"].strip())
                qa["answer"] = re.sub(r"[\u4e00-\u9fff]+", "", qa["answer"].strip())

                if not self.is_good_qa(qa["question"], qa["answer"], texts):
                    logger.debug(f"Bad qa: question:{qa['question']}\nanswer: {qa['answer']}, context: {full_text}")
                    continue

                sample = {
                    "question": qa["question"],
                    "answer": qa["answer"],
                    "contexts": texts,
                    "sources": [doc_id],
                }
            else:
                continue  # если не dict — пропускаем

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
        # Собираем ВСЕ чанки из всех файлов один раз (в начале)
        all_chunks = []
        for chunk_file in os.listdir(Paths.CHUNKS):
            path = os.path.join(Paths.CHUNKS, chunk_file)
            all_chunks.extend(self.load_chunks(path))

        logger.info(f"Total chunks loaded: {len(all_chunks)}")

        for _ in tqdm(range(num_samples), desc="generating qa dataset"):
            # Берём случайные max_contexts чанков из всего пула
            if len(all_chunks) < self.max_contexts:
                selected = all_chunks
            else:
                selected = random.sample(all_chunks, self.max_contexts)

            # Генерируем QA только из этих случайных чанков
            samples_raw = self.build_qa_samples(selected)
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
    builder.build(num_samples=50)  # можно сразу больше для теста
    builder.qa_to_lora_format()
