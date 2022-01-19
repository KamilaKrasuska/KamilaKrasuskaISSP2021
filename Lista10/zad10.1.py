import math

class Kolo:
    def __init__(self, r):
        self.r=r
    def obwod(self):
        return 2 * math.pi * self.r
    def pole(self):
        return math.pi * self.r ** 2
    
obiekt=Kolo(4)
print(obiekt.obwod())
print(obiekt.pole())       
        