#%%
from IPython.display import display, HTML
import time

seconds_since_epoch = int(time.time())

html_content = """
<div id="myContainer_{seconds_since_epoch}"></div>

<script>
function changeContent() {{
    document.getElementById("myContainer_{seconds_since_epoch}").innerHTML = "{newContent}";
}}
setTimeout(changeContent, 0);
</script>
"""

html = html_content.format(seconds_since_epoch=seconds_since_epoch, newContent="fffloo")
display(HTML(html))
#%%
