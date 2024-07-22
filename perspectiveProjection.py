import structure as sss
import vector3 as v
import numpy as np
import math as m

class camera:
    def __init__(self, position = v.vector3(0,0,0),direction = v.vector3(1,0,0), viewAngle=35) -> None:
        self.position = position
        self.direction = direction
        self.viewAngle = viewAngle
        





class perspective:
    def __init__(self, structure:sss.structure, camera=camera()) -> None:
        self.structure=structure
        self.camera=camera
        self.view = self.computeView()

    def computeView(self):
        T = computeTransformationMatrix(self.camera)
        camPosVec = np.array([[self.camera.position.X],[self.camera.position.Y],[self.camera.position.Z]])
        elements = []
        for e in self.structure.elements:
            start = np.array([[e.start.X],[e.start.Y],[e.start.Z]])
            end = np.array([[e.end.X],[e.end.Y],[e.end.Z]])
            Nstart = np.matmul(T,start-camPosVec)
            Nend = np.matmul(T,end-camPosVec)
            if float(Nstart[0])<1 and float(Nend[0])<1:
                continue
            if float(Nstart[0])<1:
                Y = float((1-Nend[0])*(Nstart[1]-Nend[1])/(Nstart[0]-Nend[0]))
                Z = float((1-Nend[0])*(Nstart[2]-Nend[2])/(Nstart[0]-Nend[0]))
                Nstart = np.array([[1],[Y],[Z]])
            if float(Nend[0])<1:
                Y = float((1-Nstart[0])*(Nend[1]-Nstart[1])/(Nend[0]-Nstart[0]))
                Z = float((1-Nstart[0])*(Nend[2]-Nstart[2])/(Nend[0]-Nstart[0]))
                Nend = np.array([[1],[Y],[Z]])
            
            NstartProject = np.array([-Nstart[1]/Nstart[0],Nstart[2]/Nstart[0]])
            NendProject = np.array([-Nend[1]/Nend[0],Nend[2]/Nend[0]])
            NstartProject = NstartProject/m.tan(self.camera.viewAngle*m.pi/180)
            NendProject = NendProject/m.tan(self.camera.viewAngle*m.pi/180)
            elements.append([NstartProject, NendProject])
        return elements


    








def computeTransformationMatrix(camera:camera):
    T11 = camera.direction.X
    T12 = camera.direction.Y
    T13 = camera.direction.Z
    if T12 == 0:
        T21 = 0
        T22 = 1
        T31 = -T13
        T32 = 0
        T33 = T11
    else:
        T21 = m.sqrt(1/(1+(T11/T12)**2))
        T22 = m.sqrt(((T11/T12)**2)/(1+(T11/T12)**2))
        T31 = -T13*m.sqrt(((T11/T12)**2)/(1+(T11/T12)**2))
        T32 = -T13*m.sqrt(1/(1+(T11/T12)**2))
        T33 = T11*m.sqrt(((T11/T12)**2)/(1+(T11/T12)**2)) - T12*m.sqrt(1/(1+(T11/T12)**2))
    T23 = 0
    T = np.array([[T11, T12, T13], [T21, T22, T23], [T31, T32, T33]])
    return T