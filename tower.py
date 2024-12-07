from build123d import *

#All measurements in mm

length = 25
width = 25
height = 75
minicube_height = 25
thickness = 2.5
text_from_top_offset = 10.0

front_face_offset = width / 2.0
back_face_offset = -width / 2.0
left_face_offset = -width / 2.0
right_face_offset = width / 2.0

# front

# front top: text
gap = 5.0
text1 = (Plane.XZ.offset(front_face_offset) * 
            Pos(0, height - text_from_top_offset) * 
            Text("Slant", font_size=10.0, align=(Align.CENTER, Align.MIN))
        )
text2 = (
            Plane.XZ.offset(front_face_offset) * 
            Pos(0, height - text_from_top_offset - gap) * 
            Text("3D", font_size=10.0, align=(Align.CENTER, Align.MAX))
        )
front_top = extrude(text1, amount=-30) + extrude(text2, amount=-30)
show_object(front_top)

# right top: text



# Create final part
base = Box(length, width, height, align=(Align.CENTER, Align.CENTER, Align.MIN))
part = base - front_top


