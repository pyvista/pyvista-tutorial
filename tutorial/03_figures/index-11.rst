import pyvista as pv
from pyvista import examples

mesh = examples.load_random_hills()

pl = pv.Plotter()
pl.add_mesh(mesh)
pl.show_axes()
pl.show_bounds()
pl.show()