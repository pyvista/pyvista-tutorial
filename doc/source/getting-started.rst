.. _getting_started:

Getting Started
===============

The only prerequisite for installing PyVista is Python itself. If you don’t have
Python yet and want the simplest way to get started, we recommend you use the
`Anaconda Distribution`_.

PyVista can be installed locally with :ref:`conda`, with :ref:`pip`. If you'd
prefer it, you can also run PyVista on the cloud using :ref:`colab` or
:ref:`mybinder`. For more detailed instructions, see the installation
guide below.


Installation
------------

PyVista can be installed on several environments, including, but not limited to:

* **Locally**

  * :ref:`pip`
  * :ref:`conda`

* **Cloud**

  * :ref:`colab`
  * :ref:`mybinder`


.. _pip:

pip
~~~

If you're using ``pip``, then installation is just::

   pip install pyvista

.. asciinema:: 507562


.. _conda:

conda
~~~~~

Install PyVista using the `Anaconda Distribution`_::

   conda install -c conda-forge pyvista

.. asciinema:: 507565


.. _Anaconda Distribution: https://www.anaconda.com/


Additional Packages
-------------------

If you prefer working within a Jupyter environment, we recommend you install
the following packages:

.. tabs::

   .. tab:: pip

      .. code::

         pip install jupyterlab trame

   .. tab:: conda

      .. code::

         conda install -c conda-forge jupyterlab trame


You can then plot using Jupyterlab or Jupyter Notebook interactively with one of three backends:

.. tabs::

   .. tab:: ipyvtklink

      .. jupyter-execute::
         :hide-code:

         import pyvista as pv
         pv.set_plot_theme('document')
         pv.global_theme.jupyter_backend = 'static'

      .. jupyter-execute::

         import pyvista as pv
         from pyvista import examples

         dataset = examples.download_lucy()
         dataset.plot(smooth_shading=True, color='white')

   .. tab:: panel

      .. jupyter-execute::

         import pyvista as pv
         from pyvista import examples
         pv.global_theme.jupyter_backend = 'panel'

         dataset = examples.download_lidar()
         dataset.plot(cmap="gist_earth")

   .. tab:: pythreejs

      .. jupyter-execute::

         import pyvista as pv
         from pyvista import examples
         pv.global_theme.jupyter_backend = 'pythreejs'
         pv.global_theme.window_size = (700, 300)
         pv.global_theme.anti_aliasing = 'fxaa'

         dataset = examples.download_cad_model()
         dataset.plot(background='w', pbr=True, metallic=0.6, roughness=0.4, split_sharp_edges=True)


.. _colab:

Google Colab
------------
Google Colab is a moving target and many of the "cloud ready" JavaScript
plotting environments that make PyVista so great to work with do not seem to be
available on Google Colab. However, we still have a working PyVista example for
`Google Colab <https://colab.research.google.com/>`_ with static plotting.

Visit the `PyVista on Colab  <https://colab.research.google.com/drive/15REd98bznqMGYVWxffpayfOOIwZ1s4Or?usp=sharing>`_ notebook to see PyVista in action. The minimum code to get PyVista running in a Colab environment is:

.. code::

   !apt-get install -qq xvfb libgl1-mesa-glx
   !pip install pyvista -qq

.. code:: python

   import pyvista

   pyvista.global_theme.jupyter_backend = 'static'
   pyvista.global_theme.notebook = True
   pyvista.start_xvfb()

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
