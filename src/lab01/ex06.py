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


