# Configure for trame
import pyvista

pyvista.set_plot_theme("document")
pyvista.set_jupyter_backend("trame")
pyvista.global_theme.axes.show = False
pyvista.global_theme.smooth_shading = True
