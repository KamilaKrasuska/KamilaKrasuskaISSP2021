a=input("Podaj pierwsza cyfre:")
a=int(a)
b=input("Podaj druga cyfre:")
b=int(b)
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print(a)