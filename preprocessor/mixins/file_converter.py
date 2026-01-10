import pathlib
import os

# Самое важное — активируем layout ДО импорта pymupdf4llm
import pymupdf.layout  # ← это активирует улучшенный режим
import pymupdf4llm


class FilePreprocessor:
    # ... остальные методы ...

    def preprocess_file_to_markdown(self, fpath: str, outfpath: str, ext: str = None):
        print(f"Processing file: {fpath}")

        if os.path.exists(outfpath):
            print(f"File {os.path.basename(outfpath)} already preprocessed!")
            return

        try:
            # Открываем документ один раз
            doc = pymupdf.open(fpath)

            # Самые полезные параметры для технической документации (2025–2026 best practice)
            md_text = pymupdf4llm.to_markdown(
                doc,
                pages=None,  # все страницы
                hdr_info=None,  # можно передать свою логику заголовков, если нужно
                write_images=False,  # если не нужны картинки → быстрее и чище
                embed_images=False,
                ignore_code=True,  # часто в тех.доках код не нужен в md
                margins=(50, 50, 50, 50),  # помогают отсечь колонтитулы
                dpi=150,  # для возможного OCR — не слишком много
                # use_ocr=True            # раскомментировать, если есть сканы
            )

            os.makedirs(os.path.dirname(outfpath), exist_ok=True)
            pathlib.Path(outfpath).write_text(md_text, encoding="utf-8")

            print(f"{fpath} converted to {outfpath} (with layout analysis)")

        except Exception as e:
            print(f"Error processing {fpath}: {e}")
        finally:
            if "doc" in locals():
                doc.close()
