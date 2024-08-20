"""
VTK + WASM
~~~~~~~~~~

Use WASM local rendering. This requires a pre-release version of VTK:

.. code-block:: bash

    pip install --extra-index-url https://wheels.vtk.org vtk==9.3.20240629.dev0

"""

# Required for vtk factory
from trame.app import get_server
from trame.decorators import TrameApp, change
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3 as vuetify
from trame.widgets.vtk import VtkRemoteView
from trame_vtklocal.widgets import vtklocal
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersCore import vtkElevationFilter, vtkGlyph3D
from vtkmodules.vtkFiltersSources import vtkConeSource, vtkCubeSource, vtkSphereSource
from vtkmodules.vtkImagingCore import vtkRTAnalyticSource
from vtkmodules.vtkImagingGeneral import vtkImageGradient
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

###############################################################################


def setup_vtk():  # noqa: PLR0915
    colors = vtkNamedColors()

    # The Wavelet Source is nice for generating a test vtkImageData set
    rt = vtkRTAnalyticSource()
    rt.SetWholeExtent(-2, 2, -2, 2, 0, 0)

    # Take the gradient of the only scalar 'RTData' to get a vector attribute
    grad = vtkImageGradient()
    grad.SetDimensionality(3)
    grad.SetInputConnection(rt.GetOutputPort())

    # Elevation just to generate another scalar attribute that varies nicely over the data range
    elev = vtkElevationFilter()
    # Elevation values will range from 0 to 1 between the Low and High Points
    elev.SetLowPoint(-2, -2, 0)
    elev.SetHighPoint(2, 2, 0)
    elev.SetInputConnection(grad.GetOutputPort())

    # Create simple PolyData for glyph table
    cs = vtkCubeSource()
    cs.SetXLength(0.5)
    cs.SetYLength(1)
    cs.SetZLength(2)
    ss = vtkSphereSource()
    ss.SetRadius(0.25)
    cs2 = vtkConeSource()
    cs2.SetRadius(0.25)
    cs2.SetHeight(0.5)

    # Set up the glyph filter
    glyph = vtkGlyph3D()
    glyph.SetInputConnection(elev.GetOutputPort())

    # Here is where we build the glyph table
    # that will be indexed into according to the IndexMode
    glyph.SetSourceConnection(0, cs.GetOutputPort())
    glyph.SetSourceConnection(1, ss.GetOutputPort())
    glyph.SetSourceConnection(2, cs2.GetOutputPort())

    glyph.ScalingOn()
    glyph.SetScaleModeToScaleByScalar()
    glyph.SetVectorModeToUseVector()
    glyph.OrientOn()
    glyph.SetScaleFactor(1)  # Overall scaling factor
    glyph.SetRange(0, 1)  # Default is (0,1)

    # Tell it to index into the glyph table according to scalars
    glyph.SetIndexModeToScalar()

    # Tell glyph which attribute arrays to use for what
    glyph.SetInputArrayToProcess(0, 0, 0, 0, "Elevation")  # scalars
    glyph.SetInputArrayToProcess(1, 0, 0, 0, "RTDataGradient")  # vectors

    coloring_by = "Elevation"
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph.GetOutputPort())
    mapper.SetScalarModeToUsePointFieldData()
    mapper.SetColorModeToMapScalars()
    mapper.ScalarVisibilityOn()

    # GetRange() call doesn't work because attributes weren't copied to glyphs
    # as they should have been...
    # mapper.SetScalarRange(glyph.GetOutputDataObject(0).GetPointData().GetArray(coloring_by).GetRange())

    mapper.SelectColorArray(coloring_by)
    actor = vtkActor()
    actor.SetMapper(mapper)

    ren = vtkRenderer()
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d("DarkGray"))

    renWin = vtkRenderWindow()  # noqa: N806
    renWin.AddRenderer(ren)

    renderWindowInteractor = vtkRenderWindowInteractor()  # noqa: N806
    renderWindowInteractor.SetRenderWindow(renWin)
    renderWindowInteractor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    ren.ResetCamera()

    return renWin, ren, cs2, ss


###############################################################################


@TrameApp()
class App:
    def __init__(self, server=None) -> None:
        self.server = get_server(server, client_type="vue3")
        self.render_window, self.renderer, self.cone, self.sphere = setup_vtk()
        self.view_local = None
        self.view_remote = None
        self.ui = self._build_ui()

    @property
    def ctrl(self):
        return self.server.controller

    @change("resolution")
    def on_resolution_change(self, resolution, **kwargs) -> None:
        self.cone.SetResolution(int(resolution))
        self.sphere.SetStartTheta(int(resolution) * 6)
        self.view_remote.update()
        self.view_local.update()

    def reset_camera(self) -> None:
        self.renderer.ResetCamera()
        self.view_local.update()
        self.view_remote.update()

    def _build_ui(self):
        with SinglePageLayout(self.server) as layout:
            layout.icon.click = self.reset_camera
            with layout.toolbar:
                vuetify.VSpacer()
                vuetify.VSlider(
                    v_model=("resolution", 6),
                    min=3,
                    max=60,
                    step=1,
                    dense=True,
                    hide_details=True,
                )
                vuetify.VBtn("Update", click=self.ctrl.view_update)

            with (
                layout.content,
                vuetify.VContainer(
                    fluid=True,
                    classes="pa-0 fill-height",
                ),
            ):
                with vuetify.VContainer(
                    fluid=True, classes="pa-0 fill-height", style="width: 50%;"
                ):
                    self.view_local = vtklocal.LocalView(
                        self.render_window,
                        eager_sync=True,
                    )
                    self.ctrl.view_update = self.view_local.update
                with vuetify.VContainer(
                    fluid=True, classes="pa-0 fill-height", style="width: 50%;"
                ):
                    self.view_remote = VtkRemoteView(self.render_window, interactive_ratio=1)

            # hide footer
            layout.footer.hide()

            return layout


###############################################################################
app = App("wasm")
await app.ui.ready

###############################################################################
# Make sure to give room for the download of WASM bundle
# Only needed at first execution
import asyncio

await asyncio.sleep(1)

###############################################################################
app.ui
