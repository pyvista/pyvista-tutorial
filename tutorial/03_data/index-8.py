pl = pyvista.Plotter()
pl.add_mesh(ugrid, show_edges=True, line_width=5)
cell_labels = [f'Cell {i}' for i in range(ugrid.n_cells)]
pl.add_point_labels(ugrid.cell_centers(), cell_labels, font_size=25)
pl.camera_position = 'xy'
pl.show()
