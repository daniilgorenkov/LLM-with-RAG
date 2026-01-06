import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
from config import LLMConfig


class LocalLoRALLM:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            LLMConfig.BASE_MODEL,
            trust_remote_code=True,
        )

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForCausalLM.from_pretrained(
            LLMConfig.BASE_MODEL,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
        )

        self.model = PeftModel.from_pretrained(
            base_model,
            LLMConfig.LORA_PATH,
        )

        self.model.eval()

    def generate(self, messages, max_new_tokens=256):
        """
        messages: List[{"role": "system"|"user"|"assistant", "content": str}]
        """

        # Convert chat messages to text
        prompt = self._build_prompt(messages)

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
        ).to(self.model.device)

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                repetition_penalty=1.1,
                eos_token_id=self.tokenizer.eos_token_id,
            )

        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    @staticmethod
    def _build_prompt(messages):
        """
        Simple chat → text conversion (model-agnostic)
        """
        prompt = ""
        for m in messages:
            role = m["role"]
            content = m["content"]

            if role == "system":
                prompt += f"Система:\n{content}\n\n"
            elif role == "user":
                prompt += f"Вопрос:\n{content}\n\n"
            elif role == "assistant":
                prompt += f"Ответ:\n{content}\n\n"

        prompt += "Ответ:\n"
        return prompt
