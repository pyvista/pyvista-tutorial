.. _sphinx:

PyVista and Sphinx
==================

Leverage PyVista to make some awesome web documentation.

.. tip::

    This section of the tutorial was adopted from `Plotting Themes
    <https://docs.pyvista.org/user-guide/themes.html>`_ and `Sphinx PyVista
    Plot Directive <https://docs.pyvista.org/extras/plot_directive.html>`_
    chapter of the PyVista documentation.

Generating 3D Plots in your Documentation
-----------------------------------------
PyVista allows you to generate images directly within Sphinx
much like the `Matplotlib plot_directive
<https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html>`_. Rather
than manually creating and adding plots after code sections, you can instead
dynamically generate images and embed them directly within your
documentation. This also works seamlessly with `sphinx-gallery
<https://sphinx-gallery.github.io/>`_, so you can create notebook examples just
like the `Matplotlib Example Gallery
<https://matplotlib.org/stable/gallery/index.html>`_.

As an added side benefit, you can be sure that the documentation you generate
matches your project API. If you include this within a `GitHub Workflow
<https://docs.github.com/en/actions/using-workflows/about-workflows>`_

This section covers the following topics.

- :ref:`static_plots`

.. _static_plots:

Static Plotting - Sphinx PyVista Plot Directive
-----------------------------------------------
You can generate static images of PyVista plots within sphinx using the
``pyvista-plot`` directive by adding the following to your ``conf.py``
when building your documentation using Sphinx.

.. code:: python

   extensions = [
       "sphinx.ext.napoleon",
       "pyvista.ext.plot_directive",
   ]

You can then issue the plotting directive within your sphinx
documentation files::

   .. pyvista-plot::
      :caption: A sphere
      :include-source: True

      >>> import pyvista
      >>> sphere = pyvista.Sphere()
      >>> out = sphere.plot()

Which will be rendered as:

.. pyvista-plot::
   :caption: This is a default sphere
   :include-source: True

   >>> import pyvista
   >>> sphere = pyvista.Sphere()
   >>> out = sphere.plot()


Examples and Usage
~~~~~~~~~~~~~~~~~~
There are two ways to use `trame <https://github.com/Kitware/trame>`_ within
Jupyter notebooks.  You can use it on a plot by plot basis by setting the
``jupyter_backend`` in ``mesh.plot()``::

   .. pyvista-plot::

       import pyvista as pv
       from pyvista import examples

       # create a point cloud from lidar data and add height scalars
       dataset = examples.download_lidar()
       point_cloud = pv.PolyData(dataset.points[::100])
       point_cloud['height'] = point_cloud.points[:, 2]
       point_cloud.plot(window_size=[500, 500],
                        cmap='jet',
                        point_size=2,
                        background='w')

And here's the resulting output in Sphinx:

.. pyvista-plot::

    import pyvista as pv
    from pyvista import examples

    # create a point cloud from lidar data and add height scalars
    dataset = examples.download_lidar()
    point_cloud = pv.PolyData(dataset.points[::100])
    point_cloud['height'] = point_cloud.points[:, 2]
    point_cloud.plot(window_size=[500, 500],
                     cmap='jet',
                     point_size=2,
                     background='w')

|

And now just directly execute ``plot`` on any dataset::

   .. pyvista-plot::

      from pyvista import examples
      dataset = examples.download_dragon()
      dataset.plot(cpos="xy")

Which looks like:

.. pyvista-plot::

   from pyvista import examples
   dataset = examples.download_dragon()
   dataset.plot(cpos="xy")


Exercises
---------

Generate Sphinx documentation on your own using the
`pyvista/pyvista-doc-example <https://github.com/pyvista/pyvista-doc-example>`_
repository. Either clone the repository with::

  git clone https://github.com/pyvista/pyvista-doc-example

Or just download the zip of the repository.

.. button-link:: https://github.com/pyvista/pyvista-doc-example/archive/refs/heads/main.zip
    :color: primary
    :shadow:

    pyvista-doc-example-main.zip


Build the documentation
~~~~~~~~~~~~~~~~~~~~~~~

Once you've downloaded `pyvista/pyvista-doc-example
<https://github.com/pyvista/pyvista-doc-example>`_, cd into the directory and
install the documentation build requirements with::

  cd pyvista-doc-example
  pip install -r requirements_docs.txt

Finally, build the documentation locally with::

  cd doc
  make html

Or, if on Windows::

  cd doc
  make.bat

You will then find the generated documentation within the ``doc/_build``
directory. Open up ``index.html`` using your browser to see the documentation.
