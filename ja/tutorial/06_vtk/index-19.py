import pyvista as pv
from pyvista import examples
import vtk

mesh = examples.download_bunny_coarse()

# Initialize VTK algorithm
splatter = vtk.vtkGaussianSplatter()

# Pass PyVista object as input to VTK
splatter.SetInputData(mesh)

# Set parameters
n = 200
splatter.SetSampleDimensions(n, n, n)
splatter.SetRadius(.02)
splatter.SetExponentFactor(-10)
splatter.SetEccentricity(2)
splatter.Update()

# Retrieve output and wrap with PyVista
vol = pv.wrap(splatter.GetOutput())

# Use PyVista to produce contours
cntrs = vol.contour([.95 * splatter.GetRadius()])

# Use PyVista to plot
p = pv.Plotter()
p.add_mesh(mesh, style='wireframe')
p.add_mesh(cntrs, color=True)
p.show()