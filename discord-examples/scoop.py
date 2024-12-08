from build123d import *
from ocp_vscode import show

with BuildPart() as pocket:
    with BuildSketch() as pocket_s:
        Circle(25)
        Rectangle(20, 50, align=(Align.MIN, Align.CENTER))
        split(bisect_by=Plane.YZ.offset(20), keep=Keep.BOTTOM)
    extrude(amount=15)
    open_face = pocket.faces().sort_by(Axis.X)[-1]
    offset(amount=-2 * MM, openings=[open_face])

show(pocket, open_face)