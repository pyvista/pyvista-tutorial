import pyvista as pv
from pyvista import examples

kinds = [
    'tetrahedron',
    'cube',
    'octahedron',
    'dodecahedron',
    'icosahedron',
]
centers = [
    (0, 1, 0),
    (0, 0, 0),
    (0, 2, 0),
    (-1, 0, 0),
    (-1, 2, 0),
]

solids = [pv.PlatonicSolid(kind, radius=0.4, center=center) for kind, center in zip(kinds, centers)]

p = pv.Plotter(window_size=[1000, 1000])
for ind, solid in enumerate(solids):
    p.add_mesh(
        solid, color='silver', specular=1.0, specular_power=10
    )
p.view_vector((5.0, 2, 3))
p.add_floor('-z', lighting=True, color='tan', pad=1.0)
p.enable_shadows()
p.show()