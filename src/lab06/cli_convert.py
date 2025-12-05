import argparse
from src.lib.json_csv import json_to_csv, csv_to_json
from src.lib.csv_xlsx import csv_to_xlsx
from pathlib import Path


def ensure_file_exists(path: Path, parser):
    if not path.exists():
        parser.error(f"Ошибка: входной файл не найден: {path}")
    if not path.is_file():
        parser.error(f"Ошибка: путь не является файлом: {path}")

def command_json_to_csv(inp: Path, out: Path, parser):
    ensure_file_exists(inp, parser)
    try:
        json_to_csv(inp, out)
        print(f"CSV сохранён в: {out}")
    except Exception as e:
        parser.error(f"Ошибка конвертации JSON → CSV: {e}")


def command_csv_to_json(inp: Path, out: Path, parser):
    ensure_file_exists(inp, parser)
    try:
        csv_to_json(inp, out)
        print(f"JSON сохранён в: {out}")
    except Exception as e:
        parser.error(f"Ошибка конвертации CSV → JSON: {e}")


def command_csv_to_xlsx(inp: Path, out: Path, parser):
    ensure_file_exists(inp, parser)
    try:
        csv_to_xlsx(inp, out)
        print(f"XLSX сохранён в: {out}")
    except Exception as e:
        parser.error(f"Ошибка конвертации CSV → XLSX: {e}")




def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help='входящий файл')
    p1.add_argument("--out", dest="output", required=True, help='выходящий файл')

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help='входящий файл')
    p2.add_argument("--out", dest="output", required=True, help='выходящий файл')

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help='входящий файл')
    p3.add_argument("--out", dest="output", required=True, help='выходящий файл')

    args = parser.parse_args()

    inp = Path(args.input)
    out = Path(args.output)

    if args.cmd == "json2csv":
        command_json_to_csv(inp, out, parser)

    elif args.cmd == "csv2json":
        command_csv_to_json(inp, out, parser)

    elif args.cmd == "csv2xlsx":
        command_csv_to_xlsx(inp, out, parser)

    else:
        parser.error("Ошибка: команда не указана. Используйте --help.")

if __name__ == "__main__":
    main()