# PyVista Figures and Visualization Tutorial - 20-Minute Presentation Script

## Introduction (1.5 minutes)

"Welcome to the PyVista Figures and Visualization tutorial. Today, we'll learn how to make great pictures with PyVista's powerful plotting tools.

Making pictures of data is more than just showing numbers - it's about telling a story, finding new things, and sharing information clearly. PyVista gives you easy Python tools to make everything from simple 3D pictures to complex multi-view figures with advanced drawing techniques.

In this session, we'll cover the basic building blocks of PyVista visualization: the Plotter class, mesh display options, subplotting, shading techniques, texture mapping, and even making animated GIFs. By the end, you'll have the tools to make pictures that not only show information but also interest your audience."

## The Plotter Class - Your Canvas (2.5 minutes)

"At the center of PyVista's visualization system is the `Plotter` class. Think of it as your 3D canvas, like Matplotlib's figure, but made for three-dimensional data.

```python
import pyvista as pv
from pyvista import examples

# Create a simple mesh
mesh = pv.Wavelet()

# Create a plotter instance
p = pv.Plotter()
p.add_mesh(mesh)
p.show()
```

The workflow is intuitive:

1. Create a Plotter instance
2. Add meshes or other objects to it
3. Show the result

But the real power comes from changing settings. The Plotter constructor takes many parameters:

- `window_size`: Control the resolution of your output
- `background`: Set the background color
- `off_screen`: Render without showing (useful for batch processing)
- `notebook`: Enable inline display in Jupyter notebooks

Let's see how window size affects our visualization:

```python
# High-resolution plotter for publication
p = pv.Plotter(window_size=[2000, 1500], background='white')
p.add_mesh(mesh, cmap='viridis')
p.show()
```

This makes a high-resolution figure perfect for papers or presentations."

## The add_mesh Method - Styling Your Data (3 minutes)

"The `add_mesh` method is where the magic happens. It's your main tool for controlling how data looks in your picture. Let's look at its key parameters:

**Color and Colormaps:**

```python
p = pv.Plotter()
# Single color
p.add_mesh(mesh, color='red')
# Or use a colormap
p.add_mesh(mesh, cmap='coolwarm')
# Control color limits
p.add_mesh(mesh, clim=[0, 100])
p.show()
```

**Edge Visibility:**

```python
p = pv.Plotter()
p.add_mesh(mesh, show_edges=True, edge_color='black')
p.show()
```

Showing edges is very useful for understanding mesh structure or making technical drawings.

**Opacity Control:**

```python
# Load terrain data for better demonstration
mesh = examples.download_st_helens().warp_by_scalar()

p = pv.Plotter()
# Constant opacity
p.add_mesh(mesh, opacity=0.5)
# Or use linear transfer function
p.add_mesh(mesh, opacity='linear', cmap='terrain')
p.show()
```

The 'linear' opacity makes a function where lower values are more see-through - perfect for volume rendering effects.

**Advanced Styling:**
The `add_mesh` method supports over 50 parameters! Some important ones:

- `lighting`: Enable/disable lighting effects
- `smooth_shading`: Toggle between flat and smooth shading
- `specular`: Control surface shininess
- `diffuse`: Control surface color response to light
- `ambient`: Set ambient light contribution
- `interpolate_before_map`: Improve color mapping quality"

## Building Complex Scenes (2.5 minutes)

"Real-world pictures often need multiple objects. PyVista is great at making complex scenes by calling `add_mesh` many times:

```python
# Create platonic solids scene
kinds = ['tetrahedron', 'cube', 'octahedron', 'dodecahedron', 'icosahedron']
centers = [(0, 1, 0), (0, 0, 0), (0, 2, 0), (-1, 0, 0), (-1, 2, 0)]

solids = [pv.PlatonicSolid(kind, radius=0.4, center=center)
          for kind, center in zip(kinds, centers)]

p = pv.Plotter(window_size=[1000, 1000])
for solid in solids:
    p.add_mesh(solid, color='silver', specular=1.0, specular_power=10)

# Add environment elements
p.view_vector((5.0, 2, 3))
p.add_floor('-z', lighting=True, color='tan', pad=1.0)
p.enable_shadows()
p.show()
```

This example shows several advanced techniques:

- Multiple objects with consistent styling
- Environmental elements (floor)
- Shadow rendering for realism
- Custom camera positioning

The key to complex scenes is planning. Plan your scene like a photographer:

- What's the main subject?
- What supporting elements provide context?
- How does lighting enhance the story?
- What viewing angle best conveys the information?"

## Subplotting - Multiple Views (3 minutes)

"Comparing different parts of your data side-by-side is very important for analysis. PyVista's subplotting system makes this easy:

```python
# Basic side-by-side comparison
p = pv.Plotter(shape=(1, 2))

p.subplot(0, 0)
p.add_mesh(pv.Sphere(), color='red')
p.add_text('Sphere', position='upper_edge')

p.subplot(0, 1)
p.add_mesh(pv.Cube(), color='blue')
p.add_text('Cube', position='upper_edge')

p.show()
```

But the real power comes when comparing different ways to show the same data:

```python
mesh = pv.Wavelet()
contours = mesh.contour()
slices = mesh.slice_orthogonal()

p = pv.Plotter(shape=(1, 2))

# Contour view
p.subplot(0, 0)
p.add_mesh(contours, opacity=0.5)
p.add_text('Isosurfaces', position='upper_edge')

# Slice view
p.subplot(0, 1)
p.add_mesh(slices)
p.add_text('Orthogonal Slices', position='upper_edge')

# Link cameras for synchronized interaction
p.link_views()
p.view_isometric()
p.show()
```

The `link_views()` method is very powerful - when you rotate one view, all linked views rotate together, keeping spatial relationships.

**Advanced Subplotting Tips:**

- Use `shape=(rows, cols)` for grid layouts
- `subplot(row, col)` to activate specific subplot
- Each subplot maintains independent settings
- Share colorbars across subplots with `scalar_bar_args`
- Use consistent lighting for visual coherence"

## Axes, Bounds, and Spatial Context (2 minutes)

"Scientific pictures need spatial reference. PyVista gives several tools for orientation:

```python
mesh = examples.load_random_hills()

p = pv.Plotter()
p.add_mesh(mesh, cmap='terrain')

# Add coordinate axes
p.show_axes()

# Add bounding box with labels
p.show_bounds(
    grid='front',
    location='outer',
    all_edges=True,
)

# Add a scale ruler
p.add_ruler()

# Add orientation widget
p.add_axes()

p.show()
```

**Customizing Spatial References:**

- `show_axes()`: Displays coordinate system axes
- `show_bounds()`: Creates labeled bounding box
  - `grid`: Add grid lines ('front', 'back', 'both')
  - `location`: Label placement ('inner', 'outer')
  - `font_size`: Control label size
  - `xtitle`, `ytitle`, `ztitle`: Custom axis labels

These elements change a pretty picture into a measured visualization good for scientific communication."

## Advanced Shading Techniques (3 minutes)

"Shading greatly affects how we see 3D geometry. Let's look at PyVista's shading options:

```python
# Load a mechanical part for demonstration
mesh = examples.load_nut()

# Default flat shading
p = pv.Plotter(shape=(2, 2))
p.subplot(0, 0)
p.add_mesh(mesh)
p.add_text('Flat Shading (Default)', position='upper_edge')

# Smooth shading
p.subplot(0, 1)
p.add_mesh(mesh, smooth_shading=True)
p.add_text('Smooth Shading', position='upper_edge')

# Smooth with edge preservation
p.subplot(1, 0)
p.add_mesh(mesh, smooth_shading=True, split_sharp_edges=True)
p.add_text('Smooth + Sharp Edges', position='upper_edge')

# Physically based rendering
p.subplot(1, 1)
p.add_mesh(mesh, color='white', pbr=True, metallic=0.8, roughness=0.2)
p.add_text('Physically Based Rendering', position='upper_edge')

p.link_views()
p.show()
```

**Understanding Shading Options:**

1. **Flat Shading**: Each face has the same color. Good for:
   - Faceted objects
   - Architectural models
   - When you need to see individual faces

2. **Smooth Shading**: Blends normals across faces. Good for:
   - Organic shapes
   - Continuous surfaces
   - Beautiful presentations

3. **Split Sharp Edges**: Best of both types
   - Keeps sharp features while smoothing curved areas
   - Controlled by `feature_angle` parameter
   - Essential for mechanical parts

4. **Physically Based Rendering (PBR)**:
   - `metallic`: 0 (dielectric) to 1 (metal)
   - `roughness`: 0 (mirror) to 1 (diffuse)
   - More realistic material appearance"

## Texture Mapping - Real-World Imagery (3 minutes)

"Texture mapping puts 2D images onto 3D geometry. This is very valuable for geographic data, medical imaging, and photo-realistic rendering.

Let's look at a real-world example - putting a geological map on topography:

```python
# Load topography
topo = pv.read('topo_clean.vtk')

# Define texture coordinates using ground control points
origin = [310967.75, 4238841.04, 0.0]  # Bottom-left
point_u = [358682.94, 4238841.04, 0.0]  # Bottom-right
point_v = [310967.75, 4276281.99, 0.0]  # Top-left

# Map the texture coordinates
topo.texture_map_to_plane(origin, point_u, point_v, inplace=True)

# Load and apply the GeoTIFF texture
texture = pv.read_texture('geological_map.tif')

p = pv.Plotter(window_size=[3072, 2304])  # High resolution
p.add_mesh(topo, texture=texture)
p.camera_position = [
    (337461.41, 4257141.43, 2738.50),  # Camera location
    (339000.41, 4260394.94, 1724.07),  # Focal point
    (0.105, 0.250, 0.962),              # View up vector
]
p.show()
```

**Key Concepts:**

1. **Texture Coordinates**: Define how 2D image maps to 3D surface
2. **Ground Control Points**: Real-world coordinates for georeferencing
3. **High Resolution**: Larger window sizes for detailed textures

**Applications:**

- Satellite imagery on terrain models
- Medical imaging on anatomical surfaces
- Material textures for realistic rendering
- Data visualization on geographic context"

## Creating Animated Visualizations (2.5 minutes)

"Still images tell stories, but animations bring data to life. PyVista makes creating GIFs easy:

```python
import numpy as np

# Create a wave surface
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

grid = pv.StructuredGrid(x, y, z)

# Set up plotter for GIF creation
plotter = pv.Plotter(notebook=False, off_screen=True)
plotter.add_mesh(
    grid,
    scalars=z.ravel(),
    lighting=False,  # Reduce color space for smaller files
    show_edges=True,
    scalar_bar_args={'title': 'Height'},
    clim=[-1, 1],  # Fix color scale
)

# Open GIF file
plotter.open_gif('wave.gif')

# Animate through phases
pts = grid.points.copy()
nframe = 15
for phase in np.linspace(0, 2 * np.pi, nframe + 1)[:nframe]:
    z = np.sin(r + phase)
    pts[:, -1] = z.ravel()

    # Update geometry and scalars
    plotter.update_coordinates(pts, render=False)
    plotter.update_scalars(z.ravel(), render=False)

    # Write frame
    plotter.write_frame()

plotter.close()
```

**Animation Best Practices:**

1. Use `lighting=False` for consistent colors
2. Fix color scales with `clim`
3. Keep frame count reasonable (15-30 fps)
4. Update without rendering until frame write
5. Use `off_screen=True` for batch processing

**Advanced Animation Techniques:**

- Camera orbits with `plotter.orbit()`
- Time-varying data with `update_scalars()`
- Morphing geometry with `update_coordinates()`
- Multi-view animations with subplots"

## Best Practices and Performance (2 minutes)

"Let's talk about how to make good, fast visualizations:

**Visual Design:**

1. **Color Choice**:
   - Use even colormaps ('viridis', 'plasma')
   - Avoid rainbow for number data
   - Think about colorblind-friendly palettes

2. **Lighting**:
   - Three-point lighting for complex scenes
   - Disable lighting for 2D-like visualizations
   - Use shadows sparingly - they impact performance

3. **Camera Positioning**:
   - Save good views: `plotter.camera_position`
   - Use standard views: `view_isometric()`, `view_xy()`
   - Smooth transitions: `fly_to()` method

**Making Things Faster:**

1. **Big Datasets**:
   - Decimate meshes: `mesh.decimate(0.9)`
   - Use LOD actors for multiple detail levels
   - Get regions of interest before plotting

2. **Drawing Speed**:
   - Turn off anti-aliasing for interactive work
   - Use `fast_approximate_anti_aliasing()`
   - Make window smaller during development

3. **Memory Management**:
   - Use `deep_clean()` to free memory
   - Close plotters explicitly
   - Reuse plotter instances when possible

**Publication Quality:**

1. High resolution: `window_size=[3000, 2000]`
2. White background for print
3. Consistent font sizes
4. Export as vector when possible"

## Real-World Applications Showcase (1.5 minutes)

"Let's see how these techniques work together in real applications:

**Medical Imaging:**

- Smooth shading for organic structures
- Opacity for revealing internal features
- Multiple views for comprehensive analysis

**Engineering:**

- Edge display for technical drawings
- PBR for realistic material representation
- Animations for assembly instructions

**Geoscience:**

- Texture mapping for satellite imagery
- Contours for elevation analysis
- Time series animations for temporal data

**Scientific Computing:**

- Glyphs for vector fields
- Isosurfaces for scalar fields
- Subplots for parameter studies

Each field has special needs, but PyVista's flexible toolkit can handle them all."

## Conclusion and Next Steps (1 minute)

"We've looked at the rich visualization abilities of PyVista:

- The Plotter class as your 3D canvas
- Mesh styling with add_mesh
- Multi-view layouts with subplotting
- Advanced shading and rendering techniques
- Texture mapping for real-world imagery
- Animation for dynamic storytelling

Main points:

1. Start simple, add complexity gradually
2. Let your data guide picture choices
3. Think about your audience - scientists, engineers, or regular people
4. Speed and quality are often trade-offs
5. PyVista's API is consistent and easy to find

Your next steps:

- Try with your own data
- Look at the PyVista gallery for ideas
- Join the community for support and ideas
- Share your visualizations!

Remember: great pictures don't just show data, they find insights and tell great stories. PyVista gives you the tools - now go make something amazing!"

---

## Timing Breakdown

- Introduction: 1.5 minutes
- Plotter Class: 2.5 minutes
- add_mesh Method: 3 minutes
- Complex Scenes: 2.5 minutes
- Subplotting: 3 minutes
- Axes and Bounds: 2 minutes
- Shading Techniques: 3 minutes
- Texture Mapping: 3 minutes
- Animation: 2.5 minutes
- Best Practices: 2 minutes
- Applications: 1.5 minutes
- Conclusion: 1 minute
  **Total: 20 minutes**

## Presenter Notes

1. **Code Preparation**: Pre-load all datasets to avoid download delays
2. **Live Coding**: Balance between live demos and prepared results
3. **Interactivity**: Rotate/zoom models to show 3D nature
4. **Pacing**: Each section has natural pause points for questions
5. **Examples**: Use domain-specific examples relevant to audience
6. **Troubleshooting**: Have backup static images if rendering fails
7. **Engagement**: Ask audience about their visualization challenges
8. **Resources**: Provide links to documentation and example gallery
