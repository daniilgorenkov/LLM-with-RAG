import re
import os
import json
from typing import List, Dict


class MarkdownChunker:
    def __init__(
        self,
        max_chars: int = 1200,
        overlap: int = 200,
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
        """
        Делит текст на чанки с overlap
        """
        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = start + self.max_chars
            chunk = text[start:end]
            chunks.append(chunk.strip())

            if end >= text_len:
                break

            start = end - self.overlap

        return chunks

    def chunk(self, text: str, doc_id: str, metadata: Dict) -> List[Dict]:
        """
        Главный метод
        """
        sections = self.split_by_headers(text)
        documents = []

        for sec in sections:
            section_text = "\n".join(sec["content"]).strip()
            if not section_text:
                continue

            chunks = self.chunk_text(section_text)

            for i, chunk in enumerate(chunks):
                documents.append(
                    {
                        "text": chunk,
                        "metadata": {
                            "doc_id": doc_id,
                            "section": sec["header"],
                            "level": sec["level"],
                            "chunk_id": i,
                            "text": section_text,
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
