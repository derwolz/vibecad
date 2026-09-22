# SPDX-License-Identifier: LGPL-2.1-or-later

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STEVECAD_ROOT = ROOT.parent / "SteveCAD"

for module_root in (STEVECAD_ROOT, ROOT):
    if str(module_root) not in sys.path:
        sys.path.insert(0, str(module_root))
