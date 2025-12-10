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
