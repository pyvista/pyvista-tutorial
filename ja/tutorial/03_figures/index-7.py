import pyvista as pv

pl = pv.Plotter(shape=(1, 2))

pl.subplot(0, 0)
pl.add_mesh(pv.Sphere())

pl.subplot(0, 1)
pl.add_mesh(pv.Cube())

pl.show()