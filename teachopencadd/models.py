from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Environment:
    """All derived paths and metadata for a single talktorial environment."""

    name: str
    path: Path
    is_conda: bool
    py_ver: str

    @property
    def py_exe(self) -> Path:
        if sys.platform.startswith("win"):
            return (
                self.path / "python.exe"
                if self.is_conda
                else self.path / "Scripts" / "python.exe"
            )
        return self.path / "bin" / "python"

    @property
    def bin_dir(self) -> Path:
        return self.py_exe.parent


@dataclass
class Talktorial:
    """Paths that belong to a single talktorial."""

    t_id: str  # e.g. "T001"
    directory: Path  # root folder on disk

    @property
    def req_file(self) -> Path:
        return self.directory / "requirements.txt"

    @property
    def nb_file(self) -> Path:
        return self.directory / "talktorial.ipynb"
