class ContextBuilder:
    def __init__(self, max_chars: int = 3000):
        self.max_chars = max_chars

    def build(self, results: list) -> str:
        context_parts = []
        seen = set()
        total_len = 0

        for i, r in enumerate(results, 1):
            text = r["text"]
            meta = r["metadata"]

            if text in seen:
                continue

            seen.add(text)

            header = f"[{i}] {meta['doc_id']} — {meta.get('section', 'ROOT')}"

            context_parts.append(f"{header}\n{text}")

            total_len += len(text)
            if total_len > self.max_chars:
                break

        return "\n\n".join(context_parts)
