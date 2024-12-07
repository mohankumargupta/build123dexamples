
from build123d import *

half_sphere1 = split(Sphere(radius=9*MM/2), Plane.XZ)
show_object(half_sphere1)

half_sphere2 = split(Sphere(radius=9*MM/2), Plane.XY)
sphere_top = Plane.XY.offset(75*MM) * half_sphere2
show_object(sphere_top)

#sphere2 = Sphere(radius=5/2.0)

#show_object(sphere2)

#box = Box(25,25,75)
#show_object(box)
#hole = Plane.XY.offset(25) * Circle(5)
#show_object(hole)
#box_with_hole = box - extrude(hole, -10)
#show_object(box_with_hole)


#show_object(box)