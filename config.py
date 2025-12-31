import os


class Paths:

    WORKDIR = os.getcwd()
    DATA = os.path.join(WORKDIR, "data")
    RAW_DOCS = os.path.join(DATA, "raw_docs")
    CHUNKS = os.path.join(DATA, "chunks")
    CLEAN_DOCS = os.path.join(DATA, "clean_docs")
    REFERENCES = os.path.join(DATA, "references")


class PreprocessorConfig:

    FILE_EXTENTIONS = ["pdf", "docx", "txt"]
