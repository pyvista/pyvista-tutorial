.. _sphinx:

PyVista and Sphinx
==================

Leverage PyVista to make some awesome interactive web documentation. (20 min
for talk, 10 min for exercise)

.. tip::

    This section of the tutorial was adopted from `Plotting Themes
    <https://docs.pyvista.org/user-guide/themes.html>`_ and `Sphinx PyVista
    Plot Directive <https://docs.pyvista.org/extras/plot_directive.html>`_
    chapter of the PyVista documentation.


Sphinx PyVista Plot Directive
=============================
You can generate static images of pyvista plots using the
``.. pyvista-plot::`` directive by adding the following to your
``conf.py`` when building your documentation using Sphinx.

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


State of Backends of PyVista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+--------------------+---------+----------------------+
|               | Rendering Location | Backend | Requires Framebuffer |
+---------------+--------------------+---------+----------------------+
| panel         | Client             | vtk.js  | Yes                  |
+---------------+--------------------+---------+----------------------+
| pythreejs     | Client             | threejs | No                   |
+---------------+--------------------+---------+----------------------+
| ipygany       | Client             | threejs | No                   |
+---------------+--------------------+---------+----------------------+
| ipyvtklink    | Server             | vtk     | Yes                  |
+---------------+--------------------+---------+----------------------+
| itkwidgets    | Client             | vtk.js  | Yes                  |
+---------------+--------------------+---------+----------------------+

Exercises
---------

