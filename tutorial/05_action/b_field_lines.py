"""
================================
Plotting Field Lines from pfsspy
================================

sunkit-pyvista can be used to plot field lines from `pfsspy`.

This example will only work on a UNIX system as it requires pre-compiled FORTRAN
code from `streamtracer <https://streamtracer.readthedocs.io/en/stable/>`__.
"""
from astropy.constants import R_sun
from astropy.coordinates import SkyCoord
import astropy.units as u
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pfsspy
from pfsspy import tracing
from pfsspy.sample_data import get_gong_map
import pyvista as pv
from sunkit_pyvista import SunpyPlotter
from sunkit_pyvista.sample import low_res_aia_193
from sunpy.coordinates import frames
import sunpy.map

###############################################################################
# We will be using an AIA 193 image from the sunpy sample data as the base image.

# Start by creating a plotter
plotter = SunpyPlotter()

# Plot a map
plotter.plot_map(low_res_aia_193, clip_interval=[1, 99] * u.percent)
# Add an arrow to show the solar rotation axis
plotter.plot_solar_axis()

# We load a gong_map from pfsspy
gong_fname = get_gong_map()
gong_map = sunpy.map.Map(gong_fname)

# Define the number of grid points in rho and solar surface rarius
nrho = 35
rss = 2.5

# Create points spaced between lat={-90, 90} degrees
lat = np.linspace(-np.pi / 2, np.pi / 2, 16, endpoint=False)
# Create 5 points spaced between long={0, 180} degrees
lon = np.linspace(0, 2 * np.pi, 16, endpoint=False)
# Make a 2D grid from these 1D points
lat, lon = np.meshgrid(lat, lon, indexing="ij")
# Create lon, lat and radial coordinate values by using a pfsspy
# and trace them using tracer
lat, lon = lat.ravel() * u.rad, lon.ravel() * u.rad
radius = rss
tracer = tracing.FortranTracer()
input_ = pfsspy.Input(gong_map, nrho, rss)
output_ = pfsspy.pfss(input_)
seeds = SkyCoord(lon, lat, radius * R_sun, frame=gong_map.coordinate_frame)
field_lines = tracer.trace(seeds, output_)

# We can also specify a color function while plotting the field lines.
# This function takes a single field line, and returns a color either
# in the form of a string, (r,g,b) or (r,g,b,a) tuple.
# In this case we use a Matplotlib norm and colormap to return a tuple of RGBA values.


def my_fline_color_func(field_line):
    norm = colors.LogNorm(vmin=1, vmax=1000)
    cmap = plt.get_cmap("viridis")
    return cmap(norm(np.abs(field_line.expansion_factor)))


# Plotting the field lines
plotter.plot_field_lines(field_lines, color_func=my_fline_color_func)
plotter.plotter.add_mesh(pv.Sphere(radius=1))

# Set the camera coordinate to view the plot correctly
camera_coord = SkyCoord(
    0 * u.deg,
    0 * u.deg,
    6 * R_sun,
    frame=frames.HeliographicStonyhurst,
    obstime=low_res_aia_193.date,
)
plotter.set_camera_coordinate(camera_coord)

plotter.show()
