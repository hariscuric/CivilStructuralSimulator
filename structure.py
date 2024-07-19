import vector3 as v


class element:
    def __init__(self,start:v.vector3,end:v.vector3) -> None:
        self.start = start
        self.end = end

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




