from lib.text import *

import argparse

from pathlib import Path
import sys



def command_cat(path: Path, numbered: bool):
    with path.open('r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            if numbered:
                print(f"{i:4d} | {line.rstrip()}")
            else:
                print(line.rstrip())



def command_stats(path: Path, top: int):
    text = path.read_text(encoding="utf-8")
    norm = normalize(text)

    tokens = tokenize(norm)

    freq = count_freq(tokens)

    words = top_n(freq, top)

    for words, freq in words:
        print(f"{words:15s} {freq}")


def main():
    parser=argparse.ArgumentParser(description='CLI‑утилиты лабораторной №6')
    subparsers = parser.add_subparsers(dest='command')

    cat_parser= subparsers.add_parser('cat', help='Вывести содержимое файла')
    cat_parser.add_argument('--input', required=True)
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    stats_parser=subparsers.add_parser('stats', help='Частоты слов')
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == 'cat':
        command_cat(Path(args.input), args.n)
    elif args.command == "stats":
        command_stats(Path(args.input), args.top)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

