from build123d import *
from ocp_vscode import show_all

# Parameters
length = 80 * MM
width = 60 * MM
height = 10 * MM

# Radius and diameters
center_hole_diameter = 22.0
center_hole_radius = center_hole_diameter / 2

with BuildPart() as example1:
    Box(length, width, height)
    Hole(center_hole_radius)

part = example1.part
show_all()
