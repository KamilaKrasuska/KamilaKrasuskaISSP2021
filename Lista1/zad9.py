import math
z=input("Podaj liczbę zespoloną:")
z=complex(z)
a=z.real
b=z.imag
mod=math.sqrt(a**2+b**2) #abs()
print("Moduł:")
print(mod)
arg=math.atan(b/a)
print("Argument:")
print(arg)
z2=z.conjugate()
print("¯z")
print(z2)

