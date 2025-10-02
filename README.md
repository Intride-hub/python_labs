Лабораторная работа 1


Задание 1


name=input('Имя:')
age=int(input('Возраст:'))
print(f'Привет, {name}! Через год тебе будет {age+1}.')

![Задание 1](misc/img/lab01/lab01_01.png)


Задание 2

a=float(input('a: ').replace(',','.'))
b=float(input('b: ').replace(',','.'))
sum=a+b
avg=(a+b)/2
print(f'sum={sum:.2f}; avg={avg:.2f}')



![Задание 1](misc/img/lab01/lab01_02.png)


Задание 3


price = float(input("price: "))
discount = float(input("discount: "))
vat = float(input("vat: "))
base= price * (1-discount/100)
vat_amount= base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')

![Задание 1](misc/img/lab01/lab01_03.png)


Задание 4


m=int(input("Минуты: "))
print(f'{m//60}:{m%60}')

![Задание 1](misc/img/lab01/lab01_04.png)


Задание 5


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


![Задание 1](misc/img/lab01/lab01_05.png)



задание 6


n=int(input('in_1: '))
och=0
zaoch=0
for i in range(n):
    line = input(f'in_{i+2}: ').split()
    format=line[-1]
    if format == "True":
        och+=1
    else:
        zaoch+=1
print(f'out: {och} {zaoch}')


![Задание 1](misc/img/lab01/lab01_06.png)



Задание 7

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


![Задание 7](misc/img/lab01/lab01_07.png)

