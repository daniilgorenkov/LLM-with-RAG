from rag.generator.qa_pipeline import RAGPipeline
from phd_assistant import PhDAssistant
from datetime import datetime


def run_pipeline(topic: str) -> str:
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    rag = RAGPipeline(llm_type="local_lora")
    assistant = PhDAssistant(rag)

    return assistant.generate_section_iterative(topic=topic, section_name=f"{ts}")
