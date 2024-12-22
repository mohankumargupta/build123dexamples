from build123d import *
from ocp_vscode import show, show_all, Camera

# Parameters
LENGTH = 165
WIDTH = 85
HEIGHT = 12
SLOT_INNER_WIDTH = 15

# Calculated values from parameters
HALF_LENGTH = LENGTH / 2
HALF_WIDTH = WIDTH / 2



with BuildPart() as part:
    # base body
    with BuildSketch() as base_sketch:
        RectangleRounded(LENGTH, WIDTH, radius=10)
    extrude(amount=-HEIGHT)
    
    # lip extrude
    with BuildSketch(mode=Mode.PRIVATE) as half_slot_sketch:
        CENTER_TO_CENTER_DISTANCE = LENGTH - 108
        LIP_OFFSET = 5
        s1 = SlotCenterToCenter(center_separation=CENTER_TO_CENTER_DISTANCE, height=SLOT_INNER_WIDTH+2*LIP_OFFSET)
        s2 = offset(amount=-5, mode=Mode.SUBTRACT)
        s3 = split(bisect_by=Plane.YZ, keep=Keep.BOTTOM)
    with BuildSketch() as lip_sketch:
        with Locations((HALF_LENGTH, 0)):
            add(half_slot_sketch)
    extrude(amount=5)
    mirror(about=Plane.YZ)

    # lip hole
    with BuildSketch() as lip_hole:
        s4 = SlotCenterToCenter(center_separation=CENTER_TO_CENTER_DISTANCE, height=SLOT_INNER_WIDTH, mode=Mode.PRIVATE)
        s5 = split(s4, bisect_by=Plane.YZ, keep=Keep.BOTTOM, mode=Mode.PRIVATE)
        with Locations((HALF_LENGTH, 0)):
            add(s5)
    extrude(amount=-HEIGHT, mode=Mode.SUBTRACT)
    #mirror(about=Plane.YZ)
    #mirror(about=Plane.YZ, mode=Mode.SUBTRACT)
    #extrude(mirror(about=Plane.YZ, mode=Mode.SUBTRACT))
    
       
#show_all(axes=True, axes0=True, transparent=True)
show_all(axes=True, axes0=True, transparent=False)
        
