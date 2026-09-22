@echo off
setlocal EnableExtensions
REM Agent entry for Windows. Prefer a running SteveCAD GUI over starting Cmd.
set "SCRIPT_DIR=%~dp0"
set "CLI=%SCRIPT_DIR%SteveCADAgentCli.py"

where python >nul 2>&1
if %ERRORLEVEL%==0 (
    python "%CLI%" --gui-only %*
    if %ERRORLEVEL%==0 exit /b 0
    if %ERRORLEVEL%==1 exit /b 1
)

set "CMD_EXE="
if defined STEVECAD_CMD set "CMD_EXE=%STEVECAD_CMD%"
if not defined CMD_EXE if exist "%SCRIPT_DIR%..\..\bin\SteveCADCmd.exe" set "CMD_EXE=%SCRIPT_DIR%..\..\bin\SteveCADCmd.exe"
if not defined CMD_EXE if exist "%SCRIPT_DIR%..\..\bin\FreeCADCmd.exe" set "CMD_EXE=%SCRIPT_DIR%..\..\bin\FreeCADCmd.exe"

if not defined CMD_EXE (
    echo {"ok": false, "failure_code": "CMD_NOT_FOUND", "failure_stage": "precondition", "error": "Neither a listening SteveCAD GUI nor FreeCADCmd.exe/SteveCADCmd.exe was found. Start SteveCAD.exe or set STEVECAD_CMD."}
    exit /b 1
)

"%CMD_EXE%" "%CLI%" --local %*
exit /b %ERRORLEVEL%
