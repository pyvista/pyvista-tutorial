"""
Lesson Overview
~~~~~~~~~~~~~~~

This exercise provides an overview of the content in the initial lesson for you to try out!

"""
# sphinx_gallery_thumbnail_number = 2

from pyvista import set_plot_theme

set_plot_theme("document")

###############################################################################
# Points and Arrays Within PyVista
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
# Learn about the data model of the PyVista framework and how you can visualize
# your data in style using point, cell, and field data.
# There are a variety of ways to create points within PyVista, and this section
# shows how to efficiently create an array of points by either:
#
# - Wrapping a VTK array
# - Using a [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
# - Or just using a [list](https://docs.python.org/dev/library/stdtypes.html#list)
#
# PyVista provides pythonic methods for all three approaches so you can choose
# whatever is most efficient for you. If you’re comfortable with the VTK API,
# you can choose to wrap VTK arrays, but you may find that using [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
# is more convenient and avoids the looping overhead in Python.

###############################################################################
# Wrapping a VTK Array
# ^^^^^^^^^^^^^^^^^^^^
# Let’s define points of a triangle. Using the VTK API, this can be done with:

import vtk

vtk_array = vtk.vtkDoubleArray()
vtk_array.SetNumberOfComponents(3)
vtk_array.SetNumberOfValues(9)
vtk_array.SetValue(0, 0)
vtk_array.SetValue(1, 0)
vtk_array.SetValue(2, 0)
vtk_array.SetValue(3, 1)
vtk_array.SetValue(4, 0)
vtk_array.SetValue(5, 0)
vtk_array.SetValue(6, 0.5)
vtk_array.SetValue(7, 0.667)
vtk_array.SetValue(8, 0)
print(vtk_array)

###############################################################################
# PyVista supports creating objects directly from the vtkDataArray class, but
# there’s a better, and more pythonic alternative by using numpy.ndarray.
#
# Using NumPy with PyVista
# ^^^^^^^^^^^^^^^^^^^^^^^^
#
# You can create a [NumPy](https://numpy.org/) points array with:

import numpy as np

np_points = np.array([[0, 0, 0], [1, 0, 0], [0.5, 0.667, 0]])
np_points

###############################################################################
# We use a [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
# here so that PyVista directly “points” the underlying C array to VTK.
# VTK already has APIs to directly read in the C arrays from NumPy, and since
# VTK is written in C++, everything from Python that is transferred over to VTK
# needs to be in a format that VTK can process.

# Should you wish to use VTK objects within PyVista, you can still do this.
# In fact, using [pyvista.wrap()](https://docs.pyvista.org/api/utilities/_autosummary/pyvista.wrap.html#pyvista.wrap),
# you can even get a numpy-like representation of the data. For example:

import pyvista

wrapped = pyvista.wrap(vtk_array)
wrapped

###############################################################################
# Note that when wrapping the underlying VTK array, we actually perform a
# shallow copy of the data. In other words, we pass the pointer from the
# underlying C array to the [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray),
# meaning that the two arrays are now efficiently linked (in NumPy terminology, the returned array is a view into the underlying VTK data).
# This means that we can change the array using numpy array indexing and have
# it modified on the “VTK side”.

wrapped[0, 0] = 10
vtk_array.GetValue(0)

###############################################################################
# Or we can change the value from the VTK array and see it reflected in the
# numpy wrapped array. Let’s change the value back:

vtk_array.SetValue(0, 0)
wrapped[0, 0]

###############################################################################
# Using Python Lists or Tuples
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PyVista supports the use of Python sequences
# (i.e. [list](https://docs.python.org/dev/library/stdtypes.html#list) or
# [tuple](https://docs.python.org/dev/library/stdtypes.html#list)),
# and you could define your points using a nested list of lists via:

points = [[0, 0, 0], [1, 0, 0], [0.5, 0.667, 0]]

###############################################################################
# When used in the context of [PolyData](https://docs.pyvista.org/api/core/_autosummary/pyvista.PolyData.html#pyvista.PolyData)
# to create the mesh, this list will automatically be wrapped using NumPy and
# then passed to VTK. This avoids any looping overhead and while still allowing
# you to use native python classes.
#
# Finally, let’s show how we can use these three objects in the context of a
# PyVista geometry class. Here, we create a simple point mesh containing just
# the three points:

from_vtk = pyvista.PolyData(vtk_array)
from_np = pyvista.PolyData(np_points)
from_list = pyvista.PolyData(points)

###############################################################################
# These point meshes all contain three points and are effectively identical.
# Let’s show this by accessing the underlying points array from the mesh, which
# is represented as a ``pyvista.pyvista_ndarray``

from_vtk.points

###############################################################################
# And show that these are all identical

assert np.array_equal(from_vtk.points, from_np.points)
assert np.array_equal(from_vtk.points, from_list.points)
assert np.array_equal(from_np.points, from_list.points)

###############################################################################
# Finally, let’s plot this (very) simple example using PyVista’s [pyvista.plot()](https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html#pyvista.plot)
# method. Let’s make this a full example so you can see the entire process.

import pyvista

points = [[0, 0, 0], [1, 0, 0], [0.5, 0.667, 0]]
mesh = pyvista.PolyData(points)
mesh.plot(show_bounds=True, cpos="xy", point_size=20)

###############################################################################
# We’ll get into PyVista’s data classes and attributes later, but for now we’ve
# shown how to create a simple geometry containing just points. To create a
# surface, we must specify the connectivity of the geometry, and to do that we
# need to specify the cells (or faces) of this surface.
#
# Geometry and Mesh Connectivity/Topology Within PyVista
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# With our previous example, we defined our “mesh” as three disconnected points.
# While this is useful for representing “point clouds”, if we want to create a
# surface, we have to describe the connectivity of the mesh. To do this, let’s
# define a single cell composed of three points in the same order as we defined
# earlier.

cells = [3, 0, 1, 2]

###############################################################################
# Observe how we had to insert a leading ``3`` to tell VTK that our face will
# contain three points. In our [PolyData](https://docs.pyvista.org/api/core/_autosummary/pyvista.PolyData.html#pyvista.PolyData)
# VTK doesn’t assume that faces always contain three points, so we have to
# define that. This actually gives us the flexibility to define as many (or as
# few as one) points per cell as we wish.
#
# Now we have all the necessary pieces to assemble an instance of
# [PolyData](https://docs.pyvista.org/api/core/_autosummary/pyvista.PolyData.html#pyvista.PolyData)
# that contains a single triangle. To do this, we simply provide the ``points``
# and ``cells`` to the constructor of a [PolyData](https://docs.pyvista.org/api/core/_autosummary/pyvista.PolyData.html#pyvista.PolyData).
# We can see from the representation that this geometry contains three points
# and one cell


mesh = pyvista.PolyData(points, cells)
mesh

###############################################################################
# Let’s also plot this:

mesh = pyvista.PolyData(points, [3, 0, 1, 2])
mesh.plot(cpos="xy", show_edges=True)

###############################################################################
# While we’re at it, let’s annotate this plot to describe this mesh.

pl = pyvista.Plotter()
pl.add_mesh(mesh, show_edges=True, line_width=5)
label_coords = mesh.points + [0, 0, 0.01]
pl.add_point_labels(label_coords, [f"Point {i}" for i in range(3)], font_size=20, point_size=20)
pl.add_point_labels([0.43, 0.2, 0], ["Cell 0"], font_size=20)
pl.camera_position = "xy"
pl.show()

###############################################################################
# You can clearly see how the polygon is created based on the connectivity of
# the points.
#
# This instance has several attributes to access the underlying data of the
# mesh. For example, if you wish to access or modify the points of the mesh,
# you can simply access the points attribute with [points](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.points.html#pyvista.DataSet.points).

mesh.points

###############################################################################
# The connectivity can also be accessed from the [faces](https://docs.pyvista.org/api/core/_autosummary/pyvista.PolyData.faces.html#pyvista.PolyData.faces)
# attribute with:

mesh.faces

###############################################################################
# Or we could simply get the representation of the mesh with:

mesh

###############################################################################
# In this representation we see:
#
# - Number of cells [n_cells](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.n_cells.html#pyvista.DataSet.n_cells)
# - Number of points [n_points](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.n_points.html#pyvista.DataSet.n_points)
# - Bounds of the mesh [bounds](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.bounds.html#pyvista.DataSet.bounds)
# - Number of data arrays [n_arrays](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.n_arrays.html#pyvista.DataSet.n_arrays)
#
# This is vastly different from the output from VTK. See [Object Representation](https://docs.pyvista.org/user-guide/vtk_to_pyvista.html#vtk-vs-pyvista-object-repr) for the comparison between the two representations.
#
# This mesh contains no data arrays as it consists only of geometry. This makes it useful for plotting just the geometry of the mesh, but datasets often contain more than just geometry. For example:
#
# - An electrical field computed from a changing magnetic field
# - Vector field of blood flow through artery
# - Surface stresses from a structural finite element analysis
# - Mineral deposits from geophysics
# - Weather patterns as a vector field or surface data.
#
# While each one of these datasets could be represented as a different geometry
# class, they would all contain point, cell, or field data that explains the value
# of the data at a certain location within the geometry.

###############################################################################
# Data Arrays
# ~~~~~~~~~~~
# Each [DataSet](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.html#pyvista.DataSet) contains attributes that allow you to access the underlying numeric data. This numerical data may be associated with the [points](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.points.html#pyvista.DataSet.points),
# cells, or not associated with points or cells and attached to the mesh in general.
#
# To illustrate data arrays within PyVista, let’s first construct a slightly
# more complex mesh than our previous example. Here, we create a simple mesh
# containing four isometric cells by starting with a [UniformGrid](https://docs.pyvista.org/api/core/_autosummary/pyvista.UniformGrid.html#pyvista.UniformGrid) and then casting it to an [UnstructuredGrid](https://docs.pyvista.org/api/core/_autosummary/pyvista.UnstructuredGrid.html#pyvista.UnstructuredGrid) with [cast_to_unstructured_grid()](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.cast_to_unstructured_grid.html#pyvista.DataSet.cast_to_unstructured_grid).

grid = pyvista.UniformGrid(dims=(3, 3, 1))
ugrid = grid.cast_to_unstructured_grid()
ugrid

###############################################################################
# Let’s also plot this basic mesh:

pl = pyvista.Plotter()
pl.add_mesh(ugrid, show_edges=True, line_width=5)
label_coords = ugrid.points + [0, 0, 0.02]
point_labels = [f"Point {i}" for i in range(ugrid.n_points)]
pl.add_point_labels(label_coords, point_labels, font_size=25, point_size=20)
cell_labels = [f"Cell {i}" for i in range(ugrid.n_cells)]
pl.add_point_labels(ugrid.cell_centers(), cell_labels, font_size=25)
pl.camera_position = "xy"
pl.show()

###############################################################################
# Now that we have a simple mesh to work with, we can start assigning it data.
# There are two main types of data that can be associated with a mesh: scalar
# data and vector data. Scalar data is single or multi-component data that is
# non directional and may include values like temperature, or in the case o
# multi-component data, RGBA values. Vector data has magnitude and direction
# and is represented as arrays containing three components per data point.
#
# When plotting, we can easily display scalar data, but this data must be
# “associated” with either points or cells. For example, we may wish to assign
# values to the cells of our example mesh, which we can do by accessing the
# cell_data attribute of our mesh.

###############################################################################
# Cell Data
# ~~~~~~~~~
#
# The easiest way to add scalar data to a [DataSet](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.html#pyvista.DataSet)
# is to use the ``[]`` operator. Continuing with our example above, let’s assign
# each cell a single integer. We can do this using a Python [list](https://docs.python.org/dev/library/stdtypes.html#list)
# and making it the same length as the number of cells in the [UnstructuredGrid](https://docs.pyvista.org/api/core/_autosummary/pyvista.UnstructuredGrid.html#pyvista.UnstructuredGrid).
# Or as an even simpler example, using a [range](https://docs.python.org/dev/library/stdtypes.html#range)
# of the appropriate length. Here we create the range, add it to the [cell_data](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.cell_data.html#pyvista.DataSet.cell_data),
# and then access it using the ``[]`` operator.

simple_range = range(ugrid.n_cells)
ugrid.cell_data["my-data"] = simple_range
ugrid.cell_data["my-data"]

###############################################################################
# Note how we are returned a ``pyvista.pyvista_ndarray``. Since VTK requires
# C arrays, PyVista will internally wrap or convert all inputs to C arrays.
# We can then plot this with:

ugrid.plot(cpos="xy", show_edges=True)

###############################################################################
# Note how we did not have to specify which cell data to plot as the `[]`
# operator automatically sets the active scalars:

ugrid.cell_data

###############################################################################
# We can also add labels to our plot to show which cells are assigned which
# scalars. Note how this is in the same order as the scalars we assigned.

pl = pyvista.Plotter()
pl.add_mesh(ugrid, show_edges=True, line_width=5)
cell_labels = [f"Cell {i}" for i in range(ugrid.n_cells)]
pl.add_point_labels(ugrid.cell_centers(), cell_labels, font_size=25)
pl.camera_position = "xy"
pl.show()

###############################################################################
# We can continue to assign cell data to our [DataSet](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.html#pyvista.DataSet)
# using the `[]` operator, but if you do not wish the new array to become the
# active array, you can add it using [set_array()](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSetAttributes.set_array.html#pyvista.DataSetAttributes.set_array)

data = np.linspace(0, 1, ugrid.n_cells)
ugrid.cell_data.set_array(data, "my-cell-data")
ugrid.cell_data

###############################################################################
# Now, `ugrid` contains two arrays, one of which is the “active” scalars. This
# set of active scalars will be the one plotted automatically when `scalars` is
# unset in either [add_mesh()](https://docs.pyvista.org/api/plotting/_autosummary/pyvista.Plotter.add_mesh.html#pyvista.Plotter.add_mesh)
# or [pyvista.plot()](https://docs.pyvista.org/api/plotting/_autosummary/pyvista.plot.html#pyvista.plot).
# This makes it possible to have many cell arrays associated with a dataset and
# track which one will plotted as the active cell scalars by default.
# The active scalars can also be accessed via `active_scalars`, and the name of
# the active scalars array can be accessed or set with `active_scalars_name`.

ugrid.cell_data.active_scalars_name = "my-cell-data"
ugrid.cell_data

###############################################################################
# Point Data
# ~~~~~~~~~~
#
# Data can be associated to points in the same manner as in [Cell Data](https://docs.pyvista.org/user-guide/data_model.html#pyvista-data-model-cell-data).
# The [point_data](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.point_data.html#pyvista.DataSet.point_data)
# attribute allows you to associate point data to the points of a [DataSet](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.html#pyvista.DataSet).
# Here, we will associate a simple list to the points using the `[]` operator.

simple_list = list(range(ugrid.n_points))
ugrid.point_data["my-data"] = simple_list
ugrid.point_data["my-data"]

###############################################################################
# Again, these values become the active scalars in our point arrays by default
# by using the `[]` operator:

ugrid.point_data

###############################################################################
# Let’s plot the point data. Note how this varies from the cell data plot; each
# individual point is assigned a scalar value which is interpolated across a
# cell to create a smooth color map between the lowest value at `Point 0` to
# the highest value at `Point 8`.

pl = pyvista.Plotter()
pl.add_mesh(ugrid, show_edges=True, line_width=5)
label_coords = ugrid.points + [0, 0, 0.02]
point_labels = [f"Point {i}" for i in range(ugrid.n_points)]
pl.add_point_labels(label_coords, point_labels, font_size=25, point_size=20)
pl.camera_position = "xy"
pl.show()

###############################################################################
# As in [Cell Data](https://docs.pyvista.org/user-guide/data_model.html#pyvista-data-model-cell-data),
# we can assign multiple arrays to [point_data](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.point_data.html#pyvista.DataSet.point_data)
# using [set_array()](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSetAttributes.set_array.html#pyvista.DataSetAttributes.set_array).

data = np.linspace(0, 1, ugrid.n_points)
ugrid.point_data.set_array(data, "my-point-data")
ugrid.point_data

###############################################################################
# Again, here there are now two arrays associated to the point data, and only
# one is the “active” scalars array. Like as in the cell data, we can retrieve
# this with [active_scalars](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_scalars.html#pyvista.DataSet.active_scalars),
# and the name of the active scalars array can be accessed or set with [active_scalars_name](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_scalars_name.html#pyvista.DataSet.active_scalars_name).

ugrid.point_data.active_scalars_name = "my-point-data"
ugrid.point_data

###############################################################################
# Dataset Active Scalars
# ~~~~~~~~~~~~~~~~~~~~~~
#
# Continuing from the previous sections, our `ugrid` dataset now contains both point and cell data:

ugrid.point_data

###############################################################################

ugrid.cell_data

###############################################################################
# There are active scalars in both point and cell data, but only one type of
# scalars can be “active” at the dataset level. The reason for this is that
# only one scalar type (be it point or cell) can be plotted at once, and this
# data can be obtained from [active_scalars_info](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_scalars_info.html#pyvista.DataSet.active_scalars_info):

ugrid.active_scalars_info

###############################################################################
# Note that the active scalars are by default the point scalars. You can change
# this by setting the active scalars with [set_active_scalars()](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.set_active_scalars.html#pyvista.DataSet.set_active_scalars).
# Note that if you want to set the active scalars and both the point and cell
# data have an array of the same name, you must specify the `preference`:

ugrid.set_active_scalars("my-data", preference="cell")
ugrid.active_scalars_info

###############################################################################
# This can also be set when plotting using the preference parameter in
# add_mesh() or pyvista.plot().
#
# Field Data
# ~~~~~~~~~~
#
# Field arrays are different from [point_data](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.point_data.html#pyvista.DataSet.point_data) and [cell_data](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.cell_data.html#pyvista.DataSet.cell_data) in that they are not associated with the geometry of the [DataSet](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.html#pyvista.DataSet). This means that while it’s not possible to designate the field data as active scalars or vectors, you can use it to “attach” arrays of any shape. You can even add string arrays in the field data:

ugrid.field_data["my-field-data"] = ["hello", "world"]
ugrid.field_data["my-field-data"]


###############################################################################
# Note that the field data is automatically transferred to VTK C-style arrays
# and then represented as a numpy data format.
#
# When listing the current field data, note that the association is “NONE”:

ugrid.field_data

###############################################################################
# This is because the data is not associated with points or cells, and cannot
# be made so because field data is not expected to match the number of cells or
# points. As such, it also cannot be plotted.
#
# Vectors, Texture Coords, and Normals Attributes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Both cell and point data can also store the following “special” attributes in
# addition to [active_scalars](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_scalars.html#pyvista.DataSet.active_scalars):
#
# - [active_normals](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_normals.html#pyvista.DataSet.active_normals)
# - [active_t_coords](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_t_coords.html#pyvista.DataSet.active_t_coords)
# - [active_vectors](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_vectors.html#pyvista.DataSet.active_vectors)
#
# Active Normals
# ~~~~~~~~~~~~~~
#
# The [active_normals](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_normals.html#pyvista.DataSet.active_normals)
# array is a special array that specifies the local normal direction of meshes.
# It is used for creating physically based rendering, rendering smooth shading
# using Phong interpolation, warping by scalars, etc. If this array is not set
# when plotting with `smooth_shading=True` or `pbr=True`, it will be computed.
#
# Active Texture Coordinates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# The [active_t_coords](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_t_coords.html#pyvista.DataSet.active_t_coords)
# array is used for rendering textures. See [Applying Textures](https://docs.pyvista.org/examples/02-plot/texture.html#ref-texture-example)
# for examples using this array.
#
# Active Vectors
# ~~~~~~~~~~~~~~
#
# The [active_vectors](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_vectors.html#pyvista.DataSet.active_vectors)
# is an array containing quantities that have magnitude and direction (specifically, three components).
# For example, a vector field containing the wind speed at various coordinates.
# This differs from [active_scalars](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.active_scalars.html#pyvista.DataSet.active_scalars)
# as scalars are expected to be non-directional even if they contain several
# components (as in the case of RGB data).
#
# Vectors are treated differently within VTK than scalars when performing
# transformations using the [transform()](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.transform.html#pyvista.DataSet.transform)
# filter. Unlike scalar arrays, vector arrays will be transformed along with
# the geometry as these vectors represent quantities with direction.
#
# VTK permits only one “active” vector. If you have multiple vector arrays that
# you wish to transform, set `transform_all_input_vectors=True` in [transform()](https://docs.pyvista.org/api/core/_autosummary/pyvista.DataSet.transform.html#pyvista.DataSet.transform).
# Be aware that this will transform any array with three components, so
# multi-component scalar arrays like RGB arrays will have to be discarded after
# transformation.
