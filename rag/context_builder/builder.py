from collections import defaultdict
from typing import List, Dict


class ContextBuilder:
    def __init__(self, max_chars: int = 3000):
        self.max_chars = max_chars

    def build(self, results: list) -> str:
        context_parts = []
        seen = set()
        total_len = 0

        for r in results:
            text = r["text"]

            if text in seen:
                continue

            seen.add(text)
            context_parts.append(f"[Источник: {r['doc_id']} | {r['section']}]\n{text}")

            total_len += len(text)
            if total_len > self.max_chars:
                break

        return "\n\n".join(context_parts)
