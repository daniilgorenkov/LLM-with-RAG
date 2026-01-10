import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import PreprocessorConfig, Paths

from argparse import ArgumentParser
from preprocessor.mixins.file_converter import FilePreprocessor
from preprocessor.mixins.text_clener import TextCleaner
from preprocessor.mixins.markdown_chunker import MarkdownChunker
from utils.custom_logger import set_logger

logger = set_logger(Paths.LOG_FILE)

args = ArgumentParser()
args.add_argument("--all", action="store_true", help="Run all preprocessors")


args, _ = args.parse_known_args()


class PreprocessorRunner:

    def __init__(self, run_all: bool = False, logger=None):
        logger_obj = logger or set_logger(Paths.LOG_FILE)
        logger_obj.debug("Initializing PreprocessorRunner...")
        self.logger = logger_obj
        self._ensure_dirs()
        self.file_preprocessor = FilePreprocessor()
        self.text_cleaner = TextCleaner()
        self.markdown_chunker = MarkdownChunker()
        self.run_all = run_all

    def _ensure_dirs(self):
        for k, v in Paths.__dict__.items():
            if k.isupper() and k not in ["LOG_FILE", "QA_DATASET", "QA_LORA_DATASET"]:
                os.makedirs(v, exist_ok=True)

    def convert_raw_docs(self):
        """Convert raw documents to markdown files (runs only when run_all is True)."""
        self.logger.debug("Converting raw docs...")
        try:
            files_list = os.listdir(Paths.RAW_DOCS)
        except FileNotFoundError:
            self.logger.warning(f"Raw docs directory not found: {Paths.RAW_DOCS}")
            return

        self.logger.debug(f"Found {len(files_list)} files in raw docs.")
        if not self.run_all:
            self.logger.debug("Skipping conversion of raw docs because run_all is False.")
            return

        for ext in PreprocessorConfig.FILE_EXTENTIONS:
            raw_doc_fpaths = [os.path.join(Paths.RAW_DOCS, f) for f in files_list if f.lower().endswith(ext.lower())]
            self.logger.debug(f"Processing {len(raw_doc_fpaths)} files with extension .{ext}...")
            for fpath in raw_doc_fpaths:
                try:
                    self.logger.debug(f"Converting file: {os.path.basename(fpath)}")
                    outfpath = os.path.join(Paths.CLEAN_DOCS, os.path.basename(fpath).replace(f".{ext}", ".md"))
                    self.logger.debug(f"outpath: {outfpath}")
                    self.file_preprocessor.preprocess_file_to_markdown(fpath, outfpath, ext)
                except Exception as e:
                    self.logger.exception(f"Failed to convert {fpath}: {e}")

    def clean_and_chunk(self):
        """Clean all markdown files and save chunks and references."""
        self.logger.debug("Cleaning and chunking markdown docs...")
        try:
            md_docs = [f for f in os.listdir(Paths.CLEAN_DOCS) if f.endswith(".md")]
        except FileNotFoundError:
            self.logger.warning(f"Clean docs directory not found: {Paths.CLEAN_DOCS}")
            return

        for md_doc in md_docs:
            outfpath = os.path.join(Paths.CLEAN_DOCS, md_doc)
            try:
                with open(outfpath, "r", encoding="utf-8") as f:
                    raw = f.read()

                self.logger.debug(f"Cleaning text for {md_doc}...")
                main_text, references, metadata = self.text_cleaner.clean_text(raw)
                doc_id = os.path.splitext(os.path.basename(outfpath))[0]

                # 1️⃣ сохранить чистый текст
                clean_path = os.path.join(Paths.CLEAN_DOCS, f"{doc_id}.md")
                with open(clean_path, "w", encoding="utf-8") as f:
                    f.write(main_text)

                # 2️⃣ сохранить references отдельно
                if references:
                    ref_path = os.path.join(Paths.REFERENCES, f"{doc_id}.references.md")
                    with open(ref_path, "w", encoding="utf-8") as f:
                        f.write(references)

                # 3️⃣ чанки
                docs = self.markdown_chunker.chunk(main_text, doc_id, metadata)

                # 4️⃣ сохранить чанки
                chunks_path = os.path.join(Paths.CHUNKS, f"{doc_id}.jsonl")
                self.markdown_chunker.save_chunks(docs, chunks_path)
                self.logger.debug(f"Saved chunks to {chunks_path}")
            except Exception as e:
                self.logger.exception(f"Failed to process {outfpath}: {e}")

    def run_preprocess(self):
        """High level runner: convert raw docs (optional) then clean and chunk."""
        self.logger.debug("Starting preprocessing run...")
        self.convert_raw_docs()
        self.clean_and_chunk()


if __name__ == "__main__":
    preprocessor = PreprocessorRunner(False)
    preprocessor.run_preprocess()
