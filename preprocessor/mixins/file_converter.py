import pathlib
import os
import re

import pymupdf.layout
import pymupdf
import pymupdf4llm


class FilePreprocessor:

    def _postprocess_md(self, text: str) -> str:
        # 1. Склеиваем строки, если они оборвались посреди предложения
        text = re.sub(r"(?<![.\n])\n(?!\n)", " ", text)

        # 2. Убираем лишние пробелы
        text = re.sub(r"[ \t]+", " ", text)

        # 3. Нормализуем списки
        text = re.sub(r"\n([•\-–])", r"\n\n\1", text)

        return text.strip()

    def preprocess_file_to_markdown(self, fpath: str, outfpath: str, ext: str = None):
        print(f"Processing file: {fpath}")

        if os.path.exists(outfpath):
            print(f"File {os.path.basename(outfpath)} already preprocessed!")
            return

        os.makedirs(os.path.dirname(outfpath), exist_ok=True)

        try:
            doc = pymupdf.open(fpath)

            ignore_code = "gost" not in fpath.lower()

            md_text = pymupdf4llm.to_markdown(
                doc,
                pages=None,
                hdr_info=None,
                write_images=False,
                embed_images=False,
                ignore_code=ignore_code,
                margins=(50, 50, 50, 50),
                dpi=150,
                use_ocr=False,
            )

            # если текста подозрительно мало — пробуем OCR
            if len(md_text.strip()) < 500:
                print("Low text volume detected → retry with OCR")
                md_text = pymupdf4llm.to_markdown(
                    doc,
                    pages=None,
                    write_images=False,
                    embed_images=False,
                    ignore_code=ignore_code,
                    margins=(50, 50, 50, 50),
                    dpi=200,
                    use_ocr=True,
                )

            md_text = self._postprocess_md(md_text)

            pathlib.Path(outfpath).write_text(md_text, encoding="utf-8")

            print(f"{fpath} converted to {outfpath}")

        except Exception as e:
            print(f"Error processing {fpath}: {e}")

        finally:
            if "doc" in locals():
                doc.close()
