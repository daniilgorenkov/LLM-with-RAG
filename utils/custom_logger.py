import logging
import os


def set_logger(log_file_path: str):
    logger = logging.getLogger("logger")

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)

    # ----------------------------------------------------
    # НОВОЕ: Проверяем и создаем директорию
    # ----------------------------------------------------
    log_dir = os.path.dirname(log_file_path)
    if log_dir and not os.path.exists(log_dir):
        # Создаем все промежуточные директории, если они не существуют (makedirs)
        os.makedirs(log_dir, exist_ok=True)
    # ----------------------------------------------------

    # 1. Создаем обработчик для вывода в ФАЙЛ
    file_handler = logging.FileHandler(log_file_path, mode="a", encoding="utf-8")

    # 2. Используем ваш текущий форматтер
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)5s() [PID:%(process)d] - [%(filename)20s():%(lineno)s - %(funcName)33s() ] - %(message)s"
    )

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.propagate = False

    return logger
