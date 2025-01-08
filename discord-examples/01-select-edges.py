from build123d import *
from ocp_vscode import show_all, Camera

with BuildPart() as shell:
    original = Box(10, 80, 30, align=(Align.MIN, Align.CENTER, Align.CENTER))
    topx = shell.faces().filter_by(Axis.X).sort_by(Axis.X)[-1]
    offset(amount=5, openings=topx)

    # remove the tray
    with BuildPart(mode=Mode.SUBTRACT) as tray:
        Box(10, 50, 20)

    edges = shell.edges(Select.LAST).filter_by(Axis.X)
    fillet(edges, 1)
show_all(reset_camera=Camera.KEEP)