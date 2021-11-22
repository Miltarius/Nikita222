from home31 import dqw


def q(a):
    r = list(a)
    if a == r:
        return "True"
    else:
        return "False"
a = dqw()
print(q(a))
assert q(1, 2, 3, 4, 5, 6, 7) == "True"
assert q(1, 2, 1, 4, 2, 6, 7) == "False"