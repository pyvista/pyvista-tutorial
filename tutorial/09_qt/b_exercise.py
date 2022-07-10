
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

import pyvista as pv
from pyvista import examples
from pyvistaqt import BackgroundPlotter

globe = examples.load_globe()

plotter = BackgroundPlotter()
plotter.add_mesh(globe)

