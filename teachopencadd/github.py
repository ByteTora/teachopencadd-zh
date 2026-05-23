import os
from pathlib import Path

import requests
from rich.progress import track

from .config import Settings, settings as default_settings
from .console import print_err, print_status, print_step, print_warn
from .exceptions import TeachOpenCADDError


def github_get(
    api_url: str, params: dict | None = None, timeout: int = 15
) -> dict | list:
    """Perform an unauthenticated (or token-authenticated) GET to the GitHub API."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "teachopencadd-runner",
    }
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"token {token}"

    try:
        r = requests.get(api_url, headers=headers, params=params, timeout=timeout)
    except requests.RequestException as exc:
        raise TeachOpenCADDError(
            f"Network error while accessing {api_url}: {exc}"
        ) from exc

    if r.status_code == 403 and "rate limit" in r.text.lower():
        raise TeachOpenCADDError(
            "GitHub API rate limit reached (HTTP 403). "
            "Set the GITHUB_TOKEN environment variable to increase your limit."
        )
    if r.status_code != 200:
        raise TeachOpenCADDError(
            f"GitHub API error {r.status_code} for {api_url}: {r.text}"
        )
    return r.json()


def _fetch_folder_contents(
    api_url: str,
    branch: str,
    raw_base: str,
    exclude_files: tuple[str, ...] = (),
) -> list[tuple[str, str]]:
    """Recursively return ``[(repo_path, raw_download_url), ...]`` for *api_url*."""
    items = github_get(api_url, params={"ref": branch})
    file_list: list[tuple[str, str]] = []

    for item in items:
        item_type = item.get("type")
        name = item.get("name")
        path = item.get("path")

        if item_type == "file":
            if name in exclude_files:
                continue
            raw_url = f"{raw_base}/{branch}/{path}"
            file_list.append((path, raw_url))
        elif item_type == "dir":
            file_list.extend(
                _fetch_folder_contents(item["url"], branch, raw_base, exclude_files)
            )
        else:
            print_status(f"Skipping unsupported type '{item_type}' at {path}")

    return file_list


def _download_file(raw_url: str, local_path: Path, timeout: int = 30) -> bool:
    """Download *raw_url* to *local_path*. Returns True on success."""
    local_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = requests.get(raw_url, timeout=timeout)
    except requests.RequestException as exc:
        print_warn(f"Network error downloading {raw_url}: {exc}")
        return False

    if r.status_code == 200:
        local_path.write_bytes(r.content)
        return True

    print_err(f"Failed to download {raw_url} (HTTP {r.status_code})")
    return False


def _resolve_remote_folder_name(t_id: str, cfg: Settings) -> str:
    """Ask the GitHub API for the full folder name that starts with *t_id*."""
    root_url = cfg.api_base + cfg.api_root_path.rstrip("/")
    root_contents = github_get(root_url, params={"ref": cfg.branch})

    for item in root_contents:
        if item["type"] == "dir" and item["name"].startswith(f"{t_id}_"):
            return item["name"]

    raise TeachOpenCADDError(
        f"Could not find a talktorial matching '{t_id}' on GitHub."
    )


def fetch_talktorial(
    t_id: str,
    data_only: bool = False,
    cfg: Settings = default_settings,
) -> Path:
    """
    Ensure the talktorial folder for *t_id* is present locally.

    If ``data_only=True``, only data files are downloaded (README and the
    notebook are skipped) and files land in the current directory.
    Returns the local :class:`Path` to the talktorial folder.
    """
    print_step(
        "Download talktorial data"
        if data_only
        else "Ensuring talktorial contents are available"
    )

    existing = list(Path(".").glob(f"{t_id}_*"))
    if existing:
        return existing[0]

    print_status(f"{t_id} not found locally. Querying GitHub API...")
    folder_name = _resolve_remote_folder_name(t_id, cfg)

    exclude = cfg.exclude_files
    if data_only:
        exclude = exclude + ("README.md", "talktorial.ipynb")

    output_dir = Path(".") if data_only else Path(folder_name)
    output_dir.mkdir(exist_ok=True)

    api_folder_url = cfg.api_base + cfg.api_root_path + folder_name
    print_status(
        f"Fetching file list for '{folder_name}' from branch '{cfg.branch}'..."
    )

    all_files = _fetch_folder_contents(
        api_folder_url, cfg.branch, cfg.raw_base, exclude
    )
    print_status(f"Found {len(all_files)} file(s) to download.")

    prefix = cfg.api_root_path + folder_name
    for repo_path, raw_url in track(all_files, description="Downloading files..."):
        rel = os.path.relpath(repo_path, prefix)
        local_path = output_dir / rel

        if local_path.exists():
            try:
                if local_path.stat().st_size > 0:
                    continue
            except OSError:
                pass

        _download_file(raw_url, local_path)

    print_status(f"Done. Files saved to: ./{output_dir}")
    return output_dir
