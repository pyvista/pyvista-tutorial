"""
Open Mesh File
~~~~~~~~~~~~~~

An example of opening a mesh file from the browser and viewing it with PyVista.

"""

import tempfile
from pathlib import Path

import pyvista as pv
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.app.file_upload import ClientFile
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3

pv.OFF_SCREEN = True

server = get_server()
state, ctrl = server.state, server.controller

pl = pv.Plotter()


@server.state.change("file_exchange")
def handle(file_exchange, **kwargs) -> None:
    file = ClientFile(file_exchange)

    if file.content:
        print(file.info)  # noqa: T201
        bytes = file.content  # noqa: A001
        with tempfile.NamedTemporaryFile(suffix=file.name) as path:
            with Path(path.name).open("wb") as f:
                f.write(bytes)
            ds = pv.read(path.name)
        pl.add_mesh(ds, name=file.name)
        pl.reset_camera()
    else:
        pl.clear_actors()
        pl.reset_camera()


with SinglePageLayout(server) as layout:
    with layout.toolbar:
        vuetify3.VSpacer()
        vuetify3.VFileInput(
            show_size=True,
            small_chips=True,
            truncate_length=25,
            v_model=("file_exchange", None),
            density="compact",
            hide_details=True,
            style="max-width: 300px;",
        )
        vuetify3.VProgressLinear(
            indeterminate=True, absolute=True, bottom=True, active=("trame__busy",)
        )

    with layout.content:  # noqa: SIM117
        with vuetify3.VContainer(
            fluid=True, classes="pa-0 fill-height", style="position: relative;"
        ):
            view = plotter_ui(pl)
            ctrl.view_update = view.update

# Show UI
await layout.ready
layout
###############################################################################
# .. raw:: html
#
#     <center>
#       <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/09_trame/f_trame_open_file.ipynb">
#         <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="150px">
#       </a>
#     </center>
