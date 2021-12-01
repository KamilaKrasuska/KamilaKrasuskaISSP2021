klucz = {"a" : "y", "e" : "i", "i" : "o", "o" : "a", "y" : "e"}
klucz2 = {"y":"a", "i":"e", "o":"i", "a":"o", "e":"y"}
nowy=""
def szyf(nowy):
    x=input("Podaj:")
    for i in range(len(x)):
        if x[i] in klucz:
            nowy+=x[i].replace(x[i], klucz[x[i]])
        else:
            nowy+=x[i]
    return(nowy)
def deszyf(y):
    stary=""
    for i in range(len(y)):
        if y[i] in klucz2:
            stary+=y[i].replace(y[i], klucz2[y[i]])
        else:
            stary+=y[i]
    return(stary)
nowy=szyf(nowy)
print(nowy)
print(deszyf(nowy))