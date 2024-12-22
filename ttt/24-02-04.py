from build123d import *
from ocp_vscode import show, show_all, Camera

# Parameters

LENGTH = 165
WIDTH = 85
HEIGHT = 12

# Calculated values from parameters
HALF_LENGTH = LENGTH / 2
HALF_WIDTH = WIDTH / 2

with BuildPart() as part:
    # base part
    with BuildSketch() as bottom_sketch:
        RectangleRounded(LENGTH, WIDTH, radius=10)
        CENTER_TO_CENTER_DISTANCE = LENGTH - 108
        s1 = SlotCenterToCenter(center_separation=CENTER_TO_CENTER_DISTANCE, height=12, mode=Mode.PRIVATE)
        s2 = split(s1, bisect_by=Plane.YZ, mode=Mode.PRIVATE, keep=Keep.BOTTOM)
        with Locations((HALF_LENGTH,0)):
            s3 = add(s2, mode=Mode.SUBTRACT)
    extrude(amount=-HEIGHT)

show_all(axes=True, axes0=True, transparent=True)
#show(part, reset_camera=Camera.KEEP)
#show_all(reset_camera=Camera.KEEP)