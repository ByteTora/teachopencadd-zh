import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Settings:
    env_prefix: str = "teachopencadd"
    base_dir: Path = Path("teachopencadd") / "教程"
    env_root: Path = field(
        default_factory=lambda: Path.home() / ".teachopencadd_envs"
    )
    req_file: str = "requirements.txt"
    talktorial_file: str = "talktorial.ipynb"
    is_win: bool = field(default_factory=lambda: sys.platform.startswith("win"))
    repo_owner: str = "volkamerlab"
    repo_name: str = "teachopencadd"
    branch: str = "master"
    exclude_files: tuple[str, ...] = (".gitignore",)
    api_root_path: str = "teachopencadd/talktorials/"

    @property
    def api_base(self) -> str:
        return (
            f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents/"
        )

    @property
    def raw_base(self) -> str:
        return f"https://raw.githubusercontent.com/{self.repo_owner}/{self.repo_name}"


settings = Settings()
