import adsk.core
import adsk.fusion
import traceback
from typing import Tuple

# Parameters
length = 80.0
width = 60.0
height = 10.0

def _build123d_value_to_fusion360_value(build123d_parameter_name: float) -> float:
    return build123d_parameter_name * 0.1  # convert mm to cm

def createPoint(coordinates: Tuple[float, float, float]) -> adsk.core.Point3D:
    return adsk.core.Point3D.create(*[_build123d_value_to_fusion360_value(c) for c in coordinates])

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

        # Draw a centered rectangle.  Because we want to align the bottom, we move the center point
        # down by half the height.
        centerPoint = createPoint((0, 0, -height/2)) #adjust centerpoint by height/2, offset from sketch plane
        sketch.sketchCurves.sketchLines.addCenterPointRectangle(
            centerPoint, createPoint((length / 2, width / 2, -height/2))
        )   #z value is used relative to sketch, so specify -height/2 again
        # Create the extrusion
        prof = sketch.profiles.item(0)
        distance = _build123d_value_to_fusion360_value(height)
        extInput = rootComp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extInput.setOneSideExtent(adsk.core.ValueInput.createByReal(distance), adsk.fusion.ExtentDirections.PositiveExtentDirection) # one side extent, positive direction
        rootComp.features.extrudeFeatures.add(extInput)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))

