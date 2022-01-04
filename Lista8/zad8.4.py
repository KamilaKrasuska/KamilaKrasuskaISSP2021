p=open("pesel.txt", "r")
d=open("odczyt_pesel.txt", "w+")

j=0
for i in range(10):
    pesel=p.read(10)
    sum=0
    ind=0
    rok=""
    miesiac=""
    dzien=""
    for j in pesel:
        j=int(j)

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
        
        if ind==0 or ind==1:
            rok+=str(j)
        if ind==2:
            miesiac+=str(j-2)
        elif ind==3:
            miesiac+=str(j)
        if ind==4 or ind==5:
            dzien+=str(j)
        if ind==9:
            if j%2==0:
                plec="kobieta"
            else:
                plec="mezczyzna"
        ind+=1

    if sum>9:
        sum%=10
    if sum==0:
        sum=0
    else:
        sum=10-sum
    k=p.read(1)
    if(int(k)==sum):
        d.write(pesel+k+":\n data urodzenia "+dzien+"-"+miesiac+"-20"+rok+";\t plec: "+plec+"\n")
d.close()
p.close()