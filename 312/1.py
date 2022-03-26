from math import *


class Fraction: 
        def __init__(self, top=0, bottom=1): 
            self.num = top 
            self.den = bottom 

        def input(self): 
            self.num = int(input("Введите числитель: "))         
            self.den = int(input("Введите знаменатель: "))  
            if self.den == 0: 
                print ("error") 

        def __str__(self): 
            return f"{self.num}/{self.den}"
 
        def reduce(self): 
            c = gcd(self.num, self.den) 
            self.nom = self.num // c
            self.den = self.den // c

class IrreduceadFraction(Fraction): 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()

    def inner(self, *args, **kwargs) -> None:
        super().inner(*args, **kwargs)
        self.reduce()

q = IrreduceadFraction(6, 3)
y = IrreduceadFraction(6, 4)
i = IrreduceadFraction(0, 1)