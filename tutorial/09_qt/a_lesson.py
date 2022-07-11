"""
PyVista and Qt
~~~~~~~~~~~~~~~

Demonstrate how to use PyVista to create standalone applications using pyinstaller and the Qt framework.

Overview
~~~~~~~~
"""
# sphinx_gallery_thumbnail_number = 2
import os

###############################################################################
#
# The python package `pyvistaqt` extends the functionality of `pyvista` through
# the usage of Qt. Since Qt applications operates in a separate thread than VTK,
# you can simultaneously have an active VTK plot and a non-blocking Python
# session.
#
# ![qt_multiplot](https://qtdocs.pyvista.org/_images/qt_multiplot.png)
#
###############################################################################
# Getting Started
# ~~~~~~~~~~~~~~~

os.system('pip install pyqt5')

###############################################################################
# Installation using `pip` is:

os.system('pip install pyvistaqt')


###############################################################################
# To install this package with conda run:
#
# ```bash
# $ conda install -c conda-forge pyvistaqt
# ```
#
# You can also visit [PyPI](https://pypi.org/project/pyvistaqt/) or [GitHub](https://github.com/pyvista/pyvistaqt)
# to download the source.

###############################################################################
# Once installed, use the `pyvistaqt.BackgroundPlotter` like any PyVista plotter.

import pyvistaqt

help('pyvistaqt.BackgroundPlotter')


###############################################################################
# Brief Example
# ~~~~~~~~~~~~~
#
# Create an instance of the `pyvistaqt.BackgroundPlotter` and plot a sphere.

help('pyvistaqt.BackgroundPlotter')

###############################################################################

import pyvista as pv
from pyvistaqt import BackgroundPlotter

sphere = pv.Sphere()

plotter = BackgroundPlotter()
plotter.add_mesh(sphere)

###############################################################################
# Usage
# ~~~~~
# PyVista has an interface for placing plots in `pyvistaqt` that extends the
# functionality of the `QVTKRenderWindowInteractor` class. The `pyvistaqt.QtInteractor`
# class allows you to have the same functionality of the `Plotter` class within
# a Qt application. This simplifies adding meshes, updating, and controlling
# them when using Qt.
#
# Please do keep in mind that the `BackgroundPlotter` **does not** create its
# own event loop by default. By design, the plotter will look for an active
# instance of `QApplication` instead. So in the end, it is up to the user to
# manage this event loop and there are several ways to achieve this. For
# example, it's possible to start Python interactively with `python -i`, use
# `ipython` or execute the Qt event loop by adding `plotter.app.exec_()` to the
# end of the following code.

###############################################################################
# Background Plotting
# ~~~~~~~~~~~~~~~~~~~
#
# Normal PyVista plotting windows exhibit blocking behavior, but it is possible
# to plot in the background and update the plotter in real-time using the
# `BackgroundPlotter` object. This requires `pyvistaqt`, but otherwise appears
# and functions like a normal PyVista `Plotter` instance. For example:

import pyvista as pv
from pyvistaqt import BackgroundPlotter

sphere = pv.Sphere()

plotter = BackgroundPlotter()
plotter.add_mesh(sphere)

###############################################################################
# can now operate on the sphere and have it updated in the background
sphere.points *= 0.5


###############################################################################
# # Multiple Plotters

# The following example shows how to use an interface with multiple plotters.
# Each plotter can be selected and functions like a normal PyVista `Plotter`
# instance:

import pyvista as pv
from pyvistaqt import MultiPlotter

mp = MultiPlotter(nrows=2, ncols=2)
mp[0, 0].add_mesh(pv.Sphere())
mp[0, 1].add_mesh(pv.Cylinder())
mp[1, 0].add_mesh(pv.Cube())
mp[1, 1].add_mesh(pv.Cone())


###############################################################################
# # Example PyQt5 PyVista QtInteractor

# The following example shows how to create a simple application that adds a
# sphere to an empty plotting window.

# %% load './examples_qt/main.py'


###############################################################################
# Using Different Qt bindings
# 
#
# To use different Qt bindings you must first install them. For example, to use
# `PySide2`, you install it via:

os.system('pip install PySide2')


###############################################################################
# Then you set the `QT_API` value to the specific binding you would like to use:

os.environ["QT_API"] = "pyside2"
