"""
.. _read_file_example:

Load and Plot from a File
~~~~~~~~~~~~~~~~~~~~~~~~~

Read a dataset from a known file type.

"""

###############################################################################
# We try to make loading a mesh as easy as possible - if your data is in one
# of the many supported file formats, simply use :func:`pyvista.read` to
# load your spatially referenced dataset into a PyVista mesh object.
#
# The following code block uses a built-in example file and displays an
# airplane mesh.

# sphinx_gallery_thumbnail_number = 5
import pyvista as pv
from pyvista import examples

###############################################################################
help(pv.read)

###############################################################################
# PyVista supports a wide variety of file formats. The supported file
# extensions are listed in an internal function:
help(pv.core.utilities.reader.get_reader)


###############################################################################
# The following code block uses a built-in example
# file, displays an airplane mesh and returns the camera's position:

# Get a sample file
filename = examples.planefile
filename

###############################################################################
# Note the above filename, it's a ``.ply`` file - one of the many supported
# formats in PyVista.
#
# Use ``pv.read`` to load the file as a mesh:

mesh = pv.read(filename)
cpos = mesh.plot()


###############################################################################
# The points from the mesh are directly accessible as a NumPy array:

mesh.points

###############################################################################
# The faces from the mesh are also directly accessible as a NumPy array:

mesh.faces.reshape(-1, 4)[:, 1:]  # triangular faces


###############################################################################
# Loading other files types is just as easy! Simply pass your file path to the
# :func:`pyvista.read` function and that's it!
#
# Here are a few other examples - simply replace ``examples.download_*`` in the
# examples below with ``pyvista.read('path/to/you/file.ext')``

###############################################################################
# Example STL file:
mesh = examples.download_cad_model()
cpos = [(107.0, 68.5, 204.0), (128.0, 86.5, 223.5), (0.45, 0.36, -0.8)]
mesh.plot(cpos=cpos)

###############################################################################
# Example OBJ file
mesh = examples.download_doorman()
mesh.plot(cpos="xy")


###############################################################################
# Example BYU file
mesh = examples.download_teapot()
mesh.plot(cpos=[-1, 2, -5], show_edges=True)


###############################################################################
# Example VTK file
mesh = examples.download_bunny_coarse()
cpos = [(0.2, 0.3, 0.9), (0, 0, 0), (0, 1, 0)]
mesh.plot(cpos=cpos, show_edges=True, color=True)


###############################################################################
# Exercise
# ^^^^^^^^
# Read a file yourself with :func:`pyvista.read`. If you have a supported file
# format, use that! Otherwise, download this file:
# https://github.com/pyvista/pyvista-tutorial/raw/main/tutorial/02_mesh/scipy.vtk

# (your code here)
# mesh = pv.read('path/to/file.vtk)

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/02_mesh/solutions/e_read-file.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
