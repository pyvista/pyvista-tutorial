import pyvista as pv
from pyvista import examples

dataset = examples.load_uniform()
outline = dataset.outline()
threshed = dataset.threshold([100, 500])
contours = dataset.contour()
slices = dataset.slice_orthogonal()
glyphs = dataset.glyph(factor=1e-3, geom=pv.Sphere(), orient=False)

p = pv.Plotter(shape=(2, 2))
# Show the threshold
p.add_mesh(outline, color="k")
p.add_mesh(threshed, show_scalar_bar=False)
p.camera_position = [-2, 5, 3]
# Show the contour
p.subplot(0, 1)
p.add_mesh(outline, color="k")
p.add_mesh(contours, show_scalar_bar=False)
p.camera_position = [-2, 5, 3]
# Show the slices
p.subplot(1, 0)
p.add_mesh(outline, color="k")
p.add_mesh(slices, show_scalar_bar=False)
p.camera_position = [-2, 5, 3]
# Show the glyphs
p.subplot(1, 1)
p.add_mesh(outline, color="k")
p.add_mesh(glyphs, show_scalar_bar=False)
p.camera_position = [-2, 5, 3]

p.link_views()
p.show()