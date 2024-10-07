import vector3 as v
import numpy as np


class element:
    def __init__(self,start:v.vector3,end:v.vector3) -> None:
        self.start = start
        self.end = end
        self.localXYZ = self.computeDefaultLocalXYZ()
        self.sectionHeight = 0.4
        self.sectionWidth = 0.3
        self.materialE = 30000000000.0
        self.materialG = 12500000000.0
        self.localStiffnessMatrix = self.updateStiffness()
        self.globalStiffnessMatrix = self.transformLocal2Global()


    def computeDefaultLocalXYZ(self):
        matrix = np.zeros((3,3),dtype=float)
        localX = self.end - self.start
        localX.normalize()
        if localX == v.vector3(0,0,1):
            localZ = v.vector3(-1,0,0)
            localY = v.vector3(0,1,0)
        elif localX == v.vector3(0,0,-1):
            localZ = v.vector3(1,0,0)
            localY = v.vector3(0,1,0)
        else:
            localY = v.vector3(-localX.Y,localX.X,0)
            localY.normalize()
            localZ = localX.crossProduct(localY)
            localZ.normalize()
        matrix[0,0] = localX.X
        matrix[0,1] = localX.Y
        matrix[0,2] = localX.Z
        matrix[1,0] = localY.X
        matrix[1,1] = localY.Y
        matrix[1,2] = localY.Z
        matrix[2,0] = localZ.X
        matrix[2,1] = localZ.Y
        matrix[2,2] = localZ.Z
        return matrix
    

    def updateStiffness(self):
        L = (self.end - self.start).abs()
        h = self.sectionHeight
        b = self.sectionWidth
        Iy = h**3*b/12
        Iz = b**3*h/12
        Ix = Iy + Iz
        A = h*b
        E = self.materialE
        G = self.materialG
        K = np.zeros((12,12),dtype=float)
        # Dof order:
        # 0. X translation of start node (Axial compresion)
        # 1. Y translation of start node (transverse deflection)
        # 2. Z translation of start node (transverse deflection)
        # 3. Rotation around X of start node (torsion)
        # 4. Rotation around Y of start node (moment)
        # 5. Rodation around Z of start node (moment)
        # 6. - 11. The same for end node
        K[0,0] = A*E/L
        K[1,1] = 12*E*Iz/(L**3)
        K[2,2] = 12*E*Iy/(L**3)
        K[3,3] = G*Ix/L
        K[4,4] = 4*E*Iy/L
        K[4,2] = -6*E*Iy/(L**2)
        K[2,4] = K[4,2]
        K[5,5] = 4*E*Iz/L
        K[5,1] = 6*E*Iz/(L**2)
        K[1,5] = K[5,1]
        K[6,6] = A*E/L
        K[6,1] = -A*E/L
        K[1,6] = K[6,1]
        K[7,7] = 12*E*Iz/(L**3)
        K[7,5] = -6*E*Iz/(L**2)
        K[5,7] = K[7,5]
        K[7,1] = -12*E*Iz/(L**3)
        K[1,7] = K[7,1]
        K[8,8] = 12*E*Iy/(L**3)
        K[8,4] = 6*E*Iy/(L**2)
        K[4,8] = K[8,4]
        K[8,2] = -12*E*Iy/(L**3)
        K[2,8] = K[8,2]
        K[9,9] = G*Ix/L
        K[9,3] = -G*Ix/L
        K[3,9] = K[9,3]
        K[10,10] = 4*E*Iy/L
        K[10,8] = 6*E*Iy/(L**2)
        K[8,10] = K[10,8]
        K[10,4] = 2*E*Iy/L
        K[4,10] = K[10,4]
        K[10,2] = -6*E*Iy/(L**2)
        K[2,10] = K[10,2]
        K[11,11] = 4*E*Iz/L
        K[11,7] = -6*E*Iz/(L**2)
        K[7,11] = K[11,7]
        K[11,5] = 2*E*Iz/L
        K[5,11] = K[11,5]
        K[11,1] = 6*E*Iz/(L**2)
        K[1,11] = K[11,1]
        return K
    
    def transformLocal2Global(self):
        T = np.zeros((12,12),dtype=float)
        T[:3,:3] = self.localXYZ
        T[3:6,3:6] = self.localXYZ
        T[6:9,6:9] = self.localXYZ
        T[9:,9:] = self.localXYZ
        K = np.matmul(np.matmul(T.transpose(),self.localStiffnessMatrix),T)
        return K





    def __str__(self) -> str:
        a = [self.start.X, self.start.Y, self.start.Z]
        b = [self.end.X, self.end.Y, self.end.Z]
        return str([a,b])




class structure:
    def __init__(self,elements:list[element]) -> None:
        self.elements=elements
        self.nodes=[]
        self.elementEndNodes=[]
        self.computeNodes()
        self.stiffnessMatrix = self.computeStiffnessMatrix()


    def computeNodes(self):
        for e in self.elements:
            nodeIDs=[]
            alreadyAdded = False
            for nid,n in enumerate(self.nodes):
                if e.start == n:
                    alreadyAdded=True
                    nodeIDs.append(nid)
            if not alreadyAdded:
                self.nodes.append(e.start)
                nodeIDs.append(len(self.nodes)-1)
            alreadyAdded = False
            for nid,n in enumerate(self.nodes):
                if e.end == n:
                    alreadyAdded=True
                    nodeIDs.append(nid)
            if not alreadyAdded:
                self.nodes.append(e.end)
                nodeIDs.append(len(self.nodes)-1)
            alreadyAdded = False
            self.elementEndNodes.append(nodeIDs)

    def computeStiffnessMatrix(self):
        numOfNodes = len(self.nodes)
        DoF = 6*numOfNodes
        K = np.zeros((DoF,DoF),dtype=float)
        for i, element in enumerate(self.elements):
            Kcon = np.zeros((DoF,DoF),dtype=float)
            startID = self.elementEndNodes[i][0]
            endID = self.elementEndNodes[i][1]
            Kcon[startID*6:startID*6+6,startID*6:startID*6+6] = element.globalStiffnessMatrix[:6,:6]
            Kcon[endID*6:endID*6+6,endID*6:endID*6+6] = element.globalStiffnessMatrix[6:,6:]
            Kcon[startID*6:startID*6+6,endID*6:endID*6+6] = element.globalStiffnessMatrix[:6,6:]
            Kcon[endID*6:endID*6+6,startID*6:startID*6+6] = element.globalStiffnessMatrix[6:,:6]
            K = K + Kcon
        return K

    def __str__(self) -> str:
        text1 = "structure.elements is: \n"
        text2 = '['
        for e in self.elements:
            text2=text2+str(e)+', \n'
        text2 = text2[0:-3] + ']'
        text3 = "\n \n"

        text4 = "structure.nodes is: \n"
        text5 = '['
        for n in self.nodes:
            text5 = text5+str(n)+', \n'
        text5 = text5[0:-3] + ']'
        text6 = "\n \n"

        text7 = "structure.elementEndNodes is: \n"
        text8 = '['
        for i in self.elementEndNodes:
            text8=text8 + str(i) + ', \n'
        text8 = text8[0:-3] + ']'
        text9 = "\n \n"

        return text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9




