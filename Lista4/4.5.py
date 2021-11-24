x=input("Podaj liste cyfr:")
x=list(x.split(" "))
print(x)
for i in x:
    z=1
    for j in range(1, int(i)+1):
        z*=j
    print(z)