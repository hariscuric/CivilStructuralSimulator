import graphics as gr
import perspectiveProjection as pP
import time as t
import vector3 as v
import math as m



class animator:
    def __init__(self, perspective:pP.perspective) -> None:
        self.perspective=perspective
        windowWidth = 1600
        windowHeight = 900
        self.window = gr.GraphWin("Structure", windowWidth, windowHeight)
        self.window.setBackground("black")
        self.window.setCoords(-1,-1,1,1)
        self.lines = []

    def animate(self):
        
        for e in self.perspective.view:
            Pt1x = float(e[0][0])
            Pt1y = float(e[0][1])
            Pt2x = float(e[1][0])
            Pt2y = float(e[1][1])

            pt1 = gr.Point(Pt1x, Pt1y)
            pt2 = gr.Point(Pt2x, Pt2y)
            self.lines.append(gr.Line(pt1, pt2))
            self.lines[-1].setOutline("white")
            self.lines[-1].draw(self.window)

        

    def undraw(self):
        for i in range(len(self.lines)):
            self.lines[i].undraw()

        self.lines = []

    def keyPress(self):
        key = self.window.getKey()
        if key == 'Up':
            self.perspective.camera.position = self.perspective.camera.position + (self.perspective.camera.direction * 0.1)
            self.perspective.computeView()
            self.undraw()
            self.animate()
            self.keyPress()

        if key == 'Down':
            self.perspective.camera.position = self.perspective.camera.position - (self.perspective.camera.direction * 0.1)
            self.perspective.computeView()
            self.undraw()
            self.animate()
            self.keyPress()


        if key == 'Right':
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            self.perspective.camera.position = self.perspective.camera.position - (leftDir * 0.1)
            self.perspective.computeView()
            self.undraw()
            self.animate()
            self.keyPress()


        if key == 'Left':
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            self.perspective.camera.position = self.perspective.camera.position + (leftDir * 0.1)
            self.perspective.computeView()
            self.undraw()
            self.animate()
            self.keyPress()



        if key == 'a':
            camDir = self.perspective.camera.direction
            angle = m.atan2(camDir.Y,camDir.X)
            A = m.sqrt(camDir.X**2 + camDir.Y**2)
            angle = angle + 2*m.pi/180
            self.perspective.camera.direction.X = A * m.cos(angle)
            self.perspective.camera.direction.Y = A * m.sin(angle)
            self.perspective.camera.direction.normalize()
            self.perspective.computeView()
            self.undraw()
            self.animate()
            self.keyPress()


        if key == 'd':
            camDir = self.perspective.camera.direction
            angle = m.atan2(camDir.Y,camDir.X)
            A = m.sqrt(camDir.X**2 + camDir.Y**2)
            angle = angle - 2*m.pi/180
            self.perspective.camera.direction.X = A * m.cos(angle)
            self.perspective.camera.direction.Y = A * m.sin(angle)
            self.perspective.camera.direction.normalize()
            self.perspective.computeView()
            self.undraw()
            self.animate()
            self.keyPress()

        


