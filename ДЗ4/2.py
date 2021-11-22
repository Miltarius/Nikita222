def asd(n):
    q = 1
    for q in range(2, n + 1):
        q *= 1
    return q
n = int(input('Введите число'))
print(asd(n))
assert asd(3) == 6
assert asd(4) == 24