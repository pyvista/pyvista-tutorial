:orphan:

.. _trame:

PyVista and Trame
=================

`Kitware's Trame <https://kitware.github.io/trame/index.html>`_ is an open-source platform for creating interactive and powerful visual analytics applications. Based on Python, and leveraging platforms such as VTK, ParaView, and Vega, it is possible to create web-based applications in minutes.

.. raw:: html

    <iframe src="https://player.vimeo.com/video/764741737?muted=1" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>


What is Trame?
--------------

Trame is a Python framework for building reactive web applications.

* All the logic and UI definition can be done in plain Python
* Runs on laptops, desktops, clusters, and the cloud while displaying everywhere (phone, tablet, laptop, workstation)


.. tab-set::

   .. tab-item:: Documentation

        Learn more about Trame

        .. button-link:: https://kitware.github.io/trame/
            :color: primary
            :shadow:

            Trame Documentation


   .. tab-item:: Tutorial

        Gain hands on experience with Trame through the tutorial.


        .. button-link:: https://github.com/Kitware/trame-tutorial
            :color: primary
            :shadow:

            Trame Tutorial


3D visualization in web applications
------------------------------------

PyVista and Trame work excellently together to provide a cutting-edge capabilities for 3D
visualization in reactive web applications.

1. Trame provides a high-level framework for building reactive, stateful web applications
2. PyVista provides a high-level framework for 3D visualization, exposing VTK in a “Pythonic” manner

High-level framework 1 + high-level framework 2 = a streamlined approach to making powerful web applications with 3D visualization front and center.

The following code creates a simple Trame application with a PyVista plotter embedded in the UI.
This code can be used as a base for building all of your Trame applications with PyVista as it
contains all of the boilerplate code needed to get started.


.. tab-set::

   .. tab-item:: Code

      .. code:: python

        from trame.app import get_server
        from trame.ui.vuetify import SinglePageLayout

        import pyvista as pv
        from pyvista.trame.ui import plotter_ui

        # Always set PyVista to plot off screen with Trame
        pv.OFF_SCREEN = True

        server = get_server()
        state, ctrl = server.state, server.controller

        mesh = pv.Wavelet()

        pl = pv.Plotter()
        pl.add_mesh(mesh)

        with SinglePageLayout(server) as layout:
            with layout.content:
                # Use PyVista's Trame UI helper method
                #  this will add UI controls
                view = plotter_ui(pl)

        server.start()

   .. tab-item:: Web App

      .. image:: ../../images/trame-pyvista.png
          :alt: A simple Trame application with PyVista
          :align: center


.. note::

    PyVista's Jupyter backend is powered by Trame! If you've been using
    PyVista in Jupyter lately, you've been using Trame all along -- our
    Jupyter backend is a micro Trame application.


Exercises
~~~~~~~~~

Do not run these examples in Jupyter but rather as standalone scripts.



.. raw:: html

    <div class="sphx-glr-thumbnails">


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="A simple example of how to create a Trame app with a PyVista Plotter.">

.. only:: html

  .. image:: /tutorial/09_trame/images/thumb/sphx_glr_a_trame_simple_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_09_trame_a_trame_simple.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Simple Trame App</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extending our simple example to have a dropdown menu to control the color of the actor.">

.. only:: html

  .. image:: /tutorial/09_trame/images/thumb/sphx_glr_b_trame_actor_color_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_09_trame_b_trame_actor_color.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Control the Color of an Actor</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extending our simple example to have a dropdown menu to control which scalar array is used to c...">

.. only:: html

  .. image:: /tutorial/09_trame/images/thumb/sphx_glr_c_trame_scalars_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_09_trame_c_trame_scalars.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Control Scalar Array</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Extending our simple example to control the color limits of the mapped scalars.">

.. only:: html

  .. image:: /tutorial/09_trame/images/thumb/sphx_glr_d_trame_scalar_range_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_09_trame_d_trame_scalar_range.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Control Scalar Range</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This example demonstrates how to use VTK, PyVista, and Trame together to show how the three lib...">

.. only:: html

  .. image:: /tutorial/09_trame/images/thumb/sphx_glr_e_trame_algorithm_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_09_trame_e_trame_algorithm.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Using VTK, PyVista, and Trame</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="An example of opening a mesh file from the browser and viewing it with PyVista.">

.. only:: html

  .. image:: /tutorial/09_trame/images/thumb/sphx_glr_f_trame_open_file_thumb.png
    :alt:

  :ref:`sphx_glr_tutorial_09_trame_f_trame_open_file.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Open Mesh File</div>
    </div>


.. raw:: html

    </div>


.. toctree::
   :hidden:

   /tutorial/09_trame/a_trame_simple
   /tutorial/09_trame/b_trame_actor_color
   /tutorial/09_trame/c_trame_scalars
   /tutorial/09_trame/d_trame_scalar_range
   /tutorial/09_trame/e_trame_algorithm
   /tutorial/09_trame/f_trame_open_file



.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
