from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
import torch
import config
import os


class LoraQATrainer:
    def __init__(
        self,
        model_name: str,
        data_path: str,
        output_dir: str,
        max_steps: int = 500,
        lr: float = 2e-4,
        batch_size: int = 1,
        grad_accum: int = 8,
    ):
        self.model_name = model_name
        self.data_path = data_path
        self.output_dir = output_dir

        self.max_steps = max_steps
        self.lr = lr
        self.batch_size = batch_size
        self.grad_accum = grad_accum

        self.tokenizer = None
        self.model = None
        self.dataset = None
        self.trainer = None

        os.makedirs(self.output_dir, exist_ok=True)

    # -------------------------
    # 1. Tokenizer
    # -------------------------
    def load_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            trust_remote_code=True,
            use_fast=True,
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"  # важно для training

    # -------------------------
    # 2. Base model (4-bit) — ПРАВИЛЬНО через BitsAndBytesConfig
    # -------------------------
    def load_base_model(self):
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,  # ← fp16, а не bfloat16!
            bnb_4bit_use_double_quant=True,
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
            dtype=torch.float16,
        )

        # Важно: подготовка модели для 4-bit обучения
        self.model = prepare_model_for_kbit_training(self.model)

    # -------------------------
    # 3. Attach LoRA
    # -------------------------
    def attach_lora(self):
        lora_config = LoraConfig(
            r=config.LoRAConfig.R,
            lora_alpha=config.LoRAConfig.LORA_ALPHA,
            lora_dropout=config.LoRAConfig.LORA_DROPOUT,
            bias="none",
            task_type="CAUSAL_LM",
            target_modules=config.LoRAConfig.TARGET_MODULES,
        )

        self.model = get_peft_model(self.model, lora_config)
        self.model.print_trainable_parameters()

    # -------------------------
    # 4. Dataset
    # -------------------------
    def load_dataset(self):
        self.dataset = load_dataset("json", data_files=self.data_path, split="train")

    # -------------------------
    # 5. Formatting — ИСПРАВЛЕНО: возвращаем строку, а не конкатенацию
    # -------------------------
    @staticmethod
    def format_example(example):
        text = ""
        if example.get("instruction"):
            text += f"Вопрос:\n{example['instruction']}\n\n"
        if example.get("input"):
            text += f"{example['input']}\n\n"
        if example.get("output"):
            text += f"Ответ:\n{example['output']}"
        return text

    # -------------------------
    # 6. Trainer
    # -------------------------
    def build_trainer(self):
        args = TrainingArguments(
            output_dir=self.output_dir,
            per_device_train_batch_size=self.batch_size,
            gradient_accumulation_steps=self.grad_accum,
            learning_rate=self.lr,
            max_steps=self.max_steps,
            logging_steps=10,
            save_steps=self.max_steps // 3,
            save_total_limit=3,
            optim="paged_adamw_8bit",  # отлично работает с 4bit
            # fp16=True,
            bf16=False,
            report_to="none",
            warmup_steps=20,
            gradient_checkpointing=True,  # экономит память
            dataloader_drop_last=True,
            auto_find_batch_size=False,  # Иногда помогает
            use_legacy_prediction_loop=False,  # Стандартное значение
        )

        self.trainer = SFTTrainer(
            model=self.model,
            args=args,
            train_dataset=self.dataset,
            formatting_func=self.format_example,
            # max_seq_length=2048,  # явно укажи, чтобы избежать предупреждений
            # packing=False,  # или True для ускорения
        )

    # -------------------------
    # Full pipeline
    # -------------------------
    def train(self):
        self.load_tokenizer()
        self.load_base_model()
        self.attach_lora()
        self.load_dataset()
        self.build_trainer()

        print("Начинаем обучение LoRA...")
        self.trainer.train()
        print("Обучение завершено. Сохраняем модель...")
        self.trainer.save_model(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)
        print(f"Модель сохранена в {self.output_dir}")
