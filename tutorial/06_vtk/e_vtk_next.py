"""
VTK's Next Generation API
~~~~~~~~~~~~~~~~~~~~~~~~~

This requires a pre-release version of VTK:

.. code-block:: bash

    pip install --extra-index-url https://wheels.vtk.org vtk==9.3.20240629.dev0

"""

import vtkmodules.vtkInteractionStyle
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCompositePolyDataMapper,
    vtkLightKit,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)

# for factory overrides
import vtkmodules.vtkRenderingOpenGL2  # noqa
import vtkmodules.vtkRenderingUI  # noqa

# Creates a render window interactor, connects it to a render window.
# Switch the interactor style such that left mouse click and drag orbit the camera
# around the camera's focal point.
interactor = vtkRenderWindowInteractor()
interactor.interactor_style.SetCurrentStyleToTrackballCamera()

window = vtkRenderWindow(size=(1280, 720), interactor=interactor)

renderer = vtkRenderer(automatic_light_creation=False, background=(1.0, 1.0, 1.0))
window.AddRenderer(renderer)

# Uses light kit for better lit scenes than the default in VTK.
light_kit = vtkLightKit()
light_kit.AddLightsToRenderer(renderer)

###############################################################################
# Load input mesh from a vtkPartitionedDataSetCollection file
from vtkmodules.vtkIOXML import vtkXMLPartitionedDataSetCollectionReader

reader = vtkXMLPartitionedDataSetCollectionReader()
reader.file_name = "data/mesh.vtpc"
reader.Update()
reactor = reader.output

actor = vtkActor()
actor.mapper = (reactor >> vtkCompositePolyDataMapper()).last
# Make the toroid translucent so we can look at objects inside it.
actor.property.opacity = 0.2
renderer.AddActor(actor)

###############################################################################
# Construct magpy coil objects for each coil in the reactor mesh.
from utils.build_magnetic_coils import build_magnetic_coils

coils = build_magnetic_coils(reactor, current=1000)

from vtkmodules.util.numpy_support import vtk_to_numpy

###############################################################################
# Compute B, H in a 32x32x32 grid
from vtkmodules.vtkCommonDataModel import vtkImageData

grid = vtkImageData(extent=(-16, 16, -16, 16, -16, 16), spacing=(0.1, 0.1, 0.1))
grid_points = vtk_to_numpy(grid.points.data)
b = coils.getB(grid_points) * 1000
grid.point_data.set_array("B (mT)", b)
h = coils.getH(grid_points)
grid.point_data.set_array("H (A/m)", h)

###############################################################################
# Show coils
import magpylib as magpy
from utils.save_dataset import save_dataset

magpy.show(coils, arrow=True)
save_dataset(grid, "data/solution.vti")

from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkFiltersFlowPaths import vtkStreamTracer

###############################################################################
# Compute streamlines of B field induced by toroidal coils.
from vtkmodules.vtkFiltersSources import vtkSphereSource

trace_streamlines = vtkStreamTracer(
    integrator_type=vtkStreamTracer.RUNGE_KUTTA45,
    integration_direction=vtkStreamTracer.BOTH,
    initial_integration_step=0.2,
    maximum_propagation=3.2,
)
trace_streamlines.SetInputArrayToProcess(0, 0, 0, 0, "B (mT)")

create_sphere = vtkSphereSource(theta_resolution=16)

grid >> select_ports(0, trace_streamlines)
create_sphere >> select_ports(1, trace_streamlines)

###############################################################################
# Visualize streamlines
from vtkmodules.vtkFiltersCore import vtkTubeFilter

actor = vtkActor()
actor.mapper = (
    trace_streamlines >> vtkTubeFilter(number_of_sides=3, radius=0.00383538) >> vtkPolyDataMapper()
).last
renderer.AddActor(actor)

###############################################################################
# Animate the disk position such that it oscillates between y=-1 and y=1.
from itertools import cycle

import numpy as np


class vtkTimerCallback:
    def __init__(self, sphere, window, nsteps=10):
        half_nsteps = int(nsteps / 2)
        self.radii = cycle(
            np.append(np.linspace(0, 0.8, half_nsteps), np.linspace(0.8, 0, half_nsteps))
        )
        self.sphere = sphere
        self.window = window

    def execute(self, obj, event):
        self.sphere.radius = next(self.radii)
        self.window.Render()


###############################################################################
# Sign up to receive TimerEvent

cb = vtkTimerCallback(create_sphere, window, nsteps=250)
interactor.RemoveObservers('TimerEvent')
interactor.AddObserver('TimerEvent', cb.execute)
cb.timerId = interactor.CreateRepeatingTimer(2)

renderer.ResetCamera()
window.Render()
interactor.Start()
