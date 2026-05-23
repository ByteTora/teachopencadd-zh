import os
import re
import shutil
import sys
from pathlib import Path

from .config import Settings, settings as default_settings
from .console import print_err, print_status, print_step
from .exceptions import TeachOpenCADDError
from .models import Environment
from .runner import run_command


def parse_requirements(
    req_file: Path,
) -> tuple[str, list[str], list[str]]:
    """
    Parse a talktorial requirements file.

    Returns ``(py_version, conda_packages, pip_packages)``.
    Lines marked ``# conda`` go to the conda list; everything else is pip.
    A comment like ``#python=3.11`` overrides the default Python version.
    """
    py_version = "3.11"
    conda_pkgs: list[str] = []
    pip_pkgs: list[str] = []

    py_pattern = re.compile(r"#python\s*[=:]\s*([\d\.]+)", re.IGNORECASE)
    conda_tag = re.compile(r"^([^#]+)\s*#\s*conda\b", re.IGNORECASE)

    if not req_file.exists():
        return py_version, conda_pkgs, pip_pkgs

    with open(req_file) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue

            if m := py_pattern.search(line):
                py_version = m.group(1)
                continue

            if line.startswith("#"):
                continue

            if m := conda_tag.match(line):
                conda_pkgs.append(m.group(1).strip())
            else:
                pkg = line.split("#")[0].strip()
                if pkg:
                    pip_pkgs.append(pkg)

    return py_version, conda_pkgs, pip_pkgs


def _get_conda_bin() -> str:
    for name in ("micromamba", "mamba", "conda"):
        path = shutil.which(name)
        if path:
            return path
    raise TeachOpenCADDError(
        "Could not find micromamba/mamba/conda. Please install one."
    )


def configure_env(
    t_id: str,
    req_file: Path,
    cfg: Settings = default_settings,
) -> Environment:
    """
    Create (or reuse) the environment for *t_id* and return an :class:`Environment`.

    Uses UV-backed venvs when there are no conda dependencies; falls back to
    micromamba/mamba/conda otherwise.
    """
    print_step("Environment setup")
    print_status(f"Environment directory: {cfg.env_root}")
    py_ver, conda_pkgs, pip_pkgs = parse_requirements(req_file)

    env_name = f"{cfg.env_prefix}_{t_id}_py{py_ver.replace('.', '')}"
    env_path = cfg.env_root / env_name
    is_conda = bool(conda_pkgs)
    env = Environment(name=env_name, path=env_path, is_conda=is_conda, py_ver=py_ver)

    if not is_conda:
        _setup_uv_env(env, pip_pkgs, cfg.env_root)
    else:
        _setup_conda_env(env, conda_pkgs, pip_pkgs, cfg.env_root)

    return env


def _setup_uv_env(env: Environment, pip_pkgs: list[str], env_root: Path) -> None:
    print_status(
        f"[Pip/UV Mode] No conda dependencies. Building venv for {env.name}..."
    )
    if not env.path.exists():
        env_root.mkdir(parents=True, exist_ok=True)
        run_command(["uv", "venv", str(env.path), "--python", env.py_ver])

    if pip_pkgs:
        run_command(["uv", "pip", "install", "--python", str(env.py_exe), *pip_pkgs])


def _setup_conda_env(
    env: Environment,
    conda_pkgs: list[str],
    pip_pkgs: list[str],
    env_root: Path,
) -> None:
    print_status(
        f"[Conda Mode] Conda dependencies found. Using solver for {env.name}..."
    )
    conda = _get_conda_bin()
    mamba_root = env_root / "mamba_cache"
    mamba_root.mkdir(exist_ok=True, parents=True)

    env_vars = {**os.environ, "MAMBA_ROOT_PREFIX": str(mamba_root)}

    run_command(
        [
            conda,
            "create",
            "-p",
            str(env.path),
            f"python={env.py_ver}",
            "-c",
            "conda-forge",
            "--yes",
        ],
        env=env_vars,
    )

    if conda_pkgs:
        run_command(
            [
                conda,
                "install",
                "-p",
                str(env.path),
                "-c",
                "conda-forge",
                *conda_pkgs,
                "--yes",
            ],
            env=env_vars,
        )

    if pip_pkgs:
        run_command(["uv", "pip", "install", "--python", str(env.py_exe), *pip_pkgs])


def build_jupyter_env_vars(env: Environment) -> dict[str, str]:
    """
    Return a copy of the current environment augmented with all variables
    needed to run Jupyter (and Python) inside *env* in isolation.
    """
    private_jupyter_dir = env.path / "share" / "jupyter"
    site_packages = env.path / "lib" / f"python{env.py_ver}" / "site-packages"

    env_vars = os.environ.copy()
    env_vars.update(
        {
            "PYTHONNOUSERSITE": "1",
            "JUPYTER_DATA_DIR": str(private_jupyter_dir),
            "JUPYTER_RUNTIME_DIR": str(private_jupyter_dir / "runtime"),
            "JUPYTER_CONFIG_DIR": str(private_jupyter_dir / "config"),
            "JUPYTER_PATH": str(private_jupyter_dir),
            "PYTHONPATH": str(site_packages),
            "PATH": f"{env.bin_dir}{os.pathsep}{env_vars.get('PATH', '')}",
        }
    )

    if env.is_conda:
        env_vars["CONDA_PREFIX"] = str(env.bin_dir.parent)
        mamba_root = env.path.parent / "mamba_cache"
        env_vars["MAMBA_ROOT_PREFIX"] = str(mamba_root)

    if not sys.platform.startswith("win"):
        lib_dir = str(env.bin_dir.parent / "lib")
        env_vars["LD_LIBRARY_PATH"] = (
            f"{lib_dir}{os.pathsep}{env_vars.get('LD_LIBRARY_PATH', '')}"
        )

    return env_vars


def cleanup(force: bool, cfg: Settings = default_settings) -> None:
    """Remove managed environments (and optionally the mamba cache)."""
    print_step("Environment cleanup")

    if not cfg.env_root.exists():
        print_status(f"No environment directory found at {cfg.env_root}.")
        return

    pattern = re.compile(rf"^{cfg.env_prefix}_T\d{{3}}_")
    envs = [d for d in cfg.env_root.iterdir() if d.is_dir() and pattern.match(d.name)]

    if not envs:
        print_status("No managed environments found.")
        return

    print_status(f"Found {len(envs)} environment(s) in {cfg.env_root}.")

    from rich.prompt import Confirm

    for env_path in sorted(envs):
        if not force and not Confirm.ask(f"Remove environment '{env_path.name}'?"):
            continue

        print_status(f"Deleting folder: {env_path}...")
        try:
            shutil.rmtree(env_path)
        except Exception as exc:
            raise TeachOpenCADDError(f"Error deleting {env_path}: {exc}") from exc

    mamba_cache = cfg.env_root / "mamba_cache"
    if mamba_cache.exists():
        if force or Confirm.ask("Clear Mamba package cache?"):
            print_status("Clearing cache...")
            shutil.rmtree(mamba_cache)

    print_status("Cleanup complete.")
