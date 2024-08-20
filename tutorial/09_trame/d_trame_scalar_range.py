"""
Control Scalar Range
~~~~~~~~~~~~~~~~~~~~

Extending our simple example to control the color limits of the mapped scalars.
"""

import pyvista as pv
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

mesh = pv.Wavelet()

pl = pv.Plotter()
actor = pl.add_mesh(mesh)


@state.change("scalar_range")
def set_scalar_range(scalar_range=mesh.get_data_range(), **kwargs) -> None:  # noqa: B008
    actor.mapper.scalar_range = scalar_range
    ctrl.view_update()


with SinglePageLayout(server) as layout:
    with layout.toolbar:
        vuetify3.VSpacer()
        vuetify3.VRangeSlider(
            thumb_size=16,
            thumb_label=True,
            label="Range",
            v_model=("scalar_range", [0, 300]),
            min=("0",),
            max=("500",),
            density="compact",
            hide_details=True,
            style="max-width: 400px",
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
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/09_trame/d_trame_scalar_range.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
