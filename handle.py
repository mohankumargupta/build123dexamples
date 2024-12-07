
from build123d import *

box = Box(20,20,50)
#show_object(box)
hole = Plane.XY.offset(25) * Circle(5)
#show_object(hole)
box_with_hole = box - extrude(hole, -10)
show_object(box_with_hole)


#show_object(box)