import numpy as np
A=np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[1,2,6,-4,-10]])
b=np.array([6,2,-5,17,12])
odp=np.linalg.solve(A,b)
print(odp)