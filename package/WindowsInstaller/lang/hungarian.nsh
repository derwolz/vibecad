/*
SteveCAD Installer Language File
Language: Hungarian
*/

!insertmacro LANGFILE_EXT "Hungarian"

${LangFileString} TEXT_INSTALL_CURRENTUSER "(Telepítve az aktuális felhasználónak)"

${LangFileString} TEXT_WELCOME "A varázsló segítségével tudja telepíteni a SteveCAD-et.$\r$\n\
				$\r$\n\
				$_CLICK"

#${LangFileString} TEXT_CONFIGURE_PYTHON "Python parancsfájlok fordítása..."

${LangFileString} TEXT_FINISH_DESKTOP "Indítóikon létrehozása Asztalon"
${LangFileString} TEXT_FINISH_WEBSITE "Látogasson el a github.com/10-X-eng/vibecad oldalra az aktuális hírekért, támogatásért és tippekért"

#${LangFileString} FileTypeTitle "SteveCAD-dokumentum"

#${LangFileString} SecAllUsersTitle "Telepítés minden felhasználónak"
${LangFileString} SecFileAssocTitle "Fájltársítások"
${LangFileString} SecDesktopTitle "Parancsikon Asztalra"

${LangFileString} SecCoreDescription "A SteveCAD futtatásához szükséges fájlok."
#${LangFileString} SecAllUsersDescription "Minden felhasználónak telepítsem vagy csak az aktuálisnak?"
${LangFileString} SecFileAssocDescription "A .FCStd kiterjesztéssel rendelkező fájlok megnyitása automatikusan a SteveCAD-el történjen."
${LangFileString} SecDesktopDescription "SteveCAD-ikon elhelyezése az Asztalon."
#${LangFileString} SecDictionaries "Szótárak"
#${LangFileString} SecDictionariesDescription "Helyesírás-ellenőrző szótárak, amiket letölthet és telepíthet."

#${LangFileString} PathName 'A $\"xxx.exe$\" fájl elérési útja'
#${LangFileString} InvalidFolder 'Nem találom a $\"xxx.exe$\" fájlt, a megadott helyen.'

#${LangFileString} DictionariesFailed 'Szótár letöltése a(z) $\"$R3$\" nyelvhez sikertelen.'

#${LangFileString} ConfigInfo "A SteveCAD telepítés utáni beállítása hosszú időt vehet igénybe."

#${LangFileString} RunConfigureFailed "Nem tudom végrehajtani a configure parancsfájlt!"
${LangFileString} InstallRunning "A telepítő már fut!"
${LangFileString} AlreadyInstalled "A SteveCAD ${APP_SERIES_KEY2} már teleptve van!$\r$\n\
				Installing over existing installations is not recommended if the installed version$\r$\n\
				is a test release or if you have problems with your existing SteveCAD installation.$\r$\n\
				In these cases better reinstall SteveCAD.$\r$\n\
				Dou you nevertheles want to install SteveCAD over the existing version?"
${LangFileString} NewerInstalled "A jelenleg telepítettnél régebbi SteveCAD verziót próbál telepíteni.$\r$\n\
				  Ha valóban ezt akarja, először el kell távolítania a meglévő SteveCAD $OldVersionNumber változatot."

#${LangFileString} FinishPageMessage "Gratulálok! Sikeresen telepítette a SteveCAD-et.$\r$\n\
#					$\r$\n\
#					(A program első indítása egy kis időt vehet igénybe...)"
${LangFileString} FinishPageRun "SteveCAD indítása"

${LangFileString} UnNotInRegistryLabel "Nem találom a SteveCAD-et a regisztriben.$\r$\n\
					Az Asztalon és a Start Menüben található parancsikonok nem lesznek eltávolítva!."
${LangFileString} UnInstallRunning "Először be kell zárnia a SteveCAD-et!"
${LangFileString} UnNotAdminLabel "A SteveCAD eltávolításhoz rendszergazdai jogokkal kell rendelkeznie!"
${LangFileString} UnReallyRemoveLabel "Biztosan abban, hogy el akarja távolítani a SteveCAD-t, minden tartozékával együtt?"
${LangFileString} UnFreeCADPreferencesTitle 'SteveCAD felhasználói beállítások'

#${LangFileString} SecUnProgDescription "xxx eltávolítása."
${LangFileString} SecUnPreferencesDescription 'A  SteveCAD beállítások mappa törlése$\r$\n\
						$\"$AppPre\username\$\r$\n\
						$AppSuff\$\r$\n\
						${APP_DIR_USERDATA}$\")$\r$\n\
						minden felhasználónál.'
${LangFileString} DialogUnPreferences 'You chose to delete the SteveCADs user configuration.$\r$\n\
						This will also delete all installed SteveCAD addons.$\r$\n\
						Do you agree with this?'
${LangFileString} SecUnProgramFilesDescription "A SteveCAD és minden komponensének eltávolítása."
