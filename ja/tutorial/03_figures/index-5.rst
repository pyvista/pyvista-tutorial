import pyvista as pv
from pyvista import examples

mesh = examples.download_st_helens().warp_by_scalar()

pl = pv.Plotter()
pl.add_mesh(mesh, cmap='terrain', opacity="linear")
pl.show()