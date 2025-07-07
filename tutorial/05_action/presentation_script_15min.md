# PyVista in Action - Interactive Visualization Tutorial

## 15-Minute Presentation Script

## Introduction (1 minute)

"Welcome to PyVista in Action! In this section, we'll look at how PyVista changes static 3D visualizations into dynamic, interactive experiences.

In the world of 3D data analysis, being able to interact with your visualizations is very important. Whether you're exploring complex datasets, making educational tools, or building professional applications, PyVista's interactive features help you go beyond static images.

We'll cover three main areas: PyVista's ecosystem and real-world applications, interactive widgets for desktop applications, and web-based visualization with Trame. By the end, you'll understand how to make visualizations that users can explore, change, and learn from."

## PyVista's Ecosystem and Impact (2 minutes)

"Before diving into technical details, let's see PyVista in action across various domains. PyVista has become a key part of the scientific Python ecosystem, powering visualization in fields from computational physics to geoscience.

**Scientific Computing Applications:**

- **FEniCSx**: Uses PyVista for finite element analysis visualization
- **PyMAPDL**: ANSYS integration for engineering simulations
- **PyElastica**: Simulating elastic structures with real-time visualization
- **PlasmaPy**: Plasma physics research and education

**Geoscience and GIS:**

- **GeoVista**: Specialized geoscience visualization built on PyVista
- **geemap**: Interactive mapping with 3D terrain visualization
- **GemGIS**: Geological modeling and visualization
- **gempy**: 3D structural geological modeling

**Engineering and Design:**

- **AeroSandbox**: Aerospace design optimization
- **pymead**: Aerodynamic shape optimization
- **AFEM**: Airframe finite element modeling

**Data Analysis Tools:**

- **napari**: Multi-dimensional image viewer
- **VisualPIC**: Particle-in-cell simulation visualization
- **DrillDown**: Geothermal drilling analysis

This diverse adoption shows PyVista's flexibility and power. Now let's see how you can use these capabilities in your own work."

## Interactive Widgets Overview (2 minutes)

"PyVista provides a rich set of 3D widgets that change viewers into active participants. These widgets are more than UI elements - they're tools for spatial interaction with your data.

**Core Widget Types:**

1. **Geometric Widgets**: Box, Sphere, Plane, Line
   - Define regions of interest
   - Clip, crop, or select data
   - Measure distances and angles

2. **Control Widgets**: Sliders, Checkboxes, Text
   - Adjust parameters in real-time
   - Toggle visualization features
   - Input numerical values

3. **Path Widgets**: Spline, Line
   - Define trajectories
   - Create cross-sections along paths
   - Animate camera movements

**Widget Architecture:**

```python
# Basic widget pattern
def my_callback(value):
    # Process the widget's value
    # Update the visualization
    pass

plotter.add_widget(widget_type, callback=my_callback)
```

Every widget follows this pattern:

- You define a callback function
- The widget calls your function when users interact
- Your function updates the visualization
- Changes appear immediately

This event-driven approach makes complex interactions surprisingly simple to implement."

## Box Widget - Spatial Selection (2 minutes)

"Let's start with one of the most flexible widgets - the box widget. It's perfect for selecting regions of interest in 3D space.

```python
import pyvista as pv
from pyvista import examples

# Load a detailed 3D model
mesh = examples.download_nefertiti()

# Create plotter and add mesh with box widget
p = pv.Plotter()
p.add_mesh_clip_box(mesh, color='white')
p.show(cpos=[-1, -1, 0.2])

# After interaction, access the clipped result
clipped = p.box_clipped_meshes
```

**Key Features:**

- **Interactive Handles**: Drag corners to resize, faces to translate
- **Real-time Clipping**: See results as you adjust
- **Precise Control**: Hold Shift for constrained movement
- **Multiple Modes**: Clip (remove outside) or crop (keep inside)

**Advanced Usage:**

```python
def custom_box_callback(planes):
    # planes contains the 6 planes of the box
    clipped = mesh.clip_box(planes, invert=False)
    # Process clipped mesh further
    volume = clipped.volume
    print(f'Selected volume: {volume:.2f}')

p.add_box_widget(callback=custom_box_callback)
```

**Applications:**

- Separating anatomical structures in medical data
- Selecting regions for detailed analysis
- Making cutaway views for technical illustrations
- Defining computational domains"

## Plane Widget - Slicing and Clipping (2.5 minutes)

"The plane widget is important for exploring internal structures. It provides an easy way to create cross-sections through your data.

```python
# Load volumetric data
vol = examples.download_brain()

# Clipping with a plane
p = pv.Plotter()
p.add_mesh_clip_plane(vol)
p.show()

# Or slicing to get 2D cross-sections
p = pv.Plotter()
p.add_mesh_slice(vol)
p.show()
```

**Plane Interaction Methods:**

1. **Translation**: Click and drag the plane
2. **Rotation**: Drag the edges to rotate
3. **Normal Alignment**: Right-click for quick alignment to axes

**Advanced Plane Operations:**

```python
# Custom plane callback for vector field visualization
def plot_vectors_on_plane(normal, origin):
    # Create slice through the data
    slice = mesh.slice(normal=normal, origin=origin)

    # Sample vector field on the slice
    vectors = slice['vectors']

    # Clear previous glyphs and add new ones
    p.remove_actor('glyphs')
    p.add_arrows(slice.points, vectors, mag=0.1, name='glyphs')

p.add_plane_widget(callback=plot_vectors_on_plane)
```

**Real-World Applications:**

- Medical imaging: Navigate through CT/MRI scans
- Engineering: Analyze stress distributions in cross-sections
- Geoscience: Explore subsurface structures
- CFD: Visualize flow patterns at different planes

The plane widget is very powerful when combined with scalar fields, letting you see how values change throughout a volume."

## Slider Widgets - Parameter Control (2 minutes)

"Sliders provide easy control over continuous parameters. PyVista offers both traditional slider bars and new slider widgets.

```python
# Create a mesh that responds to parameters
sphere = pv.Sphere()

p = pv.Plotter()
actor = p.add_mesh(sphere)

# Add slider to control opacity
def update_opacity(value):
    actor.GetProperty().SetOpacity(value)

p.add_slider_widget(
    callback=update_opacity,
    rng=[0, 1],
    value=1,
    title="Opacity",
    pointa=(0.1, 0.1),
    pointb=(0.4, 0.1),
    style='modern',
)

# Add slider for mesh resolution
def update_resolution(value):
    res = int(value)
    new_sphere = pv.Sphere(theta_resolution=res, phi_resolution=res)
    actor.mapper.SetInputData(new_sphere)

p.add_slider_widget(
    callback=update_resolution,
    rng=[5, 50],
    value=20,
    title="Resolution",
    pointa=(0.6, 0.1),
    pointb=(0.9, 0.1),
    style='modern',
)

p.show()
```

**Slider Features:**

- **Multiple Styles**: 'classic', 'modern', custom
- **Flexible Positioning**: Screen or 3D space placement
- **Value Display**: Shows current value
- **Custom Formatting**: Control number display format

**Multi-Slider for Coupled Parameters:**

````python
# Control multiple related parameters
p.add_mesh(mesh, scalars='elevation', clim=[0, 100])

def update_color_range(values):
    p.update_scalar_bar_range([values[0], values[1]])

p.add_slider_widget(
    callback=lambda value: update_color_range([value, current_max]),
    rng=[0, 100],
    title="Min",
)
```"

## Advanced Widget Combinations (2 minutes)
"The real power comes from combining widgets to create smart interactions:

```python
# Example: Interactive mesh analysis tool
import numpy as np

# Load engineering mesh with stress data
mesh = examples.download_shaft()

p = pv.Plotter()
p.add_mesh(mesh, scalars='Stress', cmap='jet')

# Box widget for region selection
def analyze_region(planes):
    clipped = mesh.clip_box(planes)
    if clipped.n_points > 0:
        avg_stress = np.mean(clipped['Stress'])
        max_stress = np.max(clipped['Stress'])
        p.add_text(f'Avg: {avg_stress:.2f}\nMax: {max_stress:.2f}',
                   name='stats')

p.add_box_widget(callback=analyze_region)

# Plane widget for cross-section analysis
def show_cross_section(normal, origin):
    slice = mesh.slice(normal=normal, origin=origin)
    p.remove_actor('slice')
    p.add_mesh(slice, name='slice', lighting=False)

p.add_plane_widget(callback=show_cross_section)

# Sphere widget for point query
def query_point(center):
    # Find closest point on mesh
    closest_id = mesh.find_closest_point(center)
    value = mesh['Stress'][closest_id]
    p.add_point_labels([center], [f'{value:.2f}'],
                      name='query', font_size=20)

p.add_sphere_widget(callback=query_point, radius=0.05)

p.show()
````

This makes a complete analysis environment where users can:

- Select regions with the box
- Create cross-sections with the plane
- Query specific points with the sphere
- All widgets work together smoothly"

## Web-Based Visualization with Trame (2.5 minutes)

"Trame integration brings PyVista to the web, making browser-based interactive visualizations without plugins.

```python
from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vuetify, vtk

import pyvista as pv

# Create server
server = get_server()
state, ctrl = server.state, server.controller

# Load your data
mesh = examples.download_dragon()

# Create PyVista plotter
plotter = pv.Plotter()
actor = plotter.add_mesh(mesh, color='red')

# Build web UI
with SinglePageLayout(server) as layout:
    layout.title.set_text("PyVista Web App")

    with layout.toolbar:
        # Add color picker
        vuetify.VColorPicker(
            v_model=("color", "red"),
            hide_inputs=True,
        )

        # Add opacity slider
        vuetify.VSlider(
            v_model=("opacity", 1),
            min=0, max=1, step=0.1,
            label="Opacity",
        )

    with layout.content:
        # Embed 3D view
        view = vtk.VtkRemoteView(plotter.render_window)
        ctrl.view_update = view.update

# Define state changes
@state.change("color")
def update_color(color, **kwargs):
    actor.prop.color = color
    ctrl.view_update()

@state.change("opacity")
def update_opacity(opacity, **kwargs):
    actor.prop.opacity = opacity
    ctrl.view_update()

# Start server
server.start()
```

**Trame Advantages:**

- **No Installation**: Users need only a web browser
- **Remote Rendering**: Server-side GPU, client-side interaction
- **Rich UI**: Full HTML/CSS/JavaScript capabilities
- **Responsive**: Works on desktop, tablet, mobile
- **Collaborative**: Multiple users can view same session

**Deployment Options:**

- Local development server
- Cloud platforms (AWS, Azure, GCP)
- Jupyter integration
- Desktop app with embedded browser"

## Best Practices and Performance (1.5 minutes)

"Here are key practices for making good interactive visualizations:

**Making Things Faster:**

1. **Level of Detail**: Use decimated meshes for interaction

```python
# High-res for display, low-res for interaction
display_mesh = original_mesh
interact_mesh = original_mesh.decimate(0.9)
```

2. **Callback Efficiency**: Make computation in callbacks smaller

```python
# Precompute when possible
cache = precompute_expensive_operation()

def fast_callback(value):
    result = cache[value]  # Lookup instead of compute
    update_display(result)
```

3. **Update Strategies**: Use render=False for batch updates

```python
def multi_update():
    actor1.SetVisibility(False)  # Don't render yet
    actor2.SetPosition(x, y, z)   # Don't render yet
    plotter.render()              # Single render call
```

**User Experience:**

1. **Visual Feedback**: Show widget state clearly
2. **Constraints**: Limit widget ranges to valid values
3. **Defaults**: Start with meaningful initial views
4. **Instructions**: Add text hints for complex interactions
5. **Responsiveness**: Keep callbacks under 100ms

**Code Organization:**

```python
class InteractiveAnalyzer:
    def __init__(self, mesh):
        self.mesh = mesh
        self.plotter = pv.Plotter()
        self.setup_scene()
        self.setup_widgets()

    def setup_scene(self):
        # Initial visualization setup
        pass

    def setup_widgets(self):
        # Widget configuration
        pass
```

## Real-World Example (1 minute)
"Let's see these concepts in a real application - an interactive stress analysis tool:

```python
# Engineering stress analysis application
mesh = examples.download_bracket()

class StressAnalyzer:
    def __init__(self):
        self.plotter = pv.Plotter()
        self.mesh = mesh
        self.setup()

    def setup(self):
        # Main mesh with stress visualization
        self.plotter.add_mesh(
            self.mesh,
            scalars='von_mises_stress',
            cmap='turbo',
            clim=[0, 500]
        )

        # Plane widget for cross-sections
        self.plotter.add_plane_widget(
            callback=self.analyze_plane,
            normal='x'
        )

        # Text display for results
        self.plotter.add_text('Analysis Results',
                             position='upper_right')

    def analyze_plane(self, normal, origin):
        # Create cross-section
        section = self.mesh.slice(normal=normal, origin=origin)

        # Calculate statistics
        if section.n_points > 0:
            max_stress = section['von_mises_stress'].max()
            avg_stress = section['von_mises_stress'].mean()

            # Update display
            self.plotter.add_mesh(section, name='section',
                                lighting=False, opacity=0.5)

            text = f'Max Stress: {max_stress:.1f} MPa\n'
            text += f'Avg Stress: {avg_stress:.1f} MPa'
            self.plotter.add_text(text, name='results',
                                position='upper_right')

analyzer = StressAnalyzer()
analyzer.plotter.show()
```

This creates a professional tool for engineering analysis with minimal code."

## Conclusion and Next Steps (30 seconds)

"We've looked at PyVista's interactive capabilities:

- Rich ecosystem powering diverse applications
- Desktop widgets for 3D interaction
- Web deployment with Trame
- Best practices for responsive interfaces

Key takeaways:

1. Widgets change passive viewers into active explorers
2. Callbacks connect user actions to data updates
3. Combine widgets for smart workflows
4. Trame enables browser-based deployment
5. Performance matters - optimize for smooth interaction

Your next steps:

- Try widgets on your own data
- Look at the PyVista examples gallery
- Try building a Trame web application
- Join the PyVista community for support

Remember: Interactive visualization isn't just about technology - it's about helping users to find insights in their data. PyVista gives you the tools to make that happen."

---

## Timing Breakdown

- Introduction: 1 minute
- Ecosystem Overview: 2 minutes
- Interactive Widgets Overview: 2 minutes
- Box Widget: 2 minutes
- Plane Widget: 2.5 minutes
- Slider Widgets: 2 minutes
- Advanced Combinations: 2 minutes
- Trame Web Apps: 2.5 minutes
- Best Practices: 1.5 minutes
- Real Example: 1 minute
- Conclusion: 0.5 minutes
  **Total: 15 minutes**

## Presenter Notes

1. **Live Demos**: Have pre-coded examples ready to run
2. **Interaction Time**: Allow brief pauses for audiences to see widgets in action
3. **Fallback Plan**: Have recorded GIFs/videos if live demos fail
4. **Code Snippets**: Keep them concise, focus on concepts
5. **Audience Engagement**: Ask about their visualization needs
6. **Platform Check**: Ensure demos work on presentation hardware
7. **Network**: For Trame demos, ensure network connectivity
