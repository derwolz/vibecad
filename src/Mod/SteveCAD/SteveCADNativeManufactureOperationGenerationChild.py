# SPDX-License-Identifier: LGPL-2.1-or-later

"""Fixed entry point for isolated Native CAM path generation."""

from pathlib import Path
import os

from SteveCADNativeManufactureOperationGeneration import run_child_request


request = Path(os.environ["STEVECAD_NATIVE_CAM_PATH_REQUEST"]).resolve()
run_child_request(request)
