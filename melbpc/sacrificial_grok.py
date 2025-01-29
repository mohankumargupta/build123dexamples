import adsk.core
import adsk.fusion
import math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        
        # Create a new component
        rootComp = design.rootComponent
        newComp = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create()).component
        newComp.name = 'Sacrificial Table'

        # Parameters
        length = 1260
        width = 775
        height = 25

        x_offset = 30
        y1_offset = 30
        y2_offset = 45

        spacing_small = 50
        spacing_large = 100

        diameter = 6
        radius = diameter / 2

        half_length = length / 2
        half_width = width / 2

        # Create the main box
        box = adsk.fusion.BRepBodies.addExtrude(newComp, adsk.fusion.SketchProfiles.createForExtrude(newComp.sketches.add(newComp.xYConstructionPlane), [
            adsk.fusion.SketchCurves.sketchLines.addCenterRectangle(adsk.core.Point3D.create(0, 0, 0), length, width)
        ]), adsk.fusion.FeatureOperations.NewBodyFeatureOperation, height)

        # Function to create holes
        def create_hole(x, y, z):
            sketch = newComp.sketches.add(newComp.xYConstructionPlane)
            circles = sketch.sketchCurves.sketchCircles
            circles.addByCenterRadius(adsk.core.Point3D.create(x, y, 0), radius)
            extrudes = newComp.features.extrudeFeatures
            extrudeInput = extrudes.createInput(sketch.profiles.item(0), adsk.fusion.FeatureOperations.CutFeatureOperation)
            extent = adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByReal(height))
            extrudeInput.setOneSideExtent(extent, adsk.fusion.ExtentDirections.PositiveExtentDirection)
            extrudes.add(extrudeInput)

        # Create holes for the first grid
        for i in range(13):
            for j in range(4):
                create_hole((i - 6) * spacing_large, spacing_small + j * spacing_large, 0)

        # Create holes for the second grid
        for i in range(7):
            for j in range(4):
                create_hole(half_length - y2_offset + (i - 3) * spacing_large, -half_width + y2_offset + j * spacing_large, 0)

        # Create holes for the third grid
        for i in range(12):
            for j in range(7):
                create_hole(spacing_small + i * spacing_small, -half_width + y2_offset + j * spacing_small, 0)

        # Export functionality is not directly supported in Fusion 360 API for STEP or STL, 
        # but you can manually export the design from the UI.

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))