#!/usr/bin/env python3
"""
Скрипт для создания тестового файла в кодировке CP1251
"""
from pathlib import Path

# Создаем директорию если нужно
Path("data/lab04").mkdir(parents=True, exist_ok=True)

# Текст для записи
text = "Привет"

# Записываем в кодировке CP1251
with open("data/lab04/input.txt", "w", encoding="cp1251") as f:
    f.write(text)

print("Файл data/lab04/input.txt создан в кодировке CP1251")
print(f"Текст: '{text}'")