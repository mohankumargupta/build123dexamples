#%%

from IPython.display import HTML, display

html_content = """
<html><head>
<script src="https://unpkg.com/vtk.js@32.8.1/vtk.js"></script>
</head>
<body>

<div id="container"></div>
<div>boo</div>


<script>
    function render() {

    // Import VTK.js classes
    //const vtk = window.vtk;
    //document.querySelector('container').setContent("moo")

    // Create a render window and renderer
    const renderWindow = vtk.Rendering.Core.vtkRenderWindow.newInstance();
    const renderer = vtk.Rendering.Core.vtkRenderer.newInstance();
    renderWindow.addRenderer(renderer);

    // Create an OpenGL render window
    //const openGLRenderWindow = vtk.Rendering.OpenGL.vtkRenderWindow.newInstance();
    //renderWindow.addView(openGLRenderWindow);

    // Link OpenGL render window to DOM element
    const container = document.getElementById('container');
    renderWindow.setContainer(container);

    // Create and initialize the interactor
    const interactor = vtk.Rendering.Core.vtkRenderWindowInteractor.newInstance();
    interactor.setView(openGLRenderWindow);
    interactor.initialize();
    interactor.bindEvents(container);

    // Set the interaction style
    const interactorStyle = vtk.Interaction.Style.vtkInteractorStyleTrackballCamera.newInstance();
    interactor.setInteractorStyle(interactorStyle);

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
    renderer.setBackground(0.0, 1.0, 0.1);

    // Setup camera
    const camera = renderer.getActiveCamera();
    camera.setPosition(0, 0, 10);
    camera.setFocalPoint(0, 0, 0);
    
    // Apply camera transformations
    camera.elevation(35);
    camera.roll(35);
    camera.orthogonalizeViewUp();

    // Reset camera and render
    renderer.resetCamera();
    renderWindow.render();

    // Handle container resize
    //function updateSize() {
    //    const width = container.clientWidth;
    //    const height = container.clientHeight;
    //    openGLRenderWindow.setSize(width, height);
    //    renderWindow.render();
    //}

    // Initial size update
    //updateSize();
    }
    document.querySelector('container').innerHTML = "gdgg"
    //render();

</script>
</body>
</html>
"""

html2_content = """
<div id="container" style="width: 800px; height: 600px; margin: 0; overflow: hidden; border: 1px solid #ccc;"></div>

<script src="https://unpkg.com/vtk.js@32.8.1/vtk.js"></script>
<script>

</script>

"""

# Display the HTML content in the notebook
display(HTML(html_content))
# %%
