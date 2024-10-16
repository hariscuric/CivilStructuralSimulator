# CivilStructuralSimulator

Current example looks like this (Major moment diagram is displayed):


![Simulation Snip 4](/StructureVisualization.gif)

Program is meant to solve simple linear 3D frame structural systems. (Only 1D beam elements for now, maybe also 2D shell elements in the future)

For now, frame system visualisation, linear analysis solution and diagrams' (NMV diagrams) visualizations have been implemented. System is defined in .txt files.

inputElementCoordinates.txt file defines the geometry of the system. Each row represents start and end coordinates of frame elements (6 numerical values separated by comma corresponding to 2 3D point coordinates)

inputElementForces.txt file defines the imposed distributed forces on elements in global coordinates. Number of rows of this file has to be the same as inputElementCoordinates.txt file's. Each row has 6 numbers separated by comma (distributed forces in X, Y and Z and distributed moments in X,Y and X global directions). Only uniform distributed forces are currently allowed.

inputElementSectionMaterial.txt defines rectangular section height, width, Young's elasticity modulus E and shear modulus G of each element. Number of rows again has to be the same as inputElementCoordinates.txt file's. Each row contains 4 numerical values separated by commas.

inputNodeForces.txt file defines imposed nodal forces and moments in global coordinates. Number of rows of this file has to be the same as number of nodes of the system. This corresponds to number of distinct 3D point coordinates used to define elements in inputElementCoordinates.txt in the order as they first appear in that file. Each row in inputNodeForces.txt defines 3 forces (XYZ) and 3 moments (XYZ)

inputSupports.txt defines the nodal restraints. Number of rows is the same as inputNodeForces.txt file's. Nodes that have restraints have number 1 for corresponding restrained coordinate. Free DoFs are zeros in this file.

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

e,r:

    -to increase or decrease the view angle of the camera. This has a similar effect to up and down keys (moving camera front or back)

m,n,v,b,c,x:

    -to display following diagrams: major moment (My in element local coordinates), N axial force (Fx in element local coordinates), major shear force (Fz in element local coordinates), minor moment (Mz in element local coordinates), minor shear force (Fy in element local coordinates) and T torsion moment (Mx in element local coordinates) 

z:

    -to hide any diagram currently displayed on the structure

esc:

    -to exit program






Visualized diagrams currently don't display numerical values, only shapes of diagrams. Numerical values of computed diagrams are stored in structure.elements[i].diagrams[0:6,0:11] numpy array variable. This array contains 6 diagram values for 11 stations along i'th element. For example, to obtain major moment diagram for 3'rd element (i index is 2 in this case since it starts from 0) insert following command after structure = sss.structure(elements) line in the main function (check commented lines in main.py file):

    print(structure.elements[2].diagrams[4,:])

Order of diagrams is as follows: N, V minor, V major, T torsion, M major, M minor (Fx, Fy, Fz, Mx, My, Mz in element local coordinates)

Nodal deformations of the system are stored in structure.NodalDisplacements numpy array. For example, to display 6 components of deformations (3 translations and 3 rotations) of 8'th element use the following command:

    print(structure.NodalDisplacements[7*6:7*6+6])




Future work:

Better GUI, structural deformations visualization, editting material, geometry or load assignments through GUI, finite elements implementation (direct stiffness method is implemented currently), plate and shell elements, nonlinear analysis, etc.