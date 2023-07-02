"""
.. _action_geovista:

Using GeoVista
~~~~~~~~~~~~~~
This example is provided by [@bjlittle](https://github.com/bjlittle) in
[this discussion](https://github.com/bjlittle/geovista/discussions/343).
"""

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
