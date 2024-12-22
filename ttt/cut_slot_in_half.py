from build123d import *
from ocp_vscode import show, show_all, Camera

# Create a slot
with BuildPart() as slot_part:
    SlotOverall(50, 20)

# Split the slot using the YZ plane
with BuildPart(slot_part) as split_slot:
    Plane.YZ.split(part=split_slot.part)

# Remove the unwanted half
with BuildPart(split_slot) as open_slot:
    for solid in open_slot.part.solids:
        if solid.center().x < 0:  # Assuming the positive X side is the side to keep
            solid.delete()

# Visualize or export the result
show(open_slot.part)
