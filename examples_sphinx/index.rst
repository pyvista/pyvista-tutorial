.. examples_sphinx documentation master file, created by
   sphinx-quickstart on Sat Jun 25 06:36:57 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx PyVista Plot Directive
=============================

.. pyvista-plot::
   :caption: This is a default sphere
   :include-source: True

   >>> import pyvista
   >>> pyvista.set_plot_theme("document")
   >>> import pyvista
   >>> sphere = pyvista.Sphere()
   >>> out = sphere.plot()

.. pyvista-plot::

   >>> import pyvista
   >>> sphere = pyvista.Sphere()
   >>> out = sphere.plot()

.. pyvista-plot:: plot.py

.. pyvista-plot:: plot.py

   The plot's caption.

.. pyvista-plot:: plot.py plot_function1

