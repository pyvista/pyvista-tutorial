"""
.. _glyph_example:

Plotting Glyphs (Vectors or PolyData)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use vectors in a dataset to plot and orient glyphs/geometric objects.
"""

import numpy as np
import pyvista as pv
from pyvista import examples

###############################################################################
# Example dataset with normals
mesh = examples.load_random_hills()

###############################################################################
# Glyphying can be done via the :func:`pyvista.DataSetFilters.glyph` filter
help(mesh.glyph)

###############################################################################
# Sometimes you might not want glyphs for every node in the input dataset. In
# this case, you can choose to build glyphs for a subset of the input dataset
# by using a merging tolerance. Here we specify a merging tolerance of five
# percent which equates to five percent of the bounding box's length.
#
# create a subset of arrows using the glyph filter
arrows = mesh.glyph(scale="Normals", orient="Normals", tolerance=0.05)


###############################################################################
p = pv.Plotter()
p.add_mesh(arrows, color="black")
p.add_mesh(mesh, scalars="Elevation", cmap="terrain", smooth_shading=True)
p.show()

###############################################################################
# A common approach is to load vectors directly to the mesh object and then
# access the :attr:`pyvista.DataSet.arrows` property to produce glyphs.

sphere = pv.Sphere(radius=3.14)

# make cool swirly pattern
vectors = np.vstack(
    (
        np.sin(sphere.points[:, 0]),
        np.cos(sphere.points[:, 1]),
        np.cos(sphere.points[:, 2]),
    )
).T
vectors


###############################################################################

# add and scale
sphere["vectors"] = vectors * 0.3
sphere.set_active_vectors("vectors")

# plot just the arrows
sphere.arrows.plot()

###############################################################################
# Plot the arrows and the sphere.
p = pv.Plotter()
p.add_mesh(sphere.arrows, lighting=False, scalar_bar_args={"title": "Vector Magnitude"})
p.add_mesh(sphere, color="grey", ambient=0.6, opacity=0.5, show_edges=False)
p.show()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/04_filters/solutions/e_glyphs.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
