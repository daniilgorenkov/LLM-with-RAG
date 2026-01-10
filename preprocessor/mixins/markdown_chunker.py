import re
import os
import json
from typing import List, Dict


class MarkdownChunker:
    def __init__(
        self,
        max_chars: int = 700,
        overlap: int = 180,
    ):
        self.max_chars = max_chars
        self.overlap = overlap

    def is_valid_header(self, header: str) -> bool:
        """
        Проверяет, является ли заголовок осмысленным,
        а не формулой или мусором из PDF
        """
        header = header.strip()

        # слишком короткий
        if len(header) < 5:
            return False

        # слишком длинный (обычно формулы)
        if len(header) > 120:
            return False

        # если нет букв — почти наверняка формула
        if not re.search(r"[A-Za-zА-Яа-я]", header):
            return False

        # если слишком много спецсимволов
        if sum(c in "=⋅∑εσλμ√^_" for c in header) > 3:
            return False

        return True

    def split_by_headers(self, text: str):
        """
        Разбивает markdown по заголовкам, сохраняя уровень.
        Формульные и мусорные заголовки игнорируются.
        """
        pattern = r"(#{1,6})\s+(.*)"
        lines = text.splitlines()

        sections = []
        current = {"header": "ROOT", "level": 0, "content": []}

        for line in lines:
            match = re.match(pattern, line)
            if match:
                level = len(match.group(1))
                header = match.group(2).strip()

                # ❗ фильтрация мусорных заголовков
                if not self.is_valid_header(header):
                    current["content"].append(line)
                    continue

                # сохранить предыдущую секцию
                if current["content"]:
                    sections.append(current)

                current = {
                    "header": header,
                    "level": level,
                    "content": [],
                }
            else:
                current["content"].append(line)

        if current["content"]:
            sections.append(current)

        return sections

    def chunk_text(self, text: str) -> List[str]:
        chunks = []
        start = 0
        n = len(text)

        MAX_CHUNK = self.max_chars
        OVERLAP = self.overlap
        MIN_ADVANCE = max(200, int(MAX_CHUNK * 0.65))  # ← самое важное

        iteration = 0
        MAX_ITERATIONS = n // 100 + 1000  # страховка от бесконечного цикла

        while start < n:
            iteration += 1
            if iteration > MAX_ITERATIONS:
                print("!!! Emergency break in chunk_text - too many iterations !!!")
                break

            end = min(start + MAX_CHUNK, n)

            # Ищем границу предложения в зоне lookback
            lookback = max(60, MAX_CHUNK // 8)
            search_from = max(start, end - lookback)

            boundary = end
            for i in range(end - 1, search_from - 1, -1):
                if text[i] in ".!?":
                    # минимальная проверка на нормальное окончание предложения
                    if i + 2 < n and (text[i + 1].isspace() or text[i + 1] in "\n\r"):
                        boundary = i + 1
                        break

            # Самое важное — НЕ ДАЁМ продвижению стать слишком маленьким
            if boundary - start < MIN_ADVANCE:
                boundary = start + MIN_ADVANCE
                if boundary > n:
                    boundary = n

            chunk = text[start:boundary].rstrip()

            if len(chunk) >= 220:
                chunks.append(chunk)

            # Следующий старт — с гарантированным перекрытием
            start = boundary - OVERLAP

            # Дополнительная защита от "отката назад" или стагнации
            if start < boundary - OVERLAP + 40:
                start = boundary - OVERLAP + 40

        return chunks

    def chunk(self, text: str, doc_id: str, metadata: Dict) -> List[Dict]:
        sections = self.split_by_headers(text)
        documents = []

        for sec in sections:
            section_text = "\n".join(sec["content"]).strip()
            if len(section_text) < 150:
                continue

            chunks = self.chunk_text(section_text)

            for i, chunk in enumerate(chunks):
                # Финальная фильтрация
                if len(chunk) < 220:
                    continue

                # Слишком много формул / символов — пропускаем
                formula_ratio = sum(c in "=⋅∑εσλμ√^_∈∀∃" for c in chunk) / max(1, len(chunk))
                if formula_ratio > 0.12:
                    continue

                documents.append(
                    {
                        "text": chunk,
                        "metadata": {
                            "doc_id": doc_id,
                            "section": sec["header"],
                            "level": sec["level"],
                            "chunk_id": i,
                            # "text": section_text,  ← лучше убрать, занимает много места
                            **metadata,
                        },
                    }
                )

        return documents

    def save_chunks(self, docs: list, out_path: str):
        """
        Сохраняет чанки в формате JSONL
        """
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, "w", encoding="utf-8") as f:
            for doc in docs:
                f.write(json.dumps(doc, ensure_ascii=False) + "\n")
