import graphics as gr
import inputElements as inp
import structure as sss


def main():

    print("This is structural analysis program")

    #Input structural geometry
        #input frame element start-end point coordinates
            #list and enumerate the nodes based on start-end point coordinates of elements
            #tie elements to nodes
        #specify element properties
            #specify materials
            #specify cross section
                #compute section moduli
                #build element stiffness matrix
                #transform element stiffness matrix to global coordiates
        #Compute global structural stiffness matrix

    #Visualize the geometry

    #Input the loads

    #Compute the responses



    print("input file name: ")
    filename = input()

    elements = inp.inputElements(filename)
    structure = sss.structure(elements)

    print(structure.nodes[0])

    

main()