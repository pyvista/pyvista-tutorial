"""
Display Options
~~~~~~~~~~~~~~~

Take a look at the different display options offered by the ``add_mesh`` method.
"""

import pyvista as pv
from pyvista import examples

mesh = examples.load_random_hills()

pl = pv.Plotter()
pl.add_mesh(mesh)
pl.show()

# %%
# Let's take a look at some different options for the ``add_mesh`` method to
# alter how the above data are displayed.
help(pl.add_mesh)

# %%
# Plot that mesh with the edges of cells displayed
pl = pv.Plotter()
pl.add_mesh(mesh, ...)
pl.show()

# %%
# Plot that mesh with the colored edges and as a show the surface as a solid
# color (use a named color!)
pl = pv.Plotter()
pl.add_mesh(mesh, ...)
pl.show()

# %%
# Display with a points representation style
pl = pv.Plotter()
pl.add_mesh(mesh, ...)
pl.show()

# %%
# And adjust the points display size
pl = pv.Plotter()
pl.add_mesh(mesh, ...)
pl.show()

# %%
# Change the color map and the color limits
pl = pv.Plotter()
pl.add_mesh(mesh, ...)
pl.show()

# %%
# Add some opacity
pl = pv.Plotter()
pl.add_mesh(mesh, ...)
pl.show()

# %%
# There you go! Those are a few of the most commonly used display options!

# %%
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/03_figures/exercises/a_display_options.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
