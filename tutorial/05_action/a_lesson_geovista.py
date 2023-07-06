"""
Using GeoVista
~~~~~~~~~~~~~~

This is provided by `@bjlittle <https://github.com/bjlittle>`_ in
`this discussion <https://github.com/bjlittle/geovista/discussions/343>`_
and modifined by `@tkoyama010 <https://github.com/tkoyama010>`_ .
"""

###############################################################################
# You may think that PyVista is a little too abstract for what you want to do.
# Therefore, we will introduce GeoVista, which was developed as a gateway to
# earth sciences.
#
# GeoVista is a very good external example of using PyVista in a more concrete
# use case.

import geovista as gv
import geovista.theme
import pyvista as pv

###############################################################################
# PyVista allows you to set global and local plotting themes to easily set
# (learn more in `Control Global and Local Plotting Themes
# <https://docs.pyvista.org/version/stable/examples/02-plot/themes.html>`_).


###############################################################################
# At the `Met Office <https://www.metoffice.gov.uk/>`_ , they are moving to an
# unstructured cube-sphere mesh which is a cube projected out onto a sphere
# i.e., there are six panels on the sphere. Each cube-sphere is defined by the
# number of "cells squared" within each panel e.g., the following example is a
# C48 cube-sphere, so there are 6 * 48 * 48 cells.
#
# GeoVista has samples for it.

help(gv.samples.lfric)

###############################################################################
c48 = gv.samples.lfric(resolution="c48")

###############################################################################
# Since the `c48` is defined as PolyDdata in PyVista, it can be drawn using
# PyVista's plot method.

c48.plot(show_edges=True)

###############################################################################
# Here's a sample C48 cube-sphere populated with Sea Surface Temperature data.
# In this data, cell data from PyVista's PolyData object is used as temperature
# data:

help(gv.samples.lfric_sst)

###############################################################################
c48_sst = gv.samples.lfric_sst()
c48_sst.plot(show_edges=True)

###############################################################################
# Note that, the land masses are masked.

###############################################################################
# There is a convenience within `geovista.geodesic` that creates a
# `geovista.geodesic.BBox` instance for any 1 of the 6 cube-sphere panels i.e.,
# `geovista.geodesic.panel`

from geovista.geodesic import panel

help(panel)

###############################################################################

bbox = panel("americas")
bbox.mesh.plot()

###############################################################################
# Note that, this bounding box (bbox) is constructed from geodesic lines i.e.,
# great circles, and is a 3D manifold. As such, we can then use it to extract
# points/cells from any underlying mesh. Before doing that, first let's render
# the bounding box and the mesh together so that we can see their relationship
# to one another. Note that, our bbox instance is indeed covering the correct
# panel of the cube-sphere.

plotter = pv.Plotter()
plotter.add_mesh(c48_sst, show_edges=True)
plotter.add_mesh(bbox.mesh)
plotter.add_axes()
plotter.view_yz()
plotter.show()

###############################################################################
# As a fun exercise, you could play with opacity on the bbox.mesh to see
# through the manifold to the underlying cube-sphere surface, or turn on the
# gridlines of the bbox etc

plotter = pv.Plotter()
plotter.add_mesh(c48_sst, show_edges=True)
plotter.add_mesh(bbox.boundary(), color="green", line_width=5)
plotter.add_axes()
plotter.view_xz()
plotter.show()

###############################################################################
# Let's now use the bounding box to extract the mesh that it encloses:

region = bbox.enclosed(c48_sst)

plotter = pv.Plotter()
plotter.add_mesh(region, show_edges=True)
plotter.add_axes()
plotter.view_xz()
plotter.show()

###############################################################################
# You could perhaps then play with the `preference` kwarg of the
# `bbox.enclosed` method to see the impact on the end result.


###############################################################################
# However, let's `geo-locate` the region by also rendering a texture mapped
# base layer in addition to some coastlines:

plotter = gv.GeoPlotter()
plotter.add_mesh(region, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_hypsometric())
plotter.view_xz()
plotter.show_axes()
plotter.show()

###############################################################################
# Also, as we're not so interested in the land mask, let's threshold that out
# and re-spin the render:

sea_region = region.threshold()

plotter = gv.GeoPlotter()
plotter.add_mesh(sea_region, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_hypsometric())
plotter.view_xz()
plotter.show_axes()
plotter.show()

###############################################################################
# Since we're here... let's transform the sea_region to a Robinson projection:

plotter = gv.GeoPlotter(crs="+proj=robin lon_0=-90")
plotter.add_mesh(sea_region, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_hypsometric())
plotter.view_xy()
plotter.show_axes()
plotter.show()

###############################################################################
# It's also easily possible to get the inverted result i.e., the surface of the
# mesh not enclosed by the bbox manifold:

outside = bbox.enclosed(c48_sst, outside=True)

plotter = pv.Plotter()
plotter.add_mesh(outside, show_edges=True)
plotter.add_axes()
plotter.show()

###############################################################################
# Akin to before, let's render this again, but with a base layer underneath:

plotter = gv.GeoPlotter()
plotter.add_mesh(outside, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_1())
plotter.view_xz()
plotter.show_axes()
plotter.show()

###############################################################################
# It's not quite clear what's going on here, although playing with the render
# interactively helps, but let's transform the mesh to the Mollweider
# projection to help clarify matters:

plotter = gv.GeoPlotter(crs="+proj=moll lon_0=-90")
plotter.add_mesh(outside, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_1())
plotter.view_xy()
plotter.show_axes()
plotter.show()

###############################################################################
# And again, let's remove the land mask so that we can see more of the texture
# mapped base layer:

sea_outside = outside.threshold()

plotter = gv.GeoPlotter(crs="+proj=moll lon_0=-90")
plotter.add_mesh(sea_outside, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_1())
plotter.view_xy()
plotter.show_axes()
plotter.show()

###############################################################################
# Also, explore the BBox class to create custom bounding box instances, and
# there is also the geovista.geodesic.wedge, a convenience function akin to the
# `geovista.geodesic.panel`. Plus you can easily render geodesic lines i.e.,
# great circles, with geovista.geodesic.line.
#
# The point here is that this is just the first step. GeoVista is aiming to
# provide a richer suite of such primitives to extract regions in similar ways.
# But the capability showcased by `geovista.geodesic` hints at the direction of
# where I'm taking geovista. The other point to make is that thanks to
# `pyvista`and `vtk` the extraction operation is pretty darn fast as opposed to
# other traditional approaches (perhaps I should garner metrics to back that
# up!)
