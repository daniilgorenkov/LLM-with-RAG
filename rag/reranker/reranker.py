from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
        device: str = "cpu",
        top_n: int = 5,
    ):
        self.model = CrossEncoder(model_name, device=device)
        self.top_n = top_n

    def rerank(self, question: str, docs: list) -> list:
        """
        docs: list of dicts with 'text'
        """
        # print("Первый документ из списка:", docs[0] if docs else "пусто")
        # print("Тип элементов:", type(docs[0]) if docs else None)
        pairs = [(question, d["text"]) for d in docs]

        scores = self.model.predict(pairs)

        for d, score in zip(docs, scores):
            d["rerank_score"] = float(score)

        docs = sorted(docs, key=lambda x: x["rerank_score"], reverse=True)

        return docs[: self.top_n]
