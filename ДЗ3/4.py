p = input('Введи символы')
def f(p):
    a = []
    while p != "":
        a.append(p)
        p = input('Введи символы')
    return p 
 
    
f(p)
for x in set(f(p)):
    y = f(p).count(x)
    print(x, '|', y)		   
print(f(p))
