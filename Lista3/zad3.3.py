import math
a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")
a=float(a)
b=float(b)
c=float(c)
if a>0:
    d=b*b-(4*a*c)
    #print(d)
    if d<0:
        print("Nie ma pierwiastków")
    elif d==0:
        x=(-b)/(2*a)
        print("x =")
        print(x)
    else:
        pd=math.sqrt(d)
        x1=(-b-pd)/(2*a)
        x2=(-b+pd)/(2*a)
        print("x1 =")
        print(x1)
        print("x2 =")
        print(x2)
else:
    print("To nie jest równanie kwadratowe!!")