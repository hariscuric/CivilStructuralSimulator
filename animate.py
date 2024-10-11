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
        self.activeDiagram = None


    def animate(self):
        
        l = True
        while l:
            self.draw()
            if self.activeDiagram in [0,1,2,3,4,5]:
                self.drawDiagram(self.activeDiagram)
            l = self.keyPress()
            self.undraw()


    def draw(self):
        
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


    def drawDiagram(self, diagramID):
        for e in self.perspective.diagramView:
            Pt1x = float(e[0][0])
            Pt1y = float(e[0][1])
            Pt2x = float(e[1][0])
            Pt2y = float(e[1][1])

            pt1 = gr.Point(Pt1x, Pt1y)
            pt2 = gr.Point(Pt2x, Pt2y)
            self.lines.append(gr.Line(pt1, pt2))
            self.lines[-1].setOutline("red")
            self.lines[-1].draw(self.window)


    def keyPress(self):
        key = self.window.getKey()
        if key == 'Up':
            self.perspective.camera.position = self.perspective.camera.position + (self.perspective.camera.direction * 0.5)
            self.perspective.computeView()

        if key == 'Down':
            self.perspective.camera.position = self.perspective.camera.position - (self.perspective.camera.direction * 0.5)
            self.perspective.computeView()


        if key == 'Right':
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            self.perspective.camera.position = self.perspective.camera.position - (leftDir * 0.5)
            self.perspective.computeView()


        if key == 'Left':
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            self.perspective.camera.position = self.perspective.camera.position + (leftDir * 0.5)
            self.perspective.computeView()

        if key == '8':
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            updir = self.perspective.camera.direction.crossProduct(leftDir)
            updir.normalize()

            self.perspective.camera.position = self.perspective.camera.position + (updir * 0.5)
            self.perspective.computeView()


        if key == '2':
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            updir = self.perspective.camera.direction.crossProduct(leftDir)
            updir.normalize()

            self.perspective.camera.position = self.perspective.camera.position - (updir * 0.5)
            self.perspective.computeView()




        if key == 'a':
            camDir = self.perspective.camera.direction
            angle = m.atan2(camDir.Y,camDir.X)
            A = m.sqrt(camDir.X**2 + camDir.Y**2)
            angle = angle + 2*m.pi/180
            self.perspective.camera.direction.X = A * m.cos(angle)
            self.perspective.camera.direction.Y = A * m.sin(angle)
            self.perspective.camera.direction.normalize()
            self.perspective.computeView()


        if key == 'd':
            camDir = self.perspective.camera.direction
            angle = m.atan2(camDir.Y,camDir.X)
            A = m.sqrt(camDir.X**2 + camDir.Y**2)
            angle = angle - 2*m.pi/180
            self.perspective.camera.direction.X = A * m.cos(angle)
            self.perspective.camera.direction.Y = A * m.sin(angle)
            self.perspective.camera.direction.normalize()
            self.perspective.computeView()


        if key == 'w':
            camDir = self.perspective.camera.direction
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            updir = self.perspective.camera.direction.crossProduct(leftDir)
            updir.normalize()
            newdir = camDir + (updir*0.035)
            newdir.normalize()
            self.perspective.camera.direction = newdir
            self.perspective.computeView()

        if key == 's':
            camDir = self.perspective.camera.direction
            leftDir = v.vector3(-self.perspective.camera.direction.Y, self.perspective.camera.direction.X,0)
            leftDir.normalize()

            updir = self.perspective.camera.direction.crossProduct(leftDir)
            updir.normalize()
            newdir = camDir - (updir*0.035)
            newdir.normalize()
            self.perspective.camera.direction = newdir
            self.perspective.computeView()


        if key == 'f':
            camPos = self.perspective.camera.position
            camDir = self.perspective.camera.direction
            orbitDist = self.perspective.cameraStructureDistance()
            orbitPt = camPos + (camDir*orbitDist)
            relVec = camPos - orbitPt
            angle = m.atan2(relVec.Y,relVec.X)
            A = m.sqrt(relVec.X**2 + relVec.Y**2)
            angle = angle - 2*m.pi/180
            relVec.X = A * m.cos(angle)
            relVec.Y = A * m.sin(angle)
            self.perspective.camera.position = orbitPt + relVec
            self.perspective.camera.direction = relVec.normalize() * (-1)
            self.perspective.computeView()

        if key == 'h':
            camPos = self.perspective.camera.position
            camDir = self.perspective.camera.direction
            orbitDist = self.perspective.cameraStructureDistance()
            orbitPt = camPos + (camDir*orbitDist)
            relVec = camPos - orbitPt
            angle = m.atan2(relVec.Y,relVec.X)
            A = m.sqrt(relVec.X**2 + relVec.Y**2)
            angle = angle + 2*m.pi/180
            relVec.X = A * m.cos(angle)
            relVec.Y = A * m.sin(angle)
            self.perspective.camera.position = orbitPt + relVec
            self.perspective.camera.direction = relVec.normalize() * (-1)
            self.perspective.computeView()



        if key == 't':
            camPos = self.perspective.camera.position
            camDir = self.perspective.camera.direction
            orbitDist = self.perspective.cameraStructureDistance()
            orbitPt = camPos + (camDir*orbitDist)
            relVec = camPos - orbitPt
            angle = m.asin(relVec.Z/orbitDist)
            A = m.sqrt(relVec.X**2 + relVec.Y**2)
            angle = angle + 2*m.pi/180
            if angle >= m.pi/2:
                return True
            relVec.Z = orbitDist * m.sin(angle)
            newA = orbitDist * m.cos(angle)
            relVec.X = relVec.X * newA/A
            relVec.Y = relVec.Y * newA/A
            self.perspective.camera.position = orbitPt + relVec
            self.perspective.camera.direction = relVec.normalize() * (-1)
            self.perspective.computeView()


        if key == 'g':
            camPos = self.perspective.camera.position
            camDir = self.perspective.camera.direction
            orbitDist = self.perspective.cameraStructureDistance()
            orbitPt = camPos + (camDir*orbitDist)
            relVec = camPos - orbitPt
            angle = m.asin(relVec.Z/orbitDist)
            A = m.sqrt(relVec.X**2 + relVec.Y**2)
            angle = angle - 2*m.pi/180
            if angle <= -m.pi/2:
                return True
            relVec.Z = orbitDist * m.sin(angle)
            newA = orbitDist * m.cos(angle)
            relVec.X = relVec.X * newA/A
            relVec.Y = relVec.Y * newA/A
            self.perspective.camera.position = orbitPt + relVec
            self.perspective.camera.direction = relVec.normalize() * (-1)
            self.perspective.computeView()

        if key == 'e':
            if self.perspective.camera.viewAngle>=70:
                return True
            self.perspective.camera.viewAngle = self.perspective.camera.viewAngle + 5
            self.perspective.computeView()

        if key == 'r':
            if self.perspective.camera.viewAngle<=10:
                return True
            self.perspective.camera.viewAngle = self.perspective.camera.viewAngle - 5
            self.perspective.computeView()

        if key == 'm':
            self.activeDiagram = 4

        if key == 'n':
            self.activeDiagram = 0

        if key == 'v':
            self.activeDiagram = 2

        if key == 'b':
            self.activeDiagram = 1

        if key == 'c':
            self.activeDiagram = 5

        if key == 'x':
            self.activeDiagram = 3

        if key =='z':
            self.activeDiagram = None

        if self.activeDiagram in [0,1,2,3,4,5]:
            self.perspective.computeDiagramView(self.activeDiagram)


        if key == 'Escape':
            return False
        
        return True

        


