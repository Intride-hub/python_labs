import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from lib.text import *


def main():
    text = sys.stdin.read()

    if not text:
        print("Ввод пуст")
        return

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq_dict = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(freq_dict)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")

    print("Топ-5:")
    top_words = top_n(freq_dict, 5)
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
