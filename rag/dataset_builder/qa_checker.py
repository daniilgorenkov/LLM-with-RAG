import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Union
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from config import Paths
from utils.custom_logger import set_logger

logger = set_logger(Paths.LOG_FILE)


class QADatasetEvaluator:
    """
    Класс для автоматической оценки качества синтетического QA-датасета
    с помощью семантического сходства на эмбеддингах (без внешних LLM).
    Метрики:
    - Faithfulness: насколько ответ основан на предоставленных контекстах
    - Answer Relevancy: насколько ответ релевантен вопросу
    - Context Relevancy: насколько контексты релевантны вопросу
    """

    def __init__(self, model_name: str = "intfloat/multilingual-e5-base"):
        """
        :param model_name: имя модели Sentence Transformers (должна совпадать с той,
                          которой создавались эмбеддинги чанков!)
        """
        logger.debug(" ======= QADatasetEvaluator ======= ")
        logger.debug(f"Load embed model: {model_name}...")
        self.model = SentenceTransformer(model_name)

    def _embed(self, texts: Union[str, List[str]]) -> np.ndarray:
        """
        Эмбеддит текст(ы) с правильными префиксами для e5-моделей.
        """
        if isinstance(texts, str):
            texts = [texts]
        # Первый текст — query, остальные — passages
        prefixed = [f"query: {texts[0]}"] + [f"passage: {t}" for t in texts[1:]]
        return self.model.encode(prefixed, normalize_embeddings=True)

    def _mean_similarity(self, emb1: np.ndarray, emb2_list: List[np.ndarray]) -> float:
        if len(emb2_list) == 0:
            return 0.0
        sims = cosine_similarity(emb1, np.vstack(emb2_list))[0]
        return float(np.mean(sims))

    def evaluate_file(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        data = []
        with file_path.open("r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:  # пропускаем пустые строки
                    continue
                try:
                    item = json.loads(line)
                    data.append(item)
                except json.JSONDecodeError as e:
                    logger.debug(f"Error while line parsing {line_num}: {e}")
                    logger.debug(f"Bad line: {line[:200]}...")  # покажем начало
                    # Попробуем восстановить вручную (опционально)
                    # continue  # или raise, если хочешь строгую проверку

        if not data:
            raise ValueError("Couldn't load any file!")

        logger.debug(f"Succesfully loaded {len(data)} samples from {file_path}")
        return self.evaluate(data)

    def evaluate(self, dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Основной метод оценки списка примеров.
        """
        if not dataset:
            raise ValueError("Датасет пустой!")

        faithfulness_scores = []
        answer_relevancy_scores = []
        context_relevancy_scores = []

        logger.debug(f"Measuring {len(dataset)} samples...")

        for i, item in enumerate(dataset, 1):
            question = item.get("question", "")
            answer = item.get("answer", "")
            contexts = item.get("contexts", [])

            if not question or not answer:
                logger.warning(f"Skipped sample {i} (no question or answer)")
                continue

            # Эмбеддинги
            q_emb = self._embed(question).reshape(1, -1)
            a_emb = self._embed(answer).reshape(1, -1)
            ctx_embs = self._embed(contexts) if contexts else []

            # Метрики
            faith = self._mean_similarity(a_emb, ctx_embs) if ctx_embs.size > 0 else 0.0
            ans_rel = float(cosine_similarity(a_emb, q_emb)[0][0])
            ctx_rel = self._mean_similarity(q_emb, ctx_embs) if ctx_embs.size > 0 else 0.0

            faithfulness_scores.append(faith)
            answer_relevancy_scores.append(ans_rel)
            context_relevancy_scores.append(ctx_rel)

            if i % 10 == 0:
                logger.debug(f"  Done {i}/{len(dataset)} samples...")

        # Итоговые метрики
        results = {
            "num_examples": len(faithfulness_scores),
            "faithfulness_mean": np.mean(faithfulness_scores),
            "faithfulness_std": np.std(faithfulness_scores),
            "answer_relevancy_mean": np.mean(answer_relevancy_scores),
            "answer_relevancy_std": np.std(answer_relevancy_scores),
            "context_relevancy_mean": np.mean(context_relevancy_scores),
            "context_relevancy_std": np.std(context_relevancy_scores),
            "overall_mean": np.mean(
                [np.mean(faithfulness_scores), np.mean(answer_relevancy_scores), np.mean(context_relevancy_scores)]
            ),
        }

        self._print_results(results)
        return results

    @staticmethod
    def _print_results(results: Dict[str, Any]):
        logger.debug("\n" + "=" * 50)
        logger.debug("QA Dataset evaluation results")
        logger.debug("=" * 50)
        logger.debug(f"Num samples:           {results['num_examples']}")
        logger.debug(
            f"Faithfulness (верность контексту):     {results['faithfulness_mean']:.3f} ± {results['faithfulness_std']:.3f}"
        )
        logger.debug(
            f"Answer Relevancy (ответ → вопрос):     {results['answer_relevancy_mean']:.3f} ± {results['answer_relevancy_std']:.3f}"
        )
        logger.debug(
            f"Context Relevancy (контекст → вопрос): {results['context_relevancy_mean']:.3f} ± {results['context_relevancy_std']:.3f}"
        )
        logger.debug(f"Overall mean score:                   {results['overall_mean']:.3f}")
        logger.debug("=" * 50)


# Пример использования
if __name__ == "__main__":
    evaluator = QADatasetEvaluator(model_name="intfloat/multilingual-e5-base")

    # Оценка из файла
    results = evaluator.evaluate_file(os.path.join(Paths.DATA, "qa_dataset.jsonl"))
