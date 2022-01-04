import random
import time
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
        for n in range(0,dl-1):           
            if tab[n]>tab[n+1]:
                z=tab[n]
                tab[n]=tab[n+1]
                tab[n+1]=z
    return tab

start=time.time()
bab(l1)
end=time.time()
print(end-start)

start=time.time()
bab(l2)
end=time.time()
print(end-start)

start=time.time()
bab(l3)
end=time.time()
print(end-start)