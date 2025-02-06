from build123d import *
from ocp_vscode import show_all

# Parameters
length = 80.0, 
width = 60.0, 
height = 10.0

# Radius and Diameters
center_hole_diameter = 22.0
center_hole_radius = center_hole_diameter / 2

with BuildPart() as ex2:
    Box(length, width, height)
    Hole(radius=center_hole_radius)
    
show_all()

