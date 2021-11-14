def f():
    lst = list(input('Введи список'))
    for x in set(lst):
        y = lst.count(x)
        print(x, ':', y)		   
print(f())
