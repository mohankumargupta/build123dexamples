import math
from build123d import Align, Trapezoid

def IsoscelesTrapezoid(a, b, h):
    #if a <= b:
    #    raise ValueError("The longer base 'a' must be greater than the shorter base 'b'.")
    
    # Calculate the offset from the longer base to the shorter base
    offset = (a - b) / 2
    
    # Calculate the angle using arctan (opposite/adjacent)
    angle = math.atan(h / offset)
    
    # Create the trapezoid
    Trapezoid(width=a, height=h, left_side_angle=angle, right_side_angle=angle)