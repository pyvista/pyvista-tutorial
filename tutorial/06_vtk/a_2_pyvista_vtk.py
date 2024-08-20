"""
PyVista and VTK Together
~~~~~~~~~~~~~~~~~~~~~~~~

PyVista is best known for is easy to use plotting API -- being familiar to most Python users already experienced with libraries like Matplotlib. Many people benefit from combining the power of VTK's Python bindings for their data pipelines and the flexibility and simplicity of PyVista for 3D rendering. The following section demonstrates this usage scenario.

.. tip::

    In case it was not made clear in the :ref:`mesh` section, PyVista mesh classes are subclasses of their VTK counterparts - which means PyVista can be intermixed with VTK workflows.

Nothing stops you from using VTK classes and then wrapping
the output with PyVista for streamlined plotting. For example:

.. _vtkDataArray: https://vtk.org/doc/nightly/html/classvtkDataArray.html
.. _vtkPolyData: https://vtk.org/doc/nightly/html/classvtkPolyData.html
.. _vtkImageData: https://vtk.org/doc/nightly/html/classvtkImageData.html
.. _vtkpoints: https://vtk.org/doc/nightly/html/classvtkPoints.html

"""

import pyvista as pv
import vtk
from pyvista import examples

###############################################################################
# Create a circle using vtk
polygonSource = vtk.vtkRegularPolygonSource()  # noqa: N816
polygonSource.GeneratePolygonOff()
polygonSource.SetNumberOfSides(50)
polygonSource.SetRadius(5.0)
polygonSource.SetCenter(0.0, 0.0, 0.0)
polygonSource.Update()

###############################################################################
# wrap and plot using pyvista
mesh = pv.wrap(polygonSource.GetOutput())
mesh.plot(line_width=3, cpos="xy", color="k")

###############################################################################
# In this manner, you can get the "best of both worlds" should you need
# the flexibility of PyVista and the raw power of VTK.
#
# .. note::
#    You can use :func:`pyvista.Polygon` for a one line replacement of
#    the above VTK code.

###############################################################################
# VTK Algorithms
# ~~~~~~~~~~~~~~
#
# Perhaps there is a VTK algorithm that is not (yet) exposed in PyVista that you'd like to use. This is easy enough to work with since PyVista objects are VTK objects. We can pass our PyVista meshes to the VTK algorithm, then wrap the output for plotting, further filtering, or anything.

mesh = examples.download_bunny_coarse()

###############################################################################
# Initialize VTK algorithm
splatter = vtk.vtkGaussianSplatter()

###############################################################################
# Pass PyVista object as input to VTK
splatter.SetInputData(mesh)

###############################################################################
# Set parameters
n = 200
splatter.SetSampleDimensions(n, n, n)
splatter.SetRadius(0.02)
splatter.SetExponentFactor(-10)
splatter.SetEccentricity(2)
splatter.Update()

###############################################################################
# Retrieve output and wrap with PyVista
vol = pv.wrap(splatter.GetOutput())

###############################################################################
# Use PyVista to produce contours
cntrs = vol.contour([0.95 * splatter.GetRadius()])

###############################################################################
# Use PyVista to plot
p = pv.Plotter()
p.add_mesh(mesh, style="wireframe")
p.add_mesh(cntrs, color=True)
p.show()

###############################################################################
# .. note::
#
#     The above example was adapted from VTK's `Embed Points Into Volume <https://kitware.github.io/vtk-examples/site/Cxx/PolyData/EmbedPointsIntoVolume/>`_

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/06_vtk/a_2_pyvista_vtk.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
