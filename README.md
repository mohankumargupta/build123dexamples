# Interactive jupyter notebook 

It is possible to display build123d inline in vscode without ocp_vscode

To do so, you only need build123d and notebook pypi packages. In vscode, you need python and jupyter extensions.

You then create a new notebook using Command palette-> Create: New Jupyter Notebook (must be done this way, not manually creating a ipynb file).

```py
from build123d import *
part = Box(10,10,10)
part
```



