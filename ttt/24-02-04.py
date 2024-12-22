from build123d import *
from ocp_vscode import show_all, Camera

length = 165
width = 85
height = 12

with BuildPart() as part:
    with BuildSketch() as bottom_sketch:
        RectangleRounded(length, width, radius=10)
    extrude(amount=-height)

show_all(axes=True, axes0=True, transparent=True)
#show(part, reset_camera=Camera.KEEP)
#show_all(reset_camera=Camera.KEEP)