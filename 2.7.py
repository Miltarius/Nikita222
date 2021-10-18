from random import randint
s = int(input('Введите число '))
a = randint(0, 100)
while s != a:
    if s > a:
        print('Загаданное число меньше')
    elif s < a:
        print('Загаданное число больше')
    s = int(input('Введите число '))
print('Вы угадали') 