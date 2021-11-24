x=input("Podaj liste cyfr: ")
x=list(x.split(" "))
y=sum(int(i) for i in x)
b=1
for i in x:
    b*=int(i)
print("Suma:")
print(y)
print("Iloczyn: ")
print(b)
