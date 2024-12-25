#%%
from IPython.display import display, HTML
import time

seconds_since_epoch = int(time.time())

html_content = """
<div id="myContainer_{seconds_since_epoch}"></div>

<script>
function changeContent() {{
    document.getElementById("myContainer_{seconds_since_epoch}").innerHTML = "{newContent}";
    print(vtk)
}}


setTimeout(()=>{{
  changeContent();
}}, 0);

console.log("does work");

</script>
"""

html = html_content.format(seconds_since_epoch=seconds_since_epoch, newContent="Some stuff2")
display(HTML(html))
#%%
