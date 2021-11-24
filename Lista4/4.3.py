import math
x=input("Podajesz stopnie(0) czy radiany(1):")
x=int(x)
y=input("Podaj liczbe:")
y=int(y)
def snr(y):
    r=(y*math.pi)/180
    print(r)
def rns(y):
    s=(y*180)/math.pi
    print(s)

if x==0:
    snr(y)
else:
    rns(y)