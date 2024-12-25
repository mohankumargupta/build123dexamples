#%%
from IPython.display import display, HTML
import time

seconds_since_epoch = int(time.time())

html_content = """
<div id="myContainer_{seconds_since_epoch}"></div>

<script>
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
    }})
    .catch((error) => {{
        console.error("Failed to load VTK.js:", error);
    }});

</script>
"""

html = html_content.format(seconds_since_epoch=seconds_since_epoch, newContent="Some stuff2")
display(HTML(html))
#%%





