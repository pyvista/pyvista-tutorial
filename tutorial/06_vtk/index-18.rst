import vtk
import pyvista as pv

# Create a circle using vtk
polygonSource = vtk.vtkRegularPolygonSource()
polygonSource.GeneratePolygonOff()
polygonSource.SetNumberOfSides(50)
polygonSource.SetRadius(5.0)
polygonSource.SetCenter(0.0, 0.0, 0.0)
polygonSource.Update()

# wrap and plot using pyvista
mesh = pv.wrap(polygonSource.GetOutput())
mesh.plot(line_width=3, cpos='xy', color='k')