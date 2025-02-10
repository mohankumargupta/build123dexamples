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
 
def _build123d_value_to_fusion360_value(build123d_parameter_name: float)->float:
    return build123d_parameter_name * 0.1 # convert mm to cm

def createPoint(point: Tuple[float, float, float]) -> adsk.core.Point3D:
    x, y, z = point
    return adsk.core.Point3D.create(x * 0.1, y * 0.1, z * 0.1)

def createHole(
    plane1: adsk.fusion.BRepFace,
    point: adsk.core.Point3D,
    diameter: adsk.core.ValueInput,
    depth: float,
) -> adsk.fusion.HoleFeature:
    comp: adsk.fusion.Component = plane1.body.parentComponent
    holeFeatures: adsk.fusion.HoleFeatures = comp.features.holeFeatures
    holeInput: adsk.fusion.HoleFeatureInput = holeFeatures.createSimpleInput(adsk.core.ValueInput.createByReal(diameter))
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
        distance = _build123d_value_to_fusion360_value(height)
        extInput = rootComp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extInput.setSymmetricExtent(adsk.core.ValueInput.createByReal(distance), True)
        rootComp.features.extrudeFeatures.add(extInput)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


