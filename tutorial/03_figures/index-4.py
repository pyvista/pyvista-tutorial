import pyvista as pv

mesh = pv.Wavelet()
cntr = mesh.contour()
slices = mesh.slice_orthogonal()

p = pv.Plotter(shape=(1, 2))

p.add_mesh(cntr)

p.subplot(0, 1)
p.add_mesh(slices)

p.link_views()
p.view_isometric()
p.show()