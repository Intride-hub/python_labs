<h1>Лабораторная работа 7</h1>

<h2>Задание A</h2>

```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# ----------------------------- normalize -----------------------------


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("\n\t\r", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


def test_normalize_no_casefold():
    assert normalize("ПрИвЕт", casefold=False) == "ПрИвЕт"


def test_normalize_no_yo_replacement():
    assert normalize("ёжик Ёж", yo2e=False) == "ёжик ёж"


# ----------------------------- tokenize -----------------------------


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", ["hello", "world"]),
        ("a-b-c tokens", ["a-b-c", "tokens"]),
        ("", []),
        ("слово1 слово2", ["слово1", "слово2"]),
        ("text-with-dash and word", ["text-with-dash", "and", "word"]),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


# ----------------------------- count_freq -----------------------------


def test_count_freq_basic():
    tokens = ["a", "b", "a", "c", "b", "a"]
    assert count_freq(tokens) == {"a": 3, "b": 2, "c": 1}


def test_count_freq_empty():
    assert count_freq([]) == {}


# ----------------------------- top_n -----------------------------


def test_top_n_basic():
    freq = {"a": 3, "c": 1, "b": 2}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]


def test_top_n_tie_breaker():
    freq = {"b": 3, "a": 3, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 3)]


def test_top_n_more_than_size():
    freq = {"a": 1, "b": 2}
    assert top_n(freq, 10) == [("b", 2), ("a", 1)]
```




<h2>Задание B</h2>



```python
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
```

![Задание 7](misc/img/lab01/lab07/tests.png)
