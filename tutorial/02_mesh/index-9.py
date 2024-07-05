cube = pv.Cube()
cube.cell_data['myscalars'] = range(6)

other_cube = cube.copy()
other_cube.point_data['myscalars'] = range(8)

pl = pv.Plotter(shape=(1, 2), border_width=1)
pl.add_mesh(cube, cmap='coolwarm')
pl.subplot(0, 1)
pl.add_mesh(other_cube, cmap='coolwarm')
pl.show()