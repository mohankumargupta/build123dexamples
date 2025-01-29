from build123d import *
from ocp_vscode import show_all, Camera

# Parameters
length = 1260
width = 775
height = 32

x_offset = 30
y_offset = 730
y1_offset = 30
y2_offset = 45

spacing_small = 50
spacing_large = 100

hex_depth = 5.5

# Radius and diameters
hex_inscribed_radius = 5


# Computed parameters
half_length = length / 2
half_width = width / 2

# Main design
with BuildPart() as part_builder:
    Box(length, width, height, align=(Align.MAX, Align.MAX, Align.MAX))
    with BuildSketch() as quadrant_bottom_lower:
        with Locations((-x_offset, -y_offset)):
            RegularPolygon(radius=hex_inscribed_radius, side_count=6, major_radius=False, rotation=90)
    a=extrude(amount=-hex_depth, mode=Mode.SUBTRACT)            

part = part_builder.part
show_all(reset_camera=Camera.KEEP)

filename_stem = "melbpc/sacrificial-table"
export_step(part, f"{filename_stem}.step")
export_stl(part, f"{filename_stem}.stl")

