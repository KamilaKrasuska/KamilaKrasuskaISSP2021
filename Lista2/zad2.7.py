l=[(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
def drugi(l):
    return l[1]
l=sorted(l, key=drugi)
print(l)