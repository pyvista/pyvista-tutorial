"""Fix for offlineviewer directive to support nested output directories.

When using atsphinx-mini18n with ``mini18n_build_style = "nested"``, the Japanese
sub-build outputs to ``build/mini18n-html/ja/``. The upstream
``pyvista.ext.viewer_directive`` computes the build root as ``outdir.parent``, which
gives ``build/mini18n-html/`` instead of the correct ``build/``.  This causes the
``is_path_relative_to`` check to fail and the directive to return an empty node list,
leaving the "Interactive Scene" tab empty.

The fix: derive the build root from ``doctreedir.parent`` instead of ``outdir.parent``.
Both the English and Japanese mini18n builds share the same ``doctreedir``
(``build/.doctrees``), so ``doctreedir.parent = build/`` is correct for both.
"""

from __future__ import annotations

import os
from pathlib import Path
import shutil

from docutils import nodes
from docutils.utils import relative_path  # pragma: no cover
from sphinx.util import logging
from trame_vtk.tools.vtksz2html import HTML_VIEWER_PATH

logger = logging.getLogger(__name__)


def _is_path_relative_to(path: Path, other: Path) -> bool:
    return path.is_relative_to(other)


class FixedOfflineViewerDirective:
    """Replacement for OfflineViewerDirective with corrected build-root detection."""

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):  # pragma: no cover
        source_dir = Path(self.state.document.settings.env.app.srcdir)
        output_dir = Path(self.state.document.settings.env.app.outdir)
        # Use doctreedir.parent as the build root so that nested output directories
        # (e.g., build/mini18n-html/ja/ produced by atsphinx-mini18n) resolve
        # correctly.  Both the primary and language sub-builds share the same
        # doctreedir (build/.doctrees), so doctreedir.parent == build/ in all cases.
        build_dir = Path(self.state.document.settings.env.app.doctreedir).parent

        # path passed to ``.. offlineviewer:: <path>``
        source_file = str(Path(self.state.document.current_source).parent / self.arguments[0])
        source_file = Path(source_file).absolute().resolve()
        if not source_file.is_file():
            logger.warning(f'Source file {source_file} does not exist.')
            return []

        # copy viewer HTML to _static
        static_path = output_dir / '_static'
        static_path.mkdir(exist_ok=True)
        viewer_name = Path(HTML_VIEWER_PATH).name
        if not (static_path / viewer_name).exists():
            shutil.copy(HTML_VIEWER_PATH, static_path)

        if _is_path_relative_to(source_file, build_dir):
            dest_partial_path = source_file.parent.relative_to(build_dir)
        elif _is_path_relative_to(source_file, source_dir):
            dest_partial_path = source_file.parent.relative_to(source_dir)
        else:
            logger.warning(
                f'Source file {source_file} is not a subpath of either the build '
                f'directory or the source directory. Cannot extract base path.',
            )
            return []

        dest_path = output_dir / '_images' / dest_partial_path
        dest_path.mkdir(parents=True, exist_ok=True)
        dest_file = (dest_path / source_file.name).resolve()
        if source_file != dest_file:
            try:
                shutil.copy(source_file, dest_file)
            except Exception as e:  # noqa: BLE001
                logger.warning(f'Failed to copy file from {source_file} to {dest_file}: {e}')

        relpath_to_source_root = relative_path(self.state.document.current_source, source_dir)
        rel_viewer_path = (
            Path() / relpath_to_source_root / '_static' / viewer_name
        ).as_posix()
        rel_asset_path = Path(os.path.relpath(dest_file, static_path)).as_posix()
        html = (
            f"<iframe src='{rel_viewer_path}?fileURL={rel_asset_path}' "
            "width='100%%' height='400px' frameborder='0'></iframe>"
        )
        return [nodes.raw('', html, format='html')]


def setup(app):
    """Re-register the offlineviewer directive with the fixed implementation."""
    from docutils.parsers.rst import Directive

    # Merge the Directive base class into FixedOfflineViewerDirective at
    # registration time so it satisfies docutils' class-hierarchy check.
    FixedClass = type(
        'OfflineViewerDirective',
        (FixedOfflineViewerDirective, Directive),
        {},
    )
    app.add_directive('offlineviewer', FixedClass, override=True)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
