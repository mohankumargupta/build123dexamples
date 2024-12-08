from build123d import *
from ocp_vscode import *
from math import sqrt

# Parameters
diameter = 80
inner_radius = 17.5
thickness = 5
hole_diameter = 10
hole_origin = 28

# Calculated values
radius = diameter / 2
inner_diameter = inner_radius * 2
hole_radius = hole_diameter / 2

# Helper functions

def pythagorean_side(hypotenuse: float, known_side: float) -> float:
    """
    Calculate the unknown side of a right triangle given the hypotenuse and one side.
    
    Args:
        hypotenuse (float): Length of the hypotenuse
        known_side (float): Length of the known side
    
    Returns:
        float: Length of the unknown side
    """
    return sqrt(hypotenuse**2 - known_side**2)


def sketch1():
    l1 = CenterArc(center=(0,0), radius=inner_radius, start_angle=90, arc_size=180)
    l2 = Line(l1@1, (pythagorean_side(diameter/2, inner_radius), (l1@1).Y))
    l3 = ThreePointArc(l2@1, (0, -radius),  ((l2@1).X,(l1@0).Y))
    l4 = Line(l3@1, l1@0)
    return Compound([l1, l2, l3, l4])

if __name__ == "__main__": 
    sketch_bottom = sketch1()
    #show(sketch_bottom, reset_camera=Camera.KEEP)
    part = extrude(make_face(sketch_bottom), amount=thickness)
    #hole = Pos(X=0, Y=hole_origin) * Hole(radius=hole_radius, depth=thickness)
    hole = PolarLocations(radius=hole_origin, count=3, start_angle=90, angular_range=180, endpoint=True) * Hole(radius=hole_radius, depth=thickness)
    part -= hole
    show(part, reset_camera=Camera.KEEP)


