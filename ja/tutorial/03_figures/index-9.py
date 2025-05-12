import pyvista as pv

mesh = pv.Wavelet()
cntr = mesh.contour()
slices = mesh.slice_orthogonal()
thresh = mesh.threshold(200)

p = pv.Plotter(shape="1|3")

p.subplot(1)
p.add_mesh(cntr)

p.subplot(2)
p.add_mesh(slices)

p.subplot(3)
p.add_mesh(thresh)

p.subplot(0)
p.add_mesh(mesh)

p.link_views()
p.view_isometric()
p.show()