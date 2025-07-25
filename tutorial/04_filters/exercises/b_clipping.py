"""
Clipping with Planes & Boxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clip/cut any dataset using using planes or boxes.
"""

# sphinx_gallery_thumbnail_number = 2
import pyvista as pv
from pyvista import examples

# %%
# Clip with Plane
# +++++++++++++++
#
# Clip any dataset by a user defined plane using the
# :func:`pyvista.DataSetFilters.clip` filter
dataset = examples.download_bunny_coarse()
dataset

# %%
help(dataset.clip)

# %%
# Perform a clip with a Y axis normal
clipped = ...
clipped

# %%
# Plot the result.
pl = pv.Plotter()
pl.add_mesh(dataset, style="wireframe", color="blue", label="Input")
pl.add_mesh(clipped, label="Clipped")
pl.add_legend()
pl.camera_position = [(0.24, 0.32, 0.7), (0.02, 0.03, -0.02), (-0.12, 0.93, -0.34)]
pl.show()


# %%
# Clip with Bounds
# ++++++++++++++++
#
# Clip any dataset by a set of XYZ bounds using the
# :func:`pyvista.DataSetFilters.clip_box` filter.
#
# First, download an example dataset.
dataset = examples.download_office()

# %%
help(dataset.clip_box)

# %%
# Clip the dataset with a bounding box defined by the values in ``bounds``
# ``(xmin, xmax, ymin, ymax, zmin, zmax)``
bounds = [2, 4.5, 2, 4.5, 1, 3]
clipped = ...
clipped

# %%
# Plot the original dataset and the clipped one.
pl = pv.Plotter()
pl.add_mesh(dataset, style="wireframe", color="blue", label="Input")
pl.add_mesh(clipped, label="Clipped")
pl.add_legend()
pl.show()


# %%
# Clip with Rotated Box
# +++++++++++++++++++++
#
# Clip any dataset by an arbitrarily rotated solid box using the
# :func:`pyvista.DataSetFilters.clip_box` filter.
mesh = examples.load_airplane()

# Use `pv.Box()` or `pv.Cube()` to create a region of interest
roi = pv.Cube(center=(0.9e3, 0.2e3, mesh.center[2]), x_length=500, y_length=500, z_length=500)
roi.rotate_z(33, inplace=True)

pl = pv.Plotter()
pl.add_mesh(roi, opacity=0.75, color="red")
pl.add_mesh(mesh, opacity=0.5)
pl.show()

# %%
# Run the box clipping algorithm with the defined box geometry.
extracted = ...

pl = pv.Plotter(shape=(1, 2))
pl.add_mesh(roi, opacity=0.75, color="red")
pl.add_mesh(mesh)
pl.subplot(0, 1)
pl.add_mesh(extracted)
pl.add_mesh(roi, opacity=0.75, color="red")
pl.link_views()
pl.view_isometric()
pl.show()

# %%
# Crinkled Clipping
# +++++++++++++++++
# Crinkled clipping is useful if you don't want the clip filter to truly clip
# cells on the boundary, but want to preserve the input cell structure and to
# pass the entire cell on through the boundary.
#
# This option is available for :func:`pyvista.DataSetFilters.clip`,
# :func:`pyvista.DataSetFilters.clip_box`, and
# :func:`pyvista.DataSetFilters.clip_sruface`, but not available when clipping
# by scalar in :func:`pyvista.DataSetFilters.clip_scalar`.

# Input mesh
mesh = pv.Wavelet()

# %%
# Define clipping plane
normal = (1, 1, 1)
plane = pv.Plane(i_size=30, j_size=30, direction=normal)

# %%
# Perform a standard clip
clipped = mesh.clip(normal=normal)

# %%
# Perform a crinkled clip to compare
crinkled = mesh.clip(..., normal=normal)

# %%
# Plot comparison
pl = pv.Plotter(shape=(1, 2))
pl.add_mesh(clipped, show_edges=True)
pl.add_mesh(plane.extract_feature_edges(), color="r")
pl.subplot(0, 1)
pl.add_mesh(crinkled, show_edges=True)
pl.add_mesh(plane.extract_feature_edges(), color="r")
pl.link_views()
pl.show()

# %%
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/04_filters/exercises/b_clipping.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
