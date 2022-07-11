import pyvista as pv

p = pv.Plotter(shape=(1, 2))

p.subplot(0, 0)
p.add_mesh(pv.Sphere())

p.subplot(0, 1)
p.add_mesh(pv.Cube())

p.show()