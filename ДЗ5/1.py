a = [1, 3, 7, 4, 2, 5, 6]
a = sorted(a)
def s(a, q):
    e = 0
    p = len(a) - 1
    while e <= p:
        s = (e + p) // 2
        if a[s] == q:
            return s 
        elif a[s] < q:
            e = s + 1 
        elif a[s] > q:
            p = s - 1
    return None
q = int(input('Введите'))
print(s(a, q))
assert s([], 2) == 3
assert s([1, 2, 4, 6, 3, 7, 5], 9) == 7
assert s([1, 3, 7, 4, 2, 5, 6], 9) == None