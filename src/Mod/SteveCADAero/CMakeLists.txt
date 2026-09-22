# SPDX-License-Identifier: LGPL-2.1-or-later

SET(SteveCADAero_SRCS
    Init.py
    InitGui.py
    AeroCommandLoader.py
    Commands.py
    SteveCADAero.py
    AeroConfig.py
    AeroAirfoil.py
    AeroIcons.py
    AeroSolvers.py
    AeroResults.py
    AeroJSBSim.py
    AeroWorkspace.py
    AeroRepair.py
    AeroStamp.py
    AeroMass.py
    AeroFlightCard.py
    AeroPreview.py
    requirements-aero.txt
    README.md
)

SET(SteveCADAero_Icons
    icons/stevecad-aero-analyze.svg
)

SET(SteveCADAero_Data
    data/e63.dat
)

SET(SteveCADAero_Tests
    tests/__init__.py
    tests/conftest.py
    tests/test_airfoil.py
    tests/test_assistant_push.py
    tests/test_config.py
    tests/test_icons.py
    tests/test_jsbsim.py
    tests/test_public_api.py
    tests/test_repair.py
    tests/test_results.py
    tests/test_solvers.py
    tests/test_workbench.py
    tests/test_flight_card.py
    tests/test_honesty.py
)

SET(SteveCADAero_All
    ${SteveCADAero_SRCS}
    ${SteveCADAero_Data}
    ${SteveCADAero_Icons}
    ${SteveCADAero_Tests}
)

SOURCE_GROUP("" FILES ${SteveCADAero_SRCS})

ADD_CUSTOM_TARGET(SteveCADAero ALL
    SOURCES ${SteveCADAero_All}
)

fc_copy_sources(SteveCADAero "${CMAKE_BINARY_DIR}/Mod/SteveCADAero" ${SteveCADAero_All})

INSTALL(
    FILES
        ${SteveCADAero_SRCS}
    DESTINATION
        Mod/SteveCADAero
)

INSTALL(
    FILES
        ${SteveCADAero_Data}
    DESTINATION
        Mod/SteveCADAero/data
)

INSTALL(
    FILES
        ${SteveCADAero_Icons}
    DESTINATION
        Mod/SteveCADAero/icons
)

if(BUILD_TEST)
    INSTALL(
        FILES
            ${SteveCADAero_Tests}
        DESTINATION
            Mod/SteveCADAero/tests
    )
endif()
