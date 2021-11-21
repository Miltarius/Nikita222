a = int(input('Введи число, а я тебе время года'))
def qw(a):
    if a in [3, 4, 5]:
        print('Весна')
    elif a in [6, 7, 8]:
        print('Лето')
    elif a in [9, 10, 11]:
        print('Осень')  
    elif a in [12, 1, 2]:
        print('Зима') 
    return a   
print(qw(a))