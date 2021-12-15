import random
l1=[]
l2=[]
l3=[]
for i in range(0,100):
    l1.append(random.randint(0,20))
for i in range(0,200):
    l2.append(random.randint(0,20))
for i in range(0,300):
    l3.append(random.randint(0,20))

def bab(tab):
    dl=len(tab)
    for i in range(dl):       
        for n in range(0,dl-1-i):           
            if tab[n]>tab[n+1]:
                z=tab[n]
                tab[n]=tab[n+1]
                tab[n+1]=z
    return tab

print(bab(l1))
print(bab(l2))
print(bab(l3))