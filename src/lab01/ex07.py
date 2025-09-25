s = input().strip()

ind=-1
for i, char in enumerate(s):
    if char.isupper():
        ind= i
        break
step = 0
for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isalpha():
        step = (i + 1) - ind

res=[]
i=ind
while i < len(s):
    res.append(s[i])
    if s[i] == '.':
        break
    i += step

print(''.join(res)) 
print(step)


