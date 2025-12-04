import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    json_p = Path(json_path)
    csv_p = Path(csv_path)

    if not json_p.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    # --- загрузка JSON ---
    with json_p.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("JSON-файл поврежден или имеет неверный формат")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Пустой JSON или неподдерживаемая структура — ожидается список словарей")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать список словарей")

    # Определение всех возможных ключей (универсальная таблица)
    all_keys = sorted({key for obj in data for key in obj.keys()})

    # --- запись CSV ---
    with csv_p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_keys)
        writer.writeheader()

        for row in data:
            writer.writerow({k: row.get(k, "") for k in all_keys})


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_p = Path(csv_path)
    json_p = Path(json_path)

    if not csv_p.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with csv_p.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовка")

        if len(rows) == 0:
            raise ValueError("CSV пуст — нет строк данных")

    # --- запись JSON ---
    with json_p.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 3:
#         print("Использование: python -m src.lab05.json_csv <input> <output>")
#         sys.exit(1)

#     input_path = sys.argv[1]
#     output_path = sys.argv[2]

#     try:
#         if input_path.endswith(".json") and output_path.endswith(".csv"):
#             json_to_csv(input_path, output_path)
#         elif input_path.endswith(".csv") and output_path.endswith(".json"):
#             csv_to_json(input_path, output_path)
#         else:
#             raise ValueError("Неверное расширение файлов")
#         print(f"Файл успешно создан: {output_path}")
#     except Exception as e:
#         print(f"Ошибка: {e}")