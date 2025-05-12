import numpy as np
import pyvista as pv

points = np.random.rand(100, 3)
mesh = pv.PolyData(points)
mesh.plot(point_size=10, style='points', color='tan')