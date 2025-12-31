import json
import os
import faiss
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer


class EmbeddingBuilder:
    def __init__(
        self,
        model_name: str = "intfloat/multilingual-e5-base",
        device: str = "cuda",
    ):
        self.model = SentenceTransformer(model_name, device=device)

    def build_embeddings(self, chunks_path: str):
        texts = []
        metadatas = []

        with open(chunks_path, "r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                texts.append("passage: " + obj["text"])
                metadatas.append(obj["metadata"])

        print(f"Loaded {len(texts)} chunks")

        embeddings = self.model.encode(
            texts,
            batch_size=16,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

        return embeddings, metadatas

    def save_faiss(
        self,
        embeddings: np.ndarray,
        metadatas: list,
        out_dir: str,
    ):
        os.makedirs(out_dir, exist_ok=True)

        dim = embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)
        index.add(embeddings)

        faiss.write_index(index, os.path.join(out_dir, "index.faiss"))

        with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(metadatas, f, ensure_ascii=False, indent=2)
