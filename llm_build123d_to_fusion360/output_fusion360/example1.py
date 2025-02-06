import adsk.core, adsk.fusion, adsk.cam, traceback
import math

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Parameters
        length = 80.0  # mm
        width = 60.0   # mm
        height = 10.0  # mm

        # Radius and Diameters
        center_hole_diameter = 22.0  # mm
        center_hole_radius = center_hole_diameter / 2

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)


        # Create a box (extruded rectangle)
        # 1. Draw a rectangle on the sketch.  We'll center it.
        center_x = 0
        center_y = 0
        lines = sketch.sketchCurves.sketchLines
        rect = lines.addTwoPointRectangle(
            adsk.core.Point3D.create(center_x - length / 2, center_y - width / 2, 0),
            adsk.core.Point3D.create(center_x + length / 2, center_y + width / 2, 0)
        )


        # 2. Extrude the rectangle.
        prof = sketch.profiles.item(0)  # Get the profile of the rectangle
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define the distance (height) of the extrusion.  Use a ValueInput.
        distance = adsk.core.ValueInput.createByReal(height)
        extInput.setDistanceExtent(False, distance)  # False means one-sided extrusion.
        box_extrude = extrudes.add(extInput)


        # Create the center hole (extruded circle)
        # 1. Create a new sketch on the top face of the box.  Find the top face.
        top_face = None
        for face in box_extrude.endFaces: #find the top face
            for loop in face.loops:
                if loop.isOuter:
                    normal = loop.edges[0].tangentAt(loop.edges[0].startVertex.geometry)
                    if normal.z > 0.99999:
                        top_face = face
                        break #inner loop
            if top_face: break #outer loop

        if not top_face:
            ui.messageBox("Could not find top face.")
            return

        hole_sketch = sketches.add(top_face)
       

        # 2. Draw a circle on the sketch.  Place it at the center.
        circles = hole_sketch.sketchCurves.sketchCircles
        center_circle = circles.addByCenterRadius(adsk.core.Point3D.create(center_x, center_y, 0), center_hole_radius)

        # 3. Extrude the circle to create the hole (cut operation).
        hole_prof = hole_sketch.profiles.item(0)
        hole_extInput = extrudes.createInput(hole_prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
      
        # Use a negative distance to cut through the box.
        hole_distance = adsk.core.ValueInput.createByReal(-height)
        hole_extInput.setDistanceExtent(False, hole_distance)  # Cut through the entire body.
        extrudes.add(hole_extInput)
       

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
