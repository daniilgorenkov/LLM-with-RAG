import os
import re
from openai import OpenAI


class LLMClient:
    def __init__(self, model="gpt-4o-mini"):
        from dotenv import load_dotenv

        load_dotenv("secret.env")
        self.client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
        self.model = model

    def generate(self, messages: list) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.1,
        )
        return response.choices[0].message.content

    def ask_direct_llm(self, prompt: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=300,
        )

        text = response.choices[0].message.content.strip()

        if "Вопрос:" not in text or "Ответ:" not in text:
            return None

        q = text.split("Вопрос:")[1].split("Ответ:")[0].strip()
        a = text.split("Ответ:")[1].strip()

        if not q or not a:
            return None

        return {"question": q, "answer": a}
