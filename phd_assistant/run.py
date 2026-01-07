import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)
from rag.generator.qa_pipeline import RAGPipeline
from phd_assistant import PhDAssistant

rag = RAGPipeline(llm_type="local_lora")
assistant = PhDAssistant(rag)

result = assistant.generate_section(
    topic="Системы диагностики подвижного состава железных дорог", section_name="01_overview"
)

print(result["draft"])
