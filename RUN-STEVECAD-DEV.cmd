@rem SPDX-License-Identifier: LGPL-2.1-or-later
@echo off
setlocal
cd /d "%~dp0"

if not exist "%~dp0Launch-SteveCAD-Dev.cmd" (
    echo.
    echo SteveCAD development launcher is missing:
    echo   %~dp0Launch-SteveCAD-Dev.cmd
    echo.
    pause
    exit /b 1
)

call "%~dp0Launch-SteveCAD-Dev.cmd" %*
exit /b %errorlevel%
