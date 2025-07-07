"""
.. _line_widget_example:

Line Widget
~~~~~~~~~~~

The line widget can be enabled and disabled by the
:func:`pyvista.Plotter.add_line_widget` and
:func:`pyvista.Plotter.clear_line_widgets` methods respectively.
Unfortunately, PyVista does not have any helper methods to utilize this
widget, so it is necessary to pass a custom callback method.

One particularly fun example is to use the line widget to create a source for
the :func:`pyvista.DataSetFilters.streamlines` filter. Again note the use of
the ``name`` argument in ``add_mesh``.
"""

import numpy as np
import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")

mesh = examples.download_kitchen()
furniture = examples.download_kitchen(split=True)

arr = np.linalg.norm(mesh["velocity"], axis=1)
clim = [arr.min(), arr.max()]

# %%

pl = pv.Plotter()
pl.add_mesh(furniture, name="furniture", color=True)
pl.add_mesh(mesh.outline(), color="black")
pl.add_axes()


def simulate(pointa, pointb) -> None:
    streamlines = mesh.streamlines(
        n_points=10, max_steps=100, pointa=pointa, pointb=pointb, integration_direction="forward"
    )
    pl.add_mesh(
        streamlines, name="streamlines", line_width=5, render_lines_as_tubes=True, clim=clim
    )


pl.add_line_widget(callback=simulate, use_vertices=True)
pl.show()

# %%
# And here is a screen capture of a user interacting with this
#
# .. image:: ../../images/gifs/line-widget-streamlines.gif

# %%
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/08_widgets/c_line-widget.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
