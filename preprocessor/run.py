from importlib import metadata
import sys
import os

# print(sys.path)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import PreprocessorConfig, Paths

from argparse import ArgumentParser
from mixins.file_converter import FilePreprocessor
from mixins.text_clener import TextCleaner
from mixins.markdown_chunker import MarkdownChunker


args = ArgumentParser()
args.add_argument("--all", action="store_true", help="Run all preprocessors")


args, _ = args.parse_known_args()


class PreprocessorRunner:

    def __init__(self):
        self.file_prerpocessor = FilePreprocessor()
        self.text_cleaner = TextCleaner()
        self.markdown_chunker = MarkdownChunker()

    def run_preprocess(self):
        print("Starting preprocessing...")
        files_list = os.listdir(Paths.RAW_DOCS)
        print(f"Found {len(files_list)} files in raw docs.")
        for ext in PreprocessorConfig.FILE_EXTENTIONS:

            raw_doc_fpaths = [os.path.join(Paths.RAW_DOCS, f) for f in files_list if f.endswith(ext)]
            print(f"Processing {len(raw_doc_fpaths)} files with extension .{ext}...")
            if raw_doc_fpaths:
                for fpath in raw_doc_fpaths:
                    print(f"Processing file: {fpath}")
                    outfpath = os.path.join(Paths.CLEAN_DOCS, os.path.basename(fpath).replace(f".{ext}", ".md"))
                    if args.all:
                        print("see all arg")
                        self.file_prerpocessor.preprocess_file_to_markdown(fpath, outfpath, ext)

            md_docs = [f for f in os.listdir(Paths.CLEAN_DOCS) if f.endswith(".md")]
            print("see text cleanup arg")
            for md_doc in md_docs:
                outfpath = os.path.join(Paths.CLEAN_DOCS, md_doc)
                with open(outfpath, "r", encoding="utf-8") as f:
                    raw = f.read()

                print("Cleaning text...")
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
                print(f"Saved chunks to {chunks_path}")


if __name__ == "__main__":
    preprocessor = PreprocessorRunner()
    preprocessor.run_preprocess()
