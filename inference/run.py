import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)

load_dotenv("secret.env")
from rag.generator.qa_pipeline import RAGPipeline

if __name__ == "__main__":
    rag = RAGPipeline("local_lora")

    while True:
        question = input("\nВопрос: ")
        if question.lower() in ("exit", "quit"):
            break

        answer = rag.ask(question)
        print("\nОтвет:\n", answer)
