# rag/retriever/retriever.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict
from config import Paths


class Retriever:
    def __init__(
        self,
        index_path: str,
        meta_path: str,
        model_name: str = "intfloat/multilingual-e5-base",
        device: str = "cpu",
    ):
        self.index = faiss.read_index(index_path)

        with open(meta_path, "r", encoding="utf-8") as f:
            self.metadatas = json.load(f)

        self.model = SentenceTransformer(model_name, device=device)

        assert self.index.ntotal == len(self.metadatas), "FAISS index and metadata size mismatch"

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Возвращает top_k наиболее релевантных чанков
        """
        query_embedding = self.model.encode(
            ["query: " + query],
            normalize_embeddings=True,
        )

        scores, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k,
        )

        results = []
        for score, idx in zip(scores[0], indices[0]):
            meta = self.metadatas[idx]
            results.append(
                {
                    "score": float(score),
                    "doc_id": meta.get("doc_id"),
                    "section": meta.get("section"),
                    "level": meta.get("level"),
                    **meta,
                }
            )

        return results


if __name__ == "__main__":
    retriever = Retriever(
        index_path=f"{Paths.VECTORS}/index.faiss",
        meta_path=f"{Paths.VECTORS}/meta.json",
        device="cpu",
    )

    query = "Что такое динамическое взаимодействие колесо–рельс?"

    results = retriever.search(query, top_k=5)

    for i, r in enumerate(results, 1):
        print(f"\n#{i}")
        print("Score:", round(r["score"], 3))
        print("Doc:", r["doc_id"])
        print("Section:", r["section"])
