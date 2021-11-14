def d():
    p = input('Введи символы')
    a = []
    while p != "":
        a.append(p)
        p = input('Введи символы')
        print(a)
    return a
print(d())