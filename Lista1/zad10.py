import cmath
z=0+1j
sz=cmath.sin(z)
a1=sz.real
b1=sz.imag
cz=cmath.cos(z)
a2=cz.real
b2=cz.imag
print("Sin(z) =")
print(sz)
print("cz. rzeczywista:")
print(a1)
print("cz. urojona:")
print(b1)
print("Cos(z) =")
print(cz)
print("cz. rzeczywista:")
print(a2)
print("cz. urojona:")
print(b2)
print("Zależność: ")
print(sz**2+cz**2) #zależność jest prawie spełniona, jednak 
#wynika to najprawdopodobie z zaokrąglania zmiennych przez program