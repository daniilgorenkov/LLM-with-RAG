#!/usr/bin/env bash

set -e  # выход при любой ошибке

echo "Клонируем репозиторий..."
if [ -d "LLM-with-RAG" ]; then
    echo "Папка LLM-with-RAG уже существует. Пропускаем клонирование."
    cd LLM-with-RAG
    git pull origin main || echo "Не удалось обновить репозиторий, продолжаем..."
else
    git clone https://github.com/daniilgorenkov/LLM-with-RAG.git
    cd LLM-with-RAG
fi

echo "Создаём виртуальное окружение..."
python3 -m venv .venv

echo "Активируем окружение..."
source .venv/bin/activate

echo "Обновляем pip, wheel, setuptools..."
pip install --upgrade pip wheel setuptools

echo "Устанавливаем зависимости..."
pip install -r requirements.txt

echo "Готово! Активировано окружение: .venv"
echo "Для запуска используй:"
echo "source .venv/bin/activate && python3 путь/к/скрипту.py"

git config --global user.name "DaniilGorenkov" && git config --global user.email "gorenkov.daniil@gmail.com"