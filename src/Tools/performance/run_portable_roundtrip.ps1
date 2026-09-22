param(
    [Parameter(Mandatory=$true)][string]$Document,
    [Parameter(Mandatory=$true)][string]$Name,
    [Parameter(Mandatory=$true)][string]$Bundle,
    [string]$BaselineReport,
    [string]$ResultsRoot,
    [switch]$ProfileCallbacks,
    [switch]$ProfileCommandChecks,
    [switch]$ExerciseGeneratedRecompute,
    [switch]$TraceNativeEvents,
    [switch]$AllowTimelineMigration,
    [string[]]$AllowClearedInvalidObjects = @()
)
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
$bundle = (Resolve-Path -LiteralPath $Bundle).Path
$exe = Join-Path $bundle 'SteveCAD.exe'
$probe = Join-Path $PSScriptRoot 'portable_roundtrip_probe.py'
if ($Name -notmatch '^[A-Za-z0-9_-]+$') { throw 'Use a simple diagnostic run name' }
if (-not $ResultsRoot) { $ResultsRoot = Join-Path $root 'build/portable-validation-results' }
$resultsRoot = [IO.Path]::GetFullPath($ResultsRoot)
$run = [IO.Path]::GetFullPath((Join-Path $resultsRoot $Name))
if (-not $run.StartsWith($resultsRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Diagnostic output must remain inside the results directory'
}
if (Test-Path -LiteralPath $run) { throw 'Use a new run name; existing diagnostic evidence is retained' }
$source = (Resolve-Path -LiteralPath $Document).Path
$required = @('SteveCAD.exe', 'bin/python311.dll', 'bin/pythonw.exe', 'bin/Qt6Core.dll',
              'lib/qt6/plugins/platforms/qwindows.dll', 'Mod/SteveCAD/SteveCADGui.py')
foreach ($relative in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $bundle $relative) -PathType Leaf)) {
        throw "Incomplete portable runtime: $relative"
    }
}
New-Item -ItemType Directory -Path $run | Out-Null
$copy = Join-Path $run 'probe-document.FCStd'
$originalHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash
Copy-Item -LiteralPath $source -Destination $copy
if ((Get-FileHash -LiteralPath $copy -Algorithm SHA256).Hash -ne $originalHash) { throw 'Copy checksum mismatch' }

# The root portable launcher establishes Python and Qt from its own bundle.
# Prevent inherited developer/test settings from injecting another runtime.
foreach ($key in @('PYTHONHOME','PYTHONPATH','FC_PYTHONHOME','QT_PLUGIN_PATH',
                   'QT_QPA_PLATFORM_PLUGIN_PATH','STEVECAD_DEV_ROOT','STEVECAD_DEV_COMMIT')) {
    [Environment]::SetEnvironmentVariable($key, $null, 'Process')
}
$env:QT_QPA_PLATFORM = 'windows'
$env:QT_FORCE_STDERR_LOGGING = '1'
$env:PYTHONNOUSERSITE = '1'
$env:PYTHONUSERBASE = Join-Path $run 'python-user'
$env:FREECAD_USER_HOME = Join-Path $run 'freecad-user'
$env:FREECAD_USER_DATA = Join-Path $run 'freecad-data'
$env:FREECAD_USER_TEMP = Join-Path $run 'freecad-temp'
$env:STEVECAD_HOME = Join-Path $run 'stevecad-data'
$env:STEVECAD_AGENT_HOME = Join-Path $run 'agent'
[Environment]::SetEnvironmentVariable('STEVECAD_AGENT_PORT', $null, 'Process')
$env:STEVECAD_ROUNDTRIP_COPY = $copy
$env:STEVECAD_ALLOW_CLEARED_INVALID_OBJECTS = ConvertTo-Json -InputObject @($AllowClearedInvalidObjects) -Compress
$env:STEVECAD_ROUNDTRIP_REPORT = Join-Path $run 'roundtrip.json'
$env:STEVECAD_INPUT_SENDER = Join-Path $PSScriptRoot 'native_input_sender.py'
if ($BaselineReport) {
    $env:STEVECAD_ROUNDTRIP_BASELINE = (Resolve-Path -LiteralPath $BaselineReport).Path
} else {
    [Environment]::SetEnvironmentVariable('STEVECAD_ROUNDTRIP_BASELINE', $null, 'Process')
}
$env:STEVECAD_RESTORE_DETAIL_TRACE = '1'
[Environment]::SetEnvironmentVariable('STEVECAD_PROFILE_CALLBACKS', $(if ($ProfileCallbacks) { '1' } else { $null }), 'Process')
[Environment]::SetEnvironmentVariable('STEVECAD_PROFILE_COMMANDS', $(if ($ProfileCommandChecks) { '1' } else { $null }), 'Process')
[Environment]::SetEnvironmentVariable('STEVECAD_EXERCISE_GENERATED_RECOMPUTE', $(if ($ExerciseGeneratedRecompute) { '1' } else { $null }), 'Process')
[Environment]::SetEnvironmentVariable('STEVECAD_TRACE_NATIVE_EVENTS', $(if ($TraceNativeEvents) { '1' } else { $null }), 'Process')
[Environment]::SetEnvironmentVariable('STEVECAD_ALLOW_TIMELINE_MIGRATION', $(if ($AllowTimelineMigration) { '1' } else { $null }), 'Process')
$argsList = @('--user-cfg', ('"' + (Join-Path $run 'user.cfg') + '"'),
              '--log-file', ('"' + (Join-Path $run 'application.log') + '"'),
              ('"' + $probe + '"'))
$process = Start-Process -FilePath $exe -ArgumentList $argsList -WorkingDirectory $bundle `
    -WindowStyle Hidden -RedirectStandardOutput (Join-Path $run 'stdout.log') `
    -RedirectStandardError (Join-Path $run 'stderr.log') -PassThru
[pscustomobject]@{ LauncherPid=$process.Id; Original=$source; OriginalSha256=$originalHash;
                  Copy=$copy; Executable=$exe; Results=$run } | ConvertTo-Json
