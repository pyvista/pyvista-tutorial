"""
.. _create_point_cloud_exercise:

Create Point Cloud
~~~~~~~~~~~~~~~~~~

Create a :class:`pyvista.PolyData` object from a point cloud of vertices and
scalar arrays for those points.

"""

import numpy as np
import pyvista as pv
from pyvista import examples

###############################################################################
# Point clouds are generally constructed using :class:`pyvista.PolyData` and
# can easily have scalar or vector data arrays associated with the individual
# points. In this example, we'll start by working backwards using a point cloud
# that is available from our ``examples`` module. This however is no
# different than creating a PyVista mesh with your own NumPy arrays of vertice
# locations.


# Define some helpers - ignore these and use your own data if you like!
def generate_points(subset=0.02):
    """A helper to make a 3D NumPy array of points (n_points by 3)."""
    dataset = examples.download_lidar()
    ids = np.random.randint(low=0, high=dataset.n_points - 1, size=int(dataset.n_points * subset))
    return dataset.points[ids]


points = generate_points()
# Output the first 5 rows to prove it's a numpy array (n_points by 3)
# Columns are (X, Y, Z)
points[0:5, :]

###############################################################################
# Now that you have a NumPy array of points/vertices either from our sample
# data or your own project, create a PyVista mesh using those points.

# insert your code here
point_cloud = ...

###############################################################################
# Now, perform a sanity check to show that the points have been loaded
# correctly.

np.allclose(points, point_cloud.points)

###############################################################################
# Now that we have a PyVista mesh, we can plot it. Note that we add an option
# to use eye dome lighting - this is a shading technique to improve depth
# perception with point clouds (learn more about `EDL
# <https://docs.pyvista.org/examples/02-plot/edl.html>`_).
point_cloud.plot(eye_dome_lighting=True)

###############################################################################
# Now what if you have data attributes (scalar or vector arrays) that you'd
# like to associate with every point of your mesh? You can easily add NumPy
# data arrays that have a length equal to the number of points in the mesh
# along the first axis. For example, lets add a few arrays to this new
# ``point_cloud`` mesh.
#
# Make an array of scalar values with the same length as the points array.
# Each element in this array will correspond to points at the same index:
#
# .. note::
#    You can use a component of the ``points`` array or use the ``n_points``
#    property of the mesh to make an array of that length.

data = ...  # your code here

###############################################################################
# Add that data to the mesh with the name "elevation".

# your code here

###############################################################################
# And now we can plot the point cloud with that elevation data. PyVista is
# smart enough to plot the scalar array you added by default. This time, let's
# render every point as its own sphere using ``render_points_as_spheres``.
point_cloud.plot(render_points_as_spheres=True)

###############################################################################
# That data is kind of boring, right? You can also add data arrays with more
# than one scalar value - perhaps a vector with three elements? Let's make a
# little function that will compute vectors for every point in the point cloud
# and add those vectors to the mesh.
#
# This time, we're going to create a totally new, random point cloud containing
# 100 points using :func:`numpy.random.random`.

# Create a random point cloud with Cartesian coordinates
points = np.random.rand(100, 3)
# Construct PolyData from those points
point_cloud = pv.PolyData(points)


def compute_vectors(mesh):
    """Create normalized vectors pointing outward from the center of the cloud."""
    origin = mesh.center
    vectors = mesh.points - origin
    return vectors / np.linalg.norm(vectors, axis=1)[:, None]


vectors = compute_vectors(point_cloud)
vectors[0:5, :]


###############################################################################
# Add the vector array as point data to the new mesh:


###############################################################################
# Now we can make arrows using those vectors using the glyph filter (see the
# `Glyph Example <https://docs.pyvista.org/examples/01-filter/glyphs.html>`_
# for more details).

arrows = point_cloud.glyph(
    orient="vectors",
    scale=False,
    factor=0.15,
)

# Display the arrows
plotter = pv.Plotter()
plotter.add_mesh(point_cloud, color="maroon", point_size=10.0, render_points_as_spheres=True)
plotter.add_mesh(arrows, color="lightblue")
# plotter.add_point_labels([point_cloud.center,], ['Center',],
#                          point_color='yellow', point_size=20)
plotter.show_grid()
plotter.show()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/02_mesh/exercises/b_create-point-cloud.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
