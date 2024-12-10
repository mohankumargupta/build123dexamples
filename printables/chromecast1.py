from build123d import *
from ocp_vscode import *

length = 42.5
depth = 21
height = 41

def endX(obj: Edge):
    return (obj@1).X

def endY(obj: Edge):
    return (obj@1).Y

def start(obj: Edge):
    return obj@0

def end(obj: Edge):
    return obj@1

a1 = RadiusArc(start_point=(0,10), end_point=(19.25,0), radius=19.25 ) 
a2 = RadiusArc(start_point=(0,12), end_point=(21.25,0), radius=21.25 ) 
pts1 = [
    end(a1),
    (endX(a1), endY(a1) - 4.5),
    (endX(a1) - 3, endY(a1) - 4.5),
]
l1 = Polyline(pts1)
pts2 = [
    end(a2),
    (endX(a2), endY(a2) - 6.5),
    (endX(a2) - 5, endY(a2) - 6.5),
]
l2 = Polyline(pts2)

profile =  Compound([a1,a2, l1, l2, Line(l1@1, l2@1), Line(a1@0, a2@0)])
profile2 = Plane.XZ.offset(18.75) * profile
face = make_face(Plane.XZ *profile)

part1 = extrude(face, amount=18.75)
part1_mirror = mirror(part1, about=Plane.YZ)
part2 = revolve(face, revolution_arc=180)
part = Part() + Compound([
  part1, 
  part1_mirror,
  part2
])
show(part, reset_camera=Camera.KEEP)