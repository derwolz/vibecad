/*
init.nsh

Initialization functions
*/

#--------------------------------
# User initialization

Var FCLangName

Function InitUser

  # Get FreeCAD language
  
  ReadRegStr $FCLangName SHELL_CONTEXT "${APP_REGKEY_SETUP}" "FreeCAD Language"
  
  ${If} $FCLangName != ""
    StrCpy $LangName $FCLangName
  ${EndIf}
  
FunctionEnd

#--------------------------------
# Installed-version discovery and clean replacement

Function FindInstalledSteveCAD

  StrCpy $OldVersionNumber ""
  StrCpy $SteveCADInstalledBuild ""
  StrCpy $SteveCADInstalledDisplayVersion ""
  StrCpy $SteveCADInstalledDisposition "none"
  StrCpy $SteveCADInstalledInstallRoot ""
  StrCpy $SteveCADInstalledPatch ""
  StrCpy $SteveCADInstalledReleaseVersion ""
  StrCpy $SteveCADInstalledUninstallString ""
  StrCpy $SteveCADInstalledUpdateVersion ""

  # Find the highest installed patch in this major/minor series. Historical
  # SteveCAD/FreeCAD installers used one registry key per patch release.
  IntOp $4 ${APP_VERSION_PATCH} + 20
  ${for} $5 0 $4
    StrCpy $R0 "${APP_VERSION_MAJOR}${APP_VERSION_MINOR}$5"
    StrCpy $R2 "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}$R0"
    ReadRegStr $0 SHCTX "$R2" "DisplayVersion"
    ${if} $0 == ""
      # Preserve discovery of the legacy emergency-release key shape.
      StrCpy $R0 "${APP_VERSION_MAJOR}${APP_VERSION_MINOR}$51"
      StrCpy $R2 "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}$R0"
      ReadRegStr $0 SHCTX "$R2" "DisplayVersion"
    ${endif}
    ${if} $0 != ""
      StrCpy $OldVersionNumber $R0
      StrCpy $SteveCADInstalledPatch $5
      StrCpy $SteveCADInstalledDisplayVersion $0
      ReadRegStr $SteveCADInstalledUninstallString SHCTX "$R2" "UninstallString"
      StrCpy $R3 "SOFTWARE\${APP_NAME}$OldVersionNumber"
      ReadRegStr $SteveCADInstalledInstallRoot SHCTX "$R3" ""
      ReadRegStr $SteveCADInstalledReleaseVersion SHCTX "$R3" "ReleaseVersion"
      ReadRegStr $SteveCADInstalledUpdateVersion SHCTX "$R3" "UpdateVersion"
      ClearErrors
      ReadRegDWORD $1 SHCTX "$R3" "Build"
      ${if} ${Errors}
        StrCpy $SteveCADInstalledBuild ""
        ClearErrors
      ${else}
        StrCpy $SteveCADInstalledBuild $1
      ${endif}
    ${endif}
  ${next}

FunctionEnd

Function SelectExistingSteveCADInstallMode

  # The MultiUser plug-in normally restores the install scope from the target
  # patch's registry key. Search the entire major/minor series as a migration
  # fallback so a new patch still updates the existing per-user/per-machine
  # installation instead of creating a second copy in another scope.
  StrCpy $6 ""
  StrCpy $7 ""
  IntOp $4 ${APP_VERSION_PATCH} + 20
  ${for} $5 0 $4
    StrCpy $R0 "${APP_VERSION_MAJOR}${APP_VERSION_MINOR}$5"
    ReadRegStr $0 HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}$R0" "DisplayVersion"
    ${if} $0 != ""
      ReadRegStr $6 HKLM "SOFTWARE\${APP_NAME}$R0" ""
    ${endif}
    ReadRegStr $0 HKCU "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}$R0" "DisplayVersion"
    ${if} $0 != ""
      ReadRegStr $7 HKCU "SOFTWARE\${APP_NAME}$R0" ""
    ${endif}
  ${next}

  ${if} $6 != ""
  ${andif} $7 == ""
    Call MultiUser.InstallMode.AllUsers
  ${elseif} $7 != ""
  ${andif} $6 == ""
    Call MultiUser.InstallMode.CurrentUser
  ${elseif} $6 != ""
  ${andif} $7 != ""
  ${andif} $SteveCADUpdateInstallRoot != ""
    GetFullPathName $6 "$6"
    GetFullPathName $7 "$7"
    GetFullPathName $0 "$SteveCADUpdateInstallRoot"
    ${if} $0 == $6
      Call MultiUser.InstallMode.AllUsers
    ${elseif} $0 == $7
      Call MultiUser.InstallMode.CurrentUser
    ${endif}
  ${endif}

FunctionEnd

Function ClassifyInstalledSteveCAD

  StrCpy $SteveCADInstalledDisposition "unknown"

  # Installers produced after this change persist a fully sortable numeric
  # identity. It includes semantic version, prerelease rank, and build.
  !if "${APP_VERSION_ORDER_KNOWN}" == "1"
    ${if} $SteveCADInstalledUpdateVersion != ""
      ${VersionCompare} "${APP_UPDATE_VERSION}" "$SteveCADInstalledUpdateVersion" $0
      ${if} $0 == "1"
        StrCpy $SteveCADInstalledDisposition "upgrade"
      ${elseif} $0 == "0"
        StrCpy $SteveCADInstalledDisposition "repair"
      ${else}
        StrCpy $SteveCADInstalledDisposition "downgrade"
      ${endif}
      Return
    ${endif}
  !endif

  # Compatibility with already-published installers: exact public releases
  # have always persisted ReleaseVersion and Build separately.
  ${if} $SteveCADInstalledReleaseVersion == "${APP_RELEASE_VERSION}"
  ${andif} $SteveCADInstalledBuild != ""
    ${if} $SteveCADInstalledBuild < ${APP_VERSION_BUILD}
      StrCpy $SteveCADInstalledDisposition "upgrade"
    ${elseif} $SteveCADInstalledBuild == ${APP_VERSION_BUILD}
      StrCpy $SteveCADInstalledDisposition "repair"
    ${else}
      StrCpy $SteveCADInstalledDisposition "downgrade"
    ${endif}
    Return
  ${endif}

  # Patch releases have an unambiguous order even for a legacy install.
  ${if} $SteveCADInstalledPatch != ""
    ${if} $SteveCADInstalledPatch < ${APP_VERSION_PATCH}
      StrCpy $SteveCADInstalledDisposition "upgrade"
      Return
    ${elseif} $SteveCADInstalledPatch > ${APP_VERSION_PATCH}
      StrCpy $SteveCADInstalledDisposition "downgrade"
      Return
    ${endif}
  ${endif}

  # A final release sorts after a legacy prerelease of the same patch. A
  # prerelease must never replace an installed final release automatically.
  !if "${APP_VERSION_SUFFIX}" == ""
    ${if} $SteveCADInstalledReleaseVersion != ""
    ${andif} $SteveCADInstalledReleaseVersion != "${APP_VERSION_MAJOR}.${APP_VERSION_MINOR}.${APP_VERSION_PATCH}"
      StrCpy $SteveCADInstalledDisposition "upgrade"
    ${endif}
  !else
    ${if} $SteveCADInstalledReleaseVersion == "${APP_VERSION_MAJOR}.${APP_VERSION_MINOR}.${APP_VERSION_PATCH}"
      StrCpy $SteveCADInstalledDisposition "downgrade"
    ${endif}
  !endif

FunctionEnd

Function BeginManualSteveCADReplacement

  StrCpy $SteveCADUpdateMode "manual"
  StrCpy $SteveCADUpdateInstallRoot $SteveCADInstalledInstallRoot
  Call ValidateSteveCADUpdateInstallRoot
  ${if} ${Errors}
    StrCpy $SteveCADUpdateMode "false"
    MessageBox MB_OK|MB_ICONSTOP "$(InvalidExistingInstall)" /SD IDOK
    SetErrorLevel 28
    Quit
  ${endif}
  ClearErrors

FunctionEnd

Function SteveCADDirectoryPagePre

  # A replacement must use the registered installation root. Skipping the
  # directory page prevents a clean upgrade from being redirected midway.
  ${if} $SteveCADUpdateMode == "install"
  ${orif} $SteveCADUpdateMode == "manual"
    Abort
  ${endif}

FunctionEnd

#--------------------------------
# MultiUser custom method

Function PostMultiUserPageInit
  Call FindInstalledSteveCAD

  ${if} $OldVersionNumber == ""
    Return
  ${endif}

  # The verified in-app updater already supplies a silent, pinned install root.
  # Preserve that path while sharing the same clean replacement sections.
  ${if} $SteveCADUpdateMode != "false"
    Return
  ${endif}

  Call ClassifyInstalledSteveCAD

  ${if} $SteveCADInstalledDisposition == "upgrade"
    MessageBox MB_OKCANCEL|MB_ICONINFORMATION "$(UpgradeInstalled)" /SD IDOK IDOK AcceptManualReplacement
    Goto CancelManualReplacement
  ${elseif} $SteveCADInstalledDisposition == "repair"
    MessageBox MB_YESNO|MB_ICONQUESTION "$(RepairInstalled)" /SD IDNO IDYES AcceptManualReplacement
    Goto CancelManualReplacement
  ${elseif} $SteveCADInstalledDisposition == "downgrade"
    MessageBox MB_OK|MB_ICONSTOP "$(DowngradeBlocked)" /SD IDOK
    SetErrorLevel 27
    Quit
  ${else}
    MessageBox MB_YESNO|MB_ICONEXCLAMATION "$(ReplaceUnknownInstalled)" /SD IDNO IDYES AcceptManualReplacement
    Goto CancelManualReplacement
  ${endif}

  AcceptManualReplacement:
    Call BeginManualSteveCADReplacement
    Return

  CancelManualReplacement:
    ${if} ${Silent}
      Quit
    ${else}
      Abort
    ${endif}
FunctionEnd


#--------------------------------
# visible installer sections

Section "!${APP_NAME}" SecCore
 SectionIn RO
SectionEnd

Section "$(SecFileAssocTitle)" SecFileAssoc
 StrCpy $CreateFileAssociations "true" 
SectionEnd

Section "$(SecDesktopTitle)" SecDesktop
 StrCpy $CreateDesktopIcon "true"
SectionEnd

# Section descriptions
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecCore} "$(SecCoreDescription)"
!insertmacro MUI_DESCRIPTION_TEXT ${SecFileAssoc} "$(SecFileAssocDescription)"
!insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "$(SecDesktopDescription)"
!insertmacro MUI_FUNCTION_DESCRIPTION_END


# .onInit must be here after the section definition because we have to set
# the selection states of the dictionary sections
Function .onInit

  StrCpy $SteveCADUpdateMode "false"
  StrCpy $SteveCADUpdateInstallRoot ""
  StrCpy $OldVersionNumber ""
  ${GetParameters} $R8
  ClearErrors
  ${GetOptions} $R8 "/STEVECADUPDATE" $R9
  ${IfNot} ${Errors}
    StrCpy $SteveCADUpdateMode "install"
  ${EndIf}
  ClearErrors
  ${GetOptions} $R8 "/STEVECADROLLBACK" $R9
  ${IfNot} ${Errors}
    StrCpy $SteveCADUpdateMode "rollback"
  ${EndIf}
  ClearErrors
  ${GetOptions} $R8 "/STEVECADINSTALLROOT=" $SteveCADUpdateInstallRoot

  ${if} $SteveCADUpdateMode != "false"
   ${IfNot} ${Silent}
    SetErrorLevel 25
    Quit
   ${EndIf}
  ${endif}

  ReadRegStr $R0 HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion" CurrentVersion
  ${if} $R0 == "5.0" # 2000
  ${orif} $R0 == "5.1" # XP
  ${orif} $R0 == "5.2" # 2003
  ${orif} $R0 == "6.0" # Vista
  ${orif} $R0 == "6.1" # 7
    MessageBox MB_OK|MB_ICONSTOP "${APP_NAME} ${APP_VERSION} requires Windows 8 or newer." /SD IDOK
    Quit
  ${endif}
  
  # check if it is a 64bit system
  ${if} ${RunningX64}
   SetRegView 64
   !define LIBRARY_X64
  ${endif}
  
  # Check that FreeCAD is not currently running
  StrCpy $R1 0
  CheckSteveCADProcess:
  ${nsProcess::FindProcess} ${BIN_FREECAD} $R0
  # if running result is '0', if not running it is '603'
  ${if} $R0 == "0"
   ${if} $SteveCADUpdateMode != "false"
    IntOp $R1 $R1 + 1
    ${if} $R1 >= 600
     ${nsProcess::Unload}
     SetErrorLevel 20
     Quit
    ${endif}
    Sleep 500
    Goto CheckSteveCADProcess
   ${else}
    MessageBox MB_OK|MB_ICONSTOP "$(UnInstallRunning)" /SD IDOK
    Abort
   ${endif}
  ${endif}
  # plugin must be unloaded
  ${nsProcess::Unload}
  
  # initialize the multi-user installer UI
  !insertmacro MULTIUSER_INIT
  Call SelectExistingSteveCADInstallMode

  # this can be reset to "true" in section SecDesktop
  StrCpy $CreateDesktopIcon "false"
  StrCpy $CreateFileAssociations "false"
 
  ${IfNot} ${Silent}
    # Show banner while installer is initializing 
    Banner::show /NOUNLOAD "Checking system"
    Banner::destroy
  ${EndIf}

  # if installer runs silent the post install mode page routine has to be called here
  ${If} ${Silent}
    Call PostMultiUserPageInit
  ${endif}

  ${if} $SteveCADUpdateMode != "false"
    Call ValidateSteveCADUpdateInstallRoot
    ${If} ${Errors}
      SetErrorLevel 25
      Quit
    ${EndIf}
  ${endif}

  ${if} $SteveCADUpdateMode == "rollback"
    Call RestoreSteveCADUpdateBackup
    SetErrorLevel 24
    ${IfNot} ${Errors}
      SetErrorLevel 0
    ${EndIf}
    Quit
  ${endif}

FunctionEnd

Function ValidateSteveCADUpdateInstallRoot

  ${if} $SteveCADUpdateInstallRoot == ""
    SetErrors
    Return
  ${endif}
  StrCpy $R2 "${APP_REGKEY}"
  ${if} $OldVersionNumber != ""
    StrCpy $R2 "SOFTWARE\${APP_NAME}$OldVersionNumber"
  ${endif}
  ReadRegStr $R3 SHCTX "$R2" ""
  ${if} $R3 == ""
    SetErrors
    Return
  ${endif}
  GetFullPathName $R3 "$R3"
  GetFullPathName $SteveCADUpdateInstallRoot "$SteveCADUpdateInstallRoot"
  StrCmp $R3 $SteveCADUpdateInstallRoot 0 ValidateSteveCADUpdateInstallRootFailed
  IfFileExists "$R3\bin\SteveCAD.exe" 0 ValidateSteveCADUpdateInstallRootFailed
  StrCpy $INSTDIR $R3
  ClearErrors
  Return

  ValidateSteveCADUpdateInstallRootFailed:
    SetErrors
    Return

FunctionEnd

Function RestoreSteveCADUpdateBackup

  StrCpy $SteveCADUpdateBackupDir "$INSTDIR.stevecad-rollback"
  StrCpy $SteveCADUpdateFailedDir "$INSTDIR.stevecad-failed"
  IfFileExists "$SteveCADUpdateBackupDir\bin\SteveCAD.exe" 0 RestoreSteveCADUpdateFailed
  IfFileExists "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" 0 RestoreSteveCADUpdateFailed
  ReadINIStr $R2 "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "UninstallKey"
  ReadINIStr $R3 "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "AppKey"
  ${if} $R2 == ""
  ${orif} $R3 == ""
    Goto RestoreSteveCADUpdateFailed
  ${endif}
  SetOutPath "$TEMP"
  RMDir /r "$SteveCADUpdateFailedDir"
  IfFileExists "$SteveCADUpdateFailedDir\*.*" 0 RestoreSteveCADUpdateFailedReady
    Goto RestoreSteveCADUpdateFailed
  RestoreSteveCADUpdateFailedReady:
  StrCpy $R5 "false"
  IfFileExists "$INSTDIR\*.*" 0 RestoreSteveCADUpdateBackupTree
  ClearErrors
  Rename "$INSTDIR" "$SteveCADUpdateFailedDir"
  IfErrors RestoreSteveCADUpdateFailed
  StrCpy $R5 "true"
  RestoreSteveCADUpdateBackupTree:
  ClearErrors
  Rename "$SteveCADUpdateBackupDir" "$INSTDIR"
  IfErrors 0 RestoreSteveCADUpdateTreeReady
    ${if} $R5 == "true"
      Rename "$SteveCADUpdateFailedDir" "$INSTDIR"
    ${endif}
    Goto RestoreSteveCADUpdateFailed
  RestoreSteveCADUpdateTreeReady:
  RMDir /r "$SteveCADUpdateFailedDir"

  DeleteRegKey SHCTX "${APP_UNINST_KEY}"
  DeleteRegKey SHCTX "${APP_REGKEY}"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "DisplayName"
  WriteRegStr SHCTX "$R2" "DisplayName" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "DisplayVersion"
  WriteRegStr SHCTX "$R2" "DisplayVersion" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "UninstallString"
  WriteRegStr SHCTX "$R2" "UninstallString" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "QuietUninstallString"
  WriteRegStr SHCTX "$R2" "QuietUninstallString" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "DisplayIcon"
  WriteRegStr SHCTX "$R2" "DisplayIcon" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "StartMenu"
  WriteRegStr SHCTX "$R2" "StartMenu" "$R4"
  WriteRegStr SHCTX "$R2" "URLUpdateInfo" "${APP_WEBPAGE}"
  WriteRegStr SHCTX "$R2" "URLInfoAbout" "${APP_WEBPAGE}"
  WriteRegStr SHCTX "$R2" "Publisher" "${APP_NAME} Project"
  WriteRegStr SHCTX "$R2" "HelpLink" "${APP_WEBPAGE}/issues"
  WriteRegDWORD SHCTX "$R2" "NoModify" 0x00000001
  WriteRegDWORD SHCTX "$R2" "NoRepair" 0x00000001
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "InstallPath"
  WriteRegStr SHCTX "$R3" "" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "Version"
  WriteRegStr SHCTX "$R3" "Version" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "ReleaseVersion"
  WriteRegStr SHCTX "$R3" "ReleaseVersion" "$R4"
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "UpdateVersion"
  ${if} $R4 == ""
    DeleteRegValue SHCTX "$R3" "UpdateVersion"
  ${else}
    WriteRegStr SHCTX "$R3" "UpdateVersion" "$R4"
  ${endif}
  ReadINIStr $R4 "$INSTDIR\stevecad-update-registry.ini" "Registry" "Build"
  WriteRegDWORD SHCTX "$R3" "Build" $R4
  Delete "$INSTDIR\stevecad-update-registry.ini"
  ClearErrors
  Return

  RestoreSteveCADUpdateFailed:
    SetErrors
    Return

FunctionEnd

# this function is called at first after starting the uninstaller
Function un.onInit

  # Macro to investigate name of FreeCAD's preferences folders to be able remove them
  !insertmacro UnAppPreSuff $AppPre $AppSuff # macro from Utils.nsh

  !insertmacro MULTIUSER_UNINIT

  # Check that FreeCAD is not currently running
  ${nsProcess::FindProcess} ${BIN_FREECAD} $R0
  # if running result is '0', if not running it is '603'
  ${if} $R0 == "0"
   MessageBox MB_OK|MB_ICONSTOP "$(UnInstallRunning)" /SD IDOK
   Abort
  ${endif}
  # plugin must be unloaded
  ${nsProcess::Unload}
  
  # check if it is a 64bit system
  ${if} ${RunningX64}
   SetRegView 64
  ${endif}

  # Ascertain whether the user has sufficient privileges to uninstall.
  # abort when FreeCAD was installed with admin permissions but the user doesn't have administrator privileges
  ReadRegStr $0 HKLM "${APP_UNINST_KEY}" "DisplayVersion"
  ${if} $0 != ""
  ${andif} $MultiUser.Privileges != "Admin"
  ${andif} $MultiUser.Privileges != "Power"
   MessageBox MB_OK|MB_ICONSTOP "$(UnNotAdminLabel)" /SD IDOK
   Abort
  ${endif}
  # warning when FreeCAD couldn't be found in the registry
  ${if} $0 == "" # check in HKCU
   ReadRegStr $0 HKCU "${APP_UNINST_KEY}" "DisplayVersion"
   ${if} $0 == ""
     MessageBox MB_OK|MB_ICONEXCLAMATION "$(UnNotInRegistryLabel)" /SD IDOK
   ${endif}
  ${endif}

  # question message if the user really wants to uninstall FreeCAD
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "$(UnReallyRemoveLabel)" /SD IDYES IDYES +2 # continue if yes
  Abort

FunctionEnd
