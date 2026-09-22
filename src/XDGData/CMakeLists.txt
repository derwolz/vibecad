include(GNUInstallDirs)

if(NOT DEFINED APPDATA_RELEASE_DATE)
    if(EXISTS "${CMAKE_SOURCE_DIR}/.git")
        execute_process(COMMAND git log -1 --pretty=%cd --date=short
            OUTPUT_VARIABLE APPDATA_RELEASE_DATE
            WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
            OUTPUT_STRIP_TRAILING_WHITESPACE)
    else()
        string(TIMESTAMP APPDATA_RELEASE_DATE "%Y-%m-%d")
    endif()
endif()

configure_file(
    org.freecad.FreeCAD.metainfo.xml.in
    ${CMAKE_BINARY_DIR}/org.freecad.FreeCAD.metainfo.xml
)
install(
    FILES ${CMAKE_BINARY_DIR}/org.freecad.FreeCAD.metainfo.xml
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/metainfo
)

# Keep native installs and portable packages on the same desktop identity.
# Native builds retain their existing executable name and single-instance flags.
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/../../package/linux/stevecad.desktop" STEVECAD_DESKTOP_ENTRY)
string(REPLACE "Exec=stevecad " "Exec=FreeCAD - --single-instance "
    STEVECAD_DESKTOP_ENTRY "${STEVECAD_DESKTOP_ENTRY}")
file(GENERATE OUTPUT "${CMAKE_BINARY_DIR}/stevecad.desktop" CONTENT "${STEVECAD_DESKTOP_ENTRY}")
# Preserve existing pinned launchers and the upstream AppStream launchable ID,
# without adding a second application-menu entry.
file(GENERATE OUTPUT "${CMAKE_BINARY_DIR}/org.freecad.FreeCAD.desktop"
    CONTENT "${STEVECAD_DESKTOP_ENTRY}NoDisplay=true\n")
install(
    FILES "${CMAKE_BINARY_DIR}/stevecad.desktop" "${CMAKE_BINARY_DIR}/org.freecad.FreeCAD.desktop"
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/applications
)
install(
    FILES "${CMAKE_CURRENT_SOURCE_DIR}/../Gui/Icons/stevecad.svg"
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/icons/hicolor/scalable/apps
)

install(
    FILES org.freecad.FreeCAD.xml
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/mime/packages
)

configure_file(
    FreeCAD.thumbnailer.in
    ${CMAKE_BINARY_DIR}/FreeCAD.thumbnailer
)
install(
    FILES ${CMAKE_BINARY_DIR}/FreeCAD.thumbnailer
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/thumbnailers
)

configure_file(
    ${CMAKE_SOURCE_DIR}/src/Tools/freecad-thumbnailer.in
    ${CMAKE_BINARY_DIR}/freecad-thumbnailer
)
install(
    PROGRAMS ${CMAKE_BINARY_DIR}/freecad-thumbnailer
    TYPE BIN
)
