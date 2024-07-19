import vector3 as v


class element:
    def __init__(self,start:v.vector3,end:v.vector3) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        a = str(self.start)
        b = str(self.end)
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
        text2 = self.elements.__str__()
        text3 = "\n \n"

        text4 = "structure.nodes is: \n"
        text5 = self.nodes.__str__()
        text6 = "\n \n"

        text7 = "structure.elementEndNodes is: \n"
        text8 = self.elementEndNodes.__str__()
        text9 = "\n \n"

        return text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9




