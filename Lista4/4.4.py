n=input("Podaj n:")
n=int(n)
a1=1
q=2
def ciag(n, a1, q):
    an=a1*q**(n-1)
    print(an)

ciag(n, a1, q)