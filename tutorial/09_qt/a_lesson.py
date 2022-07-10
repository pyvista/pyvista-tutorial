"""
PyVista and Qt
~~~~~~~~~~~~~~~

Demonstrate how to use PyVista to create standalone applications using pyinstaller and the Qt framework.

"""
# sphinx_gallery_thumbnail_number = 2
import os

###############################################################################
# Overview
# ^^^^^^^^
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
# ^^^^^^^^^^^^^^^

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
# ^^^^^^^^^^^^^
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
# ^^^^^
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
# ^^^^^^^^^^^^^^^^^^^
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

###############################################################################
# # Freezing PyVista with pyinstaller
#
# You can make some fantastic standalone programs with `pyinstaller` and
# `pyvista`, and you can even make a graphical user interface incorporating
# `PyQt5` or `pyside2`. Depending on your version of VTK, this requires some
# extra steps to setup.
#
# When running VTK v9, you need to add several additional `hiddenimports`.
# For clarity and completeness, create a spec file (we’ll name it `pyvista.spec`)
# following the directions given at [Using Spec Files](https://pyinstaller.readthedocs.io/en/stable/spec-files.html).
# Modify the `Analysis` and add the following hidden imports:
#
# ```python
# main_py = os.path.join(some_path, 'main.py')
# a = Analysis([main_py],
#              pathex=[],
#              binaries=[],
#              hiddenimports=['vtkmodules',
#                             'vtkmodules.all',
#                             'vtkmodules.qt.QVTKRenderWindowInteractor',
#                             'vtkmodules.util',
#                             'vtkmodules.util.numpy_support',
#                             'vtkmodules.numpy_interface.dataset_adapter',
#                            ],
# ```
#
###############################################################################
# Flask Application
# ~~~~~~~~~~~~~~~~~
#
# You can use `pyvista` in to make a flask application to display static plots.
# See the following example as well as the demo at [Flask Example](https://github.com/pyvista/pyvista/tree/main/examples_flask).
#$
# For dynamic examples, it’s recommended to use [Jupyter Notebooks](https://jupyter.org/).
# See our documentation regarding this at [Jupyter Notebook Plotting](https://docs.pyvista.org/user-guide/jupyter/index.html#jupyter-plotting).
# 
# ![flask example](https://docs.pyvista.org/_images/flask_example.png)
#
###############################################################################
# Python Application app.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~

# %%load 'examples_flask/static_ex/app.py'

###############################################################################

os.system('cd examples_flask/static_ex && python app.py')


###############################################################################
# Ajax Template index.html
# ~~~~~~~~~~~~~~~~~~~~~~~~
#
# This template should be within the `templates` directory in the same path as
# `app.py`.
#
# This template returns the `meshtype` parameter back to the `get_img` method
# in the flask app, which is used to select the type of mesh to be plotted.

# %%load 'examples_flask/static_ex/templates/index.html

