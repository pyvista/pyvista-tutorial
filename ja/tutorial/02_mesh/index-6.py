mesh.point_data['my point values'] = np.arange(mesh.n_points, dtype=float)
mesh.plot(scalars='my point values', cpos=cpos, show_edges=True)