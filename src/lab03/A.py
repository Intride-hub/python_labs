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



