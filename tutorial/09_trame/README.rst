.. _trame:

Trame
=====

`Kitware's Trame <https://kitware.github.io/trame/index.html>`_ is an open-source platform for creating interactive and powerful visual analytics applications. Based on Python, and leveraging platforms such as VTK, ParaView, and Vega, it is possible to create web-based applications in minutes.

.. raw:: html

    <iframe src="https://player.vimeo.com/video/764741737?h=bd3c37ebfb&muted=1" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>


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

        import pyvista as pv
        from pyvista import examples
        from pyvista.trame.ui import plotter_ui
        from trame.app import get_server
        from trame.ui.vuetify3 import SinglePageLayout

        # Always set PyVista to plot off screen with Trame
        pv.OFF_SCREEN = True

        server = get_server()
        state, ctrl = server.state, server.controller

        mesh = examples.load_random_hills()

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


Trame applications
~~~~~~~~~~~~~~~~~~

Using an existing app

.. code:: python

    from trame.app.demo import Cone

    app = Cone("demo")
    await app.ui.ready
    app.ui


Try Pan3D: ``pip install pan3d``

.. code:: python

    from pan3d import DatasetBuilder

    builder = DatasetBuilder(viewer=True)

    builder.import_config('example_sst_xarray.json')

    # Show viewer in cell output
    await builder.viewer.ready
    builder.viewer.ui


Exercises
~~~~~~~~~

Do not run these examples in Jupyter but rather as standalone scripts.
