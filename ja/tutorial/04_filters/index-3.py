pl = pv.Plotter()
pl.add_mesh(outline, color="k")
pl.add_mesh(threshed)
pl.camera_position = [-2, 5, 3]
pl.show()