"""
.. _load_examples:

Download and Plot Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and plot example datasets.

PyVista contains many downloadable datasets documented at
`pyvista.examples.downloads
<https://docs.pyvista.org/api/examples/_autosummary/pyvista.examples.downloads.html>`_. you can download these through Python and then immediately plot them.

This is an easy way to immediately get started with example datasets within
PyVista without having to manually copy and load them.

"""

###############################################################################
# Import PyVista and the examples module
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pyvista
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
# Here, we plot the dataset using a custom view direction.
pl = pyvista.Plotter()
_ = pl.add_volume(
        dataset, cmap="coolwarm", opacity="sigmoid_5", show_scalar_bar=False,
)
pl.camera_position = [
    (194.6, -141.8, 182.0),
    (34.5, 61.0, 32.5),
    (-0.229, 0.45, 0.86)
]
pl.show()
