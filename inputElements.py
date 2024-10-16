import csv
import vector3 as v
import structure as sss
import numpy as np

def inputElements():

    elements=[]


    with open('inputElementCoordinates.txt') as fileObj:
        reader_obj = csv.reader(fileObj)
        for i, row in enumerate(reader_obj):
            if i ==0:
                continue 
            x1=float(row[0])
            y1=float(row[1])
            z1=float(row[2])
            x2=float(row[3])
            y2=float(row[4])
            z2=float(row[5])

            elements.append(sss.element(v.vector3(x1,y1,z1),v.vector3(x2,y2,z2)))

    with open('inputElementForces.txt') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            forces = np.array([float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5])],dtype=float)
            elements[i-1].globalDistForces = forces
            elements[i-1].Global2LocalForces()

    with open('inputElementSectionMaterial.txt') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            elements[i-1].sectionHeight = float(row[0])
            elements[i-1].sectionWidth = float(row[1])
            elements[i-1].materialE = float(row[2])
            elements[i-1].materialG = float(row[3])
            elements[i-1].update()


    
    return elements