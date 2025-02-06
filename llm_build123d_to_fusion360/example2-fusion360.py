import adsk.core
import adsk.fusion
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        # Ensure we have a design open
        if not design:
            ui.messageBox('No active Fusion 360 design')
            return

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Create a new sketch on the XY plane
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        # Draw a rectangle for the box
        lines = sketch.sketchCurves.sketchLines
        rect = lines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(10, 10, 0))

        # Extrude the rectangle to create the box
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(10)
        extInput.setDistanceExtent(False, distance)
        box = extrudes.add(extInput)

        # Create a sketch for the cylinder
        cylinderSketch = sketches.add(xyPlane)
        circles = cylinderSketch.sketchCurves.sketchCircles
        circle = circles.addByCenterRadius(adsk.core.Point3D.create(5, 5, 0), 3)

        # Extrude the circle to create the cylinder
        cylinderProf = cylinderSketch.profiles.item(0)
        cylinderExtInput = extrudes.createInput(cylinderProf, adsk.fusion.FeatureOperations.CutFeatureOperation)
        cylinderDistance = adsk.core.ValueInput.createByReal(10)
        cylinderExtInput.setDistanceExtent(False, cylinderDistance)
        cylinder = extrudes.add(cylinderExtInput)

        ui.messageBox('Box with cut cylinder created successfully!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))