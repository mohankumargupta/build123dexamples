import adsk.core
import adsk.fusion
import traceback
from typing import Tuple

# Parameters
length = 80.0
width = 60.0
height = 10.0

def _build123d_value_to_fusion360_value(build123d_parameter_name: float) -> float:
    return build123d_parameter_name * 0.1 # convert mm to cm

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
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketch.sketchCurves.sketchLines.addCenterPointRectangle(
            centerPoint, adsk.core.Point3D.create(_build123d_value_to_fusion360_value(length / 2), _build123d_value_to_fusion360_value(width / 2), 0)
        )  # z is relative to sketch plane

        # Create the extrusion
        prof = sketch.profiles.item(0)
        distance = _build123d_value_to_fusion360_value(height)
        extInput = rootComp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distanceExtent = adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByReal(distance))
        direction = adsk.fusion.ExtentDirections.PositiveExtentDirection
        extInput.setOneSideExtent(distanceExtent, direction)

        rootComp.features.extrudeFeatures.add(extInput)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))