.. _getting_started:

Getting Started
===============

The only prerequisite for installing PyVista is Python itself. If you don't have
Python yet and want the simplest way to get started, we recommend you use the
`Anaconda Distribution`_.

.. _Anaconda Distribution: https://www.anaconda.com/

PyVista can be installed locally with conda or pip. If you'd
prefer it, you can also run PyVista on the cloud using :ref:`colab` or
:ref:`mybinder`. For more detailed instructions, see the installation
guide below.


Installation
------------

PyVista can be installed on several environments, including, but not limited to:

.. tab-set::

   .. tab-item:: pip

      .. code::

         pip install 'pyvista[all,trame]' jupyterlab

   .. tab-item:: conda

      .. code::

         conda install -c conda-forge pyvista jupyterlab trame trame-vuetify trame-vtk ipywidgets




You can then plot in Jupyter with either a static or interactive backend:

   .. pyvista-plot::

      import pyvista as pv
      from pyvista import examples

      dataset = examples.download_lucy()
      dataset.plot(smooth_shading=True, color='white')


.. _mybinder:

MyBinder
--------
MyBinder, similar to Google Colab, allows you to run Jupyter notebooks on the
cloud. Click on the link below to open up a MyBinder environment to run
PyVista.

|binder|

.. |binder| image:: https://static.mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks
   :alt: Launch on Binder


.. _colab:

Google Colab
------------
Google Colab is a moving target and many of the "cloud ready" JavaScript
plotting environments that make PyVista so great to work with do not seem to be
available on Google Colab. However, we still have a working PyVista example for
`Google Colab <https://colab.research.google.com/>`_ with static plotting.

Visit the `PyVista on Colab  <https://colab.research.google.com/drive/1y0yURyB-5ApO3zM0vsSK7OaobxjncI3h?usp=sharing>`_ notebook to see PyVista in action. The minimum code to get PyVista running in a Colab environment is:

.. code::

   !apt-get install -qq xvfb libgl1-mesa-glx
   !pip install pyvista -qq

.. code:: python

   import pyvista

   pyvista.set_jupyter_backend('static')
   pyvista.global_theme.notebook = True
   pyvista.start_xvfb()
