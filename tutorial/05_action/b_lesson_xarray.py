"""
.. _action_example:

PyVista xarray
~~~~~~~~~~~~~~

pyvista-xarray is xarray DataArray accessors for PyVista to visualize datasets in 3D
Using GeoVista and pyvista-xarray.
"""

###############################################################################
# Usage
# +++++
#
# You must import pvxarray in order to register the DataArray accessor with
# xarray. After which, a pyvista namespace of accessors will be available.
#
# The following is an example to visualize a `RectilinearGrid` with PyVista:

import pvxarray  # noqa
import xarray as xr

ds = xr.tutorial.load_dataset("air_temperature")
da = ds.air[dict(time=0)]  # Select DataArray for a timestep

# Plot in 3D
da.pyvista.plot(x="lon", y="lat", show_edges=True, cpos='xy')

# Or grab the mesh object for use with PyVista
mesh = da.pyvista.mesh(x="lon", y="lat")

###############################################################################
# Simple RectilinearGrid
# ++++++++++++++++++++++

import numpy as np
import xarray as xr

lon = np.array([-99.83, -99.32])
lat = np.array([42.25, 42.21])
z = np.array([0, 10])
temp = 15 + 8 * np.random.randn(2, 2, 2)

ds = xr.Dataset(
    {
        "temperature": (["z", "x", "y"], temp),
    },
    coords={
        "lon": (["x"], lon),
        "lat": (["y"], lat),
        "z": (["z"], z),
    },
)

mesh = ds.temperature.pyvista.mesh(x="lon", y="lat", z="z")
mesh.plot()

###############################################################################
# Raster with rioxarray
# +++++++++++++++++++++
#
# import rioxarray
# import xarray as xr
#
# da = rioxarray.open_rasterio("TC_NG_SFBay_US_Geo_COG.tif")
# da = da.rio.reproject("EPSG:3857")
#
# # Grab the mesh object for use with PyVista
# mesh = da.pyvista.mesh(x="x", y="y", component="band")
#
# mesh.plot(scalars="data", cpos='xy', rgb=True)

###############################################################################

# import rioxarray
#
# da = rioxarray.open_rasterio("Elevation.tif")
# da = da.rio.reproject("EPSG:3857")
#
# # Grab the mesh object for use with PyVista
# mesh = da.pyvista.mesh(x="x", y="y")
#
# # Warp top and plot in 3D
# mesh.warp_by_scalar().plot()

###############################################################################
# StructuredGrid
# ++++++++++++++

import pyvista as pv
import xarray as xr

ds = xr.tutorial.open_dataset("ROMS_example.nc", chunks={"ocean_time": 1})

if ds.Vtransform == 1:
    Zo_rho = ds.hc * (ds.s_rho - ds.Cs_r) + ds.Cs_r * ds.h
    z_rho = Zo_rho + ds.zeta * (1 + Zo_rho / ds.h)
elif ds.Vtransform == 2:
    Zo_rho = (ds.hc * ds.s_rho + ds.Cs_r * ds.h) / (ds.hc + ds.h)
    z_rho = ds.zeta + (ds.zeta + ds.h) * Zo_rho

ds.coords["z_rho"] = z_rho.transpose()  # needing transpose seems to be an xarray bug

da = ds.salt[dict(ocean_time=0)]

# Make array ordering consistent
da = da.transpose("s_rho", "xi_rho", "eta_rho", transpose_coords=False)

# Grab StructuredGrid mesh
mesh = da.pyvista.mesh(x="lon_rho", y="lat_rho", z="z_rho")

# Plot in 3D
p = pv.Plotter()
p.add_mesh(mesh, lighting=False, cmap='plasma', clim=[0, 35])
p.view_vector([1, -1, 1])
p.set_scale(zscale=0.001)
p.show()
