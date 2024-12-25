from build123d import *
from ocp_vscode import show_all

with BuildPart() as box:
    Box(10,10,10)

part1 = box.part - Pos((-3,3)) * Hole(radius=2, depth=10)
show_all()

