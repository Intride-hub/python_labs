from src.lib.text import *

import argparse

from pathlib import Path
import sys

def ensure_file_exists(path: Path, parser):
    if not path.exists():
        parser.error(f"Ошибка: входной файл не найден: {path}")
    if not path.is_file():
        parser.error(f"Ошибка: путь не является файлом: {path}")

def command_cat(path: Path, numbered: bool, parser):
    ensure_file_exists(path, parser)
    try:
        with path.open('r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                if numbered:
                    print(f"{i:4d} | {line.rstrip()}")
                else:
                    print(line.rstrip())
    except Exception as e:
        parser.error(f"Ошибка при чтении файла: {e}")



def command_stats(path: Path, top: int, parser):
    ensure_file_exists(path, parser)
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        parser.error(f"Ошибка при чтении файла: {e}")
    
    try:
        norm = normalize(text)
        tokens = tokenize(norm)
        freq = count_freq(tokens)
        words = top_n(freq, top)

        for words, freq in words:
           print(f"{words:15s} {freq}")

    except Exception as e:
        parser.error(f"Ошибка при чтении файла: {e}")

def main():
    parser=argparse.ArgumentParser(description='CLI‑утилиты лабораторной №6')
    subparsers = parser.add_subparsers(dest='command')

    cat_parser= subparsers.add_parser('cat', help='Вывести содержимое файла')
    cat_parser.add_argument('--input', required=True, help='входящий файл')
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    stats_parser=subparsers.add_parser('stats', help='Частоты слов')
    stats_parser.add_argument("--input", required=True, help='входящий файл')
    stats_parser.add_argument("--top", type=int, default=5, help='вывести топ слов')

    args = parser.parse_args()

    if args.command == 'cat':
        command_cat(Path(args.input), args.n, parser)
    elif args.command == "stats":
        command_stats(Path(args.input), args.top, parser)
    else:
        parser.error("Ошибка: команда не указана. Посмотрите помощь через --help.")


if __name__ == "__main__":
    main()

