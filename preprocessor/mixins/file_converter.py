import pymupdf4llm
import os
import pathlib
from config import Paths


class FilePreprocessor:

    def _check_if_md_exists(self, file_path: str):
        return os.path.exists(file_path)

    def _clear_converted_files(self, file_path: str):
        os.remove(file_path)
        print(f"File {file_path} removed")

    def preprocess_file_to_markdown(self, fpath: str, outfpath: str, ext: str):
        """:param: ext: string without dot aka `pdf` or `docx`"""

        print(f"Processing file: {fpath}")
        outfpath = fpath.replace(f".{ext}", ".md")
        if not self._check_if_md_exists(outfpath):
            md_text = pymupdf4llm.to_markdown(fpath)
            pathlib.Path(outfpath).write_bytes(md_text.encode())  # Save as Markdown, or convert to plain text if needed
            print(f"{fpath} converted to {outfpath}")
            self._clear_converted_files(fpath)
        else:
            try:
                self._clear_converted_files(fpath)
            except Exception:
                pass
            print(f"File {os.path.basename(outfpath)} already preprocessed!")
