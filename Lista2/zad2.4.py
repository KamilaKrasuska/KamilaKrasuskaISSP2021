#a=input("Podaj napis: ")
a="restart"
out=""
pierwsza=a[0]
for i, letter in enumerate(a):
    if (pierwsza==letter and (i!=0)):
        out+="$"
    else:
        out+=letter
print(out)