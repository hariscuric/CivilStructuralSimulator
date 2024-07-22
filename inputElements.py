import csv
import vector3 as v
import structure as sss

def inputElements(filename):

    elements=[]


    with open(filename) as fileObj:
        reader_obj = csv.reader(fileObj)
        for row in reader_obj: 
            x1=float(row[0])
            y1=float(row[1])
            z1=float(row[2])
            x2=float(row[3])
            y2=float(row[4])
            z2=float(row[5])

            elements.append(sss.element(v.vector3(x1,y1,z1),v.vector3(x2,y2,z2)))

    
    return elements