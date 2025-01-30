import adsk.core, adsk.fusion, traceback

# Parameters
length = 1260  # mm
width = 775  # mm
height = 32  # mm

x_offset = 30  # mm
y_offset = 730  # mm
y1_offset = 30  # mm
y2_offset = 45  # mm

spacing_small = 50  # mm
spacing_large = 100  # mm

hex_depth = 5.5  # mm

# Radius and diameters
hex_inscribed_radius = 5  # mm

# Computed parameters
half_length = length / 2
half_width = width / 2

def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        rootComp = design.rootComponent

        # Get the user parameters
        params = design.userParameters

        # Add user parameters
        params.add('length', adsk.core.ValueInput.createByString(f"{length}mm"), 'mm', '')
        params.add('width', adsk.core.ValueInput.createByString(f"{width}mm"), 'mm', '')
        params.add('height', adsk.core.ValueInput.createByString(f"{height}mm"), 'mm', '')
        params.add('x_offset', adsk.core.ValueInput.createByString(f"{x_offset}mm"), 'mm', '')
        params.add('y_offset', adsk.core.ValueInput.createByString(f"{y_offset}mm"), 'mm', '')
        params.add('y1_offset', adsk.core.ValueInput.createByString(f"{y1_offset}mm"), 'mm', '')
        params.add('y2_offset', adsk.core.ValueInput.createByString(f"{y2_offset}mm"), 'mm', '')
        params.add('spacing_small', adsk.core.ValueInput.createByString(f"{spacing_small}mm"), 'mm', '')
        params.add('spacing_large', adsk.core.ValueInput.createByString(f"{spacing_large}mm"), 'mm', '')
        params.add('hex_depth', adsk.core.ValueInput.createByString(f"{hex_depth}mm"), 'mm', '')
        params.add('hex_inscribed_radius', adsk.core.ValueInput.createByString(f"{hex_inscribed_radius}mm"), 'mm', '')

        # Function to get parameter values
        def userparameter_value(name):
            return design.unitsManager.evaluateExpression(params.itemByName(name).expression, 'mm')

        # Create the base box
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        sketchLines = sketch.sketchCurves.sketchLines
        sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(0, 0, 0),
            adsk.core.Point3D.create(userparameter_value('length'), userparameter_value('width'), 0)
        )
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(userparameter_value('height'))
        extInput.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(distance), adsk.fusion.ExtentDirections.PositiveExtentDirection)
        baseExtrude = extrudes.add(extInput)  # Store the extrusion feature

        # Get the top face of the base body
        baseBody = baseExtrude.bodies.item(0)
        topFace = None
        for face in baseBody.faces:
            if face.geometry.surfaceType == adsk.core.SurfaceTypes.PlaneSurfaceType:
                normal = face.geometry.normal
                if normal.z == 1:  # Top face has a normal pointing in the +Z direction
                    topFace = face
                    break

        if not topFace:
            ui.messageBox('Top face not found!')
            return

        # Create the hexagonal cut on the top face
        sketch = sketches.add(topFace)
        centerPoint = adsk.core.Point3D.create(
            userparameter_value('length') - userparameter_value('x_offset'),
            userparameter_value('y2_offset'),
            0  # Z-coordinate is 0 relative to the sketch plane
        )
        sketch.sketchCurves.sketchLines.addScribedPolygon(
            centerPoint,
            6,
            90,
            userparameter_value('hex_inscribed_radius'),
            True
        )
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(userparameter_value('hex_depth'))
        extInput.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(distance), adsk.fusion.ExtentDirections.NegativeExtentDirection)
        extrudes.add(extInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

            