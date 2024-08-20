"""
Display Options
~~~~~~~~~~~~~~~

Take a look at the different display options offered by the ``add_mesh`` method.
"""

import pyvista as pv
from pyvista import examples

mesh = examples.load_random_hills()

p = pv.Plotter()
p.add_mesh(mesh)
p.show()

###############################################################################
# Let's take a look at some different options for the ``add_mesh`` method to
# alter how the above data are displayed.
#
# See also https://docs.pyvista.org/api/plotting/_autosummary/pyvista.Plotter.add_mesh.html
help(p.add_mesh)

###############################################################################
# Plot that mesh with the edges of cells displayed
p = pv.Plotter()
p.add_mesh(mesh, show_edges=True)
p.show()

###############################################################################
# Plot that mesh with the colored edges and as a show the surface as a solid
# color (use a named color!)
p = pv.Plotter()
p.add_mesh(mesh, color="magenta", show_edges=True, edge_color="blue")
p.show()

###############################################################################
# Display with a points representation style
p = pv.Plotter()
p.add_mesh(mesh, style="points")
p.show()

###############################################################################
# And adjust the points display size
p = pv.Plotter()
p.add_mesh(mesh, style="points", point_size=10, render_points_as_spheres=True)
p.show()

###############################################################################
# Change the color map and the color limits
p = pv.Plotter()
p.add_mesh(mesh, cmap="terrain", clim=[2, 5])
p.show()

###############################################################################
# Add some opacity
p = pv.Plotter()
p.add_mesh(mesh, cmap="terrain", clim=[2, 5], opacity="linear")
p.show()

###############################################################################
# There you go! Those are a few of the most commonly used display options!

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/03_figures/solutions/a_display_options.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
