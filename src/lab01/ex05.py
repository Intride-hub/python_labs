name=input('ФИО: ')
namecl=name.strip()
words = namecl.split()
init=[]
for w in words:
    fir = w[0]
    up = fir.upper()
    init.append(up)
initre=''.join(init)
lenth=sum(len(word) for word in words) + (len(words)-1)
print(f'Инициалы: {initre}')
print(f'Длина (символы): {lenth}')
