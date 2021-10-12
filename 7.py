a = int(input('Введите число a'))
b = int(input('Введите число b'))
c = 0
for x in range(a, b + 1):
    if x % 5 == 0:
        c += x
print(c)
