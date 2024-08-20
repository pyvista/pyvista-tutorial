"""
Simple Trame App
~~~~~~~~~~~~~~~~

A simple example of how to create a Trame app with a PyVista Plotter.

This example contains the boilerplate code to use anytime you are creating a
new Trame application with PyVista.

"""

import pyvista as pv
from pyvista import examples
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

mesh = examples.load_random_hills()

pl = pv.Plotter()
pl.add_mesh(mesh)

with SinglePageLayout(server) as layout, layout.content:
    view = plotter_ui(pl)

# Show UI
await layout.ready
layout
###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/09_trame/a_trame_simple.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
