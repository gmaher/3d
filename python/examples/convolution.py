import sys
import os
sys.path.append(os.path.abspath('../'))

import modules as lib

cubes = []
for i in range(4):
    for j in range(2):
        for k in range(2):
            cube = lib.geometry.cube(center=(k,j,i))
            cubes.append(cube)

scene = lib.scene.Scene()

for c in cubes:
    scene.addObject(c, color=(255,255,255), linecolor=(0,0,0), linewidth=3)

scene.render()
