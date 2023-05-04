.. _tutorial:

PyVista Tutorial
================

.. toctree::
   :maxdepth: 2
   :caption: Lessons
   :hidden:

   tutorial/00_intro/index
   tutorial/01_basic/index
   tutorial/02_mesh/index
   tutorial/03_figures/index
   tutorial/04_filters/index
   tutorial/05_action/index
   tutorial/06_vtk/index
   tutorial/07_sphinx/index
   tutorial/08_widgets/index

Welcome to the PyVista Tutorial!

Below you'll find the schedule for the tutorial. Each lesson is split up into a
talk and an exercise section where you'll be able to practice what was
demonstrated in the tutorial. These lessons are designed to be highly
interactive, where each lesson page below contains a MyBinder button where you
can run the notebooks in the `MyBinder <https://mybinder.org/>`_ environment.
You can also download notebooks and Python scripts for your local environment.

.. button-link:: https://github.com/pyvista/pyvista-tutorial/raw/gh-pages/notebooks.zip
   :color: primary
   :shadow:

   Download the Tutorial's Jupyter Notebooks


Questions
~~~~~~~~~

If you have any questions about PyVista, feel free to post your questions in
|discuss| or |slack|.


Tutorial Overview
~~~~~~~~~~~~~~~~~

+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| **Lesson**      | **Description**                                                                                                       |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`intro`    | Introduction - Using PyVista for 3D Visualization within Python.                                                      |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`basic`    | Reading and plotting 3D data using the `pyvista.examples`_ module and external files.                                 |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`mesh`     | Learn the basics of the PyVista data types and how to open common 3D file formats to visualize the data in 3D.        |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`figures`  | Demonstrate many features of the PyVista plotting API to create compelling 3D visualizations and touch on animations. |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`filters`  | Demonstrate the PyVista filters API to perform mesh analysis and alteration.                                          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`action`   | Show how PyVista is already being used within several projects and can be used for all things visualization.          |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`vtk`      | Show how PyVista uses VTK and how you can combine the best of both worlds!                                            |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`sphinx`   | Leverage PyVista to make some awesome interactive web documentation.                                                  |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`widgets`  | Use PyVista with a variety of helpful widgets.                                                                        |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| :ref:`qt`       | Demonstrate how to use PyVista to create standalone applications using `pyinstaller`_ and the Qt framework.           |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+

.. |discuss| image:: https://img.shields.io/badge/GitHub-Discussions-green?logo=github
   :target: https://github.com/pyvista/pyvista/discussions

.. |slack| image:: https://img.shields.io/badge/Slack-pyvista-green.svg?logo=slack
   :target: http://slack.pyvista.org

.. _Alex Kaszynski: https://github.com/akaszynski
.. _Bane Sullivan: https://banesullivan.com
.. _Tetsuo Koyama: https://github.com/tkoyama010
.. _pyvista.examples: https://docs.pyvista.org/api/examples/_autosummary/pyvista.examples.examples.html#
.. _pyinstaller: https://www.pyinstaller.org/
