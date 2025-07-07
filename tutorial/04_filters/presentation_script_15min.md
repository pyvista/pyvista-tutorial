# PyVista Filters Tutorial - 15-Minute Presentation Script

## Introduction (1 minute)

"Welcome to the PyVista filters tutorial. I'm excited to guide you through one of the most powerful features of PyVista - data filtering.

In scientific visualization, we often work with complex 3D datasets that have more information than we can show at once. Filters are our tools for getting, changing, and highlighting the specific information we need. Think of filters as smart data mining tools that help us find patterns and insights hidden in our 3D data.

Today, we'll look at how PyVista makes these powerful operations easy through a simple, Pythonic interface."

## What Are Filters and Why Use Them? (2 minutes)

"Before we dive into code, let's understand what filters are. In 3D visualization, filters are algorithms that change datasets. They can:

- Get parts of data based on rules
- Make new quantities from existing data
- Create geometric shapes of abstract data
- Make complex geometries simpler for analysis

The VTK library, which PyVista wraps, has hundreds of filters. PyVista makes the most common ones available as simple method calls on your data objects. This means instead of writing complex VTK pipeline code, you can simply call `dataset.threshold()` or `dataset.slice()`.

The beauty of PyVista's approach is that filters are easy to find - they're methods on your data objects, so your IDE can help you find them. They're also chainable, letting you build complex processing pipelines with readable code."

## Overview of Common Filters (2.5 minutes)

"Let's look at the most commonly used filters in detail:

**Slice Filters:**

- `slice()`: Makes a single flat cut through your data. Perfect for looking at internal structures.
- `slice_orthogonal()`: Makes three perpendicular slices, giving you cross-sections along X, Y, and Z axes at the same time.
- `slice_along_axis()`: Makes multiple parallel slices along a specified axis - great for animation or detailed analysis.

**Threshold Filters:**

- `threshold()`: Keeps only cells where scalar values are within a specified range. Important for focusing on regions of interest.
- `threshold_percent()`: Similar to threshold, but uses percentages of the scalar range - useful when you don't know exact values.

**Geometric Filters:**

- `clip()`: Cuts your dataset with a plane, keeping only one side. Different from slice - this keeps 3D geometry.
- `extract_geometry()`: Gets the outer surface of your dataset.
- `outline_corners()`: Makes a wireframe box showing data extents - perfect for context in visualizations.

**Analysis Filters:**

- `contour()`: Makes isosurfaces or isolines at specified scalar values.
- `glyph()`: Places geometric shapes (arrows, spheres, etc.) at data points, scaled or oriented by data values.

Each of these filters has parameters you can adjust to fine-tune the results."

## Loading Data and Setting Up (1.5 minutes)

"Let's start with hands-on examples. First, we'll load a sample dataset and get it ready for filtering:

```python
import pyvista as pv
from pyvista import examples

# Load a structured dataset with scalar values
dataset = examples.load_uniform()
print(f"Dataset type: {type(dataset)}")
print(f"Number of points: {dataset.n_points}")
print(f"Number of cells: {dataset.n_cells}")

# Check available scalar arrays
print(f"Available arrays: {dataset.array_names}")

# Set the active scalars - this determines what values filters will use
dataset.set_active_scalars("Spatial Point Data")
```

Understanding your data is very important before filtering. Always check:

- The type of dataset (structured, unstructured, etc.)
- Available scalar and vector arrays
- Data ranges and distribution

This information helps your filter choices and parameter selection."

## Basic Threshold Filter - Deep Dive (2.5 minutes)

"The threshold filter is one of the most basic operations. Let's look at it carefully:

```python
# First, let's examine our scalar range
scalar_range = dataset.get_data_range()
print(f"Scalar range: {scalar_range}")

# Apply threshold keeping values between 100 and 500
threshed = dataset.threshold([100, 500])

# What happened?
print(f"Original cells: {dataset.n_cells}")
print(f"Remaining cells: {threshed.n_cells}")
print(f"Percentage kept: {threshed.n_cells/dataset.n_cells*100:.1f}%")
```

The threshold filter removes entire cells where any point falls outside the range. This is important to understand - it's not interpolating or changing values, it's making yes/no decisions about what to keep.

You can also use single values:

```python
# Keep only values above 300
above_300 = dataset.threshold(300)

# Keep only values below 200
below_200 = dataset.threshold(upper=200)
```

For more flexibility, use percentage-based thresholds:

```python
# Keep the middle 50% of the data range
middle_half = dataset.threshold_percent(0.25, 0.75)
```

This is very useful when working with datasets where you don't know the exact scalar ranges beforehand."

## Visualizing Filter Results (2 minutes)

"Visualization is key to understanding filter effects. Let's make a complete view:

```python
# Create outline for reference
outline = dataset.outline()

# Set up the plotter
p = pv.Plotter()
p.add_mesh(outline, color="k", line_width=2)
p.add_mesh(threshed, scalars="Spatial Point Data",
           opacity=0.8, clim=scalar_range)

# Add text annotation
p.add_text(f"Threshold: [100, 500]\nCells kept: {threshed.n_cells}/{dataset.n_cells}",
           position='upper_left')

# Set a good viewing angle
p.camera_position = [-2, 5, 3]
p.show()
```

Key visualization tips:

- Always include context (like outlines) to show what's been removed
- Use consistent color scales (clim) when comparing filtered results
- Add notes to document your filter parameters
- Think about opacity for better depth perception"

## Comparing Multiple Filters (2.5 minutes)

"Different filters show different parts of your data. Let's apply several and compare:

```python
# Apply various filters
contours = dataset.contour(isosurfaces=5)  # 5 evenly spaced contours
slices = dataset.slice_orthogonal()
glyphs = dataset.glyph(
    factor=1e-3,  # Scale factor
    geom=pv.Sphere(radius=0.5),  # Glyph geometry
    orient=False  # Don't orient glyphs
)

# Advanced: Extract a specific region then apply secondary filter
roi = dataset.extract_subset([10, 30, 10, 30, 10, 30])  # Region of interest
roi_contours = roi.contour()

# Create comparison visualization
p = pv.Plotter(shape=(2, 2), border_width=2)

# Original with outline
p.subplot(0, 0)
p.add_text("Original Data", position='upper_edge')
p.add_mesh(dataset, opacity=0.3)
p.add_mesh(outline, color="k")

# Contours
p.subplot(0, 1)
p.add_text("Contour Filter", position='upper_edge')
p.add_mesh(contours)
p.add_mesh(outline, color="k")

# Orthogonal slices
p.subplot(1, 0)
p.add_text("Orthogonal Slices", position='upper_edge')
p.add_mesh(slices)
p.add_mesh(outline, color="k")

# Glyphs
p.subplot(1, 1)
p.add_text("Glyph Filter", position='upper_edge')
p.add_mesh(glyphs)
p.add_mesh(outline, color="k")

p.link_views()  # Synchronize camera across subplots
p.show()
```

Each filter serves a specific purpose:

- Contours are perfect for finding regions of constant value
- Slices help look at internal structures
- Glyphs show point-based data and vector fields"

## Filter Pipeline - Advanced Techniques (2 minutes)

"PyVista's filter chaining lets you make smart data processing pipelines:

```python
# Complex pipeline example
result = (dataset
    .threshold(value=100, invert=False)  # Remove low values
    .elevation()  # Add height-based scalars
    .clip(normal='z', origin=[0, 0, 0])  # Cut in half
    .extract_geometry()  # Get outer surface
    .smooth(n_iter=100)  # Smooth the surface
    .compute_normals()  # Add surface normals
)

# Analyze the pipeline result
print(f"Pipeline started with: {dataset.n_points} points")
print(f"Pipeline ended with: {result.n_points} points")
print(f"New arrays added: {set(result.array_names) - set(dataset.array_names)}")

# Visualize with normals as arrows
p = pv.Plotter()
p.add_mesh(result, scalars="Elevation", smooth_shading=True)
p.add_arrows(result.cell_centers().points,
             result['Normals'],
             mag=0.1,
             color='red')
p.show()
```

Pipeline best practices:

- Order matters - threshold before expensive operations
- Each filter adds computational cost
- Some filters add new data arrays you can use
- Document your pipeline with comments"

## Performance Considerations and Tips (1 minute)

"When working with big datasets, filter performance becomes very important:

1. **Filter Order**: Apply restrictive filters (threshold, clip) early to make data smaller
2. **Memory Usage**: Filters create new objects - watch memory with big datasets
3. **Caching**: Store intermediate results if you'll reuse them
4. **Decimation**: Use `decimate()` to reduce polygon count before expensive operations

````python
# Example: Efficient pipeline for large data
filtered_data = (large_dataset
    .threshold(important_range)  # Reduce size first
    .decimate(0.5)  # Reduce by 50%
    .smooth()  # Now smoothing is faster
)
```"

## Real-World Applications (1 minute)
"Let's talk about how these filters apply to real problems:

**Medical Imaging**: Use threshold to separate tissue types by density, then isosurface to make 3D organ models

**Computational Fluid Dynamics**: Slice filters to look at flow patterns, contours for pressure distributions, glyphs for velocity vectors

**Geoscience**: Clip to make geological cross-sections, threshold to find ore bodies or aquifers

**Engineering**: Extract geometry for surface stress analysis, use glyphs to show displacement or strain

The key is combining filters creatively to answer your specific questions."

## Key Takeaways and Best Practices (30 seconds)
"Remember these important points:
1. Filters are methods on PyVista objects - easy to understand and find
2. Always understand your data before filtering
3. Filters can be chained for complex operations
4. Show results with context to check filter behavior
5. Think about performance with big datasets
6. Combine multiple filters to get complete insights"

## Closing and Next Steps (30 seconds)
"We've looked at the basic filters in PyVista, but this is just the beginning. The library offers many more specialized filters for specific domains.

Your next steps:
- Try these filters on your own data
- Look at the PyVista documentation for advanced filters
- Try making custom filter pipelines for your specific needs

Thank you for joining this deep dive into PyVista filters. In our next session, we'll look at mesh operations and advanced visualization techniques. Happy filtering!"

---

## Timing Breakdown
- Introduction: 1 minute
- What Are Filters: 2 minutes
- Overview of Filters: 2.5 minutes
- Loading Data: 1.5 minutes
- Threshold Deep Dive: 2.5 minutes
- Visualization: 2 minutes
- Filter Comparison: 2.5 minutes
- Filter Pipeline: 2 minutes
- Performance Tips: 1 minute
- Real-World Applications: 1 minute
- Takeaways: 30 seconds
- Closing: 30 seconds
**Total: 15 minutes**

## Presenter Notes
1. **Pacing**: This script has natural pause points after each code block for live demos
2. **Code Preparation**: Have all code snippets in a notebook, pre-run intensive operations
3. **Interaction**: Ask audience about their data types during real-world applications section
4. **Visual Focus**: Spend time on each visualization, pointing out specific features
5. **Common Issues**: Be prepared to discuss:
   - Memory errors with large datasets
   - Choosing appropriate filter parameters
   - Understanding why certain filters might produce empty results
6. **Resources**: Have links ready to PyVista documentation and example gallery
````
