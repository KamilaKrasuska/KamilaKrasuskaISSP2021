import random
p=open("pesel.txt", "w+")

def los(a, b):
    return random.randrange(a, b)

for i in range(10):
    c=[]
    c.append(los(0,3))
    p.write(str(c[0]))

    c.append(los(0,10))
    p.write(str(c[1]))

    m=los(0,13)
    m+=20
    m=str(m)
    c.append(int(m[0]))
    c.append(int(m[1]))
    p.write(m)

    if m == 2:
        dz=los(0,30)
    elif m == 1 or 3 or 5 or 7 or 8 or 11:
        dz=los(0,32)
    else:
        dz=los(0,31)

    if dz<10:
        c.append(0)
        p.write("0")
        c.append(dz)
    else:
        dz=str(dz)
        c.append(int(dz[0]))
        c.append(int(dz[1]))
    p.write(str(dz))

    c.append(los(0,10))
    p.write(str(c[6]))
    c.append(los(0,10))
    p.write(str(c[7]))
    c.append(los(0,10))
    p.write(str(c[8]))
    c.append(los(0,10))
    p.write(str(c[9]))

    sum=0
    ind=0
    for j in c:  
        if ind==0 or ind==4 or ind==8:
            mn=j*1
        elif ind==1 or ind==5 or ind==9:
            mn=j*3
        elif ind==2 or ind==6:
            mn=j*7
        else:
            mn=j*9
        if mn>9:
            mn%=10
        sum+=mn
        ind+=1
    if sum>9:
        sum%=10
    if sum==0:
        c.append(0)
    else:
        c.append(10-sum)
    p.write(str(c[10]))

p.close()