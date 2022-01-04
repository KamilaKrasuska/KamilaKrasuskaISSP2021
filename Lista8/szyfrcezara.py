def szyfr(z,klucz):
    nowe=""
    for i in z:
        litera=ord(i)
        if((litera>=65 and litera<=90) or (litera>=97 and litera<=122)):
            litera+=klucz
            if(litera>90 and litera<97):
                litera-=26
            elif(litera>122):
                litera-=26
        nowe+=(chr(litera))
    return nowe
def desz(z,klucz):
    nowe=""
    for i in z:
        litera=ord(i)
        if((litera>=65 and litera<=90) or (litera>=97 and litera<=122)):
            litera-=klucz
            if(litera<65):
                litera+=26
            elif(litera>90 and litera<97):
                litera+=26
        nowe+=(chr(litera))
    return nowe