from pathlib import Path
from build123d import *
from cad_utils import cad_visualize

# Method 1: Using the decorator
@cad_visualize(modules_to_import=['build123d', 'ocp_vscode'])
def create_arc_model():
    # Your CAD modeling code here
    l1 = CenterArc(center=(0,0,0), radius=17.5, start_angle=90, arc_size=180)
    return l1

# This will automatically import modules and show the model
my_model = create_arc_model()

# Method 2: Using the context manager
from cad_utils import cad_helper

with cad_helper.cad_context(modules_to_import=['build123d', 'ocp_vscode']):
    # Your CAD modeling code
    l2 = CenterArc(center=(0,0,0), radius=20, start_angle=0, arc_size=270)

# Method 3: More advanced usage with custom options
@cad_visualize(
    show=True,  # Whether to show the model
    reset_camera=Camera.KEEP,  # Specific camera reset option
    modules_to_import=['build123d', 'ocp_vscode']
)
def complex_model():
    # More complex CAD operations
    base = Box(10, 20, 5)
    cutout = Cylinder(radius=3, height=5)
    final_part = base.cut(cutout)
    return final_part

# Execute the complex model
complex_part = complex_model()