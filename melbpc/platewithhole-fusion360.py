import adsk.core, adsk.fusion, adsk.cam, traceback

# Parameters
length = 1260  # Length of the box
width = 775    # Width of the box
height = 32    # Height of the box

x_offset = 30   # X offset for the hexagon
y2_offset = 45  # Y offset for the hexagon

hex_depth = 5.5  # Depth of the hexagon cut
hex_inscribed_radius = 5  # Inscribed radius of the hexagon

# Computed parameters
half_length = length / 2
half_width = width / 2

def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent

        # Get parameter values
        def userparameter_value(name):
            return design.unitsManager.evaluateExpression(params.itemByName(name).expression, 'mm')

        # Define user parameters
        params = design.userParameters
        params.add('length', adsk.core.ValueInput.createByString(f"{length}mm"), 'mm', '')
        params.add('width', adsk.core.ValueInput.createByString(f"{width}mm"), 'mm', '')
        params.add('height', adsk.core.ValueInput.createByString(f"{height}mm"), 'mm', '')
        params.add('x_offset', adsk.core.ValueInput.createByString(f"{x_offset}mm"), 'mm', '')
        params.add('y2_offset', adsk.core.ValueInput.createByString(f"{y2_offset}mm"), 'mm', '')
        params.add('hex_depth', adsk.core.ValueInput.createByString(f"{hex_depth}mm"), 'mm', '')
        params.add('hex_inscribed_radius', adsk.core.ValueInput.createByString(f"{hex_inscribed_radius}mm"), 'mm', '')

        # Create the base box
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)
        sketch.sketchCurves.sketchLines.addTwoPointRectangle(
            adsk.core.Point3D.create(0, 0, 0),
            adsk.core.Point3D.create(userparameter_value('length'), userparameter_value('width'), 0)
        )
        prof = sketch.profiles.item(0)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(userparameter_value('height'))
        extInput.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(distance), adsk.fusion.ExtentDirections.PositiveExtentDirection)
        
        extrudes.add(extInput)

        # Create sketch     
        sketches = rootComp.sketches   
        sketch = sketches.add(rootComp.xYConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(10, 10, 0)
        
        circle = sketchCircles.addByCenterRadius(centerPoint, 2)

        # Get the profile defined by the circle
        prof = sketch.profiles.item(0)
        extrudeInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.CutFeatureOperation)
        extent = adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByString("5.5mm"))
        start_offset = adsk.fusion.OffsetStartDefinition.create(adsk.core.ValueInput.createByString("32mm"))
        extrudeInput.startExtent = start_offset
        extrudeInput.setOneSideExtent(extent,adsk.fusion.ExtentDirections.NegativeExtentDirection)
        extrudes.add(extrudeInput)
            

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

