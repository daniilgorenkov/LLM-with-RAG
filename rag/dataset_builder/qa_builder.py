import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(sys.path)
import json
from collections import defaultdict
import os
from config import Paths
import random
from rag.generator.llm_client import LLMClient
from tqdm import tqdm
import time


class QADatasetBuilder:

    PROMPT_TEMPLATE = """
        Ты — эксперт в области диагностики дефектов поверхности катания железнодорожных колес.

        На основе приведённого контекста:
        - Сформулируй ОДИН технический вопрос.
        - Дай точный и краткий ответ.
        - Используй ТОЛЬКО информацию из контекста.
        - Если информации недостаточно, напиши "Недостаточно данных".

        Верни результат СТРОГО в формате:

        Вопрос:
        <текст вопроса>

        Ответ:
        <текст ответа>

        Контекст:
        {contexts}
        """

    N_SAMPLES: int = 3

    def __init__(
        self,
        max_contexts: int = 5,
    ):
        self.max_contexts = max_contexts
        self.llm_asker = LLMClient()

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

    def build_samples(self, chunks: list):
        samples = []

        grouped = self.group_by_doc(chunks)

        for doc_id, doc_chunks in grouped.items():
            random.shuffle(doc_chunks)

            contexts = doc_chunks[: self.max_contexts]
            texts = [c["text"] for c in contexts]

            sample = {
                "question": None,  # будет сгенерировано LLM
                "answer": None,  # будет сгенерировано LLM
                "contexts": texts,
                "sources": [doc_id],
            }

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

    def generate_qa_from_llm(self):
        samples = []

        print("reading raw qa json")
        chunk_file = os.path.join(Paths.DATA, "qa_dataset_raw.jsonl")
        with open(chunk_file, "r", encoding="utf-8") as f:
            chunks = [json.loads(line) for line in f]

        print("Start grouping chunks to ask llm...")
        for i in tqdm(range(0, len(chunks), self.N_SAMPLES), desc="Asking llm..."):
            group = chunks[i : i + self.N_SAMPLES]
            if len(group) < self.N_SAMPLES:
                continue

            contexts = "\n\n".join(c["contexts"][0] for c in group)
            sources = group[0]["sources"]

            prompt = self.PROMPT_TEMPLATE.format(contexts=contexts)
            if i % 3 == 0:
                time.sleep(30)

            qa = self.llm_asker.ask_direct_llm(prompt)

            if qa is None:
                continue

            samples.append(
                {
                    "question": qa["question"],
                    "answer": qa["answer"],
                    "contexts": [contexts],
                    "sources": sources,
                }
            )
        return samples

    def build(self, num_samples: int = 1000):

        for _ in tqdm(range(num_samples), desc="generating context and sources"):
            chunks_list = os.listdir(Paths.CHUNKS)
            random_chunk = random.choice(chunks_list)
            sample_chunk = self.load_chunks(os.path.join(Paths.CHUNKS, random_chunk))
            samples_raw = self.build_samples(sample_chunk)
            self.save(samples_raw, os.path.join(Paths.DATA, "qa_dataset_raw.jsonl"))

        samples = self.generate_qa_from_llm()
        self.save(samples, os.path.join(Paths.DATA, "qa_dataset.jsonl"))


if __name__ == "__main__":
    builder = QADatasetBuilder()
    # chunks = builder.load_chunks(os.path.join(Paths.CHUNKS, "ГОСТ 34759-2021.jsonl"))
    # samples = builder.build_samples(chunks)
    # builder.save(samples, "data/qa_dataset.jsonl")
    builder.build(num_samples=100)
