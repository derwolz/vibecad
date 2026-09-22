# SPDX-License-Identifier: LGPL-2.1-or-later

SET(SteveCADPrint_SRCS
    Init.py
    InitGui.py
    BambuStudio.py
    OrcaSlicer.py
    Commands.py
    PrintCommandLoader.py
    PrintIcons.py
    PrintPanel.py
    PrintPreferences.py
    PrintSetupDialog.py
    SteveCADPrint.py
)

SET(SteveCADPrint_Icons
    icons/stevecad-print-open.svg
    icons/stevecad-print-save.svg
    icons/stevecad-print-setup.svg
)

SET(SteveCADPrint_Tests
    tests/__init__.py
    tests/conftest.py
    tests/qt_dialog_layout.py
    tests/qt_bambu_setup_integration.py
    tests/qt_backend_switch_integration.py
    tests/qt_panel_integration.py
    tests/qt_panel_persistence_integration.py
    tests/qt_progress_integration.py
    tests/qt_selection_integration.py
    tests/qt_workbench_panel_integration.py
    tests/test_backend.py
    tests/test_bambu_backend.py
    tests/test_orca_backend.py
    tests/test_commands.py
    tests/test_export.py
    tests/test_preferences.py
    tests/test_workbench.py
)

SET(SteveCADPrint_All
    ${SteveCADPrint_SRCS}
    ${SteveCADPrint_Icons}
    ${SteveCADPrint_Tests}
)

SOURCE_GROUP("" FILES ${SteveCADPrint_SRCS})

ADD_CUSTOM_TARGET(SteveCADPrint ALL SOURCES ${SteveCADPrint_All})

fc_copy_sources(SteveCADPrint "${CMAKE_BINARY_DIR}/Mod/SteveCADPrint" ${SteveCADPrint_All})

INSTALL(FILES ${SteveCADPrint_SRCS} DESTINATION Mod/SteveCADPrint)
INSTALL(FILES ${SteveCADPrint_Icons} DESTINATION Mod/SteveCADPrint/icons)

if(BUILD_TEST)
    INSTALL(FILES ${SteveCADPrint_Tests} DESTINATION Mod/SteveCADPrint/tests)
endif()
