import pyvista as pv
import numpy as np
points = np.random.random((1000, 3))
pc = pv.PolyData(points)
pc.plot(scalars=points[:, 2], point_size=5.0, cmap='jet')