s={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
a=input()
c=len(a)

def rzym(a):
    nowa=0
    for i in range(c):
        if  i!=c-1:
            if s[a[i]]<s[a[i+1]]:
                nowa-=s[a[i]]
            else:
                nowa+=s[a[i]]
        else:
            nowa+=s[a[i]]
    return(nowa)
print(rzym(a))