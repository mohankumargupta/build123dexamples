from build123d import *
from ocp_vscode import show_all

# Parameters
length = 80 * MM
width = 60 * MM
height = 10 * MM

with BuildPart() as example1:
    # All 2D and 3D objects have an align property that defaults to (Align.CENTER, Align.CENTER, Align.CENTER)
    # this indicates alignment in the X Y and Z directiorns respectively.
    # An alignment of Align.MIN in the X direction means that the 2d or 3d shape's leftmost point should be at the origin
    # An alignment of Align.MAX in the X direction means that the 2d or 3d shape's rightmmost point should be at the origin
    # An alignment of Align.CENTER in the X direction means that the 2d or 3d shape's center should be at the origin.
    Box(length, width, height)

part = example1.part
show_all()
