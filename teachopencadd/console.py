import sys
from typing import Any
from rich.console import Console
from rich.panel import Panel

_console = Console()

IS_WIN = sys.platform.startswith("win")
ARROW = "->" if IS_WIN else "→"
CROSS = "X" if IS_WIN else "✖"


def printc(message: Any) -> None:
    _console.print(message)


def print_err(message: str) -> None:
    printc(f"[bold red]{CROSS} Error:[/bold red] {message}")


def print_step(message: str) -> None:
    printc(Panel.fit(f"[bold]{message}[/bold]"))


def print_status(message: str) -> None:
    printc(f"[bold blue]{ARROW}[/bold blue] {message}")


def print_warn(message: str) -> None:
    printc(f"[bold yellow]{ARROW}[/bold yellow] {message}")
