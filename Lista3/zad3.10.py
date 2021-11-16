a = range(100,400,1)
b=[]
for x in a:
    z=x
    spr=1
    while z>0:
        k=z%10
        if k%2!=0:
            spr=0
        z/=10
    if spr==1:
        b.append(x)
print(b)