import itertools as it

class Listy:
    def __init__(self, li):
        self.li=li
    def podlisty(self):
        dl = len(self.li)
        tab=[]
        x=list(it.combinations(self.li,3))
        for j in x:
            suma=sum(j)
            if suma==0:
                tab.append(j)
        return tab

t =  [1, 2, 3, -1, -2, -3]
obiekt=Listy(t)
print(obiekt.podlisty())