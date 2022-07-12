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
   tutorial/09_qt/index

Welcome to the PyVista Tutorial!

Below you'll find the schedule for the tutorial. Each lesson is split up into a
talk and an exercise section where you'll be able to practice what was
demonstrated in the tutorial. These lessons are designed to be highly
interactive, where each lesson page below contains a MyBinder button where you
can run the notebooks in the `MyBinder <https://mybinder.org/>`_ environment.
You can also download notebooks and Python scripts for your local environment.

Questions
~~~~~~~~~

During the tutorial, feel free to ask questions if you don't understand
something or need help getting started. We're here to help!

.. note::
   This tutorial was originally created for SciPy 2022, but we plan on
   maintaining it as it's a great way to learn how to get started with
   PyVista. Once the recording is live, we'll be sure to add a link to the
   recording here for all to see.

   If you have any questions about PyVista after the tutorial, feel free to
   post your questions in |discuss| or |slack|.


Tutorial Schedule
~~~~~~~~~~~~~~~~~

+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| **Lesson**      | **Description**                                                                                                       | **Presenter**     | **Time**   |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`intro`    | Introduction - Using PyVista for 3D Visualization within Python.                                                      | `Alex Kaszynski`_ | 20 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`basic`    | Reading and plotting 3D data using the `pyvista.examples`_ module and external files.                                 | `Alex Kaszynski`_ | 20 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`mesh`     | Learn the basics of the PyVista data types and how to open common 3D file formats to visualize the data in 3D.        | `Bane Sullivan`_  | 25 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`figures`  | Demonstrate many features of the PyVista plotting API to create compelling 3D visualizations and touch on animations. | `Bane Sullivan`_  | 20 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`filters`  | Demonstrate the PyVista filters API to perform mesh analysis and alteration.                                          | `Bane Sullivan`_  | 15 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`action`   | Show how PyVista is already being used within several projects and can be used for all things visualization.          | `Tetsuo Koyama`_  | 15 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`vtk`      | Show how PyVista uses VTK and how you can combine the best of both worlds!                                            | `Bane Sullivan`_  | 20 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`sphinx`   | Leverage PyVista to make some awesome interactive web documentation.                                                  | `Alex Kaszynski`_ | 20 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`widgets`  | Use PyVista with a variety of helpful widgets.                                                                        | `Tetsuo Koyama`_  | 20 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+
| :ref:`qt`       | Demonstrate how to use PyVista to create standalone applications using `pyinstaller`_ and the Qt framework.           | `Alex Kaszynski`_ | 15 minutes |
+-----------------+-----------------------------------------------------------------------------------------------------------------------+-------------------+------------+

.. |discuss| image:: https://img.shields.io/badge/GitHub-Discussions-green?logo=github
   :target: https://github.com/pyvista/pyvista/discussions

.. |slack| image:: https://img.shields.io/badge/Slack-pyvista-green.svg?logo=slack
   :target: http://slack.pyvista.org

.. _Alex Kaszynski: https://github.com/akaszynski
.. _Bane Sullivan: https://banesullivan.com
.. _Tetsuo Koyama: https://github.com/tkoyama010
.. _pyvista.examples: https://docs.pyvista.org/api/examples/_autosummary/pyvista.examples.examples.html#
.. _pyinstaller: https://www.pyinstaller.org/
