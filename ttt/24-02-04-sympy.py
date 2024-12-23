from sympy import symbols, Eq, solve

def find_intersection_points():
    # Define symbols
    x, y = symbols('x y')

    # Define the circle's parameters
    h, k, r = 0, 66, 50  # Example: center (0, 66), radius 50

    # Define the line's y-coordinate
    c = 25  # Example: horizontal line y = 25

    # Circle equation: (x - h)^2 + (y - k)^2 = r^2
    circle_eq = Eq((x - h)**2 + (y - k)**2, r**2)

    # Substitute y = c into the circle equation
    intersection_eq = circle_eq.subs(y, c)

    # Solve for x
    x_coords = solve(intersection_eq, x)

    # Combine with the constant y = c
    #intersection_points = [(x_val, c) for x_val in x_coords]
    intersection_points = [(float(x_val.evalf()), float(c)) for x_val in x_coords]

    print(intersection_points)

find_intersection_points()