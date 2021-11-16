n = input("Podaj n:")
n=int(n)
def f(n):
    a=0
    b=1
    for z in range(n):
        print(a)
        z=a
        a+=b
        b=z
f(n)