"""
TeachOpenCADD is a collection of Jupyter Notebooks
to help you learn or teach computer aided drug design concepts.

The notebooks themselves are located under ``教程/``.
"""

from .config import Settings, settings
from .exceptions import TeachOpenCADDError

try:
    from importlib.metadata import version as _get_version

    __version__ = _get_version("teachopencadd")
except Exception:
    __version__ = "0.0.0"

__all__ = ["Settings", "settings", "TeachOpenCADDError"]
