.. _intro:

.. jupyter-execute::
   :hide-code:

   # Configure for pythreejs
   import pyvista
   pyvista.set_jupyter_backend('panel')
   pyvista.global_theme.background = 'white'
   pyvista.global_theme.window_size = [600, 400]
   pyvista.global_theme.axes.show = False
   pyvista.global_theme.smooth_shading = True
   pyvista.global_theme.antialiasing = True


Introduction
============

This section includes a brief explanation of the background and history of PyVista.

Setup PyVista and get started with 3D visualization within Python.

.. tip::

    This section of the tutorial was adopted from `Getting Started
    <https://docs.pyvista.org/getting-started/index.html>`_ chapter of the
    PyVista documentation.

PyVista is one of many visulization libraries built ontop `VTK - The
Visualization Toolkit <https://vtk.org/>`_. It's primary intent was to be an
abstraction layer over VTK to provide conviencece and functionality to VTK
exposed "Pytonically".

Read a Surface Mesh and Plot it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
VTK is powerful, really powerful. You can do just about anything within VTK and
PyVista just wants to make it easier to do it using ``numpy``-like and
``matplotlib``-like syntax. For example, if you wanted to be able to plot a
simple surface mesh:

+-------------------------------------------+-------------------------------------+
| Read and plot STL file using ``vtk``      | Read an STL file using PyVista      |
+===========================================+=====================================+
| .. code:: python                          | .. jupyter-execute::                |
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

.. tabs::

   .. tab:: VTK

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

   .. tab:: PyVista
      
      .. jupyter-execute::
         
         import pyvista as pv
         import numpy as np
         points = np.random.random((1000, 3))
         pc = pv.PolyData(points)
         pc.plot(scalars=points[:, 2], point_size=5.0, cmap='jet')



How other Libraries Compare
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: ParaView

      `ParaView <https://www.paraview.org/>`_ is an open-source, multi-platform
      data analysis and visualization application. ParaView users can quickly
      build visualizations to analyze their data using qualitative and
      quantitative techniques. The data exploration can be done interactively
      in 3D or programmatically using ParaView’s batch processing capabilities.

      How this compares with PyVista.
         
   .. tab:: iPython

      Here's a quick demo of PyVista running within a terminal using `iPython
      <https://ipython.org/>`_.

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_ipython_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>





Exercises
---------

.. leave blank after this point for Sphinx-Gallery to populate examples
