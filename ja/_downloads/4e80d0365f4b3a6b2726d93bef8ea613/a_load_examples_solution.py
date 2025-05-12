"""
.. _load_examples_solution:

Download and Plot Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   This is the solution to :ref:`load_examples`. If you haven't already tried to
   solve it on your own, you probably should try that first.

Download and plot example datasets.

PyVista contains many downloadable datasets documented at
`pyvista.examples.downloads
<https://docs.pyvista.org/api/examples/_autosummary/pyvista.examples.downloads.html>`_. You can download these through Python and then immediately plot them.

This is an easy way to immediately get started with example datasets within
PyVista without having to manually download and load them.

"""

###############################################################################
# Import PyVista and the examples module
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pyvista as pv
from pyvista import examples

###############################################################################
# Surface DataSet - Download
# ~~~~~~~~~~~~~~~~~~~~~~~~~~
# Download a surface dataset of pine roots. Note how the dataset is
# automatically loaded right into Python.
dataset = examples.download_pine_roots()
dataset


###############################################################################
# Surface DataSet - Plot
# ~~~~~~~~~~~~~~~~~~~~~~
# Plot the pine roots using PyVista's default plotting settings.
dataset.plot()


###############################################################################
# Volume DataSet - Download
# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Download the bolt dataset. This is an excellent dataset to visualize using
# "volumetric" plotting.

dataset = examples.download_bolt_nut()
dataset


###############################################################################
# Volume DataSet - Plot
# ~~~~~~~~~~~~~~~~~~~~~
# Here, we plot the dataset using a custom view direction using
# :class:`pyvista.Plotter`.

pl = pv.Plotter()
_ = pl.add_volume(
    dataset,
    cmap="coolwarm",
    opacity="sigmoid_5",
    show_scalar_bar=False,
)
pl.camera_position = [(194.6, -141.8, 182.0), (34.5, 61.0, 32.5), (-0.229, 0.45, 0.86)]
pl.show()


###############################################################################
# Exercise #1 - Use PyVista Examples
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Visualize one of PyVista's built in examples.
#
# If your IDE supports it, you should be able to type
# ``dataset = examples.download_`` and press tab to see all the available
# examples you can download.

dataset = examples.download_gears()
bodies = dataset.split_bodies()
bodies.plot(
    cmap="jet",
    multi_colors=True,
    smooth_shading=True,
    split_sharp_edges=True,
)


###############################################################################
# Exercise #2 - Download and View a File
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Experiment on your own by downloading a dataset and reading it in with
# :class:`pyvista.read`. You can use one of your own files or try downloading
# one from the following sources:
#
# - `Sample VTK DataSets <https://github.com/pyvista/vtk-data/tree/master/Data>`_
# - `Sample STL files <https://www.amtekcompany.com/teaching-resources/stl-files/>`_
# - `Thingiverse <https://www.thingiverse.com/>`_
#
# **Solution**
# Download the file ``'P_shelf_pin.stl'`` from
# https://www.thingiverse.com/thing:5412753

mesh = pv.read("P_shelf_pin.stl")
mesh.plot()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/01_basic/solutions/a_load_examples_solution.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
