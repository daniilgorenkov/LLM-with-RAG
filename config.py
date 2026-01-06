import os


class Paths:

    WORKDIR = os.getcwd()
    DATA = os.path.join(WORKDIR, "data")
    RAW_DOCS = os.path.join(DATA, "raw_docs")
    CHUNKS = os.path.join(DATA, "chunks")
    CLEAN_DOCS = os.path.join(DATA, "clean_docs")
    REFERENCES = os.path.join(DATA, "references")
    VECTORS = os.path.join(DATA, "vectors")
    LOG_FILE = os.path.join(WORKDIR, "log.log")


class PreprocessorConfig:

    FILE_EXTENTIONS = ["pdf", "docx", "txt"]
    BAD_CHARS = ["\xad\n\n", "\x0c", "\n\n", "\xad", "�", "\u200b", "***f***"]


class LLMConfig:
    ONLINE: bool = False


class CommonConfig:

    DEVICE = "cuda"
