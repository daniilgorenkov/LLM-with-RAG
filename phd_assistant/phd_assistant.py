import sys
import os
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from rag.generator.qa_pipeline import RAGPipeline
from config import Paths
from utils.custom_logger import set_logger
from prompts import AssitantPrompts
from quality import QualityChecker
import re

logger = set_logger(Paths.LOG_FILE)


class PhDAssistant(AssitantPrompts, QualityChecker):
    def __init__(self, rag: RAGPipeline):
        self.rag = rag
        self.base_dir = Path(Paths.PHD)
        self.base_dir.mkdir(exist_ok=True)

    def _load_system_prompt(self, name: str) -> str:
        with open(os.path.join(Paths.PROMPTS, f"{name}.md"), "r", encoding="utf-8") as f:
            content = f.read()
        return content

    def build_messages(self, system, user):
        return [{"role": "system", "content": system}, {"role": "user", "content": user}]

    def postprocess(self, text: str):
        return text.split("<END_OF_SECTION>")[0].strip()

    def generate(self, messages, mode):
        return self.rag.llm.generate(messages, mode)

    def simple_terms(self, text: str):
        blacklist = {"данного", "данные", "которые", "который", "системы", "процесса", "методов"}
        return [w.lower() for w in re.findall(r"\b[а-яА-Я]{6,}\b", text) if w.lower() not in blacklist]

    # ---------- CORE ----------
    def generate_text(self, prompt: str, mode: str = "draft") -> str:
        """Main cycle of generation"""

        system_prompt = self._load_system_prompt(mode)

        messages = self.build_messages(system_prompt, prompt)
        text = self.generate(messages, mode)
        return self.postprocess(text)

    def _retrieve_context(self, topic: str) -> str:
        results = self.rag.retriever.search(topic, top_k=10)

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
        logger.debug(" ============== START TEXT GENERATION FOR TOPIC ============== ")
        context = self._retrieve_context(topic)
        if not context:
            raise ValueError("Lack of context")

        logger.debug("Extracting terms from context...")
        terms = self.simple_terms(context)

        logger.debug("Generating draft...")
        draft = self.generate_text(
            self.build_generation_prompt(topic, context),
            mode="draft",
        )

        best_score = self.quality(draft, context, terms)

        history = []

        logger.debug("Starting iterative text evaluation...")
        for iteration in range(1, max_iters + 1):
            review = self.generate_text(
                self.build_review_prompt(draft, context),
                mode="review",
            )

            logger.debug("Draft reviewed")

            plan = self.generate_text(
                self.build_checklist_prompt(draft),
                mode="plan",
            )

            logger.debug("Created todo list based on review")

            revised = self.generate_text(
                self.build_revision_prompt(draft, review, plan, context),
                mode="rewrite",
            )

            logger.debug("Revised draft based on context, review and checklist")

            candidate = revised
            candidate_score = self.quality(candidate, context, terms)

            # if text better use revised otherwise use draft
            if candidate_score >= best_score:
                best = candidate
                best_score = candidate_score
            else:
                best = draft

            judge = self.generate_text(
                self.build_quality_prompt(best),
                mode="judge",
            )

            history.append(
                {
                    "iteration": iteration,
                    "draft": draft,
                    "review": review,
                    "plan": plan,
                    "revised": best,
                    "judge": judge,
                }
            )

            if judge.strip().lower() == "да":
                break

            if iteration > 1 and best_score <= history[-1].get("best_score", best_score):
                logger.debug("Quality stagnation detected")
                break

            draft = best  # следующий цикл

        final_text = history[-1]["revised"]

        finalized = self.generate_text(
            final_text,
            mode="finalize",
        )

        history[-1]["final"] = finalized
        paths = self._save_iterative(section_name, history)

        return {
            "final_text": history[-1]["final"],
            "iterations": history,
            "paths": paths,
        }

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
            try:
                (section_dir / f"{i}_final.txt").write_text(step["final"], encoding="utf-8")
            except Exception:
                pass
        return section_dir
