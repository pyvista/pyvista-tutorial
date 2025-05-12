import pyvista as pv
from pyvista import examples

mesh = pv.Wavelet()

p = pv.Plotter()
p.add_mesh(mesh)
p.show()