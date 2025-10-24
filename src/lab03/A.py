def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    res=text
    for char in ['\n','\r','\t']:
        res=res.replace(char,' ')
    
    if yo2e:
        res=res.replace('ё','е').replace('Ё','Е')
    
    if casefold:
        res=res.casefold()
    res=' '.join(res.split())


    return res

print(repr(normalize("ПрИвЕт\nМИр\t")))


print(repr(normalize("ёжик, Ёлка")))


print(repr(normalize("Hello\r\nWorld")))


print(repr(normalize("  двойные   пробелы  ")))



import re

def tokenize(text: str) -> list[str]:
    token = re.findall(r"[\w]+(?:-[\w]+)*", text)
    return token

print(tokenize("привет мир"))

 
print(tokenize("hello,world!!!"))

print(tokenize("по-настоящему круто"))

print(tokenize("2025 год"))

print(tokenize("emoji 😀 не слово"))


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq={}
    for token in tokens:
        if token in freq:
            freq[token]+=1
        else:
            freq[token]=1
    return freq

print(count_freq(["a","b","a","c","b","a"]))

print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sort_it=sorted(freq.items(), key=lambda x: (-x[1],x[0]))
    return sort_it[:n]


print(top_n(count_freq(["a","b","a","c","b","a"]),2))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]),2))







print("Запуск тестов...")
    
        # Тесты normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\r\nWorld") == "hello world"
assert normalize("  двойные   пробелы  ") == "двойные пробелы"
print("✓ normalize тесты пройдены")
    
    # Тесты tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]
assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]
print("✓ tokenize тесты пройдены")
    
    # Тесты count_freq + top_n
freq = count_freq(["a", "b", "a", "c", "b", "a"])
assert freq == {"a": 3, "b": 2, "c": 1}
assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    
    # Тай-брейк по слову при равной частоте
freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
print("✓ count_freq + top_n тесты пройдены")

print("Все тесты успешно пройдены")


