.. _intro:

Introduction
============

This section includes a brief explanation of the background and history of PyVista.

.. tip::

    This section of the tutorial was adopted from `Getting Started
    <https://docs.pyvista.org/getting-started/index.html>`_ chapter of the
    PyVista documentation.

PyVista is one of many visualization libraries built on top `VTK - The
Visualization Toolkit <https://vtk.org/>`_. It's primary intent was to be an
abstraction layer over VTK to provide convenience and functionality to VTK
exposed "Pythonically".


Brief History
-------------
PyVista was created out of a desire to make a reusable higher level abstraction
layer that "wraps" the lower level functionality of VTK.

- Originally created as a sub-libary for `femorph
  <https://www.wpafb.af.mil/News/Article-Display/Article/1503043/afrl-signs-first-of-its-kind-software-license-with-pratt-whitney/>`_
  by `@akaszynski <https://github.com/akaszynski>`_ in 2016.
- First posted to GitHub as `akaszynski/vtki
  <https://github.com/akaszynski/vtki>`_ back in 2017.
- `@banesullivan <https://github.com/banesullivan/>`_ joined the project in
  2018 to expand functionality, features, and improve the documentation with examples.
- First release of `PyVista <https://pypi.org/project/pyvista/#history>`_ on
  PyPI in 2019.
- Published a paper `Sullivan, B., & Kaszynski, A. (2019). PyVista: 3D
  plotting and mesh analysis through a streamlined interface for the
  Visualization Toolkit (VTK). Journal of Open Source Software, 4(37), 1450.
  https://doi.org/10.21105/joss.01450 <https://joss.theoj.org/papers/10.21105/joss.01450>`_
- As of October 2024, Over 150+ contributors and `~2.4k Stars
  <https://github.com/pyvista/pyvista/stargazers>`_ on GitHub.
- Used by at least 2.8k other `libraries, examples, and repositories <https://github.com/pyvista/pyvista/network/dependents>`_ on GitHub.
- Greatly expanded internal presence and continuing support thanks to

  - `@tkoyama010 <https://github.com/tkoyama010>`_
  - `@adeak <https://github.com/adeak>`_
  - `@MatthewFlamm <https://github.com/MatthewFlamm>`_
  - `@user27182 <https://github.com/user27182>`_
- Greatly expanded PyVista ecosystem thanks to

  - `@bjlittle <https://github.com/bjlittle>`_ creator of `GeoVista <https://github.com/bjlittle/geovista>`_
  - `@adtzlr <https://github.com/adtzlr>`_ creator of `FElupe <https://github.com/adtzlr/felupe>`_

|PyPIact|
|condaact|
|contributors|
|stars|

Please take a look at the `contributors page`_ and the active `list of authors`_
to learn more about the developers of PyVista.

|contrib.rocks|

Made with `contrib rocks`_.

.. |PyPIact| image:: https://img.shields.io/pypi/dm/pyvista.svg?label=PyPI%20downloads
   :target: https://pypi.org/project/pyvista/

.. |condaact| image:: https://img.shields.io/conda/dn/conda-forge/pyvista.svg?label=Conda%20downloads
   :target: https://anaconda.org/conda-forge/pyvista

.. |contributors| image:: https://img.shields.io/github/contributors/pyvista/pyvista.svg?logo=github&logoColor=white
   :target: https://github.com/pyvista/pyvista/graphs/contributors/

.. |stars| image:: https://img.shields.io/github/stars/pyvista/pyvista.svg?style=social&label=Stars
   :target: https://github.com/pyvista/pyvista
   :alt: GitHub

.. |contrib.rocks| image:: https://contrib.rocks/image?repo=pyvista/pyvista
   :target: https://github.com/pyvista/pyvista/graphs/contributors
   :alt: contrib.rocks

.. _contrib rocks: https://contrib.rocks
.. _contributors page: https://github.com/pyvista/pyvista/graphs/contributors/
.. _list of authors: https://docs.pyvista.org/getting-started/authors.html#authors
.. _contrib rocks: https://contrib.rocks

Who is PyVista for?
-------------------

Anyone who wants to visualize 3D data using Python.

Here's how people are using PyVista:

- `PyVista User Stories <https://github.com/pyvista/pyvista/discussions/2133>`_

Feel free to write about what you have achieved with PyVista or what you would
like to achieve in the future.

Brief Examples
--------------

Read and Plot a Surface Mesh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VTK is powerful, really powerful! You can do just about anything within VTK and
PyVista just wants to make it easier to do it using ``numpy``-like and
``Matplotlib``-like syntax. For example, if you wanted to be able to plot a
simple surface mesh:


.. jupyter-execute::
   :hide-code:

   # Configure for trame
   import pyvista
   pyvista.set_plot_theme('document')
   pyvista.set_jupyter_backend('trame')
   pyvista.global_theme.window_size = [600, 400]
   pyvista.global_theme.axes.show = False
   pyvista.global_theme.smooth_shading = True


**Load and plot a surface dataset**

+-------------------------------------------+-------------------------------------+
| Using ``vtk``                             | Using PyVista                       |
+===========================================+=====================================+
| .. code:: python                          | .. pyvista-plot::                   |
|                                           |                                     |
|    import vtk                             |    from pyvista import examples     |
|    reader = vtk.vtkSTLReader()            |    mesh = examples.download_bunny() |
|    reader.SetFileName("bunny.stl")        |    mesh.plot(cpos='xy')             |
|    mapper = vtk.vtkPolyDataMapper()       |                                     |
|    output_port = reader.GetOutputPort()   |                                     |
|    mapper.SetInputConnection(output_port) |                                     |
|    actor = vtk.vtkActor()                 |                                     |
|    actor.SetMapper(mapper)                |                                     |
|    ren = vtk.vtkRenderer()                |                                     |
|    renWin = vtk.vtkRenderWindow()         |                                     |
|    renWin.AddRenderer(ren)                |                                     |
|    iren = vtk.vtkRenderWindowInteractor() |                                     |
|    iren.SetRenderWindow(renWin)           |                                     |
|    ren.AddActor(actor)                    |                                     |
|    iren.Initialize()                      |                                     |
|    renWin.Render()                        |                                     |
|    iren.Start()                           |                                     |
|    del iren, renWin                       |                                     |
+-------------------------------------------+-------------------------------------+


Construct a Simple Point Cloud with Color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These examples demonstrate how you can use both PyVista and VTK to construct
and visualize a point cloud using ``numpy``. Here, we demonstrate how easy it
is to work directly with NumPy arrays.

.. tab-set::

   .. tab-item:: VTK

      This example was taken from this `SO Answer
      <https://stackoverflow.com/a/7604478/3369879>`_.

      .. code:: python

          import vtk
          from numpy import random

          class VtkPointCloud:

              def __init__(self, zMin=-10.0, zMax=10.0, maxNumPoints=1e6):
                  self.maxNumPoints = maxNumPoints
                  self.vtkPolyData = vtk.vtkPolyData()
                  self.clearPoints()
                  mapper = vtk.vtkPolyDataMapper()
                  mapper.SetInputData(self.vtkPolyData)
                  mapper.SetColorModeToDefault()
                  mapper.SetScalarRange(zMin, zMax)
                  mapper.SetScalarVisibility(1)
                  self.vtkActor = vtk.vtkActor()
                  self.vtkActor.SetMapper(mapper)

              def addPoint(self, point):
                  if self.vtkPoints.GetNumberOfPoints() < self.maxNumPoints:
                      pointId = self.vtkPoints.InsertNextPoint(point[:])
                      self.vtkDepth.InsertNextValue(point[2])
                      self.vtkCells.InsertNextCell(1)
                      self.vtkCells.InsertCellPoint(pointId)
                  else:
                      r = random.randint(0, self.maxNumPoints)
                      self.vtkPoints.SetPoint(r, point[:])
                  self.vtkCells.Modified()
                  self.vtkPoints.Modified()
                  self.vtkDepth.Modified()

              def clearPoints(self):
                  self.vtkPoints = vtk.vtkPoints()
                  self.vtkCells = vtk.vtkCellArray()
                  self.vtkDepth = vtk.vtkDoubleArray()
                  self.vtkDepth.SetName('DepthArray')
                  self.vtkPolyData.SetPoints(self.vtkPoints)
                  self.vtkPolyData.SetVerts(self.vtkCells)
                  self.vtkPolyData.GetPointData().SetScalars(self.vtkDepth)
                  self.vtkPolyData.GetPointData().SetActiveScalars('DepthArray')

          pointCloud = VtkPointCloud()
          for k in range(1000):
              point = 20*(random.rand(3)-0.5)
              pointCloud.addPoint(point)
          pointCloud.addPoint([0,0,0])
          pointCloud.addPoint([0,0,0])
          pointCloud.addPoint([0,0,0])
          pointCloud.addPoint([0,0,0])

          # Renderer
          renderer = vtk.vtkRenderer()
          renderer.AddActor(pointCloud.vtkActor)
          renderer.SetBackground(.2, .3, .4)
          renderer.ResetCamera()

          # Render Window
          renderWindow = vtk.vtkRenderWindow()
          renderWindow.AddRenderer(renderer)

          # Interactor
          renderWindowInteractor = vtk.vtkRenderWindowInteractor()
          renderWindowInteractor.SetRenderWindow(renderWindow)

          # Begin Interaction
          renderWindow.Render()
          renderWindowInteractor.Start()

   .. tab-item:: PyVista

      .. pyvista-plot::
         :context:

         import pyvista as pv
         import numpy as np
         points = np.random.random((1000, 3))
         pc = pv.PolyData(points)
         pc.plot(scalars=points[:, 2], point_size=5.0, cmap='jet')



How other Libraries Compare
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a ton of excellent visualization libraries out there and if you're
interested in data visualization, I'd encourage you for explore them all!

- `Python Libraries for Mesh, Point Cloud, and Data Visualization <https://towardsdatascience.com/python-libraries-for-mesh-and-point-cloud-visualization-part-1-daa2af36de30?gi=70edd77e5fc>`_
- `How does PyVista relate to other visualization tools? <https://github.com/pyvista/pyvista/discussions/1438>`_
- `SciVis Libraries <https://pyviz.org/scivis/index.html>`_

Here's a few of them:

.. tab-set::

   .. tab-item:: vtk

      The Visualization Toolkit (`VTK <https://vtk.org/>`_) is open source
      software for manipulating and displaying scientific data. It comes with
      state-of-the-art tools for 3D rendering, a suite of widgets for 3D
      interaction, and extensive 2D plotting capability.

      .. image:: https://miro.medium.com/max/1400/1*B3aEPDxSvgR6Giyh4I4a2w.jpeg
         :alt: VTK

   .. tab-item:: ParaView

      `ParaView <https://www.paraview.org/>`_ is an open-source, multi-platform
      data analysis and visualization application. ParaView users can quickly
      build visualizations to analyze their data using qualitative and
      quantitative techniques. The data exploration can be done interactively
      in 3D or programmatically using ParaView’s batch processing capabilities.

      .. image:: https://www.kitware.com/main/wp-content/uploads/2018/11/ParaView-5.6.png
         :alt: ParaView

   .. tab-item:: vedo

      `vedo <https://vedo.embl.es/>`_ is a Python library for scientific
      analysis of 3D objects and point clouds based on VTK and numpy.

      .. image:: https://user-images.githubusercontent.com/32848391/80292484-50757180-8757-11ea-841f-2c0c5fe2c3b4.jpg
         :alt: vedo

   .. tab-item:: Mayavi

      `Mayavi <https://docs.enthought.com/mayavi/mayavi/>`_ is a general
      purpose, cross-platform tool for 2-D and 3-D scientific data
      visualization.

      .. image:: https://viscid-hub.github.io/Viscid-docs/docs/dev/_images/mvi-000.png
         :alt: Mayavi



Exercises
---------
Install PyVista by visiting :ref:`getting_started`.

Once you've installed PyVista, open the example below and see if you can run
the "Hello World" of PyVista. You can download the example by scrolling to the
bottom of the page and clicking on either the ``*.py`` (script) or ``*.ipynb``
(notebook) file format.
