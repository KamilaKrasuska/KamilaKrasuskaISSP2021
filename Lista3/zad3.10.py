a = range(100,401,1)
b=[]
for x in a:
    z=x
    spr=1
    m=3
    while m>0:
        k=z%10
        g=k%2
        g=int(g)
        if g!=0:
            spr=0
        z=z/10
        m-=1
    if spr==1:
        b.append(x)
print(b)