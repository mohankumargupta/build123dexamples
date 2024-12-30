# https://www.hubs.com/blog/cad-modeling-1-enclosures/

from build123d import *
from ocp_vscode import show_all, Camera

# Parameters

LENGTH = 90 
WIDTH = 50
HEIGHT = 8

# Computed Parameters

HALF_WIDTH = WIDTH / 2

with BuildPart() as part:
    with BuildSketch() as sketch1:
        with BuildLine() as line1:
            l1 = Line((0, -HALF_WIDTH), (HALF_WIDTH, -HALF_WIDTH))
            l2 = Line(l1@1, l1@1 + (0, WIDTH))
            TOP_Y = LENGTH - HALF_WIDTH
            TOP_X = 35 / 2
            l3 = Line((0, TOP_Y), (TOP_X, TOP_Y))
            l4 = Line(l3@1, l3@1 + (0, -20.0) )
            l5 = Line(l4@1, l2@1)
            mirror(about=Plane.YZ)
        make_face()   
    extrude(amount=HEIGHT)          

show_all(reset_camera=Camera.KEEP)
enclosure = part.part
print(f"Volume: {enclosure.volume}")