# PyVista Tutorial

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Abstract


[PyVista](https://github.com/pyvista/pyvista) is a general purpose 3D visualization library used for over 500+ open source projects and many closed source projects for the visualization of everything from [computer aided engineering and geophysics to volcanoes and digital artwork](https://dev.pyvista.org/getting-started/external_examples.html).

PyVista exposes a Pythonic API to the [Visualization Toolkit (VTK)](http://www.vtk.org) to provide tooling that is immediately usable without any prior knowledge of VTK and is being built as the 3D equivalent of [matplotlib](https://matplotlib.org/), with plugins to [Jupyter](https://jupyter.org/) to enable visualization of 3D data using both server and client-side rendering.

We will provide a hands-on tutorial accessible to anyone with internet access and a computer via many of PyVista's existing [example Jupyter notebooks](https://docs.pyvista.org/examples/index.html) and new material through a comprehensive overview highlighting popular 3D visualization use cases.



## Keywords

[visualization](https://github.com/topics/visualization)
[meshviewer](https://github.com/topics/meshviewer)
[vtk](https://github.com/topics/vtk)
[3d](https://github.com/topics/3d)

## Other Information and Files
See our examples at [PyVista Examples](http://docs.pyvista.org/examples/index.html)

### Tutorial Description.

- Use PyVista to create 3D visualizations from a variety of datasets in common formats.
- Overview the classes and data structures of PyVista with real-world examples.
- Be familiar of the various filters and features of PyVista.
- Know which Python libraries are used and can be used by PyVista (meshio, trimesh etc).

We see this tutorial catering to anyone who wants to visualize data in any domain, and this ranges from basic Python users to advanced power users.

1. Basic knowledge of Python to get started. Be able to install Jupyter Lab on your machine and be up and running.
2. Intermediate users will want to be familiar with [NumPy](https://numpy.org/) and other libraries that are compatible with PyVista, like [trimesh](https://trimsh.org/examples.html) or [meshio](https://github.com/nschloe/meshio).
3. Advanced users should be familiar the Visualization Toolkit (VTK), general data science, and GUI frameworks like Qt.

### Tutorial Outline.

0. Getting Started (Alexander Kaszynski) - PyVista for 3D Visualization within Python. (10 min for talk, 10 min for exercise)

1. Basic usage (Alexander Kaszynski) - Reading and plotting 3D data using ``examples`` module and external files.  (10 min for talk, 10 min for exercise)

2. What is a Mesh? (Bane Sullivan) - Learn the basics of the PyVista data types and how to open common 3D file formats to visualize the data in 3D (15 min for talk, 10 min for exercise)

3. Plotting Options and Animations (Bane Sullivan) - Demonstrate many features of the PyVista plotting API to create compelling 3D visualizations and touch on animations (10 min for talk, 10 min for exercise)

4. PyVista in Action (Tetsuo Koyama) - Show how PyVista is already being used within several projects and can be used for all things visualization. (15 min for talk)

5. Break. Stretch fingers and grab some coffee. (15 minutes)

6. PyVista Data Model (Bane Sullivan) - Learn about PyVista's data model in further detail. (15 min for talk, 10 min for exercise)

7. PyVista & VTK (Bane Sullivan) - Show how PyVista uses VTK and how you can combine the best of both worlds! (10 minutes for talk, 10 minutes for exercise)

8. Quick break. Prepare for the final run. (10 minutes)

9. PyVista & Sphinx (Alexander Kaszynski) - Leverage PyVista to make some awesome interactive web documentation. (20 min for talk, 10 min for exercise)

10. PyVista & Qt (Tetsuo Koyama) - Demonstrate how to use PyVista to create standalone applications using pyinstaller and the Qt framework. (15 min for talk, 10 for exercise)

11. Open up to Questions. (15 minutes)


### Additional Tutorial Information.

We will base the material for the tutorial on [the examples in PyVista's online documentation](https://docs.pyvista.org/examples/index.html).
[Transform 2021: Guide to PyVista Tutorial](https://github.com/banesullivan/transform-2021) will also be used as material.
The tutorial itself will be in the [pyvista/pyvista-tutorial](https://github.com/pyvista/pyvista-tutorial) repository.

### Tutorial Prerequisites.

We see this tutorial catering to anyone who wants to visualize data in any domain, and this ranges from basic Python users to advanced power users.
In fact, our tutorial instructors and community members are involved in any domain.

1. Basic knowledge of Python to get started. Be able to install Jupyter Lab on your machine and be up and running.
2. Intermediate users will want to be familiar with [NumPy](https://numpy.org/) and other libraries that are compatible with PyVista, like  [trimesh](https://trimsh.org/examples.html) or [meshio](https://github.com/nschloe/meshio).
3. Advanced users will be familiar with GUI frameworks like Qt, VTK, and advanced data science.

## Appropriate level of the attendees' Python knowledge.

Something for everyone!

- [x] Beginner
- [x] Intermediate
- [x] Advanced

## Instructor Bio(s).

### [Alexander Kaszynski](https://github.com/akaszynski)

[Alex Kaszynski](https://github.com/akaszynski/resume), co-creator of [PyVista](https://github.com/pyvista/) and creator of the [PyAnsys](https://github.com/pyansys) organization.

Advocate for all things Python with extensive experience presenting as a speaker at IGTI conferences for the past decade, and for the past almost three at Ansys pushing for automation through Python for CAE applications.

Regularly present Python demos within [Ansys](https://ansys.github.io/), including talks with 500+ "live" virtual attendees, and prior to COVID, in person talks of 100+. Enjoys presenting and demoing Python, especially 3D visualization but also its application to CAE and automation.

### [Bane Sullivan](https://github.com/banesullivan)

[Bane Sullivan](https://banesullivan.com), co-creator of [PyVista](https://github.com/pyvista/), is a Research Software Engineer working at the intersection of geoscience, visualization, and data science.

Bane is a geophysicist/hydrologist by training and has been working to grow PyVista's adoption within the subsurface geoscience communities, previously presenting PyVista at [Transform 2021](https://www.youtube.com/watch?v=FmNmRBsEBHE).

### [Tetsuo Koyama](https://github.com/tkoyama010)

Interested in scientific computing and visualization with computer graphics.
Developer team member of PyVista.
Past experience as a speaker:
- [PyConJP 2019 speaker "Introduction to FEM Analysis with Python"](https://youtu.be/6JuB1GiDLQQ)
- [PyConJP 2020 speaker "How to plot unstructured mesh file on Jupyter Notebook"](https://youtu.be/X3Z54Kw4I6Y)
- [SciPy Japan 2020 speaker "Translation Project of Mayavi2 documents"](https://youtu.be/epxm9SjLMS0)
- [PyConJP 2021 speaker "Visualize 3D scientific data in a Pythonic way like matplotlib"](https://youtu.be/ru-nENLgleo)



## Paper.

[![DOI](https://joss.theoj.org/papers/10.21105/joss.01450/status.svg)](https://doi.org/10.21105/joss.01450)
