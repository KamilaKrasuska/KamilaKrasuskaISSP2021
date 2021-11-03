import math
a=input("Wpisz a: ")
b=input("Wpisz b: ")
kat=input("Wpisz kat: ")
a=int(a)
b=int(b)
kat=int(kat)
kat=math.radians(kat)
skat=math.sin(kat)
p=(1/2)*a*b*skat
print(p)