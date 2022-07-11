"""
Exercise
~~~~~~~~

"""
# sphinx_gallery_thumbnail_number = 3

from pyvista import set_plot_theme

set_plot_theme("document")

###############################################################################
# Let's create a box pyvista.PolyData (surface mesh) from vertices and faces.
# Please set each side length 1.0.

# insert your code here (answer below)

###############################################################################
import numpy as np
import pyvista as pv

# mesh points
vertices = np.array(
    [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
    ]
)

# mesh faces
faces = np.hstack(
    [
        [4, 0, 1, 2, 3],  # square
        [4, 4, 5, 6, 7],  # square
        [4, 0, 1, 5, 4],  # square
        [4, 1, 2, 6, 5],  # square
        [4, 2, 3, 7, 6],  # square
        [4, 3, 0, 4, 7],  # square
    ]
)

surf = pv.PolyData(vertices, faces)

# plot each face with a different color
surf.plot(
    cpos=[-1, 1, 0.5],
    show_edges=True,
    line_width=5,
)


###############################################################################
# We can add data to the box you created. Please add the point number of each
# point as point data. Also, add a face number to each face as cell data.

# insert your code here (answer below)

###############################################################################

import numpy as np

surf["point_number"] = range(8)
surf["face_number"] = range(6)

# plot each face with a different color
surf.plot(show_edges=True, line_width=5, scalars="face_number")

