"""
Using VTK, PyVista, and Trame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to use VTK, PyVista, and Trame together
to show how the three libraries complement each other.
"""

import pyvista as pv
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vuetify
from vtkmodules.vtkFiltersSources import vtkConeSource

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

source = vtkConeSource()

pl = pv.Plotter()
pl.add_mesh(source, color='seagreen')


@state.change("resolution")
def update_contour(resolution, **kwargs):
    source.SetResolution(int(resolution))
    ctrl.view_update()


with SinglePageLayout(server) as layout:
    with layout.toolbar:
        vuetify.VSpacer()
        vuetify.VSlider(
            v_model=("resolution", 15),
            min=5,
            max=30,
            hide_details=True,
            dense=True,
            style="max-width: 300px",
            change=ctrl.view_update,
        )
        vuetify.VProgressLinear(
            indeterminate=True,
            absolute=True,
            bottom=True,
            active=("trame__busy",),
        )

    with layout.content:
        with vuetify.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ):
            # Use PyVista UI template for Plotters
            view = plotter_ui(pl)
            ctrl.view_update = view.update

server.start()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/09_trame/e_trame_algorithm.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
