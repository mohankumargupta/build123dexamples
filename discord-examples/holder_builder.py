from build123d import *
from ocp_vscode import *

thickness = 2
tolerance = 0.2

remote_width = 32.5 + thickness*2 + tolerance
remote_height = 85 + thickness*2 + tolerance
remote_depth = 12.4 + thickness*2 + tolerance # not including the nub or buttons
nub_width = 12.25 + tolerance
nub_height = 50.25  + tolerance
nub_offset = 17
edge_width = 2.5 + tolerance # edge of container to clip remote holder on
edge_hangover = 15

nub_radius = nub_width / 2

front_cover_height = 10

remote_radius = remote_width / 2

with BuildPart() as remote_holder:
    with BuildSketch(Plane.XZ) as backplate:
        with BuildLine() as base:
            ra = RadiusArc((remote_width/2, remote_radius), (0, 0), remote_radius)
            l1 = Line(ra @ 0, ra @ 0 + (0, remote_height-remote_radius))
            Line((0, remote_height), l1 @ 1)
            mirror(about=Plane.YZ)
        make_face()
        with Locations((0, remote_height/2)):
            RectangleRounded(
                nub_width,
                nub_height,
                nub_radius-tolerance,
                mode=Mode.SUBTRACT
            )
    extrude(amount = thickness)
    
    with BuildSketch(Plane.XY.offset((remote_height) - thickness)) as top_hook:
        Rectangle(remote_width, edge_width)
    extrude(amount = thickness)
    
    with BuildSketch(Plane.XZ.offset(-(edge_width+thickness)/2-1)) as back_hook:
        with Locations((0, remote_height - edge_hangover/2)):
            Rectangle(remote_width, edge_hangover)
    extrude(amount = thickness)
    
    with BuildSketch(Plane.XZ.offset(remote_depth)) as frontplate:
        with BuildLine() as base:
            ra = RadiusArc((remote_width/2, remote_radius), (0, 0), remote_radius)
            l1 = Line(ra @ 0, ra @ 0 + (0, front_cover_height))
            Line((0, remote_radius + front_cover_height), l1 @ 1)
            mirror(about=Plane.YZ)
        make_face()
    extrude(amount = thickness)

    with BuildSketch(Plane.XZ) as bottom:
        with BuildLine() as base:
            ra = RadiusArc((remote_width/2, remote_radius), (0, 0), remote_radius)
            l1 = Line(ra @ 0, ra @ 0 + (0, front_cover_height))
            Line((0, remote_radius + front_cover_height), l1 @ 1)
            mirror(about=Plane.YZ)
        make_face()
        offset(amount=-2, mode=Mode.SUBTRACT)
        with Locations((0, remote_radius+front_cover_height)):
            Rectangle(remote_width-(thickness*2), thickness*2, mode=Mode.SUBTRACT)
    extrude(amount = remote_depth + thickness)

show_all()