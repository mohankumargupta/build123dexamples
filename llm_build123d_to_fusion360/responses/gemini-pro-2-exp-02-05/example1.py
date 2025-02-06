import adsk.core
import adsk.fusion
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent
        
        # Get parameter values
        def userparameter_value(name):
            return design.unitsManager.evaluateExpression(params.itemByName(name).expression, 'mm')

        # Parameters
        params = design.userParameters
        params.add("length", adsk.core.ValueInput.createByString("80 mm"), "mm", '')
        params.add("width", adsk.core.ValueInput.createByString("60 mm"), "mm", '')
        params.add("height", adsk.core.ValueInput.createByString("10 mm"), "mm", '')

        # Radius and Diameters
        params.add("center_hole_diameter", adsk.core.ValueInput.createByString("22 mm"), "mm", '')
        params.add("center_hole_radius", adsk.core.ValueInput.createByString("center_hole_diameter/2"), "mm", '')

        # Create a new sketch on the xy plane
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)

        # Draw a rectangle
        lines = sketch.sketchCurves.sketchLines
        rect_point1 = adsk.core.Point3D.create(-userparameter_value('length')/2, -userparameter_value('width')/2, 0)
        rect_point2 = adsk.core.Point3D.create(userparameter_value('length')/2, userparameter_value('width')/2, 0)
        rectangle = lines.addTwoPointRectangle(rect_point1, rect_point2)
        
        # Get the profile of the rectangle
        profile = sketch.profiles.item(0)

        # Create an extrusion
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define the extent of the extrusion - Use DistanceExtentDefinition
        distance = adsk.core.ValueInput.createByReal(userparameter_value('height'))
        extInput.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(distance), adsk.fusion.ExtentDirections.PositiveExtentDirection)

        # Create the extrusion
        extrude = extrudes.add(extInput)
       
        # Create a new sketch on the top face of the box for the hole
        top_face = extrude.endFaces.item(0)  
        sketch_hole = rootComp.sketches.add(top_face)

        # Draw a circle for the hole
        circles = sketch_hole.sketchCurves.sketchCircles
        
        center_point = adsk.core.Point3D.create(0,0,0)

        circle = circles.addByCenterRadius(center_point, userparameter_value('center_hole_radius')/10) #/10 for cm
        
        hole_profile = sketch_hole.profiles.item(0)

        # Create a hole - Extrude Cut
        cut_ext = rootComp.features.extrudeFeatures
        cut_input = cut_ext.createInput(hole_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
        
        #Set Extent
        distance = adsk.core.ValueInput.createByReal(userparameter_value('height'))

        cut_input.setOneSideExtent(adsk.fusion.DistanceExtentDefinition.create(distance), adsk.fusion.ExtentDirections.NegativeExtentDirection)
    
        hole_extrude = cut_ext.add(cut_input)




    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

