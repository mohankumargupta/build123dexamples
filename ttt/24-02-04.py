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
    
    # lip hole
    with BuildSketch() as lip_hole:
        s4 = SlotCenterToCenter(center_separation=CENTER_TO_CENTER_DISTANCE, height=SLOT_INNER_WIDTH, mode=Mode.PRIVATE)
        s5 = split(s4, bisect_by=Plane.YZ, keep=Keep.BOTTOM, mode=Mode.PRIVATE)
        with Locations((HALF_LENGTH, 0)):
            add(s5)
    extrude(amount=-HEIGHT, mode=Mode.SUBTRACT)
       
#show_all(axes=True, axes0=True, transparent=True)
show_all(axes=True, axes0=True, transparent=False)
        

"""
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
        print(s2.show_topology())
        LIP_OFFSET = 5
        s4 = offset(s2, amount=LIP_OFFSET, mode=Mode.PRIVATE, kind=Kind.TANGENT)
        with Locations((HALF_LENGTH - LIP_OFFSET,0)):
            s7=add(s4)
            s8=add(s2, mode=Mode.SUBTRACT)    
    extrude(amount=3)
    

show_all(axes=True, axes0=True, transparent=True)
#show(part, reset_camera=Camera.KEEP)
#show_all(reset_camera=Camera.KEEP)

"""