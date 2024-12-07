from build123d import *

box = Box(40,40,40)
show_object(box, options=dict(alpha=0.6, color="green"))
#show_object(box, options={'alpha':0.6})

#profile = Plane.YZ.offset(20) * Pos(0, -50) * Rectangle(20,20, align=(Align.CENTER, Align.MIN, Align.MIN))

#show_object(profile)

slot = SlotOverall(40, 10)
show_object(slot)