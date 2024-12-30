# https://www.hubs.com/blog/cad-modeling-1-enclosures/

import math
from build123d import *
from ocp_vscode import show_all, Camera, show_clear
from helpers import IsoscelesTrapezoid

# Parameters

LENGTH = 90 
WIDTH = 50
HEIGHT = 8

# Computed Parameters

HALF_WIDTH = WIDTH / 2

with BuildPart() as part:
    with BuildSketch() as sketch1:
        r1=Rectangle(WIDTH, WIDTH)
        with Locations((0, HALF_WIDTH)):
            r2=Trapezoid(width=50, height=20, left_side_angle=math.atan2(20,7.5)* (180 / math.pi), right_side_angle=math.atan2(20,7.5)* (180 / math.pi), align=(Align.CENTER, Align.MIN))
        center_y = 55
        with Locations((0, center_y)): 
            Rectangle(35,20)
    extrude(amount=HEIGHT)          

show_all(reset_camera=Camera.KEEP)
enclosure = part.part
print(f"Volume: {enclosure.volume}")