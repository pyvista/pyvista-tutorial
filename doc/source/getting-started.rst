.. _getting_started:

Getting Started
===============

The only prerequisite for installing PyVista is Python itself. If you don’t have
Python yet and want the simplest way to get started, we recommend you use the
`Anaconda Distribution`_.

PyVista can be installed with :ref:`conda`, with :ref:`pip`, run on the cloud
using Google Colab or MyBinder. For more detailed instructions, see the Python
installation guide below.

Installation
------------

PyVista can be installed on several enviornments, including, but not limited to:

* **Locally**

  * :ref:`pip`
  * :ref:`conda`

* **Cloud**

  * Google Colab
  * |binder|

.. |binder| image:: https://static.mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/pyvista/pyvista-examples/master
   :alt: Launch on Binder


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

         pip install jupyterlab pythreejs ipyvtklink panel

   .. tab:: conda

      .. code::

         conda install -c conda-forge jupyterlab pythreejs ipyvtklink panel


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
         pv.global_theme.jupyter_backend = 'pythreejs'
         pv.global_theme.window_size = (700, 300)
         pv.global_theme.antialiasing = True

         dataset = examples.download_cad_model()
         dataset.plot(background='w', pbr=True, metallic=0.6, roughness=0.4, split_sharp_edges=True)
