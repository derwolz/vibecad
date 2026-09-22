/*
SteveCAD Installer Language File
Language: English
*/

!insertmacro LANGFILE_EXT "English"

${LangFileString} TEXT_INSTALL_CURRENTUSER "(Installed for Current User)"

${LangFileString} TEXT_WELCOME "This wizard will guide you through the installation of $(^NameDA). $\r$\n\
				$\r$\n\
				$_CLICK"

#${LangFileString} TEXT_CONFIGURE_PYTHON "Compiling Python scripts..."

${LangFileString} TEXT_FINISH_DESKTOP "Create desktop shortcut"
${LangFileString} TEXT_FINISH_WEBSITE "Visit github.com/10-X-eng/vibecad for the latest news, support and tips"

#${LangFileString} FileTypeTitle "SteveCAD-Document"

#${LangFileString} SecAllUsersTitle "Install for all users?"
${LangFileString} SecFileAssocTitle "File associations"
${LangFileString} SecDesktopTitle "Desktop icon"

${LangFileString} SecCoreDescription "The SteveCAD files."
#${LangFileString} SecAllUsersDescription "Install SteveCAD for all users or just the current user."
${LangFileString} SecFileAssocDescription "Files with a .FCStd extension will automatically open in SteveCAD."
${LangFileString} SecDesktopDescription "A SteveCAD icon on the desktop."
#${LangFileString} SecDictionaries "Dictionaries"
#${LangFileString} SecDictionariesDescription "Spell-checker dictionaries that can be downloaded and installed."

#${LangFileString} PathName 'Path to the file $\"xxx.exe$\"'
#${LangFileString} InvalidFolder 'The file $\"xxx.exe$\" is not in the specified path.'

#${LangFileString} DictionariesFailed 'Download of dictionary for language $\"$R3$\" failed.'

#${LangFileString} ConfigInfo "The following configuration of SteveCAD could take a while."

#${LangFileString} RunConfigureFailed "Could not run configure script."
${LangFileString} InstallRunning "The installer is already running!"
${LangFileString} UpgradeInstalled "$SteveCADInstalledDisplayVersion is installed.$\r$\n\
				This installer will update it to ${APP_VERSION} using a clean replacement of the program files.$\r$\n\
				Your documents and preferences will be preserved.$\r$\n$\r$\n\
				Continue with the update?"
${LangFileString} RepairInstalled "SteveCAD ${APP_VERSION} is already installed.$\r$\n\
				Would you like to repair it by cleanly replacing the program files?$\r$\n\
				Your documents and preferences will be preserved."
${LangFileString} DowngradeBlocked "A newer SteveCAD release is already installed:$\r$\n\
				$SteveCADInstalledDisplayVersion$\r$\n$\r$\n\
				This installer contains ${APP_VERSION} and will not downgrade it automatically.$\r$\n\
				Uninstall the newer release first if you intentionally need to downgrade."
${LangFileString} ReplaceUnknownInstalled "An existing SteveCAD installation was found:$\r$\n\
				$SteveCADInstalledDisplayVersion$\r$\n$\r$\n\
				Its complete version/build order cannot be determined. Continuing will cleanly replace its$\r$\n\
				program files with ${APP_VERSION}; documents and preferences will be preserved.$\r$\n$\r$\n\
				Continue?"
${LangFileString} InvalidExistingInstall "The registered SteveCAD installation directory is missing or invalid.$\r$\n\
				The installer stopped without changing it. Uninstall the damaged entry before reinstalling SteveCAD."
# Retained for compatibility with downstream installer extensions that may
# still reference the historical language identifiers.
${LangFileString} AlreadyInstalled "SteveCAD ${APP_SERIES_KEY2} is already installed."
${LangFileString} NewerInstalled "A newer SteveCAD installation already exists."

#${LangFileString} FinishPageMessage "Congratulations! SteveCAD has been installed successfully.$\r$\n\
#					$\r$\n\
#					(The first start of SteveCAD might take some seconds.)"
${LangFileString} FinishPageRun "Launch SteveCAD"

${LangFileString} UnNotInRegistryLabel "Unable to find SteveCAD in the registry.$\r$\n\
					Shortcuts on the desktop and in the Start Menu will not be removed."
${LangFileString} UnInstallRunning "You must close SteveCAD first!"
${LangFileString} UnNotAdminLabel "You must have administrator privileges to uninstall SteveCAD!"
${LangFileString} UnReallyRemoveLabel "Are you sure you want to completely remove SteveCAD and all of its components?"
${LangFileString} UnFreeCADPreferencesTitle 'SteveCAD$\'s user preferences'

#${LangFileString} SecUnProgDescription "Uninstalls xxx."
${LangFileString} SecUnPreferencesDescription 'Deletes SteveCAD$\'s configuration$\r$\n\
						(folder $\"$AppPre\username\$\r$\n\
						$AppSuff\$\r$\n\
						${APP_DIR_USERDATA}$\")$\r$\n\
						for you or for all users (if you are admin).'
${LangFileString} DialogUnPreferences 'You chose to delete the SteveCAD user configuration.$\r$\n\
						This will also delete all installed SteveCAD addons, and will affect the$\r$\n\
						preferences for all versions of SteveCAD.$\r$\n\
						Are you sure you want to proceed?'
${LangFileString} SecUnProgramFilesDescription "Uninstall SteveCAD and all of its components."
