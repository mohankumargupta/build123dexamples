from build123d import *
from ocp_vscode import show, show_all, Camera

# Parameters

LENGTH = 165
WIDTH = 85
HEIGHT = 12

# Calculated values from parameters
HALF_LENGTH = LENGTH / 2

with BuildPart() as part:
    # base part
    with BuildSketch() as bottom_sketch:
        RectangleRounded(LENGTH, WIDTH, radius=10)
        SLOT_RADIUS = 15
        LEFT_SLOT_CENTER = HALF_LENGTH - (LENGTH - 108)/2
        s1 = SlotOverall(50, 12, mode=Mode.PRIVATE)
        s2 = split(s1, bisect_by=Plane.YZ, mode=Mode.PRIVATE, keep=Keep.BOTTOM)
        with Locations((HALF_LENGTH,0)):
            s3 = add(s2, mode=Mode.SUBTRACT)
    extrude(amount=-HEIGHT)

show_all(axes=True, axes0=True, transparent=True)
#show(part, reset_camera=Camera.KEEP)
#show_all(reset_camera=Camera.KEEP)