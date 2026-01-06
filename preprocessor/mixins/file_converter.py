import pymupdf4llm
import os
import pathlib
from config import Paths


class FilePreprocessor:

    def _check_if_md_exists(self, file_path: str):
        return os.path.exists(file_path)

    def preprocess_file_to_markdown(self, fpath: str, outfpath: str, ext: str = None):
        """
        :param fpath: путь к исходному файлу (pdf, docx и т.д.)
        :param outfpath: путь, куда нужно сохранить .md файл
        :param ext: расширение исходного файла (необязательно, если не используется)
        """
        print(f"Processing file: {fpath}")

        # Проверяем, существует ли уже целевой .md файл
        if not self._check_if_md_exists(outfpath):
            # Конвертируем PDF в Markdown с помощью pymupdf4llm
            md_text = pymupdf4llm.to_markdown(fpath)

            # Создаём директорию, если её нет
            os.makedirs(os.path.dirname(outfpath), exist_ok=True)

            # Сохраняем в нужное место
            pathlib.Path(outfpath).write_text(
                md_text, encoding="utf-8"
            )  # лучше write_text, а не write_bytes + encode вручную

            print(f"{fpath} converted to {outfpath}")
        else:
            print(f"File {os.path.basename(outfpath)} already preprocessed!")
