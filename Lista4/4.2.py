x=input("Podaj liste cyfr:")
x=list(set(x.split(" ")))
for i in x:
    if i not in x:
        x.append(i)
print(x)