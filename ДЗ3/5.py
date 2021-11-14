def ds(q):
    w = sum(q) / len(q)
    print('Cреднее арифметическое = ', w)  
q = list() 
n = input('Введите ')  
while n != '':
    q.append(n)
    n = input('Введите ') 
ds(q)