import itertools as it

class Listy:
    def __init__(self, li):
        self.li=li
    def podlisty(self):
        dl = len(self.li)
        tab=[]
        for i in range(dl+1):
            tab.extend(list(it.combinations(self.li,i)))
        return tab

t =  [1, 2, 3]
obiekt=Listy(t)
print(obiekt.podlisty())