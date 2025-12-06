import pyvista as pv
from pyvista import examples
uni = examples.load_uniform()

pl = pv.Plotter(shape=(1, 2), border=False)
pl.add_mesh(uni, scalars='Spatial Point Data', show_edges=True)
pl.subplot(0, 1)
pl.add_mesh(uni, scalars='Spatial Cell Data', show_edges=True)
pl.show()