import pyvista as pv
from pyvista import examples

mesh = pv.Wavelet()

pl = pv.Plotter()
pl.add_mesh(mesh)
pl.show()