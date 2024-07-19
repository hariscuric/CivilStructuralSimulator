import vector3 as v
import structure as sss


a=v.vector3(1,3,3)
b=v.vector3(1,2,3)

e = sss.element(a,b)

s = sss.structure([e])

print(e)