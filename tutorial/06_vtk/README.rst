.. _vtk:

PyVista & VTK
=============

Show how PyVista uses VTK and how you can combine the best of both worlds! (10 minutes for talk, 10 minutes for exercise)

.. tip::

    This section of the tutorial was adopted from the `Transitioning from VTK to PyVista <https://docs.pyvista.org/user-guide/vtk_to_pyvista.html>`_
    chapter of the PyVista documentation.


Transitioning from VTK to PyVista
---------------------------------


VTK is primarily developed in C++ and uses chained setter and getter
commands to access data. Instead, PyVista wraps the VTK data types
into numpy arrays so that users can benefit from its bracket syntax
and fancy indexing.  This section demonstrates the difference between
the two approaches in a series of examples.

For example, to hard-code values for a `vtk.vtkImageData`_ data
structure using VTK Python's bindings, one would write the following:

.. pyvista-plot::
   :context:

   import vtk
   from math import cos, sin

Create values for a 300x300 image dataset

.. pyvista-plot::
   :context:

   values = vtk.vtkDoubleArray()
   values.SetName("values")
   values.SetNumberOfComponents(1)
   values.SetNumberOfTuples(300*300)

   for x in range(300):
      for y in range(300):
         values.SetValue(x*300 + y, 127.5 + (1.0 + sin(x/25.0)*cos(y/25.0)))

Create the image structure

.. pyvista-plot::
   :context:

   image_data = vtk.vtkImageData()
   image_data.SetOrigin(0, 0, 0)
   image_data.SetSpacing(1, 1, 1)
   image_data.SetDimensions(300, 300, 1)

Assign the values to the image

.. pyvista-plot::
   :context:

   image_data.GetPointData().SetScalars(values)

As you can see, there is quite a bit of boilerplate that goes into
the creation of a simple `vtk.vtkImageData`_ dataset. PyVista provides
much more concise syntax that is more "Pythonic". The equivalent code in
PyVista is:


.. pyvista-plot::
   :context:

   import pyvista as pv
   import numpy as np

Use the meshgrid function to create 2D "grids" of the x and y values.
This section effectively replaces the vtkDoubleArray.

.. pyvista-plot::
   :context:

   xi = np.arange(300)
   x, y = np.meshgrid(xi, xi)
   values = 127.5 + (1.0 + np.sin(x/25.0)*np.cos(y/25.0))

Create the grid.  Note how the values must use Fortran ordering.

.. pyvista-plot::
   :context:

   grid = pv.ImageData(dimensions=(300, 300, 1))
   grid.point_data["values"] = values.flatten(order="F")

Here, PyVista has done several things for us:

#. PyVista combines the dimensionality of the data (in the shape of
   the :class:`numpy.ndarray`) with the values of the data in one line. VTK uses
   "tuples" to describe the shape of the data (where it sits in space)
   and "components" to describe the type of data (1 = scalars/scalar
   fields, 2 = vectors/vector fields, n = tensors/tensor
   fields). Here, shape and values are stored concretely in one
   variable.

#. :class:`pyvista.ImageData` wraps `vtk.vtkImageData`_, just with a
   different name; they are both containers of evenly spaced points. Your
   data does not have to be an "image" to use it with
   `vtk.vtkImageData`_; rather, like images, values in the dataset are
   evenly spaced apart like pixels in an image.

   Furthermore, since we know the container is for uniformly spaced data,
   pyvista sets the origin and spacing by default to ``(0, 0, 0)`` and
   ``(1, 1, 1)``. This is another great thing about PyVista and Python!
   Rather than having to know everything about the VTK library up front,
   you can get started very easily! Once you get more familiar with it
   and need to do something more complex, you can dive deeper. For
   example, changing the origin and spacing is as simple as:

   .. pyvista-plot::
      :context:

      grid.origin = (10, 20, 10)
      grid.spacing = (2, 3, 5)

#. The name for the :attr:`point_array <pyvista.point_array>` is given
   directly in dictionary-style fashion. Also, since VTK stores data
   on the heap (linear segments of RAM; a C++ concept), the
   data must be flattened and put in Fortran ordering (which controls
   how multidimensional data is laid out in physically 1d memory; numpy
   uses "C"-style memory layout by default). This is why in our earlier
   example, the first argument to ``SetValue()`` was written as
   ``x*300 + y``. Here, numpy takes care of this for us quite nicely
   and it's made more explicit in the code, following the Python best
   practice of "Explicit is better than implicit".

Finally, with PyVista, each geometry class contains methods that allow
you to immediately plot the mesh without also setting up the plot.
For example, in VTK you would have to do:

.. code:: python

   actor = vtk.vtkImageActor()
   actor.GetMapper().SetInputData(image_data)
   ren = vtk.vtkRenderer()
   renWin = vtk.vtkRenderWindow()
   renWin.AddRenderer(ren)
   renWin.SetWindowName('ReadSTL')
   iren = vtk.vtkRenderWindowInteractor()
   iren.SetRenderWindow(renWin)
   ren.AddActor(actor)
   iren.Initialize()
   renWin.Render()
   iren.Start()

However, with PyVista you only need:

.. pyvista-plot::
   :context:

   grid.plot(cpos='xy', show_scalar_bar=False, cmap='coolwarm')


.. _vtk.vtkImageData: https://vtk.org/doc/nightly/html/classvtkImageData.html


PointSet Construction
~~~~~~~~~~~~~~~~~~~~~
PyVista heavily relies on NumPy to efficiently allocate and access
VTK's C arrays.  For example, to create an array of points within VTK
one would normally loop through all the points of a list and supply
that to a  `vtkPoints`_ class.  For example:

.. pyvista-plot::
   :context:

   import vtk
   vtk_array = vtk.vtkDoubleArray()
   vtk_array.SetNumberOfComponents(3)
   vtk_array.SetNumberOfValues(9)
   vtk_array.SetValue(0, 0)
   vtk_array.SetValue(1, 0)
   vtk_array.SetValue(2, 0)
   vtk_array.SetValue(3, 1)
   vtk_array.SetValue(4, 0)
   vtk_array.SetValue(5, 0)
   vtk_array.SetValue(6, 0.5)
   vtk_array.SetValue(7, 0.667)
   vtk_array.SetValue(8, 0)
   vtk_points = vtk.vtkPoints()
   vtk_points.SetData(vtk_array)
   vtk_points

To do the same within PyVista, you simply need to create a NumPy array:

.. pyvista-plot::
   :context:

   import numpy as np
   np_points = np.array([[0, 0, 0], [1, 0, 0], [0.5, 0.667, 0]])

.. note::
   You can use :func:`pyvista.vtk_points` to construct a `vtkPoints`_
   object, but this is unnecessary in almost all situations.

Since the end goal is to construct a :class:`pyvista.DataSet
<pyvista.core.dataset.DataSet>`, you would simply pass the
``np_points`` array to the :class:`pyvista.PolyData` constructor:

.. pyvista-plot::
   :context:

   import pyvista as pv
   poly_data = pv.PolyData(np_points)

Whereas in VTK you would have to do:

.. pyvista-plot::
   :context:

   vtk_poly_data = vtk.vtkPolyData()
   vtk_poly_data.SetPoints(vtk_points)

The same goes with assigning face or cell connectivity/topology.  With
VTK you would normally have to loop using :func:`InsertNextCell` and
:func:`InsertCellPoint`.  For example, to create a single cell
(triangle) and then assign it to `vtkPolyData`_:

.. pyvista-plot::
   :context:

   cell_arr = vtk.vtkCellArray()
   cell_arr.InsertNextCell(3)
   cell_arr.InsertCellPoint(0)
   cell_arr.InsertCellPoint(1)
   cell_arr.InsertCellPoint(2)
   vtk_poly_data.SetPolys(cell_arr)

In PyVista, we can assign this directly in the constructor and then
access it (or change it) from the :attr:`faces
<pyvista.PolyData.faces>` attribute.

.. pyvista-plot::
   :context:

   faces = np.array([3, 0, 1, 2])
   poly_data = pv.PolyData(np_points, faces)
   poly_data.faces


PyVista Tradeoffs
~~~~~~~~~~~~~~~~~
While most features can, not everything can be simplified in PyVista without
losing functionality or performance.

In the :class:`collision <pyvista.PolyDataFilters.collision>` filter,
we demonstrate how to calculate the collision between two meshes.  For
example:

.. pyvista-plot::
   :context:
   :include-source: False

   # Configure for trame
   import pyvista
   pyvista.set_plot_theme('document')
   pyvista.set_jupyter_backend('trame')
   pyvista.global_theme.axes.show = False
   pyvista.global_theme.smooth_shading = True


.. pyvista-plot::
   :context:

   import pyvista as pv

   # create a default sphere and a shifted sphere
   mesh_a = pv.Sphere()
   mesh_b = pv.Sphere(center=(-0.4, 0, 0))
   out, n_coll = mesh_a.collision(mesh_b, generate_scalars=True, contact_mode=2)

   pl = pv.Plotter()
   pl.add_mesh(out)
   pl.add_mesh(mesh_b, style='wireframe', color='k')
   pl.camera_position = 'xy'
   pl.show()

Under the hood, the collision filter detects mesh collisions using
oriented bounding box (OBB) trees.  For a single collision, this filter
is as performant as the VTK counterpart, but when computing multiple
collisions with the same meshes, as in the `Collision Example <https://docs.pyvista.org/examples/01-filter/collisions.html>`_
example, it is more efficient to use the `vtkCollisionDetectionFilter
<https://vtk.org/doc/nightly/html/classvtkCollisionDetectionFilter.html>`_,
as the OBB tree is computed once for each mesh.  In most cases, pure
PyVista is sufficient for most data science, but there are times when
you may want to use VTK classes directly.


PyVista and VTK Together
------------------------

PyVista is best known for is easy to use plotting API -- being familiar to most Python users already experienced with libraries like Matplotlib. Many people benefit from combining the power of VTK's Python bindings for their data pipelines and the flexibility and simplicity of PyVista for 3D rendering. The following section demonstrates this usage scenario.

.. tip::

    In case it was not made clear in the :ref:`mesh` section, PyVista mesh classes are subclasses of their VTK counterparts - which means PyVista can be intermixed with VTK workflows.

Nothing stops you from using VTK classes and then wrapping
the output with PyVista for streamlined plotting. For example:

.. pyvista-plot::
   :context:

   import vtk
   import pyvista as pv

   # Create a circle using vtk
   polygonSource = vtk.vtkRegularPolygonSource()
   polygonSource.GeneratePolygonOff()
   polygonSource.SetNumberOfSides(50)
   polygonSource.SetRadius(5.0)
   polygonSource.SetCenter(0.0, 0.0, 0.0)
   polygonSource.Update()

   # wrap and plot using pyvista
   mesh = pv.wrap(polygonSource.GetOutput())
   mesh.plot(line_width=3, cpos='xy', color='k')

In this manner, you can get the "best of both worlds" should you need
the flexibility of PyVista and the raw power of VTK.

.. note::
   You can use :func:`pyvista.Polygon` for a one line replacement of
   the above VTK code.

VTK Algorithms
~~~~~~~~~~~~~~

Perhaps there is a VTK algorithm that is not (yet) exposed in PyVista that you'd like to use. This is easy enough to work with since PyVista objects are VTK objects. We can pass our PyVista meshes to the VTK algorithm, then wrap the output for plotting, further filtering, or anything.


.. pyvista-plot::
   :context:

    import pyvista as pv
    from pyvista import examples
    import vtk

    mesh = examples.download_bunny_coarse()

    # Initialize VTK algorithm
    splatter = vtk.vtkGaussianSplatter()

    # Pass PyVista object as input to VTK
    splatter.SetInputData(mesh)

    # Set parameters
    n = 200
    splatter.SetSampleDimensions(n, n, n)
    splatter.SetRadius(.02)
    splatter.SetExponentFactor(-10)
    splatter.SetEccentricity(2)
    splatter.Update()

    # Retrieve output and wrap with PyVista
    vol = pv.wrap(splatter.GetOutput())

    # Use PyVista to produce contours
    cntrs = vol.contour([.95 * splatter.GetRadius()])

    # Use PyVista to plot
    p = pv.Plotter()
    p.add_mesh(mesh, style='wireframe')
    p.add_mesh(cntrs, color=True)
    p.show()


.. note::

    The above example was adapted from VTK's `Embed Points Into Volume <https://kitware.github.io/vtk-examples/site/Cxx/PolyData/EmbedPointsIntoVolume/>`_


.. _vtkDataArray: https://vtk.org/doc/nightly/html/classvtkDataArray.html
.. _vtkPolyData: https://vtk.org/doc/nightly/html/classvtkPolyData.html
.. _vtkImageData: https://vtk.org/doc/nightly/html/classvtkImageData.html
.. _vtkpoints: https://vtk.org/doc/nightly/html/classvtkPoints.html


Exercises
---------

.. leave blank after this point for Sphinx-Gallery to populate examples
