import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)
from rag.generator.qa_pipeline import RAGPipeline
from phd_assistant import PhDAssistant
from datetime import datetime
from utils.telegram_bot import send_as_album
from config import Paths

def send_files():
    dirname = sorted(os.listdir(os.path.join(Paths.PHD)),reverse=True)[0]
    file = os.path.join(Paths.PHD,dirname,"final.md")
    send_as_album(os.getenv("TG_BOT_TOKEN"),os.getenv("CHAT_ID"),[file])

if __name__ == "__main__":
    load_dotenv("secret.env")

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    rag = RAGPipeline(llm_type="local_lora")
    assistant = PhDAssistant(rag)

    assistant.generate_section_iterative(
        topic="Какие системы диагностики существуют", section_name=f"{ts}_overview"
    )

    send_files()

