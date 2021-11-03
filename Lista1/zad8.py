import math
x=1
while x>0:
    a=input("Podaj a:")
    b=input("Podaj b (mniejsze od a):") 
    a=int(a)
    b=int(b)
    if (b<a):
        x=0
Z=b%a
Z*=Z+3
print(Z)