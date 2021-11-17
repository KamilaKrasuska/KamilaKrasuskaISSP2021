import re

spr=0
while spr==0:
    haslo=input("Podaj hasło: ")
    x=re.search("[a-z]", haslo)
    if x:
        x=re.search("[A-Z]", haslo)
        if x:
            x=re.search("[0-9]", haslo)
            if x:
                x=re.search("[@#$]", haslo)
                if x:
                    z=len(haslo)
                    if z >= 6 and z <=16:
                        print("Hasło jest poprawne")
                        spr=1
    if spr==0:
        print("Hasło nie spełnia wymaganiań")