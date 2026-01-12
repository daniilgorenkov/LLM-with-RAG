import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lora_trainer import LoraQATrainer
import config

if __name__ == "__main__":
    trainer = LoraQATrainer(
        model_name=config.LLMConfig.BASE_MODEL,
        data_path=config.Paths.QA_LORA_DATASET,
        output_dir=os.path.join(config.Paths.DATA, "big_lora_qween"),
        max_steps=config.LoRAConfig.EPOCHS,
    )

    trainer.train()
