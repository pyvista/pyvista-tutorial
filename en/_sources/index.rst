PyVista Tutorial
================

.. toctree::
   :maxdepth: 2
   :hidden:

   getting-started
   tutorial

Welcome to PyVista's tutorial!

Here you can find all the resources to be up and running with PyVista in no
time. Feel free to reference our dedicated documentation at `PyVista
Documentation <https://docs.pyvista.org/>`_

.. tab-set::

   .. tab-item:: JupyterLab

      Here's a quick demo of PyVista running within `Jupyterlab
      <https://jupyter.org/>`_.

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_jupyterlab_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

   .. tab-item:: IPython

      Here's a quick demo of PyVista running within a terminal using `IPython
      <https://ipython.org/>`_.

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_ipython_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>


Quick Links
-----------

.. grid:: 2

   .. grid-item-card:: Tutorial
      :class-title: pyvista-card-title
      :link: tutorial
      :link-type: ref

      Jump right to the tutorial content.

      .. pyvista-plot::

         from pyvista import examples
         dataset = examples.download_saddle_surface()
         dataset.plot()

   .. grid-item-card:: Installation and Getting Started
      :class-title: pyvista-card-title
      :link: getting_started
      :link-type: ref

      Get PyVista setup on your environment.

      .. asciinema:: 507562


Example Gallery
---------------

Click below for our extensive example gallery!

.. image:: _static/pyvista_banner.png
   :target: http://docs.pyvista.org/examples/index.html


PyVista Overview
----------------

`PyVista <https://github.com/pyvista/pyvista>`_ is a general purpose 3D visualization library used for over 500+ open source projects and many closed source projects for the visualization of everything from `computer aided engineering and geophysics to volcanoes and digital artwork <https://dev.pyvista.org/getting-started/external_examples.html>`_.

PyVista exposes a Pythonic API to the `Visualization Toolkit (VTK) <http://www.vtk.org>`_ to provide tooling that is immediately usable without any prior knowledge of VTK and is being built as the 3D equivalent of `Matplotlib <https://matplotlib.org/>`_, with plugins to `Jupyter <https://jupyter.org/>`_ to enable visualization of 3D data using both server and client-side rendering.

We will provide a hands-on tutorial accessible to anyone with internet access and a computer via many of PyVista's existing `example Jupyter notebooks <https://docs.pyvista.org/examples/index.html>`_ and new material through a comprehensive overview highlighting popular 3D visualization use cases.


Tutorial Description
--------------------

- Use PyVista to create 3D visualizations from a variety of datasets in common
  formats.
- Overview the classes and data structures of PyVista with real-world examples.
- Be familiar with the various filters and features of PyVista.
- Know which Python libraries are used and can be used by PyVista (meshio,
  trimesh etc).

We see this tutorial catering to anyone who wants to visualize data in any
domain, and this ranges from basic Python users to advanced power users.

1. Basic knowledge of Python to get started. Be able to install Jupyter Lab on
   your machine and be up and running.
2. Intermediate users will want to be familiar with `NumPy
   <https://numpy.org/>`_ and other libraries that are compatible with PyVista,
   like `trimesh <https://trimsh.org/examples.html>`_ or `meshio
   <https://github.com/nschloe/meshio>`_.
3. Advanced users should be familiar with the Visualization Toolkit (VTK), general
   data science, and GUI frameworks like Qt.


Instructor Bios
---------------

Alexander Kaszynski
~~~~~~~~~~~~~~~~~~~

`Alex Kaszynski <https://github.com/akaszynski/resume>`_, co-creator of PyVista
and creator of the `PyAnsys <https://github.com/pyansys>`_ organization.

Advocate for all things open source and has contributed to the creation of
Ansys's open source projects at `Ansys <https://ansys.github.io/>`_ and
`PyMAPDL <https://https://github.com/pyansys/pymapdl>`_. Enjoys presenting and
demoing Python, especially 3D visualization but also its application to CAE and
automation.

Bane Sullivan
~~~~~~~~~~~~~

`Bane Sullivan <https://banesullivan.com>`_, co-creator of PyVista, is a Research Software Engineer working at the intersection of geoscience, visualization, and data science.

Bane is a geophysicist/hydrologist by training and has been working to grow PyVista's adoption within the subsurface geoscience communities, previously presenting PyVista at `Transform 2021 <https://www.youtube.com/watch?v=FmNmRBsEBHE>`_.

Tetsuo Koyama
~~~~~~~~~~~~~

`Tetsuo Koyama <https://github.com/tkoyama010>`_ is interested in scientific computing and visualization with computer graphics.
Developer team member of PyVista.
Past experience as a speaker:

- `PyConJP 2019 speaker "Introduction to FEM Analysis with Python" <https://youtu.be/6JuB1GiDLQQ>`_
- `PyConJP 2020 speaker "How to plot unstructured mesh file on Jupyter Notebook" <https://youtu.be/X3Z54Kw4I6Y>`_
- `SciPy Japan 2020 speaker "Translation Project of Mayavi2 documents" <https://youtu.be/epxm9SjLMS0>`_
- `PyConJP 2021 speaker "Visualize 3D scientific data in a Pythonic way like Matplotlib" <https://youtu.be/ru-nENLgleo>`_

Bill Little
~~~~~~~~~~~

`Bill Little <https://github.com/bjlittle>`_, creator of `GeoVista <https://github.com/bjlittle/geovista>`_, is a software engineer working at the `UK Met Office <https://www.metoffice.gov.uk>`_ and a core developer on `SciTools <https://github.com/orgs/SciTools/repositories>`_, which includes `Cartopy <https://github.com/SciTools/cartopy>`_ and `Iris <https://github.com/SciTools/iris>`_.

Tutorial Prerequisites
----------------------

We see this tutorial catering to anyone who wants to visualize data in any
domain, and this ranges from basic Python users to advanced power users.  In
fact, our tutorial instructors and community members are involved in any
domain.

1. Basic knowledge of Python to get started. Be able to install Jupyter Lab on
   your machine and be up and running.
2. Intermediate users will want to be familiar with `NumPy
   <https://numpy.org/>`_ and other libraries that are compatible with PyVista,
   like `trimesh <https://trimsh.org/examples.html>`_ or `meshio
   <https://github.com/nschloe/meshio>`_.
3. Advanced users will be familiar with GUI frameworks like Qt, VTK, and
   advanced data science.
