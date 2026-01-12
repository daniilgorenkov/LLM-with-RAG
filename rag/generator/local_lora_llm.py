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

    def generate(self, messages,mode:str="draft"):
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
            if mode == "draft":
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=900,
                    temperature=0.6,
                    top_p=0.9,
                    top_k=50,
                    do_sample=True,
                    repetition_penalty=1.1,
                    eos_token_id=self.tokenizer.eos_token_id,
                    pad_token_id=self.tokenizer.pad_token_id,
                    )
            elif mode == "review":
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=400,
                    temperature=0.2,
                    top_p=0.8,
                    top_k=20,
                    do_sample=True,
                    eos_token_id=self.tokenizer.eos_token_id,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
            elif mode == "rewrite":
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=2048,
                    temperature=0.5,
                    top_p=0.9,
                    top_k=40,
                    do_sample=True,
                    repetition_penalty=1.15,
                    eos_token_id=self.tokenizer.eos_token_id,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
            elif mode == "plan":
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=250,
                    temperature=0.15,
                    top_p=0.75,
                    top_k=20,
                    do_sample=True,
                    repetition_penalty=1.05,
                    eos_token_id=self.tokenizer.eos_token_id,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
            elif mode == "judge":
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=150,
                    temperature=0.1,
                    top_p=0.7,
                    top_k=15,
                    do_sample=True,
                    eos_token_id=self.tokenizer.eos_token_id,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
            elif mode == "finalize":
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=300,
                    temperature=0.25,
                    top_p=0.85,
                    top_k=30,
                    do_sample=True,
                    repetition_penalty=1.05,
                    eos_token_id=self.tokenizer.eos_token_id,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
        generated_tokens = outputs[0][inputs.input_ids.shape[1] :]
        response = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        return response.strip()
