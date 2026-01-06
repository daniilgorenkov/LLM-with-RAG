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
    QA_DATASET = os.path.join(DATA, "qa_dataset.jsonl")
    QA_LORA_DATASET = os.path.join(DATA, f"qa_lora.jsonl")
    LORA_QWEEN = os.path.join(DATA, "lora_qween")


class PreprocessorConfig:

    FILE_EXTENTIONS = ["pdf", "docx", "txt"]
    BAD_CHARS = ["\xad\n\n", "\x0c", "\n\n", "\xad", "�", "\u200b", "***f***"]


class LLMConfig:
    ONLINE: bool = False


class CommonConfig:

    DEVICE = "cuda"


class LoRAConfig:

    R = 8
    LORA_ALPHA = 16
    LORA_DROPOUT = 0.05
    TARGET_MODULES = ["q_proj", "v_proj"]
    BATCH_SIZE = 1
    EPOCHS = 300
    GRAD_ACCUM = 8
