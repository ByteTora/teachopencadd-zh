import argparse
import sys
from pathlib import Path

from rich.table import Table

from .config import Settings, settings as default_settings
from .console import print_err, print_status, print_step, printc
from .env import build_jupyter_env_vars, cleanup, configure_env
from .exceptions import TeachOpenCADDError
from .github import fetch_talktorial
from .jupyter import setup_jupyter, test_talktorial
from .models import Talktorial
from .runner import run_command

_talktorial_list: list[tuple[str, str]] = [
    ("T001", "化合物数据获取 (ChEMBL)"),
    ("T002", "分子筛选：ADME 和类先导化合物标准"),
    ("T003", "分子筛选：不想要的子结构"),
    ("T004", "基于配体的筛选：化合物相似性"),
    ("T005", "化合物聚类"),
    ("T006", "最大公共子结构"),
    ("T007", "基于配体的筛选：机器学习"),
    ("T008", "蛋白质数据获取：Protein Data Bank (PDB)"),
    ("T009", "基于配体的药效团"),
    ("T010", "结合位点相似性与脱靶预测"),
    ("T011", "在线 API 网络服务查询"),
    ("T012", "从 KLIFS 获取数据"),
    ("T013", "从 PubChem 获取数据"),
    ("T014", "结合位点检测"),
    ("T015", "蛋白质-配体对接"),
    ("T016", "蛋白质-配体相互作用"),
    ("T017", "高级 NGLView 使用"),
    ("T018", "先导化合物优化自动化流程"),
    ("T019", "分子动力学模拟"),
    ("T020", "分子动力学模拟分析"),
    ("T021", "独热编码"),
    ("T022", "基于配体的筛选：神经网络"),
    ("T023", "什么是激酶？"),
    ("T024", "激酶相似性：序列"),
    ("T025", "激酶相似性：激酶口袋 (KiSSim 指纹)"),
    ("T026", "激酶相似性：相互作用指纹"),
    ("T027", "激酶相似性：配体谱"),
    ("T028", "激酶相似性：不同视角比较"),
    ("T033", "分子表示"),
    ("T034", "基于 RNN 的分子性质预测"),
    ("T035", "基于 GNN 的分子性质预测"),
    ("T036", "E(3)-不变图神经网络简介"),
    ("T037", "不确定性估计"),
    ("T038", "蛋白质-配体相互作用预测"),
]


def print_talktorials() -> None:
    table = Table(title="TeachOpenCADD 教程概览")

    table.add_column("ID", style="magenta")
    table.add_column("主题", style="cyan")
    for ident, topic in _talktorial_list:
        table.add_row(ident, topic)

    printc(table)


def _parse_t_id(raw: str) -> str:
    cleaned = raw.lower().lstrip("t").split("_")[0]
    try:
        return f"T{int(cleaned):03d}"
    except ValueError:
        raise TeachOpenCADDError(f"无效的教程 ID: '{raw}'")


def _find_or_fetch_talktorial(t_id: str, cfg: Settings) -> Talktorial:
    matches = list(cfg.base_dir.glob(f"{t_id}_*")) if cfg.base_dir.exists() else []
    if not matches:
        print_status(f"在本地未找到 {t_id}，正在从 GitHub 获取...")
        directory = fetch_talktorial(t_id, cfg=cfg)
    else:
        directory = matches[0]
    return Talktorial(t_id=t_id, directory=directory)


def main(cfg: Settings = default_settings) -> int:
    parser = argparse.ArgumentParser(
        description="TeachOpenCADD 教程运行器",
        epilog="访问 https://projects.volkamerlab.org/teachopencadd 获取更多信息。",
    )
    parser.add_argument("talktorial", nargs="?", help="教程 ID (例如 T001 或 1)")
    parser.add_argument(
        "-c", "--cleanup", action="store_true", help="删除教程环境"
    )
    parser.add_argument(
        "-f", "--force", action="store_true", help="跳过确认提示"
    )
    parser.add_argument(
        "-d", "--download-data", action="store_true", help="仅下载数据"
    )
    parser.add_argument("-t", "--test", action="store_true", help="运行 nbval 测试")
    parser.add_argument(
        "-e",
        "--env-dir",
        type=str,
        default=str(cfg.env_root),
        metavar="DIR",
        help="环境存储位置",
    )
    parser.add_argument(
        "-b",
        "--branch",
        type=str,
        default=cfg.branch,
        metavar="BRANCH",
        help="下载用的 GitHub 分支",
    )
    parser.add_argument(
        "-l", "--list", action="store_true", help="列出所有可用教程"
    )
    args = parser.parse_args()

    if args.list:
        print_talktorials()
        return 0

    cfg.branch = args.branch
    cfg.env_root = Path(args.env_dir)

    try:
        if args.cleanup:
            cleanup(args.force, cfg)
            return 0

        if not args.talktorial:
            print(parser.format_help())
            return 0

        t_id = _parse_t_id(args.talktorial)

        if args.download_data:
            fetch_talktorial(t_id, data_only=True, cfg=cfg)
            return 0

        talk = _find_or_fetch_talktorial(t_id, cfg)
        env = configure_env(t_id, talk.req_file, cfg)
        env_vars = build_jupyter_env_vars(env)

        setup_jupyter(env, talk.nb_file)

        jupyter_bin = env.bin_dir / ("jupyter.exe" if cfg.is_win else "jupyter")
        if not jupyter_bin.exists():
            raise TeachOpenCADDError(f"Jupyter 二进制文件未找到: {jupyter_bin}")

        topic = dict(_talktorial_list)[t_id]
        if args.test:
            print_step(f"测试 {t_id}: {topic}")
            test_talktorial(talk.nb_file, env, env_vars)
            return 0

        print_step(f"启动 {t_id}: {topic}...")
        run_command(
            [str(jupyter_bin), "notebook", str(talk.nb_file), "--port", "9999"],
            env=env_vars,
            capture_output=False,
        )

    except TeachOpenCADDError as exc:
        print_err(str(exc))
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
