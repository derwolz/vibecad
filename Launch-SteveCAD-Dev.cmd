@rem SPDX-License-Identifier: LGPL-2.1-or-later
@echo off
setlocal
cd /d "%~dp0"

powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0Launch-SteveCAD-Dev.ps1" %*

if errorlevel 1 (
    echo.
    echo SteveCAD development launch failed.
    pause
)
