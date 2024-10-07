import math as m

beta = 20 * m.pi/180
gama = 27 * m.pi/180

print(((m.cos(beta)-m.sqrt(m.cos(beta)**2-m.cos(gama)**2))/(m.cos(beta)+m.sqrt(m.cos(beta)**2-m.cos(gama)**2)))*m.cos(beta))

