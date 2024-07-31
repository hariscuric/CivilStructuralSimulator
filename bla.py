import vector3 as v
import structure as sss
import numpy as np

import graphics as gr

windowWidth = 900
windowHeight = 600
window = gr.GraphWin("Structure", windowWidth, windowHeight)
window.setBackground("black")
window.setCoords(-1,-1,1,1)

pt1 = gr.Point(0, 0)
pt2 = gr.Point(-0.95, 0.5)
Line1 = gr.Line(pt1, pt2)
Line1.setOutline("white")
Line1.draw(window)



def bla(window):
    key = window.getKey()
    print(key)
    bla(window)


def blabla(window):
    key = window.getMouse()
    print(key)
    blabla(window)

blabla(window)





