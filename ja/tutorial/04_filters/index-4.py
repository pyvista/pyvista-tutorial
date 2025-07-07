import pyvista as pv
from pyvista import examples

dataset = examples.load_uniform()
outline = dataset.outline()
threshed = dataset.threshold([100, 500])
contours = dataset.contour()
slices = dataset.slice_orthogonal()
glyphs = dataset.glyph(factor=1e-3, geom=pv.Sphere(), orient=False)

pl = pv.Plotter(shape=(2, 2))
# Show the threshold
pl.add_mesh(outline, color="k")
pl.add_mesh(threshed, show_scalar_bar=False)
pl.camera_position = [-2, 5, 3]
# Show the contour
pl.subplot(0, 1)
pl.add_mesh(outline, color="k")
pl.add_mesh(contours, show_scalar_bar=False)
pl.camera_position = [-2, 5, 3]
# Show the slices
pl.subplot(1, 0)
pl.add_mesh(outline, color="k")
pl.add_mesh(slices, show_scalar_bar=False)
pl.camera_position = [-2, 5, 3]
# Show the glyphs
pl.subplot(1, 1)
pl.add_mesh(outline, color="k")
pl.add_mesh(glyphs, show_scalar_bar=False)
pl.camera_position = [-2, 5, 3]

pl.link_views()
pl.show()