"""
Using GeoVista
~~~~~~~~~~~~~~

This is provided by `@bjlittle <https://github.com/bjlittle>`_ in
`this discussion <https://github.com/bjlittle/geovista/discussions/343>`_
and modified by `@tkoyama010 <https://github.com/tkoyama010>`_ .
"""

###############################################################################
# You may think that PyVista is a little too abstract for what you want to do.
# Therefore, we will introduce GeoVista, which was developed as a gateway to
# cartographic capability.
#
# GeoVista is a very good external example of using PyVista in a more concrete
# use case.

import sys

if "google.colab" in sys.modules:
    subprocess.run("pip install geovista", shell=True, check=True)

import geovista as gv
import geovista.theme
import pyvista as pv

###############################################################################
# .. note:: **Motivation of GeoVista**
#
#     The goal of GeoVista is simple; to complement PyVista with a convenient
#     cartographic capability.
#
#     In this regard, from a design perspective we aim to keep GeoVista as pure
#     to PyVista as possible i.e., minimise specialisation as far as
#     practically possible in order to maximise native compatibility within the
#     PyVista and VTK ecosystems.
#
#     We intend GeoVista to be a cartographic gateway into the powerful world
#     of PyVista, and all that it offers.
#
#     GeoVista is intentionally agnostic to packages such as geopandas, iris,
#     xarray et al, which specialise in preparing your spatial data for
#     visualisation. Rather, we delegate that responsibility and choice of tool
#     to you the user, as we want GeoVista to remain as flexible and open-ended
#     as possible to the entire Scientific Python community.
#
#     Simply put, "GeoVista is to PyVista", as "Cartopy is to Matplotlib".

###############################################################################
# .. note:: **Plotting Theme**
#
#      GeoVista defines its own plotting theme in `geovista.theme`.
#      PyVista allows you to set global and local plotting themes to easily set
#      (learn more in `Control Global and Local Plotting Themes
#      <https://docs.pyvista.org/version/stable/examples/02-plot/themes.html>`_
#      ).

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
# .. note:: **LFRic - a modelling system fit for future computers**
#
#      If you are interested in LFRic, please refer to
#      `LFRic - a modelling system fit for future computers <https://www.metoffice.gov.uk/research/approach/modelling-systems/lfric>`_ .

###############################################################################
# Since the `c48` is defined as PolyData in PyVista, it can be drawn using
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

###############################################################################
# `region` is defined as PolyData of PyVista.

help(region)

###############################################################################

plotter = pv.Plotter()
plotter.add_mesh(region, show_edges=True)
plotter.add_axes()
plotter.view_xz()
plotter.show()

###############################################################################
# Let's check what kind of array does `region` have.

print(region.array_names)

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
# GeoVista has its own `Plotter` class, `GeoPlotter`. It is a customized class
# that inherits from PyVista's `Plotter` class and provides practical methods
# for geoscience such as `add_coastlines` and `add_base_layer`.

help(gv.GeoPlotter)

###############################################################################
# Also, as we're not so interested in the land mask, let's threshold that out
# and re-spin the render. To threshold the region and make `sea_region` we can
# use `threshold` method of PyVista.

sea_region = region.threshold(scalars='Surface Temperature')

###############################################################################

help(region.threshold)

###############################################################################

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

###############################################################################
# So far we've demonstrated GeoVista's ability to cope with unstructured data.
# Now let's plot a curvilinear mesh using Met Office Unified Model (UM) ORCA2
# Sea Water Potential Temperature data, with 10m Natural Earth coastlines and a
# 1:50m Natural Earth I base layer.

import geovista as gv
from geovista.pantry import um_orca2
import geovista.theme

# Load sample data.
sample = um_orca2()
sample

###############################################################################
# Create the mesh from the sample data.

mesh = gv.Transform.from_2d(sample.lons, sample.lats, data=sample.data)

###############################################################################
# Remove cells from the mesh with NaN values.

mesh = mesh.threshold()

###############################################################################
# Plot the mesh.

plotter = gv.GeoPlotter()
sargs = {"title": f"{sample.name} / {sample.units}"}
plotter.add_mesh(mesh, show_edges=True, scalar_bar_args=sargs)
plotter.add_base_layer(texture=gv.natural_earth_1())
plotter.add_coastlines(resolution="10m")
plotter.view_xy()
plotter.add_axes()
plotter.show()

###############################################################################
# .. important:: **Experimental**
#
#      GeoVista is still in the experimental stages. They would love your
#      feedback, but as immature packages their API, documentation, test
#      coverage and CI are still 'under construction'.

###############################################################################
# Whilst you're here, why not hop on over to the
# `pyvista-xarray project <https://github.com/pyvista/pyvista-xarray>`_
# and check it out!
#
# xarray DataArray accessors for PyVista to visualize datasets in 3D
#
# You must import `pvxarray` in order to register the DataArray accessor with
# xarray. After which, a pyvista namespace of accessors will be available.

import pvxarray  # noqa
import xarray as xr

###############################################################################
# Load mean sea surface temperature dataset

ds = xr.open_dataset("sst.mnmean.nc", engine="netcdf4")

###############################################################################
# Plot in 3D

ds.sst[0].pyvista.plot(x="lon", y="lat", show_edges=True, cpos="xy")

###############################################################################
# Or grab the mesh object for use with PyVista and GeoVista.

mesh = ds.sst[0].pyvista.mesh(x="lon", y="lat")

plotter = gv.GeoPlotter()
plotter.add_mesh(mesh, show_edges=True)
plotter.add_coastlines()
plotter.add_base_layer(texture=gv.natural_earth_hypsometric())
plotter.view_xz()
plotter.show_axes()
plotter.show(cpos="xy")

###############################################################################
# .. note::
#     This is inspired by
#     `Xarray Fundamentals
#     <https://tutorial.xarray.dev/workshops/online-tutorial-series/01_xarray_fundamentals.html>`_
#     in Xarray Tutorial.
#
# .. image:: https://zenodo.org/badge/doi/10.5281/zenodo.598201.svg
#    :target: https://doi.org/10.5281/zenodo.598201

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/05_action/a_lesson_geovista.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
