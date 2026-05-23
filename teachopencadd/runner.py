import subprocess
import sys
from typing import Any

from rich.panel import Panel

from .console import print_err, print_status, printc
from .exceptions import TeachOpenCADDError


def run_command(command: list[Any], **kwargs: Any) -> subprocess.CompletedProcess:
    """
    Run *command* via subprocess.

    Raises TeachOpenCADDError on non-zero exit so callers decide whether to abort.
    Pass ``check=True`` to make non-zero exits propagate automatically; omit it to
    inspect the return value yourself.
    """
    kwargs.setdefault("capture_output", False)
    kwargs.setdefault("text", True)

    cmd_str = " ".join(map(str, command))
    print_status(f"Run '{cmd_str}'")

    try:
        result = subprocess.run(command, shell=False, **kwargs)
    except KeyboardInterrupt:
        printc("")

        printc(Panel.fit("[bold]Shutting down TeachOpenCADD.[/bold]"))
        sys.exit(0)
    except FileNotFoundError:
        raise TeachOpenCADDError(f"Command not found: {command[0]}")

    if result.returncode != 0:
        printc(Panel(cmd_str, title="[red]Command Failed[/red]", border_style="red"))
        if result.stdout:
            printc(Panel(result.stdout, title="stdout", border_style="yellow"))
        if result.stderr:
            printc(Panel(result.stderr, title="stderr", border_style="red"))
        raise TeachOpenCADDError(
            f"Command exited with code {result.returncode}: {cmd_str}"
        )

    return result
