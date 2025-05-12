# Getting started with PyVista and Trame
"""
Getting started
~~~~~~~~~~~~~~~

Getting started with PyVista and Trame

"""

import pyvista as pv
from pyvista import examples

###############################################################################
# PyVista's Jupyter backend is powered by **Trame**. So by default you are
# using trame without knowing it.
#
# By default PyVista is serving you a micro trame application that let you
# toggle between **Remote** and **Local** rendering along with some various
# options to configure your visualization.
#
# **First try the Remote/Local rendering toggle and notice the differences**
#
# .. raw:: html
#
#    <div class="alert alert-block alert-info">
#    Look at the orientation axis between the 2 rendering modes.
#    </div>
#
# One sends images generated on the server side while the other is sending geometry to vtk.js.
dataset = examples.download_lucy()
dataset.plot(smooth_shading=True, color="white")

###############################################################################
# Building applications with PyVista and Trame
#
# Now, let's build a simple application that updates the mesh color with the click of a button.

import random

from pyvista.plotting.colors import hexcolors
from pyvista.trame.ui import get_viewer
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3 as v3

plotter = pv.Plotter()
actor = plotter.add_mesh(dataset)
viewer = get_viewer(plotter)
view = None


def change_color() -> None:
    actor.prop.color = random.choice(list(hexcolors.keys()))  # noqa: S311
    view.update()


# Create UI
with SinglePageLayout(viewer.server) as layout:
    with layout.toolbar.clear() as tb:
        tb.density = "compact"
        tb.theme = "dark"
        viewer.ui_controls(mode="trame")
        v3.VBtn(icon="mdi-palette", click=change_color)
    with layout.content:
        view = viewer.ui(add_menu=False, mode="trame")


# Show UI
await layout.ready
layout
