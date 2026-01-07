from numpy import dtype
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
            dtype=torch.float16,
        )

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForCausalLM.from_pretrained(
            LLMConfig.BASE_MODEL,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
            dtype=torch.float16,
        )

        self.model = PeftModel.from_pretrained(
            base_model,
            LLMConfig.LORA_PATH,
            dtype=torch.float16,
        )

        self.model.eval()

    def _messages_to_prompt(self, messages):
        """
        Convert OpenAI-style chat messages into a single prompt string
        """
        prompt = ""

        for m in messages:
            role = m["role"]
            content = m["content"]

            if role == "system":
                prompt += f"<|system|>\n{content}\n"
            elif role == "user":
                prompt += f"<|user|>\n{content}\n"
            elif role == "assistant":
                prompt += f"<|assistant|>\n{content}\n"

        prompt += "<|assistant|>\n"
        return prompt

    def generate(self, messages, max_new_tokens=256):
        """
        messages: List[{"role": "system"|"user"|"assistant", "content": str}]
        """
        prompt = self._messages_to_prompt(messages)

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
                repetition_penalty=1.5,
                eos_token_id=self.tokenizer.eos_token_id,
            )
        generated_tokens = output[0][inputs.input_ids.shape[1] :]
        response = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        return response.strip()
