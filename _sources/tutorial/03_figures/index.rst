:orphan:

.. _figures:

Plotting Options and Animations
===============================

Demonstrate many features of the PyVista plotting API to create compelling 3D visualizations and touch on animations (10 min for talk, 10 min for exercise)

.. tip::

    This section of the tutorial was adopted from the Plotting section
    of `PyVista's Example Gallery <https://docs.pyvista.org/examples/index.html#plotting>`_.


PyVista enables many possibilities for altering how you display 3D data, a few of our
most common features include:

* Color mapping scalar values with ``Matplotlib`` colormaps
* Showing the edges and nodes of different mesh types
* Label points in 3D space along side your meshes
* Creating side-by-side comparisons
* Making a dataset transparent or using a scalar value to map opacity
* Adding textures/images draped over a mesh (texture mapping)
* Use sophisticated lighting techniques like smooth shading or Eye Dome Lighting
* Creating animations as GIFs or movie files

This section will overview PyVista's :class:`pyvista.Plotter` API and how to perform these tasks.
The goal of this lesson is not to be a comprehensive overview of PyVista's plotting API, but
rather to demonstrate how it works and how you can learn to use it!


The Basics
----------

PyVista's plotting API is data-centric, where the 3D data are individually added to the scene with different display parameters
in a Matplotlib-like fashion.


Add Mesh to Plotter Object
~~~~~~~~~~~~~~~~~~~~~~~~~~

When plotting, users must first create a :class:`pyvista.Plotter` instance (much like a Matplotlib figure). Then data are added to the plotter instance through the :func:`pyvista.Plotter.add_mesh` method. This workflow typically looks like:

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
    from pyvista import examples

    mesh = pv.Wavelet()

    p = pv.Plotter()
    p.add_mesh(mesh)
    p.show()


You can customize how that mesh is displayed through the parameters of the :func:`pyvista.Plotter.add_mesh` method. For example, we can change the colormap via the ``cmap`` argument:



.. pyvista-plot::
   :context:

    p = pv.Plotter()
    p.add_mesh(mesh, cmap='coolwarm')
    p.show()


Or show the edges of the mesh with ``show_edges``:

.. pyvista-plot::
   :context:

    p = pv.Plotter()
    p.add_mesh(mesh, show_edges=True)
    p.show()


Or adjust the opacity to be a scalar value or linear transfer function via the ``opacity`` argument:

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    mesh = examples.download_st_helens().warp_by_scalar()

    p = pv.Plotter()
    p.add_mesh(mesh, cmap='terrain', opacity="linear")
    p.show()


Take a look at all of the options for `add_mesh <https://docs.pyvista.org/api/plotting/_autosummary/pyvista.Plotter.add_mesh.html>`_.

The ``add_mesh`` method can be called over and over to add different data to the same ``Plotter`` scene. For example, we can create many different mesh objects and plot them together:


.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    kinds = [
        'tetrahedron',
        'cube',
        'octahedron',
        'dodecahedron',
        'icosahedron',
    ]
    centers = [
        (0, 1, 0),
        (0, 0, 0),
        (0, 2, 0),
        (-1, 0, 0),
        (-1, 2, 0),
    ]

    solids = [pv.PlatonicSolid(kind, radius=0.4, center=center) for kind, center in zip(kinds, centers)]

    p = pv.Plotter(window_size=[1000, 1000])
    for solid in solids:
        p.add_mesh(
            solid, color='silver', specular=1.0, specular_power=10
        )
    p.view_vector((5.0, 2, 3))
    p.add_floor('-z', lighting=True, color='tan', pad=1.0)
    p.enable_shadows()
    p.show()


Subplotting
~~~~~~~~~~~

Creating side-by-side comparisons of datasets is easy with PyVista's subplotting API. Get started by specifying the shape of the :class:`pyvista.Plotter` object then registering the active subplot by the :func:`pyvista.Plotter.subplot` method much like how you subplot with Matplotlib's API.


.. pyvista-plot::

    import pyvista as pv

    p = pv.Plotter(shape=(1, 2))

    p.subplot(0, 0)
    p.add_mesh(pv.Sphere())

    p.subplot(0, 1)
    p.add_mesh(pv.Cube())

    p.show()

Below is an example of side-by-side comparisons of the contours and slices of a single dataset.

.. tip::

    You can link the cameras of both views with the :func:`pyvista.Plotter.link_views` method


.. pyvista-plot::

    import pyvista as pv

    mesh = pv.Wavelet()
    cntr = mesh.contour()
    slices = mesh.slice_orthogonal()

    p = pv.Plotter(shape=(1, 2))

    p.add_mesh(cntr)

    p.subplot(0, 1)
    p.add_mesh(slices)

    p.link_views()
    p.view_isometric()
    p.show()


Other custom layouts are supported by the ``shape`` argument as string descriptors:

* ``shape="3|1"`` means 3 plots on the left and 1 on the right,
* ``shape="4/2"`` means 4 plots on top and 2 at the bottom.

Here is an example of three plots on the right and one on the left:


.. pyvista-plot::

    import pyvista as pv

    mesh = pv.Wavelet()
    cntr = mesh.contour()
    slices = mesh.slice_orthogonal()
    thresh = mesh.threshold(200)

    p = pv.Plotter(shape="1|3")

    p.subplot(1)
    p.add_mesh(cntr)

    p.subplot(2)
    p.add_mesh(slices)

    p.subplot(3)
    p.add_mesh(thresh)

    p.subplot(0)
    p.add_mesh(mesh)

    p.link_views()
    p.view_isometric()
    p.show()


.. note::

    There is a comprehensive overview of subplotting in the `Multi-Window Plotting Example <https://docs.pyvista.org/examples/02-plot/multi-window.html>`_ This example details how to create more complex layouts.



Controlling the Scene
---------------------

.. tip::

  For a full list of methods on the :class:`pyvista.Plotter`, please see the `API documentation <https://docs.pyvista.org/api/plotting/_autosummary/pyvista.Plotter.html>`_

Axes and Bounds
~~~~~~~~~~~~~~~

Axes can be added to the scene with :func:`pyvista.Plotter.show_axes`

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    mesh = examples.load_random_hills()

    p = pv.Plotter()
    p.add_mesh(mesh)
    p.show_axes()
    p.show()

And bounds similarly with :func:`pyvista.Plotter.show_bounds`

.. tip::

    See `Plotting Bounds <https://docs.pyvista.org/examples/02-plot/bounds.html>`_ for more details.

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    mesh = examples.load_random_hills()

    p = pv.Plotter()
    p.add_mesh(mesh)
    p.show_axes()
    p.show_bounds()
    p.show()



Exercises
---------

.. leave blank after this point for Sphinx-Gallery to populate examples



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Lesson Overview">

.. only:: html

  .. image:: /tutorial/03_figures/images/thumb/sphx_glr_a_lesson_figures_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_a_lesson_figures.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Lesson Overview</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Comparison of default, flat shading vs. smooth shading.">

.. only:: html

  .. image:: /tutorial/03_figures/images/thumb/sphx_glr_b_shading_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_b_shading.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Types of Shading</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Texture mapping for a GeoTIFF on a topography surface.">

.. only:: html

  .. image:: /tutorial/03_figures/images/thumb/sphx_glr_c_geological-map_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_c_geological-map.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Geological Map on Topography</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Create a GIF Movie">

.. only:: html

  .. image:: /tutorial/03_figures/images/thumb/sphx_glr_d_gif_thumb.gif
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_d_gif.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Create a GIF Movie</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/03_figures/a_lesson_figures
   /tutorial/03_figures/b_shading
   /tutorial/03_figures/c_geological-map
   /tutorial/03_figures/d_gif

Bonus Content
~~~~~~~~~~~~~



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="VTK 9 introduced Physically Based Rendering (PBR) and we have exposed that functionality in PyVista. Read the blog about PBR for more details.">

.. only:: html

  .. image:: /tutorial/03_figures/bonus/images/thumb/sphx_glr_d_pbr_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_bonus_d_pbr.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Physically Based Rendering</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use string arrays in a point set to label points">

.. only:: html

  .. image:: /tutorial/03_figures/bonus/images/thumb/sphx_glr_e_labels_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_bonus_e_labels.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Label Points</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Orbit around a scene.">

.. only:: html

  .. image:: /tutorial/03_figures/bonus/images/thumb/sphx_glr_g_orbit_thumb.gif
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_bonus_g_orbit.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Orbiting</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>

Do it yourself
~~~~~~~~~~~~~~



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Take a look at the different display options offered by the add_mesh method.">

.. only:: html

  .. image:: /tutorial/03_figures/exercises/images/thumb/sphx_glr_a_display_options_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_exercises_a_display_options.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Display Options</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Control aspects of the rendered mesh&#x27;s lighting such as Ambient, Diffuse, and Specular. These options only work if the lighting argument to add_mesh is True (it&#x27;s True by default).">

.. only:: html

  .. image:: /tutorial/03_figures/exercises/images/thumb/sphx_glr_b_lighting_mesh_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_exercises_b_lighting_mesh.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Lighting Properties</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Eye-Dome Lighting (EDL) is a non-photorealistic, image-based shading technique designed to improve depth perception in scientific visualization images. To learn more, please see `this blog post`_.">

.. only:: html

  .. image:: /tutorial/03_figures/exercises/images/thumb/sphx_glr_c_edl_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_exercises_c_edl.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Eye Dome Lighting</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>

Solutions
~~~~~~~~~



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Take a look at the different display options offered by the add_mesh method.">

.. only:: html

  .. image:: /tutorial/03_figures/solutions/images/thumb/sphx_glr_a_display_options_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_solutions_a_display_options.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Display Options</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Control aspects of the rendered mesh&#x27;s lighting such as Ambient, Diffuse, and Specular. These options only work if the lighting argument to add_mesh is True (it&#x27;s True by default).">

.. only:: html

  .. image:: /tutorial/03_figures/solutions/images/thumb/sphx_glr_b_lighting_mesh_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_solutions_b_lighting_mesh.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Lighting Properties</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Eye-Dome Lighting (EDL) is a non-photorealistic, image-based shading technique designed to improve depth perception in scientific visualization images. To learn more, please see `this blog post`_.">

.. only:: html

  .. image:: /tutorial/03_figures/solutions/images/thumb/sphx_glr_c_edl_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_03_figures_solutions_c_edl.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Eye Dome Lighting</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:
   :includehidden:


   /tutorial/03_figures//bonus/index.rst
   /tutorial/03_figures//exercises/index.rst
   /tutorial/03_figures//solutions/index.rst



.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
