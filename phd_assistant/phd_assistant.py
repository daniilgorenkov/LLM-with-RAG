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

        self.SYSTEM_AUTHOR = """
        Вы — автор диссертации на соискание ученой степени кандидата наук (PhD)
        в области железнодорожного транспорта и интеллектуальных систем диагностики.

        Требования:
        - академический стиль
        - без личных местоимений
        - без вымышленных данных
        - строго на основе контекста
        - связный научный текст
        """

        self.SYSTEM_REVIEWER = """
        Вы — научный руководитель и рецензент диссертационной работы.

        Требования:
        - критический анализ
        - указание пробелов и слабых мест
        - без переписывания текста
        - опора на научные стандарты
        """

        self.SYSTEM_EDITOR = """
        Вы — научный редактор и автор диссертации.

        Задача:
        - улучшить текст
        - усилить аргументацию
        - устранить замечания
        - сохранить академический стиль
        - не добавлять данные вне контекста
        """

        self.SYSTEM_PLAN = """Вы — научный редактор и методолог.

        Ваша задача — составить план доработки текста диссертационного уровня.

        Принципы:
        - не переписывать текст
        - не давать оценочных суждений
        - не добавлять новые факты
        - не делать выводов
        - не использовать вводные рассуждения

        Формат работы:
        - каждый пункт — одно конкретное действие
        - действия должны быть проверяемыми и выполнимыми
        - избегать абстрактных формулировок
        - не использовать местоимения

        Цель:
        - повысить научную строгость текста
        - улучшить аргументацию
        - указать, где требуется уточнение или источник
        - сохранить существующую структуру текста
        """

        self.base_dir = Path(Paths.PHD)
        self.base_dir.mkdir(exist_ok=True)

    # ---------- PROMPTS ----------

    def build_generation_prompt(self, topic: str, context: str) -> str:
        return f"""
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

    def build_review_prompt(self, text: str, context: str) -> str:
        return f"""
        Вы выступаете в роли научного руководителя.

        Проанализируйте текст и укажите:

        1. Логические пробелы
        2. Неясные или общие формулировки
        3. Где требуются ссылки на источники
        4. Где можно усилить научную аргументацию
        5. Соответствие академическому стилю
        
        Стурктура ответа:
        - каждый пункт — 1–2 предложения
        - без вводных слов
        - без оценочных суждений
        НЕ ТРЕБУЙ информации, отсутствующей в контексте.

        ТЕКСТ:
        {text}

        ФОРМАТ:
        - нумерованный список
        - без переписывания текста

        КОНТЕКСТ ИЗ ИСТОЧНИКОВ:
        {context}
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

    def build_revision_prompt(self, text: str, review: str, checklist: str, context: str) -> str:
        return f"""
        Вы — автор диссертации.

        Улучшите текст с учётом замечаний научного руководителя.

        Требования:
        - академический стиль
        - усилить аргументацию
        - устранить замечания
        - увеличить глубину, но не воду
        - сохранить структуру

        ТЕКСТ:
        {text}

        ЗАМЕЧАНИЯ:
        {review}

        ЧЕК-ЛИСТ ПРОВЕРКИ:
        {checklist}

        КОНТЕКСТ ИЗ ИСТОЧНИКОВ:
        {context}
        """

    def build_quality_prompt(self, text: str) -> str:
        return f"""
        Оцените необходимость доработки текста.

        ТЕКСТ:
        {text}

        ОТВЕТОМ МОГУТ БЫТЬ ТОЛЬКО:
        - Да
        - Нет
        """

    # ---------- CORE ----------
    def _generate(self, prompt: str, mode: str = "draft") -> str:
        system_prompt = {
            "draft": self.SYSTEM_AUTHOR,
            "review": self.SYSTEM_REVIEWER,
            "rewrite": self.SYSTEM_EDITOR,
            "plan": self.SYSTEM_PLAN,
        }[mode]

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
        text = self.rag.llm.generate(messages, mode)
        if "<END_OF_SECTION>" in text:
            text = text.split("<END_OF_SECTION>")[0].strip()
        return text

    def _retrieve_context(self, topic: str) -> str:
        results = self.rag.retriever.search(topic, top_k=3)

        if not results:
            return ""

        results = self.rag.reranker.rerank(topic, results)
        return self.rag.context_builder.build(results)

    def generate_section_iterative(
        self,
        topic: str,
        section_name: str,
        max_iters: int = 3,
    ):
        context = self._retrieve_context(topic)
        if not context:
            raise ValueError("Недостаточно контекста")

        draft = self._generate(
            self.build_generation_prompt(topic, context),
            mode="draft",
        )

        history = []

        for iteration in range(1, max_iters + 1):
            review = self._generate(
                self.build_review_prompt(draft, context),
                mode="review",
            )

            plan = self._generate(
                self.build_checklist_prompt(draft),
                mode="plan",
            )

            revised = self._generate(
                self.build_revision_prompt(draft, review, plan, context),
                mode="rewrite",
            )

            judge = self._generate(
                self.build_quality_prompt(revised),
                mode="judge",
            )

            history.append(
                {
                    "iteration": iteration,
                    "draft": draft,
                    "review": review,
                    "plan": plan,
                    "revised": revised,
                    "judge": judge,
                }
            )

            if "Да" in judge:
                break

            draft = revised  # следующий цикл

        paths = self._save_iterative(section_name, history)

        return {
            "final_text": history[-1]["revised"],
            "iterations": history,
            "paths": paths,
        }

    # ---------- STORAGE ----------

    def _save(self, section_name, draft, review, checklist, revision):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        section_dir = self.base_dir / section_name
        section_dir.mkdir(exist_ok=True)

        paths = {
            "draft": section_dir / f"{ts}_draft.md",
            "review": section_dir / f"{ts}_review.md",
            "checklist": section_dir / f"{ts}_checklist.md",
            "revision": section_dir / f"{ts}_revision.md",
        }

        paths["draft"].write_text(draft, encoding="utf-8")
        paths["review"].write_text(review, encoding="utf-8")
        paths["checklist"].write_text(checklist, encoding="utf-8")
        paths["revision"].write_text(revision, encoding="utf-8")
        return paths

    def _save_iterative(self, section_name: str, history: list):
        section_dir = self.base_dir / section_name
        section_dir.mkdir(exist_ok=True)

        for step in history:
            i = step["iteration"]
            (section_dir / f"{i}_draft.md").write_text(step["draft"], encoding="utf-8")
            (section_dir / f"{i}_review.md").write_text(step["review"], encoding="utf-8")
            (section_dir / f"{i}_plan.md").write_text(step["plan"], encoding="utf-8")
            (section_dir / f"{i}_revised.md").write_text(step["revised"], encoding="utf-8")
            (section_dir / f"{i}_judge.txt").write_text(step["judge"], encoding="utf-8")

        return section_dir
