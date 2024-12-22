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
    # lip
    with BuildSketch() as lip:
        LIP_OFFSET = 5
        s4 = offset(s2, amount=LIP_OFFSET, mode=Mode.PRIVATE)
        with Locations((HALF_LENGTH,0)):
            add(s4)
            add(s2, mode=Mode.SUBTRACT)    
    extrude(amount=3)
    

show_all(axes=True, axes0=True, transparent=True)
#show(part, reset_camera=Camera.KEEP)
#show_all(reset_camera=Camera.KEEP)