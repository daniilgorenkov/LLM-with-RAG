import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from pathlib import Path
from argparse import ArgumentParser

from config import PreprocessorConfig, Paths
from preprocessor.mixins.file_converter import FilePreprocessor
from preprocessor.mixins.text_clener import TextCleaner
from preprocessor.mixins.markdown_chunker import MarkdownChunker
from utils.custom_logger import set_logger


class PreprocessorRunner:

    def __init__(self, convert: bool = False, logger=None):
        self.logger = logger or set_logger(Paths.LOG_FILE)
        self.convert = convert

        self.file_preprocessor = FilePreprocessor()
        self.text_cleaner = TextCleaner()
        self.markdown_chunker = MarkdownChunker()

        self._ensure_dirs()

    def _ensure_dirs(self):
        for k, v in Paths.__dict__.items():
            if k.isupper() and k not in ["LOG_FILE", "QA_DATASET", "QA_LORA_DATASET"]:
                os.makedirs(v, exist_ok=True)

    # ---------- STAGE 1: RAW → MD ----------

    def convert_raw_docs(self):
        if not self.convert:
            self.logger.debug("Skipping raw → md conversion")
            return

        for ext in PreprocessorConfig.FILE_EXTENTIONS:
            for fname in os.listdir(Paths.RAW_DOCS):
                if Path(fname).suffix.lower() != f".{ext.lower()}":
                    continue

                fpath = os.path.join(Paths.RAW_DOCS, fname)
                out_md = os.path.join(Paths.MD_DOCS, Path(fname).stem + ".md")

                if os.path.exists(out_md):
                    continue

                try:
                    self.logger.info(f"Converting {fname}")
                    self.file_preprocessor.preprocess_file_to_markdown(fpath, out_md, ext)
                except Exception as e:
                    self.logger.exception(f"Failed to convert {fname}: {e}")

    # ---------- STAGE 2: CLEAN → CHUNK ----------

    def clean_and_chunk(self):
        for md_file in os.listdir(Paths.MD_DOCS):
            if not md_file.endswith(".md"):
                continue

            doc_id = Path(md_file).stem
            md_path = os.path.join(Paths.MD_DOCS, md_file)

            try:
                raw = Path(md_path).read_text(encoding="utf-8")

                main_text, references, metadata = self.text_cleaner.clean_text(raw)

                # --- quality gate ---
                if len(main_text) < 800:
                    self.logger.warning(f"{doc_id}: skipped (too small)")
                    continue

                alpha_ratio = sum(c.isalpha() for c in main_text) / max(1, len(main_text))
                if alpha_ratio < 0.35:
                    self.logger.warning(f"{doc_id}: skipped (low quality)")
                    continue

                # --- save clean text ---
                Path(Paths.CLEAN_DOCS, f"{doc_id}.md").write_text(main_text, encoding="utf-8")

                # --- save references ---
                if references:
                    Path(Paths.REFERENCES, f"{doc_id}.references.md").write_text(references, encoding="utf-8")

                # --- save metadata ---
                Path(Paths.METADATA, f"{doc_id}.json").write_text(
                    json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
                )

                # --- chunking ---
                self.logger.info(f"{doc_id}: main_text len={len(main_text)}")
                docs = self.markdown_chunker.chunk(main_text, doc_id, metadata)
                self.markdown_chunker.save_chunks(docs, os.path.join(Paths.CHUNKS, f"{doc_id}.jsonl"))

            except Exception as e:
                self.logger.exception(f"Failed to process {md_file}: {e}")

    def run(self):
        self.convert_raw_docs()
        self.clean_and_chunk()


# ---------- CLI ----------

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--convert", action="store_true", help="Convert RAW → MD")
    args = parser.parse_args()

    runner = PreprocessorRunner(convert=args.convert)
    runner.run()
