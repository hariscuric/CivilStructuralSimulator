import graphics as gr
import perspectiveProjection as pP
import time as t



class animator:
    def __init__(self, perspective:pP.perspective) -> None:
        self.perspective=perspective
        windowWidth = 1600
        windowHeight = 900
        self.window = gr.GraphWin("Structure", windowWidth, windowHeight)
        self.window.setBackground("black")
        self.window.setCoords(-1,-1,1,1)

    def animate(self):
        
        lines = []
        for e in self.perspective.view:
            Pt1x = float(e[0][0])
            Pt1y = float(e[0][1])
            Pt2x = float(e[1][0])
            Pt2y = float(e[1][1])

            pt1 = gr.Point(Pt1x, Pt1y)
            pt2 = gr.Point(Pt2x, Pt2y)
            lines.append(gr.Line(pt1, pt2))
            lines[-1].setOutline("white")
            lines[-1].draw(self.window)


        t.sleep(1/30)

        for i in range(len(lines)):
            
            lines[i].undraw()