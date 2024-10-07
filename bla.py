# import vector3 as v
# import structure as sss
# import numpy as np


# import graphics as gr

# windowWidth = 900
# windowHeight = 600
# window = gr.GraphWin("Structure", windowWidth, windowHeight)
# window.setBackground("black")
# window.setCoords(-1,-1,1,1)

# pt1 = gr.Point(0, 0)
# pt2 = gr.Point(-0.95, 0.5)
# Line1 = gr.Line(pt1, pt2)
# Line1.setOutline("white")
# Line1.draw(window)



# def bla(window):
#     key = window.getKey()
#     print(key)
#     bla(window)


# def blabla(window):
#     key = window.getMouse()
#     print(key)
#     blabla(window)

# blabla(window)

import math as m

spacingBWBars = 15
barDiam = 10
RebarStrength = 420
slabThickness = 20
concreteCover = 3


As = 100/spacingBWBars * barDiam**2*m.pi/4
F = RebarStrength/1.15 * As
M = F * (slabThickness - 2*concreteCover)*0.01
print("slab moment capacity:")
print(M/1000)

reinforcementRatio = As/1000/200
print("slab reinforcementRatio:")
print(reinforcementRatio)

activeConcrete = F*1.15*1.2/20/1000
print("slab active concrete:")
print(activeConcrete)



b = 35
barSize = 14
barNum = 5
As = barNum * barSize**2 * m.pi/4
F = As * RebarStrength/1.15
M = F * (b-2*5)*0.01


print("beam capacity:")
print(M/1000)

activeConcrete = F/20/250
print("beam active concrete:")
print(activeConcrete)

reinforcementRatio = As/250/(b*10)
print("beam reinforcementRatio:")
print(reinforcementRatio)




