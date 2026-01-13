class QualityChecker:

    def length_score(self, text: str):
        words = text.split()
        return min(len(words) / 250, 1.0)  # нормализация

    def is_finished(self, text: str):
        return text.strip().endswith((".", "»", '"'))

    def repetition_penalty(self, text: str):
        sentences = text.split(".")
        unique = set(s.strip().lower() for s in sentences if len(s) > 10)
        return len(unique) / max(len(sentences), 1)

    def context_overlap(self, text: str, context: str):
        text_tokens = set(text.lower().split())
        ctx_tokens = set(context.lower().split())
        return len(text_tokens & ctx_tokens) / max(len(ctx_tokens), 1)

    def quality(self, text: str, context: str, terms: str):
        score = 0.0

        score += 0.25 * self.length_score(text)
        score += 0.25 * self.repetition_penalty(text)
        score += 0.25 * self.context_overlap(text, context)
        score += 0.25 * self.is_finished(text)

        return score
