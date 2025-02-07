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


def createValueInput(parameter: float) -> adsk.core.ValueInput:
    return adsk.core.ValueInput.createByString(f"{parameter}mm")

def createHole(
    plane1: adsk.fusion.BRepFace,
    point: adsk.core.Point3D,
    diameter: adsk.core.ValueInput,
    depth: float) -> adsk.fusion.HoleFeature:

    comp: adsk.fusion.Component = plane1.body.parentComponent
    holeFeatures: adsk.fusion.HoleFeatures = comp.features.holeFeatures
    holeInput: adsk.fusion.HoleFeatureInput = holeFeatures.createSimpleInput(
        diameter
    )
    holeInput.setPositionByPoint(
        plane1,
        point
    )
    distance = adsk.core.ValueInput.createByReal(depth)
    holeInput.setDistanceExtent(distance)

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

        # Get the root component of the active design.
        rootComp = design.rootComponent

        def get_user_parameter(parameter: str) -> adsk.core.ValueInput:
            expression = design.userParameters.itemByName("center_hole_diameter").expression
            return    adsk.core.ValueInput.createByString(expression)


        def addFixedValueUserParameter(
                param_name: str,
                value: float
        ):
            params = design.userParameters
            params.add(param_name, adsk.core.ValueInput.createByString(f'{value}mm'), "mm", '')

        def addExpressionUserParameter(
                param_name: str,
                expression: str
        ):
            params = design.userParameters
            params.add(param_name, adsk.core.ValueInput.createByString(f'{expression}mm'), "mm", '')

        # Add Parameters
        addFixedValueUserParameter("length", length)
        addFixedValueUserParameter("width", width)
        addFixedValueUserParameter("height", height)
        addFixedValueUserParameter("center_hole_diameter", center_hole_diameter)
        addExpressionUserParameter("center_hole_radius", "center_hole_diameter/2")

        # Create a new sketch on the xy plane.
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)

        # Draw a rectangle.
        sketch.sketchCurves.sketchLines.addTwoPointRectangle(
            createPoint((
                -length / 2,
                -width / 2,
                0  # Z-coordinate is 0 relative to the sketch plane
            )),
            createPoint((
                length / 2,
                width / 2,
                0  # Z-coordinate is 0 relative to the sketch plane
            ))
        )
        # Extrude the rectangle.
        ext = rootComp.features.extrudeFeatures
        profile = sketch.profiles.item(0)
        distance = createValueInput(height)

        extInput = ext.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extInput.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(distance),
                                  adsk.fusion.ExtentDirections.PositiveExtentDirection)

        extrusion = ext.add(extInput)

        # Get the top face of the box to use for the hole.
        top_face = None
        for face in extrusion.endFaces:
            # Assuming the top face is the largest in area.  A more robust method would
            # be to check the face normal.
            if top_face is None or face.area > top_face.area:
                top_face = face

        # Create the center hole using the Hole feature.
        center_point = createPoint((0, 0, 0))  # Origin point

        #hole_diameter = design.userParameters.itemByName("center_hole_diameter").valueInput
        hole_diameter = get_user_parameter("center_hole_diameter")

        createHole(top_face, center_point, hole_diameter, height * 0.1)  # height is in cm. convert to cm


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

