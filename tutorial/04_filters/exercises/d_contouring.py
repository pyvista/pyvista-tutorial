"""
Contouring
~~~~~~~~~~

Generate iso-lines or -surfaces for the scalars of a surface or volume.

3D meshes can have 2D iso-surfaces of a scalar field extracted and 2D surface
meshes can have 1D iso-lines of a scalar field extracted.
"""

import pyvista as pv
from pyvista import examples

###############################################################################
# Iso-Lines
# +++++++++
#
# Let's extract 1D iso-lines of a scalar field from a 2D surface mesh.
mesh = examples.load_random_hills()

###############################################################################
help(mesh.contour)

###############################################################################
contours = ...

###############################################################################
p = pv.Plotter()
p.add_mesh(mesh, opacity=0.85)
p.add_mesh(contours, color="white", line_width=5)
p.show()


###############################################################################
# Iso-Surfaces
# ++++++++++++
#
# Let's extract 2D iso-surfaces of a scalar field from a 3D mesh.

mesh = examples.download_embryo()
mesh

###############################################################################
# For this example dataset, let's create 5 contour levels between the values
# of 50 and 200

contours = ...

###############################################################################
p = pv.Plotter()
p.add_mesh(mesh.outline(), color="k")
p.add_mesh(contours, opacity=0.25, clim=[0, 200])
p.camera_position = [
    (-130.99381142132086, 644.4868354828589, 163.80447435848686),
    (125.21748748157661, 123.94368717158413, 108.83283586619626),
    (0.2780372840777734, 0.03547871361794171, 0.9599148553609699),
]
p.show()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/04_filters/exercises/d_contouring.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
