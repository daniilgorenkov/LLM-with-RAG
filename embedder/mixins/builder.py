import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.custom_logger import set_logger
from config import Paths, EmbedderConfig

logger = set_logger(Paths.LOG_FILE)


class EmbeddingBuilder:
    def __init__(
        self,
        model_name: str = EmbedderConfig.BASE_MODEL,
        device: str = "cuda",
    ):
        self.model = SentenceTransformer(model_name, device=device)

    def build_embeddings(self, chunks_path: str):
        """
        Строит эмбеддинги для одного .jsonl файла
        """
        texts = []
        metadatas = []

        with open(chunks_path, "r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                texts.append("passage: " + obj["text"])
                metadatas.append({**obj["metadata"], "text": obj["text"]})

        embeddings = self.model.encode(
            texts,
            batch_size=EmbedderConfig.BATCH_SIZE,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

        return embeddings, metadatas

    def build_embeddings_from_dir(self, chunks_dir: str):
        """
        Строит эмбеддинги для ВСЕХ файлов в директории
        """
        all_texts = []
        all_metadatas = []

        files = sorted(f for f in os.listdir(chunks_dir) if f.endswith(".jsonl"))

        for fname in files:
            path = os.path.join(chunks_dir, fname)
            logger.debug(f"Embedding: {fname}")

            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    obj = json.loads(line)
                    all_texts.append("passage: " + obj["text"])
                    all_metadatas.append(obj["metadata"])

        logger.debug(f"Total chunks: {len(all_texts)}")

        embeddings = self.model.encode(
            all_texts,
            batch_size=EmbedderConfig.BATCH_SIZE,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

        return embeddings, all_metadatas

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
