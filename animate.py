import graphics as gr
import perspectiveProjection as pP



class animator:
    def __init__(self, perspective:pP.perspective) -> None:
        self.perspective=perspective

    def animate(self):
        windowWidth = 1600
        windowHeight = 900
        window = gr.GraphWin("Structure", windowWidth, windowHeight)
        window.setBackground("black")
        window.setCoords(-1,-1,1,1)



        for e in self.perspective.view:
            Pt1x = float(e[0][0])
            Pt1y = float(e[0][1])
            Pt2x = float(e[1][0])
            Pt2y = float(e[1][1])

            pt1 = gr.Point(Pt1x, Pt1y)
            pt2 = gr.Point(Pt2x, Pt2y)
            Line1 = gr.Line(pt1, pt2)
            Line1.setOutline("white")
            Line1.draw(window)


        key = window.getKey()