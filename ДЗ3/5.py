def ds(q):
    return sum(q) / len(q) 


p = input('Введи символы')
a = []
while p != "":
    a.append(float(p))
    p = input('Введи символы')
    print(a)
print(ds(a))