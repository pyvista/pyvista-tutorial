.. _jupyter:

Using PyVista in Jupyter
=========================

PyVista is designed to be used in Jupyter notebooks. This section of the
tutorial will walk you through the basics of using PyVista in Jupyter
notebooks and will be a reference guide for you when configuring PyVista
to work in Jupyter.

.. image:: ../../images/jupyter.png
    :alt: PyVista's Jupyter backend
    :align: center


Trame Jupyter Backend for PyVista
---------------------------------

PyVista has the ability to display fully featured plots within a
Jupyter environment using `Trame <https://kitware.github.io/trame/index.html>`_.
We provide mechanisms to pair PyVista and Trame so that PyVista plotters
can be used in a web context with both server and client-side rendering.

The server-side rendering mode of the Trame backend works by streaming the
current render window to a canvas within Jupyter and then passing any user
actions from the canvas back to the VTK render window (this is done under
the hood by the ``vtkRemoteView`` in ``trame-vtk``.

For example, both sections of code will display an interactive canvas
within Jupyter:

.. code:: python

    import pyvista as pv
    sphere = pv.Sphere()

    # short example
    sphere.plot(jupyter_backend='trame')

    # long example
    plotter = pv.Plotter(notebook=True)
    plotter.add_mesh(sphere)
    plotter.show(jupyter_backend='trame')

For convenience, you can enable ``trame`` with (this is the default):

.. code:: python

    import pyvista as pv
    pv.set_jupyter_backend('trame')


Trame Jupyter Modes
+++++++++++++++++++

The PyVista Trame jupyter backend provides three modes of operation (technically
as three separate backend choices):

* ``'trame'``: Uses a view that can switch between client- and server-rendering modes.
* ``'server'``: Uses a view that is purely server-rendering.
* ``'client'``: Uses a view that is purely client-rendering (generally safe without a virtual frame buffer)

You can choose your backend either by using :func:`set_jupyter_backend() <pyvista.set_jupyter_backend>`
or passing ``jupyter_backend`` on the :func:`show() <pyvista.Plotter.show>` call.

.. code:: python

    import pyvista as pv
    pv.set_jupyter_backend('client')

    pv.Cone().plot()


.. code:: python

    import pyvista as pv
    pv.set_jupyter_backend('trame')

    pl = pv.Plotter()
    pl.add_mesh(pv.Cone())
    pl.show(jupyter_backend='client')


Installation
++++++++++++

Using pip, you can set up your jupyter environment with:

.. code::

    pip install 'jupyterlab' 'pyvista[all]'


Remote JupyterHubs
++++++++++++++++++

When using PyVista in Jupyter that is hosted remotely (docker, cloud JupyterHub,
or otherwise), you will need to pair the Trame backend with either
``jupyter-server-proxy`` or ``trame-jupyter-extension``.

These tools allow us to connect to the Trame web application that embeds PyVista's
render window directly in Jupyter. Without one of these mechanisms, you may see
server connection issues or 404 pages where you expect to see a PyVista Plotter.

Jupyter-Server-Proxy
~~~~~~~~~~~~~~~~~~~~

`Jupyter Server Proxy <https://jupyter-server-proxy.readthedocs.io/en/latest/>`_
lets you access the Trame server hosting the views of the PyVista plotters
alongside your notebook, and provide authenticated web access to them directly
through Jupyter.

.. note::
    In a future version of `wslink <https://github.com/Kitware/wslink>`_
    (the driving mechanism behind Trame's server), we plan to add support such that
    the server can communicate via the
    `Jupyter Comms <https://jupyter-notebook.readthedocs.io/en/stable/comms.html>`_
    to avoid the need for a secondary web server and thus ``jupyter-server-proxy``.

To configure PyVista and Trame to work with ``jupyter-server-proxy`` in a remote
environment, you will need to set some options on the global PyVista theme:

* :py:attr:`pyvista.global_theme.trame.server_proxy_enabled
  <pyvista.themes._TrameConfig.server_proxy_enabled>`
* :py:attr:`pyvista.global_theme.trame.server_proxy_prefix
  <pyvista.themes._TrameConfig.server_proxy_prefix>`

The default for ``server_proxy_prefix`` is ``'/proxy/'`` and this should be sufficient
for most remote Jupyter environment and use within Docker.

This can also be set with an environment variable:

.. code::

    export PYVISTA_TRAME_SERVER_PROXY_PREFIX='/proxy/'


The prefix will need to be modified for JupyterHub deployments.

On MyBinder, the ``JUPYTERHUB_SERVICE_PREFIX`` string often needs to prefix
``'/proxy/'``. This makes it so the prefix includes the users ID in the URL.
In PyVista, we automatically check for the presence of this variable and
prepend it to the ``server_proxy_prefix``.


Trame-Jupyter-Extension
~~~~~~~~~~~~~~~~~~~~~~~

`Trame Jupyter Extension <https://github.com/Kitware/trame-jupyter-extension/>`_
enables the trame server and client to communicate over the existing
`Jupyter Comms <https://jupyter-notebook.readthedocs.io/en/stable/comms.html>`_
infrastructure, instead of creating a separate WebSocket connection.

Using this extension removes the need for a secondary web server and thus
``jupyter-server-proxy``.

Using pip, you can install the extension:

.. code-block:: bash

    pip install trame_jupyter_extension

If using Jupyter Lab 3.x, make sure to install the version 1.x of the extension:

.. code-block:: bash

    pip install "trame_jupyter_extension<2"

Once the extension is installed, you can select whether PyVista will use it by
setting the following flag to ``True`` or ``False``:

* :py:attr:`pyvista.global_theme.trame.jupyter_extension_enabled
  <pyvista.plotting.themes._TrameConfig.jupyter_extension_enabled>`
