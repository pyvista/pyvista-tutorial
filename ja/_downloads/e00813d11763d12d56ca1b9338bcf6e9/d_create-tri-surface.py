"""
.. _triangulated_surface:

Create Triangulated Surface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a surface from a set of points through a Delaunay triangulation.

.. note::
    We will use a filter from PyVista to perform our triangulation: `delaunay_2d <https://docs.pyvista.org/api/core/_autosummary/pyvista.PolyData.delaunay_2d.html>`_.
"""

import numpy as np
import pyvista as pv

###############################################################################
# Simple Triangulations
# +++++++++++++++++++++
#
# First, create some points for the surface.

# Define a simple Gaussian surface
n = 20
x = np.linspace(-200, 200, num=n) + np.random.uniform(-5, 5, size=n)
y = np.linspace(-200, 200, num=n) + np.random.uniform(-5, 5, size=n)
xx, yy = np.meshgrid(x, y)
A, b = 100, 100
zz = A * np.exp(-0.5 * ((xx / b) ** 2.0 + (yy / b) ** 2.0))

# Get the points as a 2D NumPy array (N by 3)
points = np.c_[xx.reshape(-1), yy.reshape(-1), zz.reshape(-1)]
points[0:5, :]

###############################################################################
# Now use those points to create a point cloud PyVista data object. This will
# be encompassed in a :class:`pyvista.PolyData` object.

# simply pass the numpy points to the PolyData constructor
cloud = pv.PolyData(points)
cloud.plot(point_size=15)

###############################################################################
# Now that we have a PyVista data structure of the points, we can perform a
# triangulation to turn those boring discrete points into a connected surface.
# See :func:`pyvista.UnstructuredGridFilters.delaunay_2d`.
help(cloud.delaunay_2d)

###############################################################################
# Apply the ``delaunay_2d`` filter.

surf = cloud.delaunay_2d()

# And plot it with edges shown
surf.plot(show_edges=True)


###############################################################################
# Clean Edges & Triangulations
# ++++++++++++++++++++++++++++

# Create the points to triangulate
x = np.arange(10, dtype=float)
xx, yy, zz = np.meshgrid(x, x, [0])
points = np.column_stack((xx.ravel(order="F"), yy.ravel(order="F"), zz.ravel(order="F")))
# Perturb the points
points[:, 0] += np.random.rand(len(points)) * 0.3
points[:, 1] += np.random.rand(len(points)) * 0.3

# Create the point cloud mesh to triangulate from the coordinates
cloud = pv.PolyData(points)
cloud

###############################################################################
cloud.plot(cpos="xy")

###############################################################################
# Run the triangulation on these points
surf = cloud.delaunay_2d()
surf.plot(cpos="xy", show_edges=True)

###############################################################################
# Note that some of the outer edges are unconstrained and the triangulation
# added unwanted triangles. We can mitigate that with the ``alpha`` parameter.
surf = cloud.delaunay_2d(alpha=1.0)
surf.plot(cpos="xy", show_edges=True)

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/02_mesh/solutions/d_create-tri-surface.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
