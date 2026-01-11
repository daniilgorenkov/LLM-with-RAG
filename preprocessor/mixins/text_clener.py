import re
from config import PreprocessorConfig
from markdowncleaner import MarkdownCleaner


class TextCleaner:

    def __init__(self):
        self.cleaner = MarkdownCleaner()

    FORMULA_TOKEN = " [FORMULA] "

    @staticmethod
    def repl(match):
        return TextCleaner.FORMULA_TOKEN

    def replace_display_formulas(self, text: str) -> str:
        # $$ ... $$
        text = re.sub(r"\$\$.*?\$\$", self.repl, text, flags=re.S)
        # \[ ... \]
        text = re.sub(r"\\\[.*?\\\]", self.repl, text, flags=re.S)
        return text

    def replace_inline_formulas(self, text: str) -> str:
        # $...$
        text = re.sub(r"\$(.*?)\$", self.repl, text)
        # \( ... \)
        text = re.sub(r"\\\(.*?\\\)", self.repl, text)
        return text

    def extract_metadata(self, text: str):
        metadata = {}

        # DOI
        doi = re.search(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", text, re.I)
        if doi:
            metadata["doi"] = doi.group(0)

        # Journal + year
        journal = re.search(r"J\s+Rail.*Transit|Proc\s+IMechE.*", text)
        if journal:
            metadata["journal"] = journal.group(0)

        year = re.search(r"\b(19|20)\d{2}\b", text)
        if year:
            metadata["year"] = year.group(0)

        return metadata

    def cleanup_markdown_artifacts(self, text: str) -> str:
        # _text_ → text (markdown emphasis)
        text = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", text)
        return text

    def remove_latex_commands(self, text: str) -> str:
        # \command{content} -> content
        text = re.sub(r"\\[a-zA-Z]+\{(.*?)\}", r"\1", text)
        # \command
        text = re.sub(r"\\[a-zA-Z]+", "", text)
        return text

    def fix_scientific_notation(self, text: str) -> str:
        # 10 [−][4] → 10^-4
        text = re.sub(r"10\s*\[\-?\]\s*\[\s*(\d+)\s*\]", r"10^-\1", text)

        return text

    def replace_broken_formulas(self, text: str) -> str:
        return re.sub(r".*=\s*σ.*\(\d+\)", " [FORMULA: neural network equation] ", text)

    def normalize_newlines(self, text: str) -> str:
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def normalize_tables(self, text: str) -> str:
        # Если строка содержит много чисел и единиц измерения — добавляем перенос
        text = re.sub(r"(\d)\s+([A-Z][a-z])", r"\1\n\2", text)
        return text

    def remove_front_matter(self, text: str) -> str:
        # только если реально в начале документа
        return re.sub(r"^(?:\s{0,200})(abstract|introduction)\b", r"\1", text, flags=re.I)

    def remove_repeated_math_tokens(self, text: str) -> str:
        return re.sub(r"(\*\*?[a-zA-Z]\*\*\s*[ij]){3,}", "[BROKEN_FORMULA]", text)

    def remove_strikethrough(self, text: str) -> str:
        return re.sub(r"~~.*?~~", "", text)

    def remove_garbled_lines(self, text: str) -> str:
        lines = []
        for line in text.splitlines():
            if re.search(r"[�ðÞ]", line):
                continue
            lines.append(line)
        return "\n".join(lines)

    def remove_bad_chars(self, text: str) -> str:
        for char in PreprocessorConfig.BAD_CHARS:
            text = text.replace(char, "")
        return text

    def remove_lonely_math_lines(self, text: str) -> str:
        return re.sub(r"^\s*[=+*/()\[\]^]{5,}\s*$", "", text, flags=re.M)

    def normalize_markdown_tables(self, text: str) -> str:
        """
        Преобразует markdown-таблицы в читаемый текст
        """
        lines = text.splitlines()
        new_lines = []
        table_buffer = []

        def flush_table(table):
            if not table:
                return []

            rows = [r.strip("|").split("|") for r in table]
            rows = [[c.replace("<br>", " ").strip() for c in row] for row in rows]

            header = rows[0]
            body = rows[1:]

            out = []
            for row in body:
                for h, v in zip(header, row):
                    if v:
                        out.append(f"{h}: {v}")
                out.append("")  # пустая строка между записями
            return out

        for line in lines:
            if line.strip().startswith("|") and "|" in line:
                table_buffer.append(line)
            else:
                if table_buffer:
                    new_lines.extend(flush_table(table_buffer))
                    table_buffer = []
                new_lines.append(line)

        if table_buffer:
            new_lines.extend(flush_table(table_buffer))

        return "\n".join(new_lines)

    def split_references(self, text: str):
        pattern = r"\n(?:#+\s*)?(references|bibliography|literature|список литературы)\b.*\n"
        parts = re.split(pattern, text, flags=re.I)

        if len(parts) > 1:
            main_text = parts[0]
            references = "\n".join(parts[1:])
            return main_text.strip(), references.strip()

        return text, None

    def remove_html_artifacts(self, text: str) -> str:
        # 1. Удаляем script и style целиком
        text = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", text, flags=re.I | re.S)

        # 2. Заменяем <br> и <p> на переносы строк
        text = re.sub(r"<\s*(br|p)\s*/?\s*>", "\n", text, flags=re.I)

        # 3. Удаляем все остальные теги, но сохраняем текст
        text = re.sub(r"<[^>]+>", "", text)

        # 4. HTML entities
        html_entities = {
            "&nbsp;": " ",
            "&lt;": "<",
            "&gt;": ">",
            "&amp;": "&",
            "&quot;": '"',
            "&#39;": "'",
        }

        for k, v in html_entities.items():
            text = text.replace(k, v)

        return text

    def clean_text(self, text: str):
        text = self.cleaner.clean_markdown_string(text)
        text = self.remove_html_artifacts(text)
        metadata = self.extract_metadata(text)

        text = self.normalize_markdown_tables(text)
        text = self.replace_display_formulas(text)
        text = self.replace_inline_formulas(text)

        text = self.remove_latex_commands(text)
        text = self.fix_scientific_notation(text)

        text = self.normalize_newlines(text)
        text = self.cleanup_markdown_artifacts(text)

        text = self.remove_bad_chars(text)
        text = self.remove_garbled_lines(text)

        text = self.remove_repeated_math_tokens(text)
        text = self.remove_strikethrough(text)

        text = self.remove_lonely_math_lines(text)

        # финальная нормализация формул
        text = re.sub(r"(?:\[FORMULA\]\s*){2,}", self.FORMULA_TOKEN, text)

        text = self.remove_front_matter(text)

        main_text, references = self.split_references(text)
        return main_text, references, metadata
