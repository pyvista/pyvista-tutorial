pl = pyvista.Plotter()
pl.add_mesh(mesh, show_edges=True, line_width=5)
label_coords = mesh.points + [0, 0, 0.01]
pl.add_point_labels(label_coords, [f'Point {i}' for i in range(3)],
                    font_size=20, point_size=20)
pl.add_point_labels([0.43, 0.2, 0], ['Cell 0'], font_size=20)
pl.camera_position = 'xy'
pl.show()
