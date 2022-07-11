import pyvista as pv
from pyvista import examples

mesh = examples.download_st_helens().warp_by_scalar()

p = pv.Plotter()
p.add_mesh(mesh, cmap='terrain', opacity="linear")
p.show()