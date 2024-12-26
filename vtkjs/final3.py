#%%
from IPython.display import display, HTML
import time

seconds_since_epoch = int(time.time())

html_content = """
<div id="myContainer_{seconds_since_epoch}"></div>

<script>
function render() {{

        console.log("render function called");
        const renderWindow = vtk.Rendering.Core.vtkRenderWindow.newInstance();
        const renderer = vtk.Rendering.Core.vtkRenderer.newInstance();
        renderWindow.addRenderer(renderer);

        // Create a cube source
        const cubeSource = vtk.Filters.Sources.vtkCubeSource.newInstance();

        // Create a mapper
        const mapper = vtk.Rendering.Core.vtkMapper.newInstance();
        mapper.setInputConnection(cubeSource.getOutputPort());

        // Create an actor
        const actor = vtk.Rendering.Core.vtkActor.newInstance();
        actor.setMapper(mapper);

        // Add actor to the renderer
        renderer.addActor(actor);

        // Set renderer background color
        //renderer.setBackground(0.0, 1.0, 0.1);
        renderer.setBackground(0.0, 1.0, 0.1);

        // Setup camera
        const camera = renderer.getActiveCamera();
        //camera.setParallelProjection(true);
        //camera.setPosition(0, 0, 10);
        //camera.setFocalPoint(0, 0, 0);
        //camera.setParallelScale(1.5);

        camera.elevation(35)
        camera.roll(35)
        camera.orthogonalizeViewUp()

        // Reset camera and render
        renderer.resetCamera();
        renderWindow.render();

        const openglRenderWindow = vtk.Rendering.OpenGL.vtkRenderWindow.newInstance();
        renderWindow.addView(openglRenderWindow);
        
        container = document.querySelector("#myContainer_{seconds_since_epoch}");
        openglRenderWindow.setContainer(container);

        console.log(container);
}}

function loadVTK() {{
    return new Promise((resolve, reject) => {{
        if (typeof require !== "undefined") {{
            // Use RequireJS if available
            require.config({{
                paths: {{ vtk: "https://unpkg.com/vtk" }},
            }});
            require(["vtk"], resolve, reject);
        }} else if (typeof vtk === "undefined") {{
            // Fallback to dynamically loading the script
            const script = document.createElement("script");
            script.src = "https://unpkg.com/vtk.js";
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        }} else {{
            // VTK is already loaded
            resolve();
        }}
    }});
}}

loadVTK()
    .then(() => {{
        console.log("vtk loaded.");
        console.log(vtk);
        render();
    }})
    .catch((error) => {{
        console.error("Failed to load VTK.js:", error);
    }});

</script>
"""

html = html_content.format(seconds_since_epoch=seconds_since_epoch, newContent="Some stuff2")
display(HTML(html))
#%%





