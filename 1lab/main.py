import random
mx = 0
mn = 9999
st = int(input('Введите количество учеников: '))
cl = int(input('Введите количество предметов: '))
a = [[random.randint(1, 5) for x in range(st)] for y in range(cl)]
ans = []
for i in range(len(a)):
    for j in range(len(a[i])):
        sr = sum(a[i])/len(a[i])
        mx = max(a[i])
        mn = min(a[i])
    ans.append(sr)
    print('студент',i + 1, a[i], mx, mn, sr)
print(ans.index(max(ans)) + 1, ans.index(min(ans)) + 1)
