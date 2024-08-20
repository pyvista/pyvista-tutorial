"""
Using VTK Algorithms
~~~~~~~~~~~~~~~~~~~~

In this exercise, you will use a VTK Algorithm directly to filter a PyVista mesh.

VTK algorithms (filters) follow a standard flow for most cases:

1. Instantiate the algorithm
2. Set the input data object or connection: ``.SetInputDataObject(mesh)``
3. Adjust algorithm parameters with the setter methods, e.g., ``SetParameterName(value)``
4. Call ``.Update()`` to run the algorithm
5. Retrieve the output of the algorithm: ``output = alg.GetOutput()``

Let's see if we can try a few VTK algorithms with that standard workflow.
"""

import pyvista as pv
import vtk
from pyvista import examples

###############################################################################
# Here is a sample mesh
mesh = examples.load_random_hills()
mesh

###############################################################################
mesh.plot()

###############################################################################
# Simple Filter
# ^^^^^^^^^^^^^
# Let's start out with a simple VTK filter: ``vtkOutlineFilter``
help(vtk.vtkOutlineFilter)

###############################################################################
# Try using this VTK filter yourself here:
#
# Remember that you will have to wrap the output of the algorithm with :func:`pyvista.wrap`
alg = vtk.vtkOutlineFilter()

# (your code here, answer below)

outline = pv.wrap(alg.GetOutput())
outline

###############################################################################
alg.SetInputDataObject(mesh)
alg.SetGenerateFaces(False)  # noqa: FBT003
alg.Update()

outline = pv.wrap(alg.GetOutput())
outline

###############################################################################
# .. note::
#
#   Note that the about filter can be replaced with a ``.outline()`` filter in PyVista

###############################################################################
p = pv.Plotter()
p.add_mesh(mesh)
p.add_mesh(outline, color="k")
p.show()


###############################################################################
# Find your own filter
# ^^^^^^^^^^^^^^^^^^^^
#
# Take a look at VTK's examples and documentation to find a filter you'd like
# to apply to your mesh. The instructors will be around to help you implement.
#
# See https://kitware.github.io/vtk-examples/site/Python/

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/06_vtk/c_vtk_algorithms.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
