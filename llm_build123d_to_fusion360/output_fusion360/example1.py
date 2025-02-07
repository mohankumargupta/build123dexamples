import adsk.core
import adsk.fusion
import traceback
from typing import Tuple

# Parameters
length = 80.0
width = 60.0
height = 10.0

# Radius and Diameters
center_hole_diameter = 22.0
center_hole_radius = center_hole_diameter / 2


def createPoint(point: Tuple[float, float, float]) -> adsk.core.Point3D:
    x, y, z = point
    return adsk.core.Point3D.create(x * 0.1, y * 0.1, z * 0.1)


def createValueInput(parameter: float):
    return adsk.core.ValueInput.createByString(f"{parameter}mm")


def createHole(
    plane1: adsk.fusion.BRepFace,
    point: adsk.core.Point3D,
    diameter: adsk.core.ValueInput,
    depth: adsk.core.ValueInput,
) -> adsk.fusion.HoleFeature:
    comp: adsk.fusion.Component = plane1.body.parentComponent
    holeFeatures: adsk.fusion.HoleFeatures = comp.features.holeFeatures
    holeInput: adsk.fusion.HoleFeatureInput = holeFeatures.createSimpleInput(diameter)
    holeInput.setPositionByPoint(plane1, point)
    holeInput.setDistanceExtent(depth)

    holeFeat: adsk.fusion.HoleFeature = None
    try:
        holeFeat = holeFeatures.add(holeInput)
    except:
        holeInput.isDefaultDirection = not holeInput.isDefaultDirection  # here
        holeFeat = holeFeatures.add(holeInput)

    return holeFeat


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        if not design:
            ui.messageBox("No active Fusion design")
            return

        # rootComp = design.rootComponent

        def addFixedValueUserParameter(param_name: str, value: float):
            params = design.userParameters
            params.add(param_name, adsk.core.ValueInput.createByString(f"{value}mm"), "mm", "")

        def addExpressionUserParameter(param_name: str, expression: str):
            params = design.userParameters
            params.add(param_name, adsk.core.ValueInput.createByString(f"{expression}mm"), "mm", "")

        def get_user_parameter(parameter: str) -> adsk.core.ValueInput:
            expression = design.userParameters.itemByName(parameter).expression
            return adsk.core.ValueInput.createByString(expression)

        # Add User Parameters
        addFixedValueUserParameter("length", length)
        addFixedValueUserParameter("width", width)
        addFixedValueUserParameter("height", height)
        addFixedValueUserParameter("center_hole_diameter", center_hole_diameter)
        addExpressionUserParameter("center_hole_radius", "center_hole_diameter / 2")

        # Get root component
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)

        # Draw a centered rectangle
        centerPoint = createPoint((0, 0, 0))
        sketch.sketchCurves.sketchLines.addCenterPointRectangle(
            centerPoint, createPoint((length / 2, width / 2, 0))
        )  # z is relative to sketch plane

        # Create the extrusion
        prof = sketch.profiles.item(0)
        distance = get_user_parameter("height")
        extInput = rootComp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extInput.setSymmetricExtent(distance, True)
        ext = rootComp.features.extrudeFeatures.add(extInput)
        # Get the top face of the box
        topFace = ext.endFaces.item(0)

        # Create the center hole

        hole_center = createPoint((0, 0, 0))  # Center of the top face
        hole_diameter = get_user_parameter("center_hole_diameter")
        # Assuming through all for depth
        depth_hole = get_user_parameter("height")
        # distance = adsk.core.ValueInput.createByReal(userparameter_value('height'))
        createHole(topFace, hole_center, hole_diameter, depth_hole)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))

