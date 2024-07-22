import vector3 as v
import structure as sss
import numpy as np

import graphics as gr

windowWidth = 1600
windowHeight = 900
window = gr.GraphWin("Structure", windowWidth, windowHeight)
window.setBackground("black")
window.setCoords(-1,-1,1,1)

pt1 = gr.Point(0, 0)
pt2 = gr.Point(-0.95, 0.5)
Line1 = gr.Line(pt1, pt2)
Line1.setOutline("white")
Line1.draw(window)


key = window.getKey()





