a = input('Введи выражение')
z = a.count('(') - a.count(')')
if z > 0:
    print('Не хватает закрывающейся скобки')
elif z < 0:
    print('Не хватает открывающейся скобки')
else:
    ('Всё хорошо')