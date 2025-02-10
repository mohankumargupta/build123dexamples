from build123d import *
from ocp_vscode import show_all

# Parameters
length = 150.0 
width = 100.0 
height = 20.0
countersink_holes_offset = 10

# Radius and diameters
hole_diameter = 25.0
hole_radius = hole_diameter / 2

# Computed parameters
countersink_holes_xspacing = length - 2 * countersink_holes_offset
countersink_holes_yspacing = width - 2 * countersink_holes_offset

# Main design

with BuildPart() as pillow_block:
    Box(length, width, height)
    Hole(hole_radius)
    with Locations(pillow_block.faces().sort_by(Axis.Z).last):
        with GridLocations(x_spacing=countersink_holes_xspacing, y_spacing=countersink_holes_yspacing, x_count=2, y_count=2):
            CounterSinkHole(radius=3, counter_sink_radius=5)

part = pillow_block.part
show_all()

