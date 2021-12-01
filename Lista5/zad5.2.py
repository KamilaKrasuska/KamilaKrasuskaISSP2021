cyf={1 : "jeden", 2 : "dwa", 3 : "trzy", 4 : "cztery", 5 : "pięć", 6 : "sześć", 7 : "siedem", 8 : "osiem", 9 : "dziewięć", 
10 : "dziesięć", 11 :"jedenaście", 12 : "dwanaście", 13 : "trzynaście", 14 : "czternaście", 15 : "piętnaście", 16 : "szesnaście", 17 : "siedemnaście", 18 : "osiemnaście", 19 : "dziewiętnaście", 
20 : "dwadzieścia", 30 : "trzydzieści", 40 : "czterdzieści", 50 : "pięćdziesiąt", 60 : "sześćdziesiąt", 70 : "siedemdziesiąt", 80 : "osiemdziesiąt", 90 : "dziewiędziesiąt", 
100 : "sto", 200 : "dwieście", 300 : "trzysta", 400 : "czterysta", 500 : "pięćset", 600 : "sześćset", 700 : "siedemset", 800 : "osiemset", 900 : "dziewięćset", 1000 : "tysiąc"}
def zam():
    liczba=input("Podaj liczbę od 1 do 1999:")
    x=int(liczba)
    c=list(cyf.keys())
    ls=[]
    dzies=1
    while x>0:
        if int(liczba[-2])==1 and int(liczba[-1])>0 and dzies<100:
            x/=100
            dzies*=100
            j=(int(liczba[-2])*10)+int(liczba[-1])
            ls.insert(0,cyf[j])
        else:
            y=int(x%10)
            x/=10
            for i in c:
                if i==y*dzies:
                    ls.insert(0,cyf[i])
            dzies*=10
    ls=" ".join(ls)
    print(ls)
zam()