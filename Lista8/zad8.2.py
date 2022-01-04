import szyfrcezara as sc
import re
from datetime import date

plik=input("podaj sciezke pliku: ")

plik_zaszyf=open(plik, "r")
d=date.today().strftime("%y%m%d")
spr=0
for i in plik:
    if spr==0 and i.isnumeric():
        klucz=i
        spr=1

plik_odszyf=open("plik_odszyfrowany"+str(klucz)+"_"+d+".txt", "w+")
zaszyf=sc.desz(plik_zaszyf.read(),klucz)
plik_odszyf.write(zaszyf)