from build123d import *

# Create base cube
base_cube = Box(50, 50, 50, align=(Align.CENTER, Align.CENTER, Align.MIN))

# Create multiple text elements
text1 = (Plane.XZ.offset(25) * 
         Pos(0, 40) * 
         Text("Slant", font_size=10, align=(Align.CENTER, Align.CENTER))
)

text2 = (Plane.XZ.offset(25) * 
         Pos(0, 30) * 
         Text("3D", font_size=10, align=(Align.CENTER, Align.CENTER))
)

# Cut both texts into the cube
part = base_cube - extrude(text1, amount=-100)  - extrude(text2, amount=-100)


show_object(part)