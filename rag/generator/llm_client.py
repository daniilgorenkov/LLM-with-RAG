import os
import re
from config import CommonConfig, Paths, LLMConfig
from openai import OpenAI, RateLimitError
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from utils.custom_logger import set_logger

logger = set_logger(Paths.LOG_FILE)


class LLMClient:
    def __init__(self, model="gpt-4o-mini", online: bool = True):

        self.online = online
        logger.debug(f"Online: {self.online}")
        if not self.online:
            self.tokenizer, self.model = self._load_offline_model()
        else:
            from dotenv import load_dotenv

            load_dotenv("secret.env")
            self.client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
            self.model = model

    def _load_offline_model(self):

        self.tokenizer = AutoTokenizer.from_pretrained(LLMConfig.BASE_MODEL)
        self.model = AutoModelForCausalLM.from_pretrained(LLMConfig.BASE_MODEL, device_map="auto", dtype=torch.float16)
        return self.tokenizer, self.model

    def _check_model_status(self):
        try:
            answer = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": "Напиши краткое описание (примерно 250–300 слов) "
                        "истории развития железнодорожного транспорта в Европе с 19 века до наших дней.",
                    }
                ],
                temperature=0.2,
                max_tokens=300,
            )
            if answer:
                return True
        except RateLimitError as e:
            logger.debug(f"Rate limit exceeded for openai model {self.model}, swithing to local model.")
            return False

    def _generate_offline(self, messages: list, mode: str = "qa"):

        prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        inputs = self.tokenizer(prompt, return_tensors="pt").to(CommonConfig.DEVICE)

        if mode == "qa":
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=300,
                temperature=0.15,
                top_p=0.8,
                top_k=30,
                do_sample=True,
                eos_token_id=self.tokenizer.eos_token_id,
                pad_token_id=self.tokenizer.pad_token_id,
            )
        elif mode == "draft":
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
                max_new_tokens=1100,
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
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def generate(self, messages: list, mode: str = "qa") -> str:
        """
        :param: mode:str accepts `qa`, `draft`, `review`, `rewrite`, `plan`, `judge`
        """
        if self.online:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.1,
                )
                return response.choices[0].message.content.strip()
            except RateLimitError as e:
                logger.debug(f"Rate limit exceeded for openai model {self.model}, swithing to local model.")
                self.online = False
                self.tokenizer, self.model = self._load_offline_model()
                return self._generate_offline(messages, mode)
        else:
            return self._generate_offline(messages, mode)

    @staticmethod
    def format_llm_answer(raw_answer: str):
        """
        Надёжный парсер для разных стилей вывода Qwen
        Возвращает dict или None
        """
        text = raw_answer.split("\nassistant\n")[-1]

        # Случай "Недостаточно данных"
        if "недостаточно" in text.lower() and ("данных" in text.lower() or "информации" in text.lower()):
            return {"question": "Недостаточно данных", "answer": "Недостаточно данных"}

        # Удаляем возможное жирное форматирование
        text = re.sub(r"\*\*|\*", "", text)

        # Ищем вопрос и ответ по разным шаблонам
        patterns = [
            r"Вопрос:\s*(.+?)(?:\n\n?Ответ:|\nОтвет:|$)",
            r"Технический вопрос:\s*(.+?)(?:\n\n?Ответ:|\nОтвет:|$)",
            r"Вопрос\s*[:：]\s*(.+?)(?:\n\n?Ответ\s*[:：]|\nОтвет\s*[:：]|$)",
            r"Question\s*[:：]\s*(.+?)(?:\n\n?Answer\s*[:：]|\nAnswer\s*[:：]|$)",
            r"Одно техническое задание\s*[:：]\s*(.+?)(?:\n\n?Ответ\s*[:：]|\Краткий ответ\s*[:：]|$)",
            r"Одно техническое исследование\s*[:：]\s*(.+?)(?:\n\n?Ответ\s*[:：]|\Краткий ответ\s*[:：]|$)",
            r"Одним из технических вопросов может быть\s*[:：]\s*(.+?)(?:\n\n?Ответ\s*[:：]|\Краткий ответ\s*[:：]|$)",
            r"Одиночный технический вопрос\s*[:：]\s*(.+?)(?:\n\n?Ответ\s*[:：]|\Краткий ответ\s*[:：]|$)",
            r"Технический вопрос\s*[:：]\s*(.+?)(?:\n\n?Краткий ответ*[:：]|$)",
            r"(.+?[?!.])\s*(?:Ответ:|Краткий ответ:)(.+)",
            r"^(.+?[?!.])\s*(.+)$",
            r"(.+?[?!.])\s*(.+)",
        ]

        question = None
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                question = match.group(1).strip()
                # Ответ — всё после вопроса
                answer_start = match.end()
                answer = text[answer_start:].strip()
                answer = re.sub(r"^Ответ\s*[:：]\s*", "", answer, flags=re.IGNORECASE).strip()
                break

        if question and answer:
            return {"question": question, "answer": answer}

        # Если ничего не нашли — возвращаем как есть (для отладки)
        logger.warning(f"Не удалось распарсить ответ:\n{text}")
        return None

    def ask_direct_llm(self, prompt: str, formatted: bool = True):

        messages = [{"role": "user", "content": prompt}]

        text = self.generate(messages)

        if formatted:
            return self.format_llm_answer(text)
        else:
            return text
