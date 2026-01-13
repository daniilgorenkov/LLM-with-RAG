import requests
import os

def send_as_album(bot_token: str, chat_id: int, file_paths: list[str]):
    url = f"https://api.telegram.org/bot{bot_token}/sendMediaGroup"

    media = []
    files = {}

    for i, path in enumerate(file_paths[:10]):  # лимит Telegram — 10 файлов
        file_name = os.path.basename(path)
        key = f"file{i}"
        media.append({
            "type": "document",
            "media": f"attach://{key}",
            "caption": file_name
        })
        files[key] = open(path, "rb")

    if media:
        data = {
            "chat_id": chat_id,
            "media": str(media).replace("'", '"')  # Telegram требует JSON в двойных кавычках
        }

        response = requests.post(url, data=data, files=files)

        # Закрываем файлы
        for f in files.values():
            f.close()

        if response.status_code == 200:
            print("Отправлен альбом из", len(media), "файлов")
        else:
            print("Ошибка при отправке:", response.text)
    else:
        print("Нет файлов для отправки")

