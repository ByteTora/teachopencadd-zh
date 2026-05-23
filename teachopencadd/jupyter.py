from pathlib import Path

import nbformat

from .console import print_err, print_status
from .exceptions import TeachOpenCADDError
from .models import Environment
from .runner import run_command


def setup_jupyter(env: Environment, nb_file: Path) -> None:
    """Update the notebook's kernelspec metadata to point at *env*."""
    nb = nbformat.read(nb_file, as_version=4)
    nb.metadata.kernelspec = {
        "name": env.name.lower(),
        "display_name": f"TeachOpenCADD: {env.name}",
        "language": "python",
    }
    nbformat.write(nb, nb_file)


def test_talktorial(
    nb_file: Path,
    env: Environment,
    env_vars: dict[str, str],
) -> None:
    """Install pytest + nbval into *env* and run them against *nb_file*."""
    if not nb_file.exists():
        raise TeachOpenCADDError(f"Could not find notebook for testing: {nb_file}")

    run_command(
        ["uv", "pip", "install", "--python", str(env.py_exe), "pytest", "nbval"]
    )

    print_status("Running pytest with nbval...\n")
    run_command(
        [str(env.py_exe), "-m", "pytest", "--nbval-lax", "--current-env", str(nb_file)],
        env=env_vars,
        capture_output=False,
    )
