"""
Geological Map on Topography
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Texture mapping for a GeoTIFF on a topography surface.

To overlay an image/map from a GeoTIFF on to a topography surface, it's necessary to have texture coordinates ("texture mapping") matching the proper extends of the mesh/surface you'd like to drape the texture (GeoTIFF) on.

We can do this by using the spatial reference of the GeoTIFF itself, as this allows you to preserve the entire mesh that the texture is being draped on without having to clip out the parts where you don't have imagery. In this example, we explicitly set the texture extents onto a topography surface where the texture/GeoTIFF has a much larger extent than the topography surface.

Originally posted here: https://github.com/pyvista/pyvista-support/issues/14
"""

# sphinx_gallery_thumbnail_number = 2
import os
import tempfile

import numpy as np
import pyvista as pv
import requests
from pyvista import examples

###############################################################################
path = examples.download_file("topo_clean.vtk")
topo = pv.read(path)
topo

###############################################################################
# Load the GeoTIFF/texture (this could take a minute to download)
# https://dl.dropbox.com/s/bp9j3fl3wbi0fld/downsampled_Geologic_map_on_air_photo.tif?dl=0
url = "https://dl.dropbox.com/s/bp9j3fl3wbi0fld/downsampled_Geologic_map_on_air_photo.tif?dl=0"

response = requests.get(url)  # noqa: S113
filename = os.path.join(tempfile.gettempdir(), "downsampled_Geologic_map_on_air_photo.tif")  # noqa: PTH118
open(filename, "wb").write(response.content)  # noqa: SIM115, PTH123


###############################################################################
# In the block below, we can use the ``get_gcps`` function to get the
# Ground Control Points of the raster, however this depends on GDAL. For this
# tutorial, we are going to hard code the GCPs to avoid having users install
# GDAL.


def get_gcps(filename):
    """
    Helper function retrieves the Ground Control
    Points of a GeoTIFF. Note that this requires gdal.
    """
    import rasterio

    def get_point(gcp):
        return np.array([gcp.x, gcp.y, gcp.z])

    # Load a raster
    src = rasterio.open(filename)
    # Grab the Groung Control Points
    points = np.array([get_point(gcp) for gcp in src.gcps[0]])
    # Now Grab the three corners of their bounding box
    # -- This guarantees we grab the right points
    bounds = pv.PolyData(points).bounds
    origin = [bounds[0], bounds[2], bounds[4]]  # BOTTOM LEFT CORNER
    point_u = [bounds[1], bounds[2], bounds[4]]  # BOTTOM RIGHT CORNER
    point_v = [bounds[0], bounds[3], bounds[4]]  # TOP LEFT CORNER
    return origin, point_u, point_v


###############################################################################

# Fetch the GCPs
# origin, point_u, point_v = get_gcps(filename)

# Hard code GCPs
origin = [310967.75148705335, 4238841.045453942, 0.0]
point_u = [358682.9364281533, 4238841.045453942, 0.0]
point_v = [310967.75148705335, 4276281.98755258, 0.0]

###############################################################################

# Use the GCPs to map the texture coordinates onto the topography surface
topo.texture_map_to_plane(origin, point_u, point_v, inplace=True)

###############################################################################
# Show GCPs in relation to topo surface with texture coordinates displayed
p = pv.Plotter()
p.add_point_labels(
    np.array(
        [
            origin,
            point_u,
            point_v,
        ]
    ),
    ["Origin", "Point U", "Point V"],
    point_size=5,
)

p.add_mesh(topo)
p.show(cpos="xy")


###############################################################################
# Read the GeoTIFF as a ``Texture`` in PyVista:
texture = pv.read_texture(filename)

# Now plot the topo surface with the texture draped over it
# And make window size large for a high-res screenshot
p = pv.Plotter(window_size=np.array([1024, 768]) * 3)
p.add_mesh(topo, texture=texture)
p.camera_position = [
    (337461.4124956896, 4257141.430658634, 2738.4956020899253),
    (339000.40935731295, 4260394.940646875, 1724.0720826501868),
    (0.10526647627366331, 0.2502863297360612, 0.962432190920575),
]
p.show()

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/03_figures/c_geological-map.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
