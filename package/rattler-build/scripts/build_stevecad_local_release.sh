#!/usr/bin/env bash

set -euo pipefail

script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd "${script_directory}/../../.." && pwd)"
build_root="${repository_root}/build/release"
environment_root="${repository_root}/.pixi/envs/default"
module_directory="${build_root}/Mod/SteveCAD"

if [[ -x "${environment_root}/bin/python" ]]; then
    python_executable="${environment_root}/bin/python"
elif [[ -x "${environment_root}/python.exe" ]]; then
    python_executable="${environment_root}/python.exe"
else
    echo "SteveCAD release Python is missing from ${environment_root}." >&2
    exit 1
fi

cmake --build "${build_root}"

"${script_directory}/purge_stevecad_retired_authoring_artifacts.sh" \
    "${build_root}" \
    "${module_directory}"

freecadcmd_executable=""
for candidate in \
    "${build_root}/bin/FreeCADCmd" \
    "${build_root}/bin/FreeCADCmd.exe" \
    "${build_root}/bin/Release/FreeCADCmd.exe"; do
    if [[ -x "${candidate}" ]]; then
        freecadcmd_executable="${candidate}"
        break
    fi
done

if [[ -z "${freecadcmd_executable}" ]]; then
    echo "The SteveCAD release build produced no FreeCADCmd executable." >&2
    exit 1
fi
if [[ ! -f "${module_directory}/SteveCADCodex.py" ]]; then
    echo "The SteveCAD release module is incomplete: ${module_directory}." >&2
    exit 1
fi

"${script_directory}/install_stevecad_provider_deps.sh" "${environment_root}"
"${script_directory}/install_stevecad_codex_runtime.sh" \
    "${python_executable}" \
    "${module_directory}"

"${freecadcmd_executable}" --safe-mode --version
"${freecadcmd_executable}" --safe-mode -c \
    "import importlib.util, anthropic, jsonschema, keyring, mcp, mcp_types, openai, numpy, casadi, neuralfoil, aerosandbox, jsbsim; assert int(numpy.__version__.split('.', 1)[0]) < 2; assert importlib.util.find_spec('agents') is None; print('SteveCAD Python and Aero dependencies import ok')"
"${freecadcmd_executable}" --safe-mode -c \
    "import FreeCAD as App, AeroResults; from SteveCADAeroContext import document_aero_summary; doc=App.newDocument('SteveCADAeroReportSmoke'); AeroResults.write_report(doc, {'CL': 0.81, 'CD': 0.037, 'CM': -0.021, 'CLalpha': 5.1, 'Cmalpha': -0.4, 'PitchUnstable': False, 'source': 'smoke', 'corrections': ['Pitch stable.']}); assistant=doc.getObject('AeroAssistantJson'); assert assistant is not None; assert getattr(doc, 'AeroAssistantJson') is assistant; summary=document_aero_summary(doc); assert summary['assistant_json']['CL'] == 0.81; App.closeDocument(doc.Name); print('SteveCAD Aero report document smoke ok')"
"${freecadcmd_executable}" --safe-mode -c \
    "from SteveCADProvider import _provider_subprocess_smoke; _provider_subprocess_smoke(); print('SteveCAD provider subprocess smoke ok')"
"${freecadcmd_executable}" --safe-mode -c \
    "from SteveCADCodex import runtime_execution_smoke; result = runtime_execution_smoke(); print('SteveCAD Codex app-server smoke ok', result['version'])"
"${freecadcmd_executable}" --safe-mode -c \
    "from SteveCADGeometry import runtime_execution_smoke; result = runtime_execution_smoke(); print('SteveCAD geometry worker smoke ok', result['worker'])"

echo "SteveCAD local release is runtime-complete: ${build_root}"
