grid = pv.ImageData(dimensions=(300, 300, 1))
grid.point_data["values"] = values.flatten(order="F")