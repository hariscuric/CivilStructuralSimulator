# CivilStructuralSimulator

Program is meant to solve simple linear 3D frame structural systems. (Only 1D beam elements for now, maybe also 2D shell elements in the future)

For now, frame system visualisation, linear analysis solution and diagrams (NMV diagrams) visualizations have been implemented. System is defined in .txt files.

inputElementCoordinates.txt file defines the geometry of the system. Each row represents start and end coordinates of frame elements

inputElementForces.txt file defines the imposed distributed forces on elements in global coordinates. Number of rows of this file has to be the same as inputElementCoordinates.txt file's. Each row has 6 numbers separated by comma (distributed forces in X, Y and Z and distributed moments in X,Y and X global directions)

inputElementSectionMaterial.txt defines rectangular section height, width, Young's elasticity modulus E and shear modulus G of each element. Number of rows again has to be the same as inputElementCoordinates.txt file's

inputNodeForces.txt file defines imposed nodal forces and moments in global coordinates. Number of rows of this file has to be the same as number of nodes of the system. This corresponds to number of distinct 3D point coordinates used to define elements in inputElementCoordinates.txt in the order as they first appear in that file. Each row in inputNodeForces.txt defines 3 forces (XYZ) and 3 moments (XYZ)

inputSupports.txt defines the nodal restraints. Number of rows is the same as inputNodeForces.txt file's

Program can be run by terminal command:
python main.py

once the visualization window pops up use keybord keys:

arrows:

    -to move camera front, back, right and left

8 and 2:

    -to move camera up and down

w, s, d, a:

    -to rotate camera up, down, right and left

t, g, h, f:

    -to orbit camera around object center of mass (up, down, right and left)

m,n,v,b,c,x to display M3 moment, N axial force, 

esc:

    -to exit program



it currently looks like this:


![Simulation Snip 4](/StructureVisualisation.gif)


Future work:

Structural analysis: assignment of structure properties (materials, sections, restraints, loads, etc.) and linear structural analysis