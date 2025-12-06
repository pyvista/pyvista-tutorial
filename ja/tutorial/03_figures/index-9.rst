import pyvista as pv

mesh = pv.Wavelet()
cntr = mesh.contour()
slices = mesh.slice_orthogonal()
thresh = mesh.threshold(200)

pl = pv.Plotter(shape="1|3")

pl.subplot(1)
pl.add_mesh(cntr)

pl.subplot(2)
pl.add_mesh(slices)

pl.subplot(3)
pl.add_mesh(thresh)

pl.subplot(0)
pl.add_mesh(mesh)

pl.link_views()
pl.view_isometric()
pl.show()