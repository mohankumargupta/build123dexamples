from build123d import *

with BuildPart() as part:
    # Create a box
    Box(10, 10, 10)
    
    # Cut a cylinder from the box
    with Locations((5, 5, 5)):
        Cylinder(radius=3, height=10, mode=Mode.SUBTRACT)

# Export the result
part.part.export_stl("output.stl")

