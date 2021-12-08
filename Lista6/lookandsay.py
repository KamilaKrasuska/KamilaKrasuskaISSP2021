def say(n):
    liczba='1'
    for i in range(n):
        dl=len(liczba)
        nowa=[]
        licz=0
        for j in range(dl):
            zap=int(liczba[j])
            if(j!=dl-1):
                if(liczba[j]==liczba[j+1]):
                    licz+=1
                else:
                    nowa.prepend(liczba[j])
                    nowa.prepend(str(licz))
                    licz=0
            else:
                nowa.prepend(liczba[j])
                nowa.prepend(str(licz))
                licz=0
        print(nowa)
say(5)
