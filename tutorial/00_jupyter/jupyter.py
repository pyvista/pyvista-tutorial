"""
Test out PyVista's Jupyter Backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Become familiar with PyVista Jupyter backend.
"""

import pyvista as pv

# Set/enable the backed
pv.set_jupyter_backend("trame")

###############################################################################

pl = pv.Plotter()
pl.add_mesh(pv.ParametricKlein())
pl.show()


###############################################################################
# Client-side rendering only (in browser)

pl = pv.Plotter()
pl.add_mesh(pv.ParametricRandomHills().elevation())
pl.show(jupyter_backend="client")


###############################################################################
# Server-side rendering only

pl = pv.Plotter()
pl.add_volume(pv.Wavelet())
pl.show(jupyter_backend="server")

###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/00_jupyter/jupyter.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
