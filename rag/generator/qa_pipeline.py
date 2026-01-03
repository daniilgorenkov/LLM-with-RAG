from rag.retriever.retriever import Retriever
from rag.context_builder.builder import ContextBuilder
from rag.generator.prompt_builder import PromptBuilder
from rag.generator.llm_client import LLMClient
from rag.reranker.reranker import Reranker
from config import Paths
import os


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever(
            index_path=os.path.join(Paths.VECTORS, "index.faiss"), meta_path=os.path.join(Paths.VECTORS, "meta.json")
        )
        self.reranker = Reranker()
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMClient()

    def ask(self, question: str) -> str:
        # A — retrieve
        results = self.retriever.search(question, top_k=5)

        if not results or results[0]["score"] < 0.6:
            return "В источниках нет информации для ответа на данный вопрос."

        # B - rerank
        results = self.reranker.rerank(question, results)

        # C — context
        context = self.context_builder.build(results)

        # D — prompt + LLM
        messages = self.prompt_builder.build(context, question)
        answer = self.llm.generate(messages)

        return answer
