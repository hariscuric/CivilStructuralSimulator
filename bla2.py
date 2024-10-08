import math as m
import numpy as np

# beta = 20 * m.pi/180
# gama = 27 * m.pi/180

# print(((m.cos(beta)-m.sqrt(m.cos(beta)**2-m.cos(gama)**2))/(m.cos(beta)+m.sqrt(m.cos(beta)**2-m.cos(gama)**2)))*m.cos(beta))

a = np.array([[1,2,3],[1,0,3],[5,5,5]],dtype=float)
b = np.array([1,1,1],dtype=float)
c = np.matmul(a.transpose(),b)





d = a.transpose()
print(d)
print(a)
