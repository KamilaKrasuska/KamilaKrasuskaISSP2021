import szyfrcezara as sc
from datetime import date
klucz=int(input("podaj klucz 1-10:"))
	
plik=open("plik_do_szyfrowania.txt", "r", encoding="utf-8")
d=date.today().strftime("%y%m%d")
plik_zaszyf=open("plik_zaszyfrowany"+str(klucz)+"_"+d+".txt", "w+")


zaszyf=sc.szyfr(plik.read(),klucz)
plik_zaszyf.write(zaszyf)

plik_zaszyf.close()
plik.close()


