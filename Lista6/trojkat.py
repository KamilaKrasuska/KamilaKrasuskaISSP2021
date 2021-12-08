import math
def obwod(a,b,c):
    obw=a+b+c
    return obw
def pole(a,b,c):
    p=obwod(a,b,c)/2
    pol=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return pol
def spr(a,b,c):
    if(a==b==c):
        print("Trojkat jest rownoboczny")
    elif(a==b or c==a or c==b):
        print("Trojkat jest rownoramienny")
    else:
        print("Trojkat jest roznoboczny")
def kat(a,b,c):
    najw=0
    if(a>b and a>c):
        najw=a
        spr2(b,c,najw)
    elif(b>a and b>c):
        najw=b
        spr2(a,c,najw)
    else:
        najw=c
        spr2(a,b,najw)
def spr2(a,b,najw):
    l=a**2+b**2
    p=najw**2
    if(l==p):
        print("Trojkat jest prostokatny")
    elif(l>p):
        print("Trojkat jest ostrokatny")
    elif(l<p):
        print("Trojkat jest rozwartokatny")