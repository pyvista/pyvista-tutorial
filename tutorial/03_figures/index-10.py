import pyvista as pv
from pyvista import examples

mesh = examples.load_random_hills()

p = pv.Plotter()
p.add_mesh(mesh)
p.show_axes()
p.show()