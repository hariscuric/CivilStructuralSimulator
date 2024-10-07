# CivilStructuralSimulator

Program is meant to solve simple linear 3D frame structural systems. (Only 1D beam elements for now, maybe also 2D shell elements in the future)

For now, only visualization of 3D frames has been solved. Example system is defined in input.txt file. Each line represents start and end coordinates of each frame element in 3D cartesian coordinate system.

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

esc:

    -to exit program



it currently looks like this:


![Simulation Snip 4](/StructureVisualisation.gif)


Future work:

Structural analysis: assignment of structure properties (materials, sections, restraints, loads, etc.) and linear structural analysis