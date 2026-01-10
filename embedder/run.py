import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Paths, CommonConfig
from mixins.builder import EmbeddingBuilder


class Embedder:
    def run(self):
        builder = EmbeddingBuilder(device=CommonConfig.DEVICE)  # или "cuda"

        # 1️⃣ загрузить все чанки из директории
        embeddings, metadatas = builder.build_embeddings_from_dir(chunks_dir=Paths.CHUNKS)

        # 2️⃣ сохранить один FAISS + одну meta.json
        builder.save_faiss(
            embeddings=embeddings,
            metadatas=metadatas,
            out_dir=Paths.VECTORS,
        )


if __name__ == "__main__":
    Embedder().run()
