import sys
import os
sys.path.append(os.path.abspath('../'))

import modules as lib

inp = lib.geometry.cubeGrid(2,3,4,center=[0.5,1.5,2])

lines = []
l = lib.geometry.line(start=[0,0,1.0], end=[6.0,0.5,0.5])
l2 = lib.geometry.line(start=[0,1,1.0], end=[6.0,0.5,0.5])
l3 = lib.geometry.line(start=[0,0,0.0], end=[6.0,0.5,0.5])
l4 = lib.geometry.line(start=[0,1,0.0], end=[6.0,0.5,0.5])
lines = [l,l2,l3,l4]

c1 = lib.geometry.cube(center=[6.0,1.5,2.5])
c2 = lib.geometry.cube(center=[6.0,1.5,1.5])
c3 = lib.geometry.cube(center=[6.0,1.5,0.5])
c4 = lib.geometry.cube(center=[6.0,0.5,2.5])
c5 = lib.geometry.cube(center=[6.0,0.5,1.5])
c6 = lib.geometry.cube(center=[6.0,0.5,0.5])

scene = lib.scene.Scene()

scene.addObject(inp)

for l in lines:
    scene.addObject(l)

scene.addObject(c1, opacity=1.0)
scene.addObject(c2, opacity=1.0)
scene.addObject(c3, opacity=1.0)
scene.addObject(c4, opacity=1.0)
scene.addObject(c5, opacity=1.0)
scene.addObject(c6,color=(200,0,0), opacity=0.8)

g = lib.geometry.cubeGrid(2,2,2,[0.5,1,1])
scene.addObject(g,color=(255,30,30))
scene.render()

# scene.save('convolution')
