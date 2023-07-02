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
