"""
.. _ref_edl:

Eye Dome Lighting
~~~~~~~~~~~~~~~~~

Eye-Dome Lighting (EDL) is a non-photorealistic, image-based shading technique
designed to improve depth perception in scientific visualization images.
To learn more, please see `this blog post`_.

.. _this blog post: https://blog.kitware.com/eye-dome-lighting-a-non-photorealistic-shading-technique/

"""

###############################################################################

# sphinx_gallery_thumbnail_number = 1
import pyvista as pv
from pyvista import examples

###############################################################################
# Point Cloud
# +++++++++++
#
# When plotting a simple point cloud, it can be difficult to perceive depth.
# Take this Lidar point cloud for example:

point_cloud = examples.download_lidar()
point_cloud

###############################################################################
# And now plot this point cloud as-is:

# Plot a typical point cloud with no EDL
p = pv.Plotter()
p.add_mesh(point_cloud, color="tan", point_size=5)
p.show()


###############################################################################
# We can improve the depth mapping by enabling eye dome lighting on the
# renderer with :func:`pyvista.Renderer.enable_eye_dome_lighting`.
#
# Try plotting that point cloud with Eye-Dome-Lighting yourself below:

p = pv.Plotter()
p.add_mesh(point_cloud, color="tan", point_size=5)
p.enable_eye_dome_lighting()  # Turn on eye dome lighting here
p.show()


###############################################################################
# The eye dome lighting mode can also handle plotting scalar arrays. Try the
# above block but by specifying a ``scalars`` array instead of ``color`` in
# the ``add_mesh`` call.

p = pv.Plotter()
p.add_mesh(point_cloud, scalars="Elevation", point_size=5)
p.enable_eye_dome_lighting()  # Turn on eye dome lighting here
p.show()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/03_figures/solutions/c_edl.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
