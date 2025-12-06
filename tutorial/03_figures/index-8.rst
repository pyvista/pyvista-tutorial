import pyvista as pv

mesh = pv.Wavelet()
cntr = mesh.contour()
slices = mesh.slice_orthogonal()

pl = pv.Plotter(shape=(1, 2))

pl.add_mesh(cntr)

pl.subplot(0, 1)
pl.add_mesh(slices)

pl.link_views()
pl.view_isometric()
pl.show()