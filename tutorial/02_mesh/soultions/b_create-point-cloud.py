"""
.. _create_point_cloud:

Create Point Cloud
~~~~~~~~~~~~~~~~~~

Create a :class:`pyvista.PolyData` object from a point cloud of vertices and
scalar arrays for those points.

"""

import numpy as np
import pyvista as pv
from pyvista import examples

###############################################################################
# Point clouds are generally constructed in the :class:`pyvista.PolyData` class
# and can easily have scalar/vector data arrays associated with the point
# cloud. In this example, we'll work a bit backwards using a point cloud that
# that is available from our ``examples`` module. This however is no different
# than creating a PyVista mesh with your own NumPy arrays of vertice locations.


# Define some helpers - ignore these and use your own data if you like!
def generate_points(subset=0.02):
    """A helper to make a 3D NumPy array of points (n_points by 3)"""
    dataset = examples.download_lidar()
    ids = np.random.randint(low=0, high=dataset.n_points - 1, size=int(dataset.n_points * subset))
    return dataset.points[ids]


points = generate_points()
# Print first 5 rows to prove its a numpy array (n_points by 3)
# Columns are (X Y Z)
points[0:5, :]

###############################################################################
# Now that you have a NumPy array of points/vertices either from our sample
# data or your own project, creating a PyVista mesh of those points:

# insert your code here
point_cloud = pv.PolyData(points)
point_cloud

###############################################################################
# Now, perform a sanity check

np.allclose(points, point_cloud.points)

###############################################################################
# And now that we have a PyVista mesh, we can plot it. Note that we add an
# option to use eye dome lighting - this is a shading technique to improve
# depth perception with point clouds (learn more about `EDL <https://docs.pyvista.org/examples/02-plot/edl.html>`_).
point_cloud.plot(eye_dome_lighting=True)

###############################################################################
# Now what if you have data attributes (scalar/vector arrays) that you'd like
# to associate with every node of your mesh? You can easily add NumPy data
# arrays that have a length equal to the number of points in the mesh along the
# first axis. For example, lets add a few arrays to this new ``point_cloud``
# mesh.
#
# Make an array of scalar values with the same length as the points array.
# Each element in this array will correspond to points at the same index:
#
# Hint, you can use a component of the ``points`` array or use the ``n_points``
# property of the mesh object to make an array of that length.

# Make data array using z-component of points array
data = points[:, -1]

###############################################################################
# Add that data to the mesh with the name "elevation"

point_cloud["elevation"] = data

###############################################################################
# And now we can plot the point cloud with that elevation data. PyVista is smart
# enough to plot the scalar array you added by default. Note that this time,
# we specify to render every point as its own sphere.
point_cloud.plot(render_points_as_spheres=True)

###############################################################################
# That data is kind of boring, right? You can also add data arrays with
# more than one scalar value - perhaps a vector with three elements? Let's
# make a little function that will compute vectors for every node in the point
# cloud and add those vectors to the mesh.
#
# This time, we're going to create a totally new, random point cloud.

# Create random XYZ points
points = np.random.rand(100, 3)
# Make PolyData
point_cloud = pv.PolyData(points)


def compute_vectors(mesh):
    origin = mesh.center
    vectors = mesh.points - origin
    vectors = vectors / np.linalg.norm(vectors, axis=1)[:, None]
    return vectors


vectors = compute_vectors(point_cloud)
vectors[0:5, :]

###############################################################################
# Add the vector array as point data to the new mesh:

point_cloud['vectors'] = vectors

###############################################################################
# Now we can make arrows using those vectors using the glyph filter
# (see `this example <https://docs.pyvista.org/examples/01-filter/glyphs.html>`_ for more details).

arrows = point_cloud.glyph(
    orient='vectors',
    scale=False,
    factor=0.15,
)

# Display the arrows
plotter = pv.Plotter()
plotter.add_mesh(point_cloud, color='maroon', point_size=10.0, render_points_as_spheres=True)
plotter.add_mesh(arrows, color='lightblue')
# plotter.add_point_labels([point_cloud.center,], ['Center',],
#                          point_color='yellow', point_size=20)
plotter.show_grid()
plotter.show()
