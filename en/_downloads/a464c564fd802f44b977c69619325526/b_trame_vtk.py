"""
Using VTK/PyVista and Trame
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this application, we will connect a VTK filter with PyVista.

It will use Trame to visualize the results and interactively control
parameters of the VTK filter.

"""

import pyvista as pv
from pyvista import examples
from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import vtk as vtk_widgets
from trame.widgets import vuetify3 as v3
from vtkmodules.vtkFiltersGeneral import vtkWarpScalar

mesh = examples.load_random_hills()
warp_by_scalar = vtkWarpScalar()
warp_by_scalar.SetInputData(mesh)
warp_by_scalar.SetScaleFactor(0.3)

plotter = pv.Plotter()
actor = plotter.add_mesh(warp_by_scalar)
plotter.reset_camera()

# Trame server setup
server = get_server("trame_vtk_example")
state, ctrl = server.state, server.controller


@state.change("scale")
def update_scale(scale, **kwargs) -> None:
    warp_by_scalar.SetScaleFactor(scale)
    ctrl.view_update()


with VAppLayout(server, full_height=True) as layout:  # noqa: SIM117
    with v3.VContainer(fluid=True, classes="fill-height"):
        with vtk_widgets.VtkRemoteView(plotter.render_window, interactive_ratio=1) as view:
            ctrl.view_update = view.update
            ctrl.view_reset_camera = view.reset_camera

        # Event binding
        v3.VBtn(
            icon="mdi-crop-free",
            click=ctrl.view_reset_camera,
            classes="position-absolute",
            style="left: 1rem; top: 1rem; z-index: 1",
            density="compact",
        )

        # State binding
        v3.VSlider(
            v_model=("scale", 0.3),
            min=0,
            max=0.5,
            step=0.01,
            density="compact",
            classes="position-absolute",
            style="right: 1rem; top: 1rem; width: 400px; z-index: 1",
        )

# Make sure the app is running and ready
await layout.ready
# Show UI in result
layout
