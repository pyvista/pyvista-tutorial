"""
Control Scalar Array
~~~~~~~~~~~~~~~~~~~~

Extending our simple example to have a dropdown menu to control which
scalar array is used to color the mesh.
"""

import pyvista as pv
from pyvista import examples
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

mesh = examples.download_antarctica_velocity()

pl = pv.Plotter()
actor = pl.add_mesh(mesh)
pl.view_xy()


@state.change("scalars")
def set_scalars(scalars=mesh.active_scalars_name, **kwargs) -> None:
    actor.mapper.array_name = scalars
    actor.mapper.scalar_range = mesh.get_data_range(scalars)
    ctrl.view_update()


@state.change("log_scale")
def set_log_scale(log_scale=False, **kwargs) -> None:  # noqa: FBT002
    actor.mapper.lookup_table.log_scale = log_scale
    ctrl.view_update()


with SinglePageLayout(server) as layout:
    with layout.toolbar:
        vuetify3.VSpacer()
        vuetify3.VCheckbox(
            label="Log Scale",
            v_model=("log_scale", False),
            hide_details=True,
            density="compact",
            outlined=True,
        )
        vuetify3.VSelect(
            label="Scalars",
            v_model=("scalars", mesh.active_scalars_name),
            items=("array_list", list(mesh.point_data.keys())),
            hide_details=True,
            density="compact",
            outlined=True,
            classes="pt-1 ml-2",
            style="max-width: 250px",
        )

    with (
        layout.content,
        vuetify3.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ),
    ):
        # Use PyVista UI template for Plotters
        view = plotter_ui(pl)
        ctrl.view_update = view.update

# Show UI
await layout.ready
layout
###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/09_trame/c_trame_scalars.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
