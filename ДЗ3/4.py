lst = list(input('Введи список'))
def f(lst):
    for x in set(lst):
        y = lst.count(x)
        print(x, ':', y)		   
print(f(lst))
