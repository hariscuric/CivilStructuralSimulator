import math as m
import numpy as np

# beta = 20 * m.pi/180
# gama = 27 * m.pi/180

# print(((m.cos(beta)-m.sqrt(m.cos(beta)**2-m.cos(gama)**2))/(m.cos(beta)+m.sqrt(m.cos(beta)**2-m.cos(gama)**2)))*m.cos(beta))

a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
c = a+b
print(c[0,:])
