# %%
from IPython.display import display, HTML
from vtkmodules.vtkIOXML import vtkXMLPolyDataWriter
from build123d import Cylinder

def to_vtkpoly_string(
    shape, tolerance: float = 1e-3, angular_tolerance: float = 0.1
) -> str:
    """to_vtkpoly_string

    Args:
        shape (Shape): object to convert
        tolerance (float, optional): Defaults to 1e-3.
        angular_tolerance (float, optional): Defaults to 0.1.

    Raises:
        ValueError: not a valid Shape

    Returns:
        str: vtkpoly str
    """
    if not hasattr(shape, "wrapped"):
        raise ValueError(f"Type {type(shape)} is not supported")

    writer = vtkXMLPolyDataWriter()
    writer.SetWriteToOutputString(True)
    writer.SetInputData(shape.to_vtk_poly_data(tolerance, angular_tolerance, True))
    writer.Write()

    return writer.GetOutputString()

cylinder = Cylinder(radius=10, height=30)
output = to_vtkpoly_string(cylinder)
#print(output)



RAW_HTML = """


<script>
function render(data, parent_element, ratio){{

    // Initial setup
    const renderWindow = vtk.Rendering.Core.vtkRenderWindow.newInstance();
    const renderer = vtk.Rendering.Core.vtkRenderer.newInstance({{ background: [1, 1, 1 ] }});
    renderWindow.addRenderer(renderer);

    // iterate over all children children
    for (var el of data){{
        var trans = el.position;
        var rot = el.orientation;
        var rgba = el.color;
        var shape = el.shape;

        // load the inline data
        var reader = vtk.IO.XML.vtkXMLPolyDataReader.newInstance();
        const textEncoder = new TextEncoder();
        reader.parseAsArrayBuffer(textEncoder.encode(shape));

        // setup actor,mapper and add
        const mapper = vtk.Rendering.Core.vtkMapper.newInstance();
        mapper.setInputConnection(reader.getOutputPort());
        mapper.setResolveCoincidentTopologyToPolygonOffset();
        mapper.setResolveCoincidentTopologyPolygonOffsetParameters(0.5,100);

        const actor = vtk.Rendering.Core.vtkActor.newInstance();
        actor.setMapper(mapper);

        // set color and position
        actor.getProperty().setColor(rgba.slice(0,3));
        actor.getProperty().setOpacity(rgba[3]);

        actor.rotateZ(rot[2]*180/Math.PI);
        actor.rotateY(rot[1]*180/Math.PI);
        actor.rotateX(rot[0]*180/Math.PI);

        actor.setPosition(trans);

        renderer.addActor(actor);

    }};

    renderer.resetCamera();

    const openglRenderWindow = vtk.Rendering.OpenGL.vtkRenderWindow.newInstance();
    renderWindow.addView(openglRenderWindow);

    // Add output to the "parent element"
    var container;
    var dims;

    if(typeof(parent_element.appendChild) !== "undefined"){{
        container = document.createElement("div");
        parent_element.appendChild(container);
        dims = parent_element.getBoundingClientRect();
    }}else{{
        container = parent_element.append("<div/>").children("div:last-child").get(0);
        dims = parent_element.get(0).getBoundingClientRect();
    }};

    openglRenderWindow.setContainer(container);

    // handle size
    if (ratio){{
        openglRenderWindow.setSize(dims.width, dims.width*ratio);
    }}else{{
        openglRenderWindow.setSize(dims.width, dims.height);
    }};

    // Interaction setup
    const interact_style = vtk.Interaction.Style.vtkInteractorStyleManipulator.newInstance();

    const manips = {{
        rot: vtk.Interaction.Manipulators.vtkMouseCameraTrackballRotateManipulator.newInstance(),
        pan: vtk.Interaction.Manipulators.vtkMouseCameraTrackballPanManipulator.newInstance(),
        zoom1: vtk.Interaction.Manipulators.vtkMouseCameraTrackballZoomManipulator.newInstance(),
        zoom2: vtk.Interaction.Manipulators.vtkMouseCameraTrackballZoomManipulator.newInstance(),
        roll: vtk.Interaction.Manipulators.vtkMouseCameraTrackballRollManipulator.newInstance(),
    }};

    manips.zoom1.setControl(true);
    manips.zoom2.setScrollEnabled(true);
    manips.roll.setShift(true);
    manips.pan.setButton(2);

    for (var k in manips){{
        interact_style.addMouseManipulator(manips[k]);
    }};

    const interactor = vtk.Rendering.Core.vtkRenderWindowInteractor.newInstance();
    interactor.setView(openglRenderWindow);
    interactor.initialize();
    interactor.bindEvents(container);
    interactor.setInteractorStyle(interact_style);

    // Orientation marker

    const axes = vtk.Rendering.Core.vtkAnnotatedCubeActor.newInstance();
    axes.setXPlusFaceProperty({{text: '+X'}});
    axes.setXMinusFaceProperty({{text: '-X'}});
    axes.setYPlusFaceProperty({{text: '+Y'}});
    axes.setYMinusFaceProperty({{text: '-Y'}});
    axes.setZPlusFaceProperty({{text: '+Z'}});
    axes.setZMinusFaceProperty({{text: '-Z'}});

    const orientationWidget = vtk.Interaction.Widgets.vtkOrientationMarkerWidget.newInstance({{
        actor: axes,
        interactor: interactor }});
    orientationWidget.setEnabled(true);
    orientationWidget.setViewportCorner(vtk.Interaction.Widgets.vtkOrientationMarkerWidget.Corners.BOTTOM_LEFT);
    orientationWidget.setViewportSize(0.2);

}};

new Promise(
  function(resolve, reject)
  {
    if (typeof(require) !== "undefined" ){
        require.config({
         "paths": {"vtk": "https://unpkg.com/vtk"},
        });
        require(["vtk"], resolve, reject);
    } else if ( typeof(vtk) === "undefined" ){
        var script = document.createElement("script");
    	script.onload = resolve;
    	script.onerror = reject;
    	script.src = "https://unpkg.com/vtk.js";
    	document.head.appendChild(script);
    } else { resolve() };
 }
).then(() => {
    var parent_element = "element";

    cube_data = "
<?xml version="1.0"?>
<VTKFile type="PolyData" version="0.1" byte_order="LittleEndian" header_type="UInt32" compressor="vtkZLibDataCompressor">
  <PolyData>
    <Piece NumberOfPoints="1276"                 NumberOfVerts="2"                    NumberOfLines="759"                  NumberOfStrips="0"                    NumberOfPolys="500"                 >
      <PointData Normals="Normals">
        <DataArray type="Float32" Name="Normals" NumberOfComponents="3" format="appended" RangeMin="0"                    RangeMax="1.0000000457"         offset="0"                   />
      </PointData>
      <CellData Normals="Normals">
        <DataArray type="Int64" IdType="1" Name="SUBSHAPE_IDS" format="appended" RangeMin="4"                    RangeMax="13"       
            offset="1880"                />
        <DataArray type="Int64" IdType="1" Name="MESH_TYPES" format="appended" RangeMin="2"                    RangeMax="8"
          offset="2000"                />
        <DataArray type="Float32" Name="Normals" NumberOfComponents="3" format="appended" RangeMin="0.99999997013"        RangeMax="1.0000000336"         offset="2108"                />
      </CellData>
      <Points>
        <DataArray type="Float32" Name="Points" NumberOfComponents="3" format="appended" RangeMin="18.027756133"         RangeMax="18.027756599"         offset="3480"                />
      </Points>
      <Verts>
        <DataArray type="Int64" Name="connectivity" format="appended" RangeMin=""                     RangeMax=""
 offset="4956"                />
        <DataArray type="Int64" Name="offsets" format="appended" RangeMin=""                     RangeMax=""                     offset="5000"                />
      </Verts>
      <Lines>
        <DataArray type="Int64" Name="connectivity" format="appended" RangeMin=""                     RangeMax=""
 offset="5044"                />
        <DataArray type="Int64" Name="offsets" format="appended" RangeMin=""                     RangeMax=""                     offset="6824"                />
      </Lines>
      <Strips>
        <DataArray type="Int64" Name="connectivity" format="appended" RangeMin=""                     RangeMax=""
 offset="8356"                />
        <DataArray type="Int64" Name="offsets" format="appended" RangeMin=""                     RangeMax=""                     offset="8372"                />
      </Strips>
      <Polys>
        <DataArray type="Int64" Name="connectivity" format="appended" RangeMin=""                     RangeMax=""
 offset="8388"                />
        <DataArray type="Int64" Name="offsets" format="appended" RangeMin=""                     RangeMax=""                     offset="10940"               />
      </Polys>
    </Piece>
  </PolyData>
  <AppendedData encoding="base64">
   _AQAAAACAAADQOwAAbwUAAA==eJztlntM1WUYxy0qLXVjNRPEyzKiMC8B0Zye83sWkjEEXTOBInOpXUyuonjDc2yaWQ5SQi27uiJSRGu2IC7vs9m8lMwwTFmYgkaTi27Aljov9JznPK/96uCp9Sd7v399dnZ+5/x+z/t9P7+3Xz8TExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTk76W7e1u6HbUOjycftANwQ+NcXp41gUX5F+sZA4IXQVlHwVZHk5zrYB6x0zmxUOWQXNZHvOCTxZDZNsWZmd9JmwO2cv8a8tCaG86wOzY+DIkTf+Fec/PL0DxyE7mORtSoXZnAHh43tqZoKIDmc8EJkB74TDmC0ufgO620cxjhznhXMFY5kGxj8Lg/dHMU+aHw+edwNz/w1EQEhbHHJ01BCY0zmBO/u0u6BiYDPL4cGLvbObTh1qs0P3zmacW/WRlpSxgvji4ysLEDObdgZ9as0sXMYd9V2DVNyxhbg1Ls3KClzMfrYuwZg/PY+4sue6cH+BivnrbTufBEW5mR9gA5/eNXp4ctr666w8vHwtcXxOV6dbX1uhr4yImqTeqVjJvODlPNRV5/8u9aZ1q68llTr/jY/VtUg5z8L3lasfdmcyPf3VEZT72KnPToRaln7Gnp0fpZ6eZoJ5J4df3YMrQp/QMUc+QZot6tkMmRuCPNROZ43dMxtpR45ldIbFYkR/KHHogHo9MGa7XFPWaQvazeDTvduYttXMw591L3IE15S/i1svNzKdaFmKHdObLt7MwccQe5rJrOXj98jbdPdTd29yxAht/j2cuqsvD0AH3MSdXurC19TB3+M3dbhz2cAJz9TU3xkYOcNg+r7F9n5k6j9R5Zft9ZftfZuo8UueZzzyZjW0hpcxzy9Pwke59zNR5pM4zU+eROq9sc0DbfJgDUhIx4XQQ2ubJPM07Z2bqPFLn0bYuaFsv5qjwoZj8/nS0rS/a1p15UVGr+uzIPJTOK+o887pbUX2wNp15YFCJqriSjdJ5RZ1H6byizqN0XlHn0dZblM7XUOdROl9DnWd+cHKtg7zjvf9B7zkxzq2vdeprZR8x31+Qap0duII5v/QtKz8j1zuHoBLrG7k32aconbeo8yid9+xr5pHTr1pT9z3P7A6+E96JSEHpPFDn9QxBz1B8gtJ5oM7rtQC9FuIlZvGVXlPQa0prDXqtqfNAnecOtBe/BOcfOMUsnmQWfyrpPFDndfegSbpHnQTdSeo8UOeZG15zwRcNJ7nDoza5wTUmg1k8X21jh/7O6jEZTtu1Ps5PTFoJCfkxfp1P/Yf2kFIf59O+Br2v5dmZY2Y+A8sT+vs4v9nm/K1VMbB5XBjz0OhJsK1sgvYPaP/4c/74XpxP/be0986mnrdCjs316/wym/PJt5b2rXTSx/ldNueTz53a5+R5h/a87AXmK9494uP8qPRwVbUsz8f5sgdB+q+o/8yve/cs88ac42pG7iv6GZV+Rrvzk8gJ52Um4openV8ssxXngPS/V+d73DXtdJBf54sD9XkAn5bzAHUG23txfr21BKtOFPp1/qVFq3BNZGCvzg/+u/Or9ed255/7n86nfYp6n44LXIijD/+gpPOed5mSzqPe7zdzvrwr/Tpf3rl+nS/vbh/nU1A7P/smzpczA7OcJbye9J4xtIeV9rDd+V0258sZhlnONv/Z+XU258uZysf5dG+Wvje786nzFnWeWfY1867jt8DK7c8xV+waBEvPzNLvR9Dvx386v1hmK2dLH+eLl244v+1fnC9nXR/n0zkHOsT54k9m6jxQ5284v7kX51PngTrP7DmrF1ys5A7LGd7H+X9lNRg2bNiw4T7NaNiwYcOG+x7/CceX2kU=AQAAAACAAABoJwAASAAAAA==eJzt18EJgDAQRFEPwRjF/tvNwW0gICxk31xeC/P78W2EJ8kyXuFNsoyNJElu70OyjC/JMmb/C5Ik+b/ZPUFSr5NcdwKkHidRAQAAAACAAABoJwAAPQAAAA==eJzt1TEKACAMA0ApiP7/xQ72CYJiL8utWUKi7UTaSZZxPtKDJEme18+T9bR7kiT/dZAkSZIkyesul3QcjQ==AQAAAACAAAAcOwAA8QMAAA==eJzt1luITlEUB/CTa5nSeFByiQcURSg8mO/sB8olUi6RKDVSIiEmNMx+8EJJMSkPbkloXJIHxXxnJ+XFJZfy4pLkkktJPMv+trW3v73m42wzPK2pqV+r9Z19OWuvs7NMqyz8icVisVgsFovFYrFYLBaLxWKxWCwWi8VisVgsFovF4n/lkx/a1JemO02xb8xpU8cbjlRir+m9W5kz35yXD29Vkx5MzmsPxPir9h2q8rTZxSEH49nejS3qbMc+55UdW9TVxlMuH+OdCzaqPgOvuzjkYDzbtnydmtD+kLnjXrNa0v6O+e6VVWpQlqnYnxqWqcWvBjBPfLJQTds0uGYNzoaPnaP6Hx3JfP6zUjPWjGNumDldnTFTmO+OnKjmnpvBfHP/aNUybJYbF5y9PjhUvWmcz1yd2qia9yx2+eDscWtf1bR5BXP7s6/5+EerXT44GzP2ef7s9FoXB2cvX9zKX7xe7zx7xKX88oFNLqdOPBv1/nC+4cRW5vsXWvOWwduZe72dlx/6uNN50bEheb/Ru9zz68Szq+9vV5Ze2838dvz8yt6Lbcxx3XvbnCrkB9tnVv0z7bgFjBvidm4FzC3kYNyusYD1Bts9KWB/gu0eFn4P0XafC7/PaPuOCv+O0PadFv6dom0NGKiHYFszxtcM2taYgXoLtjVpfE2ibQ0bqOdgW/MG6j/YnhED5yXYnikD5yvYnkHjzyDanlkD5zfYnnED5z3Y9gQD/SHY9hAD/STY9hzjew7a9iXj+xLa9jHj+5jtewb6Xpdx2yeN75No21eN76u2Dxvow13GbQ830M9jd9YKH+x/W41Nz69Zg/3citi0lpo12K+XmfbK5YP93ro42L8LFwf7d+fiYF8DBt57zRr8Sw7VUmxNtWegPg3UpMvBONV2bE1nwcB5MXBGXA7G6azF1nQ2XZzOrzPENcbp7DtTf4jjGuPUW2Jr6kWxfe9ycbDvdS4O9r3RxcG+fzJTv42tqVe7OFhn7k/7eMXn1IvTt8OPm8O4Xcbpe8RM3zK/JznsQ4jT95HlYJy+p8z0LWambzczfeuZ6W7ATHcJX58K6rDLON1VmOlu48+LgnMR4nRfYjkYp7sWM93NmOkux0x3vyI23RWZ6W7JTPdPZrqvMtNdl5nuw8x0f67Gprs3M93VO2P//HP3G/3jn7lMTpnflnHq81PHKrOuOF7vOanrSsnpKWd11vW7uemEeJl1lVljan7qb1Pj3Rm3jFPnVmaeqfllnLoucc/Ww9/aiP+bdR3/z7HqjZsa785YZX5bLz/1t91ZV+q4ZZw6tzLzTM0v49S5lZ2n7sZ89B9cJr+nnv8vnvPXY30HYUAx7Q==AQAAAACAAADQOwAAQQQAAA==eJztl92LVlUUhyeoKDEpRlOcZowuyog+iLCbmHdvRLCC6ioougkC88quxKCMmCgIooaIEIyEJPsgKujKcN79eJFESYWCVJQ3E0REReFFH2J7dmfVQ+AfULPvfry855y91vqd9fzOxMTlefejNxyYmHgoT/yjkc5rjm7IE5vOzC7pnTdtyB8u7h4t6blNM/maDxaa/urYZfmpfaebfvCiqfz+99NpSW9eXJff2X9L05/cc2l+YfHept/YMZk37tnV9NtXXZwPn3i66VNzK/P8ij1Nf/TkBfnXL19t+tCN5+brNr/X9Lo1Z9JrN9P0fVecSle/e7Tpvc9/l8qBz5t+dsfJ9OnkN03fcehYmvzhx6ZvfeJIeuX635re+vHB9Pu35+Ql/cBLb6Wd287Pf/VhX9r23Iqmj/wxn668f1XT+/fOpa0nLmn64c+2pxd/Wt30F8dvT1Nvrm368buvTWvPW9/08e2r0srTU01fuOXr0cH56aZ/3vjyaObwTNPTd45Gu57Z0PRdtz02u+WXv/VC6PqfcfynXjuOa+s9x3HP+qwSz6pnKHGGerYSZ6tnLnHmWkuJWmqNJWqstZeovfakRE9qr0r0qvawRA9rb0v0tva8RM/rLErMos6oxIzq7ErMrs6UmGmdNTHr6gHCA9UbhDeqZwjPVC8RXqoeIzxWvUd4r3qS8GT1KuHV6mHCw9XbhLer51n9yPrX9fuC/j/Wfca6/1jPLTpP0TmLzl9UV1G9RX0o6k9R34r6WdTnov4XzaVoXkVzRPNFc0d+QD5B/kG+Qn5DPkT+RL5FfkY+Dz0bengv4tpRXDu8R/GsFM8a3rs4W4qzDe9p1JKiluG9jtpT1D7sAbQf0N6I3qbo7bBnYhYpZjHspZhditkNeyxmnWPWw94Lb+TwxrAnw0s5vDTs1aJ9W7SHw6s5vDrs7bH2+cK/dv5Z979/FwsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQCxALEAsQC+j5v+f/nv97/u/5v+f/nv97/u/5v+f/nv+Xff4/Gwv6d0H/LujfBf27oH8XLKPvgp7/e/7v+b/n/57/l03+7zm/5/ye83vO7zm/5/ye83vO7zm/5/ye83vO7zm/5/ye83vO7zn/v5Xze7bv2b5n+57te7b/H2b7PwGAl55UAQAAAACAAAAQAAAADgAAAA==eJxjYIAARigNAAAYAAI=AQAAAACAAAAQAAAADgAAAA==eJxjZIAAJigNAAAwAAQ=AQAAAACAAABwLwAAJQUAAA==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AQAAAACAAACgDwAAJwMAAA==eJwtxVOAEAYAANDuumzbtm3btm3btm3btm271Wq1Wq1Wq9VqtY977+eFDBEstMM5oqM4umM5rhM4sZM5pdM4vTM5q3M4t/O5oIu4uEu5rCu4squ5puu4vhu5qVu4tdu5o7u4u3u5rwd4sId5pMd4vCd5qmd4tud5oZd4uVd5rTd4s7d5p/d4vw/5qE/4tM/5oq/4um/5rh/4sZ/6uV/6td/6vT/6s7/6u386MCD4UA7rCI7saI7pOI7vRE7qFE7tdM7oLM7uXM7rAi7sYi7pMi7vSq7qGq7tem7oJm7uVm7rDu7sbu7pPu7vQR7qER7tcZ7oKZ7uWZ7rBV7sZV7pNV7vTd7qHd7tfT7oIz7uUz7rC77sa77pO77vR37iZ37hV37jd/7gT/7ib/7hgMDggxzG4R3JUR3DsR3PCZ3EyZ3KaZ3BmZ3NOZ3H+V3IRV3CpV3OFV3F1V3Ldd3Ajd3MLd3G7d3JXd3Dvd3PAz3Ewz3KYz3Bkz3NMz3H873IS73Cq73OG73F273Le33Ah33MJ33G533JV33Dt33PD/2Lf/Vv/t1/+E//5b/9j//1fw4RUg7tcI7oKI7uWI7rBE7sZE7pNE7vTM7qHM7tfC7oIi7uUi7rCq7saq7pOq7vRm7qFm7tdu7oLu7uXu7rAR7sYR7pMR7vSZ7qGZ7teV7oJV7uVV7rDd7sbd7pPd7vQz7qEz7tc77oK77uW77rB37sp37ul37tt37vj/7sr/7unw4MCj6UwzqCIzuaYzqO4zuRkzqFUzudMzqLszuX87qAC7uYS7qMy7uSq7qGa7ueG7qJm7uV27qDO7ube7qP+3uQh3qER3ucJ3qKp3uW53qBF3uZV3qN13uTt3qHd3ufD/qIj/uUz/qCL/uab/qO7/uRn/iZX/iV3/idP/iTv/ibfzggVPBBDuPwjuSojuHYjueETuLkTuW0zuDMzuaczuP8LuSiLuHSLueKruLqruW6buDGbuaWbuP27uSu7uHe7ueBHuLhHuWxnuDJnuaZnuP5XuSlXuHVXueN3uLt3uW9PuDDPuaTPuPzvuSrvuHbvueH/h9R1fmO
  </AppendedData>
</VTKFile>    
"

    var data = {data};
    render(data, parent_element, 0.5);
});

</script>
<body>
Hi
</body>

</div>
"""

actual_html = HTML(RAW_HTML)


display(actual_html, metadata=dict(isolated=True))


# %%
