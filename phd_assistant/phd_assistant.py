import sys
import os
from pathlib import Path
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag.generator.qa_pipeline import RAGPipeline
from config import Paths


class PhDAssistant:
    def __init__(self, rag: RAGPipeline):
        self.rag = rag

        self.role_prompt = """
        Вы — научный ассистент, оказывающий помощь в написании диссертации
        на соискание ученой степени кандидата наук (PhD).

        Требования:
        - академический стиль русского языка
        - без личных местоимений
        - без вымышленных данных
        - опора ТОЛЬКО на предоставленный контекст
        - логичная структура
        - допускается использование английских терминов и названий систем
        """

        self.base_dir = Path(Paths.PHD)
        self.base_dir.mkdir(exist_ok=True)

    # ---------- PROMPTS ----------

    def build_generation_prompt(self, topic: str, context: str) -> str:
        return f"""
        {self.role_prompt}

        ЗАДАНИЕ:
        Написать фрагмент диссертационного текста на тему:

        «{topic}»

        ТРЕБОВАНИЯ:
        - язык: русский
        - стиль: научный
        - 2–3 связных абзаца
        - без списков
        - без выводов
        - без вымышленных фактов

        ЗАПРЕЩЕНО:
        - нумерованные списки
        - маркированные списки
        - перечисления через двоеточие

        ТЕКСТ ДОЛЖЕН БЫТЬ:
        - только связные абзацы
        - каждый абзац — 3–5 предложений

        КОНТЕКСТ ИЗ ИСТОЧНИКОВ:
        {context}

        СГЕНЕРИРУЙ ТОЛЬКО ТЕКСТ РАЗДЕЛА.
        ЗАВЕРШИ ТЕКСТ ЛОГИЧЕСКИ.
        ПОСЛЕДНЕЕ ПРЕДЛОЖЕНИЕ ДОЛЖНО БЫТЬ ЗАКОНЧЕННЫМ.
        НЕ ПРОДОЛЖАЙ ПОСЛЕ ЭТОГО РАЗДЕЛА.
        В КОНЦЕ ТЕКСТА НАПИШИ: <END_OF_SECTION>
        """

    def build_review_prompt(self, text: str) -> str:
        return f"""
        Вы выступаете в роли научного руководителя.

        Проанализируйте текст и укажите:

        1. Логические пробелы
        2. Неясные или общие формулировки
        3. Где требуются ссылки на источники
        4. Где можно усилить научную аргументацию
        5. Соответствие академическому стилю

        ТЕКСТ:
        {text}

        ФОРМАТ:
        - нумерованный список
        - без переписывания текста
        """

    def build_checklist_prompt(self, text: str) -> str:
        return f"""
        На основе текста ниже сформируйте checklist для его доработки.

        ТЕКСТ:
        {text}

        ТРЕБОВАНИЯ:
        - формат markdown checklist
        - каждый пункт — конкретное действие

        ФОРМАТ:
        - [ ] ...
        """

    # ---------- CORE ----------
    def _generate(self, prompt: str) -> str:
        messages = [
            {"role": "system", "content": self.role_prompt},
            {"role": "user", "content": prompt},
        ]
        text = self.rag.llm.generate(messages)
        if "<END_OF_SECTION>" in text:
            text = text.split("<END_OF_SECTION>")[0].strip()
        return text

    def _retrieve_context(self, topic: str) -> str:
        results = self.rag.retriever.search(topic, top_k=3)

        if not results or results[0]["score"] < 0.6:
            return ""

        results = self.rag.reranker.rerank(topic, results)
        return self.rag.context_builder.build(results)

    def generate_section(self, topic: str, section_name: str):
        context = self._retrieve_context(topic)

        if not context:
            raise ValueError("Недостаточно контекста для генерации раздела")

        draft_prompt = self.build_generation_prompt(topic, context)
        draft = self._generate(draft_prompt)

        review = self._generate(self.build_review_prompt(draft))

        checklist = self._generate(self.build_checklist_prompt(draft))
        paths = self._save(section_name, draft, review, checklist)

        return {
            "draft": draft,
            "review": review,
            "checklist": checklist,
            "paths": paths,
        }

    # ---------- STORAGE ----------

    def _save(self, section_name, draft, review, checklist):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        section_dir = self.base_dir / section_name
        section_dir.mkdir(exist_ok=True)

        paths = {
            "draft": section_dir / f"{ts}_draft.md",
            "review": section_dir / f"{ts}_review.md",
            "checklist": section_dir / f"{ts}_checklist.md",
        }

        paths["draft"].write_text(draft, encoding="utf-8")
        paths["review"].write_text(review, encoding="utf-8")
        paths["checklist"].write_text(checklist, encoding="utf-8")

        return paths
