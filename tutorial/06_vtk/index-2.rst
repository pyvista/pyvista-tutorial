values = vtk.vtkDoubleArray()
values.SetName("values")
values.SetNumberOfComponents(1)
values.SetNumberOfTuples(300*300)

for x in range(300):
   for y in range(300):
      values.SetValue(x*300 + y, 127.5 + (1.0 + sin(x/25.0)*cos(y/25.0)))