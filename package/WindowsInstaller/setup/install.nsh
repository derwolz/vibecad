/*

install.nsh

Installation of program files, dictionaries and external components

*/

#--------------------------------
# Program files
!include LogicLib.nsh

Section -PrepareSteveCADUpdate

  ${if} $SteveCADUpdateMode == "install"
  ${orif} $SteveCADUpdateMode == "manual"
    StrCpy $SteveCADUpdateBackupDir "$INSTDIR.stevecad-rollback"
    IfFileExists "$SteveCADUpdateBackupDir\*.*" 0 PreviousRollbackRemoved
      RMDir /r "$SteveCADUpdateBackupDir"
      IfFileExists "$SteveCADUpdateBackupDir\*.*" 0 PreviousRollbackRemoved
        SetErrorLevel 21
        Quit
    PreviousRollbackRemoved:
    IfFileExists "$INSTDIR\*.*" 0 UpdateInstallDirectoryReady
      StrCpy $R2 "${APP_UNINST_KEY}"
      StrCpy $R3 "${APP_REGKEY}"
      ${if} $OldVersionNumber != ""
        StrCpy $R2 "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}$OldVersionNumber"
        StrCpy $R3 "SOFTWARE\${APP_NAME}$OldVersionNumber"
      ${endif}
      SetOutPath "$TEMP"
      ClearErrors
      Rename "$INSTDIR" "$SteveCADUpdateBackupDir"
      IfErrors 0 +3
        SetErrorLevel 22
        Quit
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "UninstallKey" "$R2"
      IfErrors SteveCADUpdateRegistrySaveFailed
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "AppKey" "$R3"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R2" "DisplayName"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "DisplayName" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R2" "DisplayVersion"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "DisplayVersion" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R2" "UninstallString"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "UninstallString" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R2" "QuietUninstallString"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "QuietUninstallString" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R2" "DisplayIcon"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "DisplayIcon" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R2" "StartMenu"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "StartMenu" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R3" ""
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "InstallPath" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R3" "Version"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "Version" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R3" "ReleaseVersion"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "ReleaseVersion" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegStr $R4 SHCTX "$R3" "UpdateVersion"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "UpdateVersion" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      ReadRegDWORD $R4 SHCTX "$R3" "Build"
      ClearErrors
      WriteINIStr "$SteveCADUpdateBackupDir\stevecad-update-registry.ini" "Registry" "Build" "$R4"
      IfErrors SteveCADUpdateRegistrySaveFailed
      Goto SteveCADUpdateRegistrySaved
      SteveCADUpdateRegistrySaveFailed:
        ClearErrors
        Rename "$SteveCADUpdateBackupDir" "$INSTDIR"
        SetErrorLevel 26
        Quit
      SteveCADUpdateRegistrySaved:
      CreateDirectory "$INSTDIR"
      IfErrors 0 UpdateInstallDirectoryReady
        ClearErrors
        Rename "$SteveCADUpdateBackupDir" "$INSTDIR"
        SetErrorLevel 26
        Quit
    UpdateInstallDirectoryReady:
  ${endif}

SectionEnd

Section -ProgramFiles SecProgramFiles

  # if the $INSTDIR does not contain "FreeCAD" we must add a subfolder to avoid that FreeCAD will e.g.
  # be installed directly to C:\programs - the uninstaller will then delete the whole
  # C:\programs directory
  StrCpy $String "$INSTDIR"
  StrCpy $Search "${APP_NAME}"
  Call StrPoint # function from Utils.nsh
  ${if} $Pointer == "-1"
   StrCpy $INSTDIR "$INSTDIR\${APP_DIR}"
  ${endif}
  
  # turn on logging
  # Note that this can first be done here since the log file is written to $INSTDIR
  # to $INSTDIR must have a valid path before logging can be turned on
  LogSet on

  # Install and register the core FreeCAD files
  
  # Initializes the plug-ins dir ($PLUGINSDIR) if not already initialized.
  # $PLUGINSDIR is automatically deleted when the installer exits.
  InitPluginsDir
  
  # Binaries
  SetOutPath "$INSTDIR\bin"
  # recursively copy all files under bin
  File /r "${FILES_FREECAD}\bin\*.*"
  
  # MSVC redistributable DLLs
  !ifdef FILES_DEPS
    !echo "Including MSVC Redist files from ${FILES_DEPS}"
    SetOutPath "$INSTDIR\bin"
    File "${FILES_DEPS}\*.*"
  !endif
  
  # Others
  SetOutPath "$INSTDIR\data"
  File /r "${FILES_FREECAD}\data\*.*"
  SetOutPath "$INSTDIR\doc"
  File /r "${FILES_FREECAD}\doc\*.*"
  SetOutPath "$INSTDIR\Ext"
  File /r "${FILES_FREECAD}\Ext\*.*"
  SetOutPath "$INSTDIR\lib"
  File /r "${FILES_FREECAD}\lib\*.*"
  SetOutPath "$INSTDIR\Mod"
  File /r "${FILES_FREECAD}\Mod\*.*"
  SetOutPath "$INSTDIR"
  File /r "${FILES_THUMBS}"
    
  # Create uninstaller
  WriteUninstaller "$INSTDIR\${SETUP_UNINSTALLER}"

SectionEnd

Section -ValidateSteveCADUpdate

  ${if} $SteveCADUpdateMode == "install"
  ${orif} $SteveCADUpdateMode == "manual"
    IfErrors RollbackSteveCADUpdate
    IfFileExists "$INSTDIR\bin\freecadcmd.exe" 0 RollbackSteveCADUpdate
    ExecWait '"$INSTDIR\bin\freecadcmd.exe" --safe-mode -c "import SteveCADUpdate"' $R0
    ${if} $R0 != 0
      Goto RollbackSteveCADUpdate
    ${endif}
    Goto SteveCADUpdateValidated

    RollbackSteveCADUpdate:
      Call RestoreSteveCADUpdateBackup
      SetErrorLevel 23
      Quit

    SteveCADUpdateValidated:
  ${endif}

SectionEnd
