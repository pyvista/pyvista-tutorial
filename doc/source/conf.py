# Configuration file for the Sphinx documentation builder.

import os
from pathlib import Path
import sys

if sys.version_info >= (3, 0):
    import faulthandler

    faulthandler.enable()

sys.path.insert(0, str(Path(__file__).absolute().parent))
import make_external_gallery

make_external_gallery.make_example_gallery()

# -- PyVista configuration ---------------------------------------------------
import pyvista

# Manage errors
pyvista.set_error_output_file('errors.txt')
# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True  # Not necessary - simply an insurance policy
# Preferred plotting style for documentation
pyvista.set_plot_theme('document')
pyvista.global_theme.window_size = [1024, 768]
pyvista.global_theme.font.size = 22
pyvista.global_theme.font.label_size = 22
pyvista.global_theme.font.title_size = 22
pyvista.global_theme.return_cpos = False
pyvista.set_jupyter_backend(None)
# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(os.path.abspath('./images/'), 'auto-generated/')
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True
os.environ['PYVISTA_BUILDING_GALLERY'] = 'true'


# -- Project information -----------------------------------------------------

project = 'PyVista Tutorial'
copyright = '2022, PyVista Developers'
author = 'PyVista Developers'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.asciinema',
    'sphinx_tabs.tabs',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'jupyter_sphinx',
    'sphinx_copybutton',
    'sphinx_panels',
    'sphinx_gallery.gen_gallery',
    'jupyter_sphinx',
    'pyvista.ext.plot_directive',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "numpy": ("https://numpy.org/devdocs", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "pyvista": ("https://docs.pyvista.org/", None),
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

html_title = project
html_short_title = ''
# html_favicon = '_static/favicon.png'
html_extra_path = []  # TODO: 'CNAME',
html_use_smartypants = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_context = {
    'github_user': 'pyvista',
    'github_repo': 'pyvista-tutorial',
    'github_version': 'main',
    'doc_path': 'doc',
}
html_logo = "./_static/pyvista_logo_sm.png"

html_theme_options = {
    # 'default_mode': 'light',
    # 'google_analytics_id': '',
    'show_prev_next': True,
    'github_url': 'https://github.com/pyvista/pyvista-tutorial',
    'icon_links': [
        {
            'name': 'Support',
            'url': 'https://github.com/pyvista/pyvista/discussions',
            'icon': 'fa fa-comment fa-fw',
        },
        {
            'name': 'Docs',
            'url': 'https://docs.pyvista.org/',
            'icon': 'fa fa-book fa-fw',
        },
        {
            'name': 'Slack Community',
            'url': 'http://slack.pyvista.org',
            'icon': 'fab fa-slack',
        },
        {
            'name': 'Contributing',
            'url': 'https://github.com/pyvista/pyvista/blob/main/CONTRIBUTING.rst',
            'icon': 'fa fa-gavel fa-fw',
        },
        {
            'name': 'The Paper',
            'url': 'https://doi.org/10.21105/joss.01450',
            'icon': 'fa fa-file-text fa-fw',
        },
    ],
    'navbar_end': ['navbar-icon-links'],
}

html_sidebars = {
    'index': [],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']


# notfound_context = {
#     'body': '''
# <h1>Page not found.</h1>\n\nPerhaps try the <a href='/'>home page.</a>.
# <br>
# ''',
# }
notfound_no_urls_prefix = True

# Copy button customization
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r'>>> ?|\.\.\. '
copybutton_prompt_is_regexp = True

# sphinx-panels shouldn't add bootstrap css since the pydata-sphinx-theme
# already loads it
panels_add_bootstrap_css = False


# -- sphinx-gallery --------
from sphinx_gallery.sorting import FileNameSortKey

tutorial_dirs = [
    '../../tutorial/00_intro/',
    '../../tutorial/01_basic/',
    '../../tutorial/02_mesh/',
    '../../tutorial/03_data/',
    '../../tutorial/04_break/',
    '../../tutorial/05_figures/',
    '../../tutorial/06_sphinx/',
    '../../tutorial/07_break/',
    '../../tutorial/08_vtk/',
    '../../tutorial/09_qt/',
]

sphinx_gallery_conf = {
    # convert rst to md for ipynb
    'pypandoc': True,
    # path to your examples scripts
    'examples_dirs': tutorial_dirs,
    # path where to save gallery generated examples
    'gallery_dirs': [d.lstrip('../../') for d in tutorial_dirs],
    # Pattern to search for example files
    'filename_pattern': r'\.py',
    # Remove the 'Download all examples' button from the top level gallery
    'download_all_examples': False,
    # Remove sphinx configuration comments from code blocks
    'remove_config_comments': True,
    # Sort gallery example by file name instead of number of lines (default)
    'within_subsection_order': FileNameSortKey,
    # directory where function granular galleries are stored
    'backreferences_dir': None,
    # Modules for which function level galleries are created.  In
    'doc_module': 'pyvista',
    'image_scrapers': ('pyvista', 'matplotlib'),
    'first_notebook_cell': '%matplotlib inline\n'
    'from pyvista import set_plot_theme\n'
    'set_plot_theme("document")\n',
}


def setup(app):
    app.add_css_file('copybutton.css')
    app.add_css_file('no_search_highlight.css')
    app.add_css_file('fontawesome/css/all.css')
