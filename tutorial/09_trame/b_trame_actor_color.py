"""
Control the Color of an Actor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html
    <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/09_trame/b_trame_actor_color.ipynb">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
    </a>

Extending our simple example to have a dropdown menu to control the color of
the actor.

"""
import pyvista as pv
from pyvista.plotting.colors import hexcolors
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vuetify

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

mesh = pv.Cone()

pl = pv.Plotter()
actor = pl.add_mesh(mesh, color='seagreen')


@state.change("color")
def color(color="seagreen", **kwargs):
    actor.prop.color = color
    ctrl.view_update()


with SinglePageLayout(server) as layout:
    with layout.toolbar:
        vuetify.VSpacer()
        vuetify.VSelect(
            label="Color",
            v_model=("color", "seagreen"),
            items=("array_list", list(hexcolors.keys())),
            hide_details=True,
            dense=True,
            outlined=True,
            classes="pt-1 ml-2",
            style="max-width: 250px",
        )

    with layout.content:
        with vuetify.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ):
            # Use PyVista UI template for Plotters
            view = plotter_ui(pl, default_server_rendering=False)
            ctrl.view_update = view.update

server.start()
