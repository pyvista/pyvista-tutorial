# 3D Visualization with PyVista

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks/tutorial/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Abstract

[PyVista](https://github.com/pyvista/pyvista) is a general purpose 3D visualization library used for over 1400+ open source projects and many closed source projects for the visualization of everything from [computer aided engineering and geophysics to volcanoes and digital artwork](https://dev.pyvista.org/getting-started/external_examples.html).

PyVista exposes a Pythonic API to the [Visualization Toolkit (VTK)](http://www.vtk.org) to provide tooling that is immediately usable without any prior knowledge of VTK and is being built as the 3D equivalent of [Matplotlib](https://matplotlib.org/), with plugins to [Jupyter](https://jupyter.org/) to enable visualization of 3D data using both server- and client-side rendering.

We will provide a hands-on tutorial accessible to anyone with internet access and a computer via many of PyVista's existing [example Jupyter notebooks](https://docs.pyvista.org/examples/index.html) and new material through a comprehensive overview highlighting popular 3D visualization use cases.

## Keywords

[visualization](https://github.com/topics/visualization)
[meshviewer](https://github.com/topics/meshviewer)
[vtk](https://github.com/topics/vtk)
[3d](https://github.com/topics/3d)

## Other Information and Files

See our examples at [PyVista Examples](http://docs.pyvista.org/examples/index.html)

PyVista is a [NumFOCUS Affiliated Project](https://numfocus.org/sponsored-projects/affiliated-projects)

### Tutorial Description

Our tutorial will demonstrate PyVista's latest capabilities and bring a wide range of users to the forefront of 3D visualization in Python.

- Use PyVista to create 3D visualizations from a variety of datasets in common formats.
- Overview the classes and data structures of PyVista with real-world examples.
- Be familiar of the various filters and features of PyVista.
- Know which Python libraries are used and can be used by PyVista (meshio, trimesh etc).

We see this tutorial catering to anyone who wants to visualize data in any domain, and this ranges from basic Python users to advanced power users.

### Tutorial Outline

0. Getting Started (Bane Sullivan) - PyVista for 3D Visualization within Python. (10 min for talk, 10 min for exercise)

1. PyVista & Jupyter (Tetsuo Koyama) - Demonstrate how to use PyVista in Jupyter for state-of-the-art 3D visualization in Notebooks and make sure the class room is up and running. (5 min for talk, 15 for exercise)

2. Basic usage (Tetsuo Koyama) - Reading and plotting 3D data using `examples` module and external files. (10 min for talk, 10 min for exercise)

3. What is a Mesh? (Bane Sullivan) - Learn the basics of the PyVista data types and how to open common 3D file formats to visualize the data in 3D (20 min for talk, 10 min for exercise)

4. Break. Stretch fingers and grab some coffee. (15 minutes)

5. Plotting Options and Animations (Bane Sullivan) - Demonstrate many features of the PyVista plotting API to create compelling 3D visualizations and touch on animations (15 min for talk, 20 min for exercise)

6. Filters (Bane Sullivan) - Demonstrate the PyVista filters API to perform mesh analysis and alteration (15 minutes)

7. PyVista in Action (Tetsuo Koyama & Bill Little) - Show how PyVista is already being used within several projects and can be used for all things visualization. (15 min for talk)

8. Quick break. Prepare for the final run. (10 minutes)

9. Trame (Jaswant Panchumarti) - Leverage PyVista and Trame to make awesome interactive web applications. (20 min for talk, 10 min for exercise)

10. VTK (Jaswant Panchumarti) - Show how PyVista uses VTK and how you can combine the best of both worlds! (10 minutes for talk, 15 minutes for exercise)

11. Open up to Questions. (15 minutes)

### Additional Tutorial Information

We will base the material for the tutorial on [the examples in PyVista's online documentation](https://docs.pyvista.org/examples/index.html).
[Transform 2021: Guide to PyVista Tutorial](https://github.com/banesullivan/transform-2021) will also be used as material.
The tutorial itself will be in the [pyvista/pyvista-tutorial](https://github.com/pyvista/pyvista-tutorial) repository.

### Tutorial Prerequisites

We see this tutorial catering to anyone who wants to visualize data in any domain, and this ranges from basic Python users to advanced power users.

In fact, our tutorial instructors and community members come from a diverse set of backgrounds.

1. Basic knowledge of Python to get started. Be able to install Jupyter Lab on your machine and be up and running.
2. Intermediate users will want to be familiar with [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/) and perhaps other libraries that are compatible with PyVista, like [trimesh](https://trimsh.org/examples.html) or [meshio](https://github.com/nschloe/meshio).
3. Advanced users should be familiar with the Visualization Toolkit (VTK) and general data science.

## Appropriate level of the attendees' Python knowledge

Something for everyone!

- [x] Beginner
- [x] Intermediate
- [x] Advanced

## Instructor Bio(s)

### [Alexander Kaszynski](https://github.com/akaszynski)

[Alexander Kaszynski](https://github.com/akaszynski/resume), co-creator of [PyVista](https://github.com/pyvista/) and creator of the [PyAnsys](https://github.com/pyansys) organization.

Advocate for all things Python with extensive experience presenting as a speaker at IGTI conferences for the past decade, and for four years at Ansys developing PyAnsys to enable automation through Python for CAE applications.

Enjoys presenting and demoing Python, especially 3D visualization but also its application to CAE and automation.

### [Bane Sullivan](https://github.com/banesullivan)

[Bane Sullivan](https://banesullivan.com), co-creator of [PyVista](https://github.com/pyvista/), is a Research Software Engineer working at the intersection of geoscience, visualization, and data science.

Bane is a geophysicist/hydrologist by training and has been working to grow PyVista's adoption within the subsurface geoscience communities.

### [Tetsuo Koyama](https://github.com/tkoyama010)

Interested in scientific computing and visualization with computer graphics.
Developer team member of PyVista.
Past experience as a speaker:

- [PyConJP 2019 speaker "Introduction to FEM Analysis with Python"](https://youtu.be/6JuB1GiDLQQ)
- [PyConJP 2020 speaker "How to plot unstructured mesh file on Jupyter Notebook"](https://youtu.be/X3Z54Kw4I6Y)
- [SciPy Japan 2020 speaker "Translation Project of Mayavi2 documents"](https://youtu.be/epxm9SjLMS0)
- [PyConJP 2021 speaker "Visualize 3D scientific data in a Pythonic way like Matplotlib"](https://youtu.be/ru-nENLgleo)

### [Bill Little](https://github.com/bjlittle)

[Bill Little](https://github.com/bjlittle), creator of [GeoVista](https://github.com/bjlittle/geovista), is a software engineer working at the [UK Met Office](https://www.metoffice.gov.uk) and a core developer on [SciTools](https://github.com/orgs/SciTools/repositories), which includes [Cartopy](https://github.com/SciTools/cartopy) and [Iris](https://github.com/SciTools/iris).

### [Jaswant Panchumarti](https://github.com/jspanchu)

[Jaswant Panchumarti](https://github.com/jspanchu) is an R&D engineer on Kitware’s Scientific Computing Team working at the forefront of 3D visualization with VTK and WASM. Jaswant focuses on expanding the solid modeling capabilities of VTK by improving the precision, resource efficiency, and stability of computational geometry strategies.

## Paper

[![DOI](https://joss.theoj.org/papers/10.21105/joss.01450/status.svg)](https://doi.org/10.21105/joss.01450)
