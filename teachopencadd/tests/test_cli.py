"""
Unit tests for Command Line Interface.
"""

import subprocess


def capture(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_cli_help():
    """Test `teachopencadd -h` shows help."""
    out, err, exitcode = capture(["teachopencadd", "-h"])
    assert exitcode == 0
    assert "TeachOpenCADD" in out
    assert not err


def test_cli_list():
    """Test `teachopencadd -l` lists tutorials."""
    out, err, exitcode = capture(["teachopencadd", "-l"])
    assert exitcode == 0
    assert "T001" in out
    assert not err


def test_cli_no_args():
    """Test `teachopencadd` alone shows help."""
    out, err, exitcode = capture(["teachopencadd"])
    assert exitcode == 0
    assert "usage" in out.lower() or "帮助" in out or "TeachOpenCADD" in out
