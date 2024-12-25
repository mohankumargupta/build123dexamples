#%%

from IPython.display import HTML

# Define the raw HTML content
raw_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>VTK.js Hello World</title>
  <script src="https://unpkg.com/vtk.js"></script>
  <style>
    #container {
      width: 100%;
      height: 500px; /* Adjust as needed */
      margin: 0;
      overflow: hidden;
      border: 1px solid #ccc;
    }
  </style>
</head>
<body>
  <div id="container"></div>

  <script>
    // Import VTK.js classes
    const vtk = window.vtk;

    // Create a render window and renderer
    const renderWindow = vtk.Rendering.Core.vtkRenderWindow.newInstance();
    const renderer = vtk.Rendering.Core.vtkRenderer.newInstance();
    renderWindow.addRenderer(renderer);

    // Create a render window interactor
    //const renderWindowInteractor = vtk.Rendering.Core.vtkRenderWindowInteractor.newInstance();
    //renderWindowInteractor.setView(renderWindow);

    // Create an OpenGL render window
    const openGLRenderWindow = vtk.Rendering.OpenGL.vtkRenderWindow.newInstance();
    renderWindow.addView(openGLRenderWindow);

    // Link OpenGL render window to DOM element
    const container = document.getElementById('container');
    openGLRenderWindow.setContainer(container);

    // Adjust interactor to listen to events in the container
    //renderWindowInteractor.initialize();
    //renderWindowInteractor.bindEvents(container);

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
    renderer.setBackground(0.1, 0.1, 0.1); // Dark gray background

    // Adjust the camera
    renderer.resetCamera();

    // Render the scene
    renderWindow.render();
  </script>
</body>
</html>
"""

# Display the HTML using IPython's display function
HTML(raw_html)

# %%
