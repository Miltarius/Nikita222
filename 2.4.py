a = input('Введи выражение')
z = a.count('(') - a.count(')')
if z > 0:
    print('Не хватает закрывающейся скобкок-', z)
elif z < 0:
    print('Не хватает открывающейся скобок-', z)
else:
    ('Всё хорошо')