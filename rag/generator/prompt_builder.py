class PromptBuilder:
    def build(self, context: str, question: str) -> list:
        return [
            {
                "role": "system",
                "content": (
                    "Ты — технический ассистент. "
                    "Отвечай строго на основе предоставленного контекста. "
                    "Не используй внешние знания. "
                    "Если ответа нет — прямо скажи об этом. "
                    "В конце обязательно укажи источники."
                ),
            },
            {
                "role": "user",
                "content": f"""
КОНТЕКСТ:
{context}

ВОПРОС:
{question}
""",
            },
        ]
