:orphan:

.. _widgets:

Widgets in PyVista
==================

PyVista has several widgets that can be added to the rendering scene to control
filters like clipping, slicing, and thresholding - specifically there are
widgets to control the positions of boxes, planes, and lines or slider bars
which can all be highly customized through the use of custom callback
functions.

Here we’ll take a look at the various widgets, some helper methods that
leverage those widgets to do common tasks, and demonstrate how to leverage the
widgets for user defined tasks and processing routines.

.. tip::

    This section of the tutorial was adopted from the `widgets section
    <https://docs.pyvista.org/examples/index.html?highlight=widgets#widgets>`_
    of the PyVista example documentation.


Widget Examples
---------------

.. leave blank after this point for Sphinx-Gallery to populate examples



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The box widget can be enabled and disabled by the pyvista.Plotter.add_box_widget and pyvista.Plotter.clear_box_widgets methods respectively. When enabling the box widget, you must provide a custom callback function otherwise the box would appear and do nothing - the callback functions are what allow us to leverage the widget to perform a task like clipping/cropping.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_a_box-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_a_box-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Box Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a checkbox to turn on/off the visibility of meshes in a scene.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_b_checkbox-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_b_checkbox-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Checkbox Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The line widget can be enabled and disabled by the pyvista.Plotter.add_line_widget and pyvista.Plotter.clear_line_widgets methods respectively. Unfortunately, PyVista does not have any helper methods to utilize this widget, so it is necessary to pass a custom callback method.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_c_line-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_c_line-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Line Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Use a class based callback to track multiple slider widgets for updating a single mesh.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_d_multi-slider-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_d_multi-slider-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Multiple Slider Widgets</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The plane widget can be enabled and disabled by the pyvista.Plotter.add_plane_widget and pyvista.Plotter.clear_plane_widgets methods respectively. As with all widgets, you must provide a custom callback method to utilize that plane. Considering that planes are most commonly used for clipping and slicing meshes, we have included two helper methods for doing those tasks!">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_e_plane-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_e_plane-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Plane Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The slider widget can be enabled and disabled by the pyvista.Plotter.add_slider_widget and pyvista.Plotter.clear_slider_widgets methods respectively. This is one of the most versatile widgets as it can control a value that can be used for just about anything.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_f_slider-bar-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_f_slider-bar-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Slider Bar Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="The sphere widget can be enabled and disabled by the pyvista.Plotter.add_sphere_widget and pyvista.Plotter.clear_sphere_widgets methods respectively. This is a very versatile widget as it can control vertex location that can be used to control or update the location of just about anything.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_g_sphere-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_g_sphere-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Sphere Widget</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" A spline widget can be enabled and disabled by the pyvista.Plotter.add_spline_widget and pyvista.Plotter.clear_spline_widgets methods respectively. This widget allows users to interactively create a poly line (spline) through a scene and use that spline.">

.. only:: html

  .. image:: /tutorial/08_widgets/images/thumb/sphx_glr_h_spline-widget_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_08_widgets_h_spline-widget.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Spline Widget</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/08_widgets/a_box-widget
   /tutorial/08_widgets/b_checkbox-widget
   /tutorial/08_widgets/c_line-widget
   /tutorial/08_widgets/d_multi-slider-widget
   /tutorial/08_widgets/e_plane-widget
   /tutorial/08_widgets/f_slider-bar-widget
   /tutorial/08_widgets/g_sphere-widget
   /tutorial/08_widgets/h_spline-widget



.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
