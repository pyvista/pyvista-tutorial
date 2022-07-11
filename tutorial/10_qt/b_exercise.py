"""
Exercise
~~~~~~~~

This exercise overviews the code in the initial lesson for you to try out!

"""
# sphinx_gallery_thumbnail_number = 2
import pyvista as pv
from pyvista import examples
from pyvistaqt import BackgroundPlotter

###############################################################################
# Please refer to the [*QtPy* documentation](https://github.com/spyder-ide/qtpy)
# page for more information.
#
# Exercise
# ~~~~~~~~
#
# Let's plot globe using `BackgroundPlotter` object.

# Your code here

###############################################################################

globe = examples.load_globe()

plotter = BackgroundPlotter()
plotter.add_mesh(globe)

