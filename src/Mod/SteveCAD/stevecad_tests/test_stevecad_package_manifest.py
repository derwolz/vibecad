# SPDX-License-Identifier: LGPL-2.1-or-later

from __future__ import annotations

from pathlib import Path
import re


STEVECAD = Path(__file__).resolve().parents[1]


def test_cmake_installs_every_top_level_stevecad_python_module() -> None:
    """A clean package must not depend on files left by an older install."""

    cmake = (STEVECAD / "CMakeLists.txt").read_text(encoding="utf-8")
    match = re.search(
        r"set\(SteveCAD_Scripts\s*(.*?)^\)",
        cmake,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert match is not None
    packaged = set(
        re.findall(r"^[ \t]*([A-Za-z0-9_]+\.py)[ \t]*$", match.group(1), re.MULTILINE)
    )
    source = {path.name for path in STEVECAD.glob("*.py")}

    assert packaged == source
