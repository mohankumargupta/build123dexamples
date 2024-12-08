from build123d import *
from math import sqrt, sin, cos, radians

def pythagorean_length(a: float, b: float) -> float:
    """
    Calculate the length of the hypotenuse given two sides.
    
    Args:
        a (float): Length of one side
        b (float): Length of the other side
    
    Returns:
        float: Length of the hypotenuse
    """
    return sqrt(a**2 + b**2)

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

def right_triangle_coordinates(a: float, b: float, angle: float = 0) -> tuple:
    """
    Generate coordinates for a right triangle.
    
    Args:
        a (float): Length of the base side
        b (float): Length of the height side
        angle (float, optional): Rotation angle in degrees. Defaults to 0.
    
    Returns:
        tuple: Coordinates of the three triangle points
    """
    # Calculate hypotenuse
    c = pythagorean_length(a, b)
    
    # Rotate if needed
    if angle != 0:
        # Convert angle to radians
        theta = radians(angle)
        
        # Rotation matrix calculations
        x1 = a * cos(theta) - 0 * sin(theta)
        y1 = a * sin(theta) + 0 * cos(theta)
        
        x2 = 0 * cos(theta) - b * sin(theta)
        y2 = 0 * sin(theta) + b * cos(theta)
        
        x3 = c * cos(theta)
        y3 = c * sin(theta)
        
        return ((0, 0), (x1, y1), (x2, y2))
    
    return ((0, 0), (a, 0), (0, b))

def create_right_triangle(a: float, b: float, angle: float = 0) -> Sketch:
    """
    Create a right triangle sketch in build123d.
    
    Args:
        a (float): Length of the base side
        b (float): Length of the height side
        angle (float, optional): Rotation angle in degrees. Defaults to 0.
    
    Returns:
        Sketch: A build123d sketch representing the right triangle
    """
    coords = right_triangle_coordinates(a, b, angle)
    with Sketch() as triangle_sketch:
        PolyLine(*coords)
    return triangle_sketch

def create_right_triangle_with_inscribed_circle(a: float, b: float) -> Sketch:
    """
    Create a right triangle with its inscribed circle.
    
    Args:
        a (float): Length of the base side
        b (float): Length of the height side
    
    Returns:
        Sketch: A build123d sketch with the triangle and its inscribed circle
    """
    # Calculate hypotenuse and inradius
    c = pythagorean_length(a, b)
    
    # Inradius calculation
    s = (a + b + c) / 2  # Semi-perimeter
    inradius = sqrt((s - a) * (s - b) * (s - c) / s)
    
    with Sketch() as triangle_with_circle:
        # Draw triangle
        PolyLine(
            (0, 0),     # Origin
            (a, 0),     # Base point
            (0, b)      # Height point
        )
        
        # Draw inscribed circle
        Circle(center=(a/2, b/2), radius=inradius)
    
    return triangle_with_circle

def triangle_area_from_sides(a: float, b: float) -> float:
    """
    Calculate the area of a right triangle given two sides.
    
    Args:
        a (float): Length of one side
        b (float): Length of the other side
    
    Returns:
        float: Area of the triangle
    """
    return 0.5 * a * b

def triangle_perimeter_from_sides(a: float, b: float) -> float:
    """
    Calculate the perimeter of a right triangle given two sides.
    
    Args:
        a (float): Length of one side
        b (float): Length of the other side
    
    Returns:
        float: Perimeter of the triangle
    """
    c = pythagorean_length(a, b)
    return a + b + c