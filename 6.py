a = int(input('Введи строку'))
k = int(input('Введите цифру'))
s = []
for i in a:
    if i.isdigit():
        s.append(i)
print(k, '-ая цифра в строке', s[k - 1])