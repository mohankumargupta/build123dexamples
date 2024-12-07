from build123d import *

length = 25
width = 25
height = 75
thickness = 2.5

xz_offset = -width/2.0


# Create base tower
part = Box(length, width, height, align=(Align.CENTER, Align.CENTER, Align.MIN))

# front 

# front top
text1 = (Plane.XZ.offset(xz_offset) * 
         Pos(0, 40) * 
         Text("Slant", font_size=10, align=(Align.CENTER, Align.CENTER))
)
part -= extrude(text1, amount=100)

#text2 = (Plane.XZ.offset(25) * 
#         Pos(0, 30) * 
#         Text("3D", font_size=10, align=(Align.CENTER, Align.CENTER))
#)
#part -= extrude(text2, amount=-10)


show_object(part)
