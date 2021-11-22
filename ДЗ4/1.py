from home31 import dqw


def eee(a, p):
    for x in range(p):
        a = a[-1:] + a[:-1]
        return a
a = dqw()
p = int(input('На сколько сместить'))
print(eee(a, p))
assert eee([1, 2, 3, 4, 5,], 1) == [5, 1, 2, 3, 4]
assert eee([1, 2, 3, 4, 5,], 2) == [4, 5, 1, 2, 3]
assert eee([1, 2, 3, 4, 5,], 3) == [3, 4, 5, 1, 2]