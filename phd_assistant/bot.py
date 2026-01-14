# bot.py
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.types import InputMediaDocument
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from config import Paths
from dotenv import load_dotenv
from runner import run_pipeline


class AskState(StatesGroup):
    waiting_for_question = State()
    generating = State()


class PhDAssistantBot:
    def __init__(self):
        load_dotenv("secret.env")

        self.bot = Bot(os.getenv("TG_BOT_TOKEN"))
        self.dp = Dispatcher(storage=MemoryStorage())

        self.lock = asyncio.Lock()

        self._register_handlers()

    # ---------------- HANDLERS ----------------

    def _register_handlers(self):
        self.dp.message(CommandStart())(self.start)
        self.dp.message(Command("ask"))(self.ask_start)
        self.dp.message(Command("cancel"))(self.cancel)

        self.dp.message(AskState.waiting_for_question, F.text)(self.ask_receive)

        self.dp.message(F.text)(self.fallback)

    async def start(self, message: Message):
        await message.answer(
            "Привет!\n\n"
            "Команды:\n"
            "/ask — задать вопрос\n"
            "/cancel — отменить ожидание\n\n"
            "После /ask просто напиши тему или вопрос."
        )

    async def ask_start(self, message: Message, state: FSMContext):
        if self.lock.locked():
            await message.answer("Сейчас идёт генерация. Подожди окончания ⏳")
            return

        await state.set_state(AskState.waiting_for_question)
        await message.answer("Ок, жду тему или вопрос 👇")

    async def cancel(self, message: Message, state: FSMContext):
        await state.clear()
        await message.answer("Ок, отменил. Можешь снова написать /ask")

    async def ask_receive(self, message: Message, state: FSMContext):
        question = message.text
        await state.set_state(AskState.generating)

        await message.answer("Вопрос принят. Генерирую ответ ⏳")

        async with self.lock:
            try:
                final_text = run_pipeline(question)
            except Exception as e:
                await state.clear()
                await message.answer(f"Ошибка:\n{e}")
                return

        await state.clear()

        # ---------- финальный текст ----------
        await message.answer(final_text[:4096])

        # ---------- сбор файлов ----------
        files = self._collect_files()

        if files:
            await self._send_files(message.chat.id, files)

    async def fallback(self, message: Message):
        await message.answer("Используй команду /ask, чтобы задать вопрос 🙂")

    # ---------------- HELPERS ----------------

    def _collect_files(self) -> list[str]:
        fresh_dir = sorted(os.listdir(Paths.PHD), reverse=True)[0]
        base_path = os.path.join(Paths.PHD, fresh_dir)

        files = []

        for d in os.listdir(base_path):
            dir_path = os.path.join(base_path, d)
            if not os.path.isdir(dir_path):
                continue

            for f in os.listdir(dir_path):
                files.append(os.path.join(dir_path, f))

        return files

    async def _send_files(self, chat_id: int, files: list[str]):
        for i in range(0, len(files), 10):
            batch = files[i : i + 10]
            media = [InputMediaDocument(media=path, caption=os.path.basename(path)) for path in batch]

            await self.bot.send_media_group(chat_id=chat_id, media=media)

    # ---------------- RUN ----------------

    async def run(self):
        await self.dp.start_polling(self.bot)
