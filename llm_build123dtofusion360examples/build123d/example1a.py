from build123d import *
from ocp_vscode import show_all

# Parameters
length = 80 * MM
width = 60 * MM
height = 10 * MM

with BuildPart() as example1:
    Box(length, width, height, align=(Align.CENTER, Align.CENTER, Align.MIN))

part = example1.part
show_all()
