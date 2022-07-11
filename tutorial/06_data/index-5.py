pl = pyvista.Plotter()
pl.add_mesh(ugrid, show_edges=True, line_width=5)
label_coords = ugrid.points + [0, 0, 0.02]
point_labels = [f'Point {i}' for i in range(ugrid.n_points)]
pl.add_point_labels(label_coords, point_labels,
                    font_size=25, point_size=20)
cell_labels = [f'Cell {i}' for i in range(ugrid.n_cells)]
pl.add_point_labels(ugrid.cell_centers(), cell_labels, font_size=25)
pl.camera_position = 'xy'
pl.show()
