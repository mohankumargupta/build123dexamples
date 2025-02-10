Okay, let's see. The user wants to convert a build123d script to Fusion 360's Python API. They provided an example conversion and now have another script to convert. The main difference in the new script is the align parameter in the Box function, which is set to (CENTER, CENTER, MIN). In the original example, the alignment was all CENTER, but now the Z-axis alignment is MIN.

First, I need to recall how alignment works in build123d. In the example explanation, they mentioned that Align.MIN in a direction means the shape's minimum (leftmost, bottommost, etc.) point is at the origin. For the Box in build123d, when align is set to (CENTER, CENTER, MIN), the box should be centered in X and Y, but aligned such that its minimum Z point (the bottom) is at the origin. So, in the Fusion 360 model, the box's bottom face should be on the XY plane (origin in Z), and centered in X and Y.

In the original example conversion, the Fusion script created a centered rectangle in the sketch and extruded symmetrically. But that was for CENTER alignment in all axes. Now, for Z being MIN, the extrusion should start at the origin and go upwards, not symmetric.

So, in the Fusion code, instead of using setSymmetricExtent, which extrudes equally in both directions from the sketch plane, we need to extrude in one direction. The sketch is on the XY plane, which is the same as the bottom face of the box. So the extrusion distance should be the height, starting from the sketch plane (origin) and going positive Z.

But wait, build123d's Box with align Z MIN would place the bottom at origin, so the height extends upwards. In Fusion, if we sketch on the XY plane and extrude upwards (positive Z) by height, that should match.

In the original example, the height was converted using _build123d_value_to_fusion360_value, which multiplies by 0.1 (mm to cm). But the user's Parameters in the new script are also in MM, so same conversion applies.

So, steps to adjust the Fusion code:

1. The sketch remains the same: centered rectangle, since X and Y are CENTER aligned. The rectangle's center is at origin, so half the length and width in each direction.

2. The extrusion should not be symmetric. Instead of setSymmetricExtent, use setOneSideExtent with the distance being the height converted to cm. The operation is NewBodyFeatureOperation.

Wait, in the original example, they used setSymmetricExtent with distance divided by 2? Wait, no. Let me check the original example code.

In the original example_fusion360.py, the rectangle is created with centerPoint and then the point (length/2, width/2, 0). That makes a rectangle from -length/2 to +length/2 in X, same for Y, so the total length is length, width. Then extrusion is symmetric with distance = height converted. But since symmetric, the total extrusion height would be 2*distance. Wait, that seems incorrect.

Wait, in build123d's Box, when all alignments are CENTER, the box is centered on all axes, so the extrusion in Fusion would need to be symmetric around the sketch plane. But if the height is 10mm, then symmetric extrusion of 5mm each way would give total 10mm. But in the original example, the height is converted to cm via _build123d_value_to_fusion360_value, which is height * 0.1. So 10mm becomes 1cm. Then symmetric extrusion of 1cm would give total 2cm height? That would be a problem. Wait, maybe there's a mistake here.

Wait, the original example in build123d has height 10*MM. In build123d, the Box is created with that height, aligned center. So the box's height is 10mm, centered on the origin in Z. So from -5mm to +5mm in Z. In the Fusion code, when they extrude symmetrically with distance = 10mm converted to cm (which is 1cm), that would extrude 1cm upwards and 1cm downwards, total height 2cm (20mm). That's incorrect. That suggests that the original example's conversion is flawed.

Wait, perhaps the user made a mistake in their example conversion. Because in build123d, the Box with height 10mm centered would be 5mm above and below the origin. But in Fusion, if they extrude symmetrically with 1cm (10mm) each way, that would create a total height of 20mm, which is double the intended.

So there's a mistake in the original example conversion. The correct approach would be to extrude the height in one direction, but centered. Wait, no. Wait, the Box in build123d with alignment CENTER in Z would have the center at the origin, with height extending equally in both directions. So the extrusion distance in Fusion would be half the height. But in the original example's code, they have:

distance = _build123d_value_to_fusion360_value(height) → which is 10mm → 1cm.

Then setSymmetricExtent with that distance, which would extrude 1cm in both directions, total 2cm (20mm). But build123d's height is 10mm. So the extrusion in Fusion is wrong. That's an error in the original example.

But the user's example is their own, and perhaps they are aware of that. However, for the current problem, the user's new script has align=(CENTER, CENTER, MIN), which places the box's bottom at the origin. So the height is entirely above the origin. So in Fusion, the extrusion should be in the positive Z direction with the full height.

So, for the current conversion, the sketch is the same (centered rectangle), but extrusion is one-directional, starting from the sketch plane (origin) and going up by height (converted to cm).

Therefore, in the Fusion code, instead of using setSymmetricExtent, we use setOneSideExtent with the distance being height converted to cm. Let's adjust that.

So, modifying the extrusion code:

extInput = rootComp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

extent_distance = adsk.core.ValueInput.createByReal(_build123d_value_to_fusion360_value(height))

extInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.PositiveExtentDirection)

rootComp.features.extrudeFeatures.add(extInput)

This way, the extrusion is in the positive Z direction by height (converted to cm), resulting in the box's bottom face at the origin (since the sketch is on XY plane), and height extending upwards.

So the main changes from the original example are:

1. The rectangle sketch remains centered in X and Y.

2. The extrusion is not symmetric but one-directional upwards.

Another thing to check: in build123d, the Box is created with align=(CENTER, CENTER, MIN), which affects the position. The Fusion sketch is on the XY plane, which is the same as the origin's Z=0. So the extrusion upwards will place the box's bottom at Z=0, aligning with MIN in Z.

Thus, the Fusion code needs to create a centered rectangle, then extrude upwards the full height (converted to cm), instead of symmetric.

The user's original example had a bug in the extrusion distance when using symmetric, but perhaps the user is following that method. However, for correctness, the current conversion should adjust the extrusion to be one-directional.

Now, writing the code:

The sketch part remains the same as the example.

For extrusion:

distance = _build123d_value_to_fusion360_value(height)

extInput = rootComp.features.extrudeFeatures.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

extent = adsk.fusion.DistanceExtentDefinition.create(adsk.core.ValueInput.createByReal(distance))

extInput.setOneSideExtent(extent, adsk.fusion.ExtentDirections.PositiveExtentDirection)

But wait, the correct method in Fusion's API is to create the extent. Alternatively, using setOneSideExtent with ValueInput directly.

Looking up the Fusion 360 API docs: The ExtrudeFeatures.createInput method, and then using setOneSideExtent.

The correct syntax is:

extInput.setOneSideExtent(adsk.core.ValueInput.createByReal(distance), adsk.fusion.ExtentDirections.PositiveExtentDirection)

So modifying the original code's extrusion part from symmetric to one-side.

So in the original example's code, the extrusion was:

extInput.setSymmetricExtent(adsk.core.ValueInput.createByReal(distance), True)

Which creates a symmetric extrusion. Now, changing that to setOneSideExtent with the distance and direction.

Thus, the corrected code for the current problem would adjust the extrusion to be one-directional, positive Z direction, with the full converted height.

So the final code for the user's script would involve:

- Sketching the same centered rectangle.

- Extruding upwards (positive direction) by the converted height.

Therefore, the Fusion 360 script would look similar to the example, but with changes in the extrusion part.

To convert the given build123d script to Fusion 360's Python API, we need to adjust the alignment in the Z-axis to Align.MIN, which positions the box's bottom face at the origin. Here's the converted script:

```python

import adsk.core
import adsk.fusion
import traceback
from typing import Tuple

# Parameters
length = 80.0
width = 60.0
height = 10.0

def _build123d_value_to_fusion360_value(build123d_parameter_name: float) -> float:
    return build123d_parameter_name * 0.1  # Convert mm to cm

def createPoint(coordinates: Tuple[float, float, float]) -> adsk.core.Point3D:
    return adsk.core.Point3D.create(*coordinates)

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

        rootComp = design.rootComponent

        # Create centered rectangle on XY plane
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        centerPoint = createPoint((0, 0, 0))
        cornerPoint = createPoint((length / 2, width / 2, 0))  # Centered in X and Y
        sketch.sketchCurves.sketchLines.addCenterPointRectangle(centerPoint, cornerPoint)

        # Extrude upwards (Z+) with bottom at origin (Align.MIN in Z)
        prof = sketch.profiles.item(0)
        distance = _build123d_value_to_fusion360_value(height)
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extInput.setOneSideExtent(
            adsk.core.ValueInput.createByReal(distance),
            adsk.fusion.ExtentDirections.PositiveExtentDirection
        )
        extrudes.add(extInput)

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))
```

Key Adjustments:

Z-Alignment Handling:

The align=(Align.CENTER, Align.CENTER, Align.MIN) in build123d places the box's bottom face at the origin. In Fusion 360, this is achieved by extruding upwards from the XY plane (Z+ direction).

Extrusion Direction:

Replaced setSymmetricExtent with setOneSideExtent to extrude the full height in the positive Z-direction, ensuring the bottom face stays at Z=0.

Unit Conversion:

The _build123d_value_to_fusion360_value function converts millimeters to centimeters (Fusion 360 uses cm by default).

This script creates a box centered in X/Y with its base at the origin, matching the behavior of the build123d code.

