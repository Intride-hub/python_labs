s=input('in: ')
def stroka(s):
    start = next(i for i, c in enumerate(s) if c.isupper())
    step = (next(i for i, c in enumerate(s) if c.isdigit()) + 1) - start
    result = ""
    for i in range(start, len(s), step):
        result += s[i]
        if s[i] == ".":
            break
    return result


print(f'out: {stroka(s)}')