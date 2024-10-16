import graphics as gr
import inputElements as inp
import structure as sss
import perspectiveProjection as pP
import vector3 as v
import animate
import math as m


def main():

    print("This is structural analysis program")

    elements = inp.inputElements()
    structure = sss.structure(elements)

    # print('Major moment diagram of 3\'rd element is:')
    # print(structure.elements[2].diagrams[4,:])

    # print('Nodal deformations (3 deflections and 3 rotations) of 8\'th node are:')
    # print(structure.NodalDisplacements[7*6:7*6+6])

    # exit()


    camera = pP.camera(v.vector3(10,10,10),v.vector3(-1,-1,-1).normalize())

    perspective = pP.perspective(structure,camera)
    animator = animate.animator(perspective)
    
    animator.animate()

    



    

main()