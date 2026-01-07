from transformers import AutoTokenizer
from config import LLMConfig


class ContextBuilder:
    def __init__(self, model_name: str = LLMConfig.BASE_MODEL):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    def build(self, results, max_context_tokens: int = 3500):  # оставляем запас под вопрос + ответ
        contexts = []
        current_tokens = 0
        header_overhead = 100  # грубая оценка токенов на заголовок + разделители

        for r in results:
            text = r.get("text", "").strip()
            if not text:
                continue

            doc_id = r.get("doc_id", "Неизвестный источник")
            section = r.get("section", "")
            chunk_id = r.get("chunk_id", "")

            header = f"[Источник: {doc_id}"
            if section:
                header += f", раздел: {section}"
            if chunk_id != "":
                header += f", chunk: {chunk_id}"
            header += "]"

            full_chunk = f"{header}\n{text}"

            # Считаем токены этого чанка
            chunk_tokens = len(self.tokenizer.encode(full_chunk, add_special_tokens=False))

            # Если добавление чанка превысит лимит — обрезаем его или пропускаем
            if current_tokens + chunk_tokens + header_overhead > max_context_tokens:
                remaining_tokens = max_context_tokens - current_tokens - header_overhead
                if remaining_tokens > 200:  # если осталось хоть немного
                    truncated_text = self.tokenizer.decode(
                        self.tokenizer.encode(full_chunk, add_special_tokens=False)[:remaining_tokens]
                    )
                    contexts.append(truncated_text)
                break  # дальше не добавляем чанки

            contexts.append(full_chunk)
            current_tokens += chunk_tokens

        return "\n\n---\n\n".join(contexts)
