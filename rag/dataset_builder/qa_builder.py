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
from nltk.stem import PorterStemmer
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
    Ты — эксперт по диагностике дефектов ж/д колёс.
    Сформулируй **ровно один** вопрос и **ровно один** короткий ответ только из текста.
    СТРОГО СЛЕДУЙ ПРАВИЛАМ:

    1. Вопрос ОБЯЗАТЕЛЬНО начинается с одного из вариантов:
       • Какое значение...?
       • Каков порог...?
       • При каком значении...?
       • Чему равно максимально допустимое...?
       • Как классифицируется дефект...?
       • В каком документе...?
       • Согласно какому ГОСТ...?
       ЗАПРЕЩЕНО начинать с: какие, как, каким образом, почему, зачем, опиши, расскажи и т.п.

    2. Ответ — максимум 1–2 предложения. Только факт из контекста.
    3. Никогда не придумывай числа, пороги, названия документов — только то, что явно есть в тексте.
    4. Если нужной информации нет — отвечай строго:
       Вопрос: Недостаточно данных
       Ответ: Недостаточно данных

    Примеры правильных пар (следуй этому стилю):

    Вопрос: Какой диапазон толщины гребня колеса в эксплуатации?
    Ответ: От 24 до 33 м.

    Вопрос: В каком документе указаны пороги вертикальной силы?
    Ответ: ГОСТ 34759-2021.

    Вопрос: До какого значения допускается вертикальная сила в системе колесо-рельс?
    Ответ: До 350 кН, согласно ГОСТ 34759-2021.

    НЕ ПРИДУМЫВАЙ НИЧЕГО!

    Контекст:
    {contexts}
    """

    N_SAMPLES: int = 3
    MAX_CONTEXT_CHARS = 1200  # немного увеличили — современные модели нормально справляются

    def __init__(self, max_contexts: int = 3):
        self.max_contexts = max_contexts
        self.llm_asker = LLMClient(online=LLMConfig.ONLINE)
        self.morph = pymorphy3.MorphAnalyzer()
        self.stemmer_en = PorterStemmer()

    def lemmatize_words(self, text: str):
        words = re.findall(r"[а-яa-z]{5,}", text.lower())
        lemmas = set()
        for w in words:
            lemma = self.morph.parse(w)[0].normal_form
            if len(lemma) >= 5:
                lemmas.add(lemma)
        return lemmas


    def normalize_word(self, word: str) -> str:
        """Нормализуем слово: русский → pymorphy, английский → PorterStemmer"""
        if re.match(r"[а-я]+", word):
            return self.morph.parse(word)[0].normal_form
        else:
            return self.stemmer_en.stem(word)

    def is_good_qa(self, question: str, answer: str, context: str) -> bool:
        q = question.strip()
        a = answer.strip()
        c = context.strip()

        if not q or not a:
            return False

        # Запрещаем самые плохие "какие" только если ответ длинный
        bad_starts = [
            "какие методы",
            "какие технологии",
            "какие системы",
            "какие существуют",
            "какие данные",
            "какие параметры",
            "какие факторы",
        ]

        if any(q.lower().startswith(b) for b in bad_starts) and len(a.split()) > 15:
            return False

        # НОВАЯ ПРОВЕРКА: пересечение нормализованных слов
        # Регулярка ловит слова/термины (кириллица + латиница + цифры + дефисы)
        context_words = re.findall(r"[а-яa-z0-9-]{3,}", c.lower())
        answer_words = re.findall(r"[а-яa-z0-9-]{3,}", a.lower())

        # Нормализуем
        context_norm = {self.normalize_word(w) for w in context_words}
        answer_norm = {self.normalize_word(w) for w in answer_words}

        common = context_norm & answer_norm

        # Минимум 2 общих нормализованных слова — достаточно для "релевантности"
        if len(common) >= 2:
            return True

        # Дополнительно разрешаем, если в ответе есть число/единица/ГОСТ (даже без 2 слов)
        if re.search(r"\d|мм|кн|гост|м|кгс|нм|до|от|не более|section|figure|table", a.lower()):
            if len(common) >= 1:  # хотя бы одно слово
                return True

        # Если ничего не нашли — отсекаем
        logger.debug(f"Ответ оторван от контекста. Общих нормализованных слов: {len(common)}")
        return False

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

            if LLMConfig.ONLINE:
                prompt = self.PROMPT_TEMPLATE.format(answer_rules=self.OPEN_AI_ANSWER_RULES, contexts=full_text)
            else:
                prompt = self.PROMPT_TEMPLATE.format(answer_rules=self.OFFLINE_LLM_ANSWER_RULES, contexts=full_text)

            qa = self.llm_asker.ask_direct_llm(prompt)

            # Убираем китайские иероглифы сразу
            if isinstance(qa, dict):
                if qa["question"] == "Недостаточно данных" or qa["answer"] == "Недостаточно данных":
                    continue 
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
    builder.build(num_samples=500)  # можно сразу больше для теста
    builder.qa_to_lora_format()
