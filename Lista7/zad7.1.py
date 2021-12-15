import time
n = input("Podaj n:")
n=int(n)
def fibiter(n):
    a=0
    b=1
    for z in range(n):
        print(a)
        z=a
        a+=b
        b=z
def fibrek(n):
    if n<1:
        return 0
    if n<2:
        return 1
    return fibrek(n-1) + fibrek(n-2)
#fibiter(n)
print(fibrek(n))