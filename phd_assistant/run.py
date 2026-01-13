import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)
from rag.generator.qa_pipeline import RAGPipeline
from phd_assistant import PhDAssistant
from datetime import datetime

ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

rag = RAGPipeline(llm_type="local_lora")
assistant = PhDAssistant(rag)

result = assistant.generate_section_iterative(
    topic="Искусственный интеллект и модели машинного обучения в системах диагностик", section_name=f"{ts}_overview"
)

# print(result["draft"])
