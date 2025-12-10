import pytest
import json
import csv
from pathlib import Path
from src.lib.json_csv import json_to_csv, csv_to_json


# ------------------------------ JSON → CSV ------------------------------


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert set(rows[0].keys()) == {"age", "name"}
    assert rows[0]["name"] == "Alice"
    assert rows[1]["age"] == "25"  # CSV → строки


# ------------------------------ CSV → JSON ------------------------------


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "input.csv"
    dst = tmp_path / "output.json"

    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Alice", "22"])
        writer.writerow(["Bob", "25"])

    csv_to_json(str(src), str(dst))

    data = json.loads(dst.read_text(encoding="utf-8"))

    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["age"] == "25"  # строки, как в CSV


# ------------------------------ NEGATIVE CASES ------------------------------


def test_json_to_csv_nonexistent_file(tmp_path: Path):
    bad = tmp_path / "missing.json"
    with pytest.raises(FileNotFoundError):
        json_to_csv(str(bad), "out.csv")


def test_json_to_csv_bad_json(tmp_path: Path):
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"
    src.write_text("{НЕВАЛИДНЫЙ JSON}", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_empty_list(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_nonexistent_file(tmp_path: Path):
    bad = tmp_path / "missing.csv"
    with pytest.raises(FileNotFoundError):
        csv_to_json(str(bad), "out.json")


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "empty.csv"
    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(src.with_suffix(".json")))
