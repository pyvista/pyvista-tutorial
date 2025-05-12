"""
.. _create_uniform_grid_solution:

Creating a Uniform Grid
~~~~~~~~~~~~~~~~~~~~~~~

Create a simple uniform grid from a 3D NumPy array of values.

"""

import numpy as np
import pyvista as pv

###############################################################################
# Take a 3D NumPy array of data values that holds some spatial data where each
# axis corresponds to the XYZ cartesian axes. This example will create a
# :class:`pyvista.ImageData` that will hold the spatial reference for
# a 3D grid by which a 3D NumPy array of values can be plotted against.

###############################################################################
# Create the 3D NumPy array of spatially referenced data.  This is spatially
# referenced such that the grid is ``(20, 5, 10)`` ``(nx, ny, nz)``.
values = np.linspace(0, 10, 1000).reshape((20, 5, 10))
values.shape

###############################################################################
# Create the ImageData
grid = pv.ImageData()

###############################################################################
# Set the grid dimensions to ``shape + 1`` because we want to inject our values
# on the CELL data.
grid.dimensions = np.array(values.shape) + 1

###############################################################################
# Edit the spatial reference
grid.origin = (100, 33, 55.6)  # The bottom left corner of the data set
grid.spacing = (1, 5, 2)  # These are the cell sizes along each axis

###############################################################################
# Assign the data to the cell data. Be sure to flatten the data for
# ``ImageData`` objects using Fortran ordering.
grid.cell_data["values"] = values.flatten(order="F")
grid

###############################################################################
# Now plot the grid!
grid.plot(show_edges=True)


###############################################################################
# Don't like cell data? You could also add the NumPy array to the point data of
# a :class:`pyvista.ImageData`. Take note of the subtle difference when
# setting the grid dimensions upon initialization.

# Create the 3D NumPy array of spatially referenced data again.
values = np.linspace(0, 10, 1000).reshape((20, 5, 10))
values.shape

###############################################################################
# Create the PyVista object and set the same attributes as earlier.
grid = pv.ImageData()

# Set the grid dimensions to ``shape`` because we want to inject our values on
# the POINT data
grid.dimensions = values.shape

# Edit the spatial reference
grid.origin = (100, 33, 55.6)  # The bottom left corner of the data set
grid.spacing = (1, 5, 2)  # These are the cell sizes along each axis

###############################################################################
# Add the data values to the cell data
grid.point_data["values"] = values.flatten(order="F")  # Flatten the array!
grid

###############################################################################
# Now plot the grid!
grid.plot(show_edges=True)


###############################################################################
# Exercise
# ^^^^^^^^
# Now create your own :class:`pyvista.ImageData` from a 3D NumPy array!
help(pv.ImageData)

###############################################################################
# Generate example 3D data using :func:`numpy.random.random`. Feel free to use
# your own 3D numpy array here.
arr = np.random.random((100, 100, 100))
arr.shape

###############################################################################
# Create the :class:`pyvista.ImageData`.
#
# .. note::
#    You will likely need to ``ravel`` the array with Fortran-ordering:
#    ``arr.ravel(order="F")``

vol = pv.ImageData()
vol.dimensions = arr.shape
vol["array"] = arr.ravel(order="F")

###############################################################################
# Plot the ImageData
vol.plot()


###############################################################################
# Example
# ^^^^^^^
# PyVista has several examples that use ``ImageData``.
#
# See the PyVista documentation for further details on
# `Volume Rendering <https://docs.pyvista.org/examples/02-plot/volume.html>`_
#
# Here's one of these example datasets:
from pyvista import examples

vol = examples.download_knee_full()

p = pv.Plotter()
p.add_volume(vol, cmap="bone", opacity="sigmoid")
p.show()

###############################################################################
vol = pv.Wavelet()
vol.plot(volume=True)

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/02_mesh/solutions/c_create-uniform-grid.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
