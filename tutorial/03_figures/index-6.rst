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

pl = pv.Plotter(window_size=[1000, 1000])
for solid in solids:
    pl.add_mesh(
        solid, color='silver', specular=1.0, specular_power=10
    )
pl.view_vector((5.0, 2, 3))
pl.add_floor('-z', lighting=True, color='tan', pad=1.0)
pl.enable_shadows()
pl.show()