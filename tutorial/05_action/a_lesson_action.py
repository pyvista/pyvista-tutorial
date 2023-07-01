"""
.. _action_example:

Action example
~~~~~~~~~~~~~~

Using GeoVista and pyvista-xarray.
"""

import pvxarray  # noqa: F401
import xarray as xr

ds = xr.tutorial.load_dataset("air_temperature")
da = ds.air[dict(time=0)]  # Select DataArray for a timestep

# Plot in 3D
da.pyvista.plot(x="lon", y="lat", show_edges=True, cpos='xy')

# Or grab the mesh object for use with PyVista
mesh = da.pyvista.mesh(x="lon", y="lat")

###############################################################################
# Using GeoVista
# ~~~~~~~~~~~~~~
# This example is provided by [@bjlittle](https://github.com/bjlittle) in
# [this discussion](https://github.com/bjlittle/geovista/discussions/343).

import geovista.samples
import geovista.theme

c48 = geovista.samples.lfric(resolution="c48")

###############################################################################

c48_sst = geovista.samples.lfric_sst()
c48_sst.plot(show_edges=True)

###############################################################################

from geovista.geodesic import panel

bbox = panel("americas")
bbox.mesh.plot()

###############################################################################

import geovista as gv

plotter = gv.GeoPlotter()
plotter.add_mesh(c48_sst, show_edges=True)
plotter.add_mesh(bbox.mesh)
plotter.add_axes()
plotter.view_yz()
plotter.show()

###############################################################################

plotter = gv.GeoPlotter()
plotter.add_mesh(c48_sst, show_edges=True)
plotter.add_mesh(bbox.boundary(), color="green", line_width=5)
plotter.add_axes()
plotter.view_xz()
plotter.show()

###############################################################################

region = bbox.enclosed(c48_sst)

plotter = gv.GeoPlotter()
plotter.add_mesh(region, show_edges=True)
plotter.add_axes()
plotter.view_xz()
plotter.show()

###############################################################################

outside = bbox.enclosed(c48_sst, outside=True)

plotter = gv.GeoPlotter()
plotter.add_mesh(outside, show_edges=True)
plotter.add_axes()
plotter.show()

###############################################################################

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
