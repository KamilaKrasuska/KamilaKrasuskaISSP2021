import szyfrcezara as sc
from datetime import date
klucz=int(input("podaj klucz 1-10:"))
	
do_szyf= open("plik_do_szyfrowania.txt", "r", encoding="utf-8")
d=date.today().strftime("%y%m%d")
szyf=open("plik_do_zaszyfrowany"+str(klucz)+"_"+d+".txt", "w+")

do_szyf.close()
szyf.close()
