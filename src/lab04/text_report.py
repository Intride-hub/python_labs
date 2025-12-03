import sys
import argparse
from pathlib import Path
from collections import Counter

# Добавляем путь к модулям для импорта из lib
sys.path.insert(0, str(Path(__file__).parent.parent))

from io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    from lib.text import normalize, tokenize
    
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def main():
    """Основная функция скрипта."""
    parser = argparse.ArgumentParser(description='Анализ частоты слов в тексте')
    parser.add_argument('--input', '-i', default='src/data/lab04/input.txt',
                       help='Входной файл (по умолчанию: src/data/lab04/input.txt)')
    parser.add_argument('--output', '-o', default='src/data/lab04/report.csv',
                       help='Выходной файл (по умолчанию: src/data/lab04/report.csv)')
    parser.add_argument('--encoding', '-e', default='utf-8',
                       help='Кодировка файла (по умолчанию: utf-8)')
    
    args = parser.parse_args()
    
    try:
        # Чтение и анализ текста с указанной кодировкой
        text = read_text(args.input, encoding=args.encoding)
        freq = frequencies_from_text(text)
        from lib.text import top_n
        sorted_freq = top_n(freq, len(freq))  # Получаем все слова отсортированными
        
        # Подсчет статистики
        total_words = sum(freq.values())
        unique_words = len(freq)
        
        # Запись в CSV
        write_csv(sorted_freq, args.output, header=("word", "count"))
        
        # Вывод статистики в консоль
        print(f"Входной файл: {args.input}")
        print(f"Кодировка: {args.encoding}")
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        
        # Вывод топ-5 слов
        top_5 = sorted_freq[:5]
        for word, count in top_5:
            print(f"{word}:{count}")
            
        print(f"\nОтчет сохранен в: {args.output}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{args.input}' не найден")
        print("Убедитесь, что файл существует")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка декодирования: {e}")
        print(f"Попробуйте указать правильную кодировку: --encoding cp1251")
        sys.exit(1)


if __name__ == "__main__":
    main()