# from Rob B.

from typing import Literal
from build123d import *
from ocp_vscode import show_all, Camera

# card_width = 2.5 * IN
card_width = 63.5 * MM
# card_length = 3.5 * IN
card_length = 80.0 * MM
# height = 0.5 * IN
height = 12 * MM
wall = 3 * MM
gap = 0.5 * MM

with BuildPart() as box_builder:
    with BuildSketch() as plan:
        #Rectangle(card_width + 2 * wall, card_length + 2 * wall)
        #fillet(plan.vertices(), radius=card_width / 15)
        RectangleRounded(width=card_width + 2 * wall, height=card_length + 2 * wall, radius=card_width / 15)
    extrude_plan = extrude(amount=wall)
    top_face = box_builder.faces().sort_by(Axis.Z).last
    # with BuildSketch(top_face) as holes:
    #     with GridLocations(
    #         x_spacing=card_width - 2 -2 * wall , y_spacing=card_length - 2 - 2 * wall, x_count=2, y_count=2
    #     ):
    #         Circle(1.5)
    # extrude(amount= -wall, mode=Mode.SUBTRACT)        
    with BuildSketch(top_face) as walls:
        add(plan.sketch)
        offset(plan.sketch, amount=-wall, mode=Mode.SUBTRACT)
    walls_extrude = extrude(amount=height / 1.333)
    with BuildSketch(top_face) as inset_walls:
        offset(plan.sketch, amount=-(wall + gap) / 2, mode=Mode.ADD)
        offset(plan.sketch, amount=-wall, mode=Mode.SUBTRACT)
    inset = extrude(amount=height / 2)
    with GridLocations(
        x_spacing=card_width - 2 -2 * wall , y_spacing=card_length - 2 - 2 * wall, x_count=2, y_count=2
    ):
        hole = Hole(radius=1.5)

box_builder.part
show_all(reset_camera=Camera.KEEP)