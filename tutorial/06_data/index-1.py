import pyvista
points = [[0, 0, 0],
          [1, 0, 0],
          [0.5, 0.667, 0]]
mesh = pyvista.PolyData(points)
mesh.plot(show_bounds=True, cpos='xy', point_size=20)
