from pyvista import examples

dataset = examples.download_lucy()
dataset.plot(smooth_shading=True, color="white")
