#!/usr/bin/env python

# In[1]:


# Configure for trame
import pyvista

pyvista.set_plot_theme("document")
pyvista.set_jupyter_backend("trame")
pyvista.global_theme.window_size = [600, 400]
pyvista.global_theme.axes.show = False
pyvista.global_theme.smooth_shading = True
