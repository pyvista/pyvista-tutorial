"""
VTK's Next Generation API
~~~~~~~~~~~~~~~~~~~~~~~~~

This requires a pre-release version of VTK:

.. code-block:: bash

    pip install --extra-index-url https://wheels.vtk.org vtk==9.3.20240629.dev0

"""

import magpylib as magpy
import numpy as np

# for factory overrides
from pyvista.examples.downloads import _download_archive_file_or_folder
from vtkmodules.util.data_model import *  # noqa: F403
from vtkmodules.util.execution_model import select_ports
from vtkmodules.util.numpy_support import vtk_to_numpy
from vtkmodules.vtkCommonCore import vtkIdList
from vtkmodules.vtkCommonDataModel import vtkDataObjectTreeIterator, vtkImageData
from vtkmodules.vtkFiltersExtraction import vtkExtractBlockUsingDataAssembly
from vtkmodules.vtkFiltersFlowPaths import vtkStreamTracer
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkIOParallelXML import vtkXMLPartitionedDataSetCollectionWriter

# Utility function to save simulation input/output datasets to filesystem
from vtkmodules.vtkIOXML import vtkXMLImageDataWriter, vtkXMLPolyDataWriter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCompositePolyDataMapper,
    vtkLightKit,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
)


def build_magnetic_coils(mesh, current=1000):
    magpy_coils = magpy.Collection()

    # Extract blocks under the "coils" node.
    coil_extractor = vtkExtractBlockUsingDataAssembly(
        assembly_name="Assembly", selector="//coils", input_data=mesh
    )
    coil_extractor.Update()

    # Build a magpy current source for every coil.
    coil_iter = vtkDataObjectTreeIterator(data_set=coil_extractor.output)
    coil_iter.visit_only_leaves = True
    coil_iter.InitTraversal()
    while not coil_iter.IsDoneWithTraversal():
        line = vtkIdList()
        coil = coil_iter.current_data_object
        coil.lines.InitTraversal()
        while coil.lines.GetNextCell(line):
            vertices = [coil.points[line.GetId(i)] for i in range(line.GetNumberOfIds())]
            magpy_coils.add(magpy.current.Polyline(vertices=vertices, current=current))
        coil_iter.GoToNextItem()

    return magpy_coils


def save_dataset(dataset, file_name) -> None:
    if file_name.endswith(".vti"):
        writer = vtkXMLImageDataWriter()
    elif file_name.endswith(".vtp"):
        writer = vtkXMLPolyDataWriter()
    elif file_name.endswith(".vtpc"):
        writer = vtkXMLPartitionedDataSetCollectionWriter()
    writer.input_data_object = dataset
    writer.file_name = file_name
    writer.Write()


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

import pathlib

###############################################################################
# Load input mesh from a vtkPartitionedDataSetCollection file
from vtkmodules.vtkIOXML import vtkXMLPartitionedDataSetCollectionReader

path = _download_archive_file_or_folder("reactor.zip", target_file="")

reader = vtkXMLPartitionedDataSetCollectionReader()
reader.file_name = pathlib.Path(path + "/reactor/" + "mesh.vtpc")
reader.Update()
reactor = reader.output

actor = vtkActor()
actor.mapper = (reactor >> vtkCompositePolyDataMapper()).last
# Make the toroid translucent so we can look at objects inside it.
actor.property.opacity = 0.2
renderer.AddActor(actor)

###############################################################################
# Construct magpy coil objects for each coil in the reactor mesh.
coils = build_magnetic_coils(reactor, current=1000)

###############################################################################
# Compute B, H in a 32x32x32 grid

grid = vtkImageData(extent=(-16, 16, -16, 16, -16, 16), spacing=(0.1, 0.1, 0.1))
grid_points = vtk_to_numpy(grid.points.data)
b = coils.getB(grid_points) * 1000
grid.point_data.set_array("B (mT)", b)
h = coils.getH(grid_points)
grid.point_data.set_array("H (A/m)", h)

###############################################################################
# Show coils
magpy.show(coils, arrow=True)
save_dataset(grid, "data/solution.vti")

###############################################################################
# Compute streamlines of B field induced by toroidal coils.
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


class vtkTimerCallback:  # noqa: N801
    def __init__(self, sphere, window, nsteps=10) -> None:
        half_nsteps = int(nsteps / 2)
        self.radii = cycle(
            np.append(np.linspace(0, 0.8, half_nsteps), np.linspace(0.8, 0, half_nsteps))
        )
        self.sphere = sphere
        self.window = window

    def execute(self, obj, event) -> None:
        self.sphere.radius = next(self.radii)
        self.window.Render()


###############################################################################
# Sign up to receive TimerEvent

cb = vtkTimerCallback(create_sphere, window, nsteps=250)
interactor.RemoveObservers("TimerEvent")
interactor.AddObserver("TimerEvent", cb.execute)
cb.timerId = interactor.CreateRepeatingTimer(2)

renderer.ResetCamera()
window.Render()
interactor.Start()
