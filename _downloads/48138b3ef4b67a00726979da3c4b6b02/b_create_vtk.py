"""
Create VTK Objects
~~~~~~~~~~~~~~~~~~

This exercise walks through the creation of a few different types of VTK datasets.
"""

import numpy as np
import pyvista as pv
import vtk

try:
    from vtkmodules.util.numpy_support import numpy_to_vtk
except:  # noqa: E722
    from vtk.util.numpy_support import numpy_to_vtk

###############################################################################
# Create ``vtkImageData``
# ^^^^^^^^^^^^^^^^^^^^^^^
image = vtk.vtkImageData()
image.SetDimensions(10, 10, 2)
image.SetSpacing(1, 2, 5)
image.SetOrigin(-0.5, -3, 0)

###############################################################################
# Add point data
values = np.arange(np.prod(image.GetDimensions()))
# Convert numpy array to VTK array
arr = numpy_to_vtk(values)
arr.SetName("values")  # CRITICAL
image.GetPointData().SetScalars(arr)
image

###############################################################################
# Plot with PyVista for simplicity
pv.plot(image, show_edges=True)

###############################################################################
# Create ``vtkStructuredGrid``
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Define structured points with NumPy
x = np.arange(-10, 10, 0.25)
y = np.arange(-10, 10, 0.25)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

# Join the points
values = np.c_[x.ravel(), y.ravel(), z.ravel()]

coords = numpy_to_vtk(values)

points = vtk.vtkPoints()
points.SetData(coords)

grid = vtk.vtkStructuredGrid()
grid.SetDimensions(*z.shape, 1)
grid.SetPoints(points)
grid

###############################################################################
# Add point data
arr = numpy_to_vtk(z.ravel())
arr.SetName("z")  # CRITICAL
grid.GetPointData().SetScalars(arr)


###############################################################################
# Plot with PyVista for simplicity
pv.plot(grid, show_edges=True)

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/06_vtk/b_create_vtk.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
