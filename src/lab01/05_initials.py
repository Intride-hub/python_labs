name=input('ФИО: ')
namecl=name.strip()
words = namecl.split()
init=[]
for w in words:
    fir = w[0]
    up = fir.upper()
    init.append(up)
initre=''.join(init)
lenth=len(namecl)
print(f'Инициалы: {initre}')
print(f'Длина (символы): {lenth}')