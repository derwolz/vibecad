# SPDX-License-Identifier: LGPL-2.1-or-later

"""GUI bootstrap for SteveCAD's additive 3D Print workbench."""


class SteveCADPrintWorkbench(Workbench):
    """External slicer profile selection and explicit 3MF handoff."""

    MenuText = "3D Print"
    ToolTip = "Prepare selected CAD objects and open them in an external slicer"

    def __init__(self):
        self.__class__.Icon = (
            FreeCAD.getHomePath() + "Mod/SteveCADPrint/icons/stevecad-print-open.svg"
        )

    def Initialize(self):
        import PrintCommandLoader
        import PrintPanel

        PrintCommandLoader.ensure_commands_registered()
        PrintPanel.ensure_panel_registered()
        send_commands = [
            "SteveCADPrint_OpenInPrusaSlicer",
            "SteveCADPrint_Save3MF",
        ]
        setup_commands = ["SteveCADPrint_Setup"]
        self.appendToolbar("Send", send_commands)
        self.appendToolbar("Setup", setup_commands)
        self.appendMenu("3D Print", send_commands + setup_commands)
        Log("Loading SteveCAD 3D Print workbench... done\n")

    def Activated(self):
        import PrintPanel

        Msg("SteveCADPrintWorkbench::Activated()\n")
        PrintPanel.show_panel()

    def Deactivated(self):
        import PrintPanel

        PrintPanel.hide_panel()
        Msg("SteveCADPrintWorkbench::Deactivated()\n")

    def GetClassName(self):
        return "Gui::PythonWorkbench"


import PrintSetupDialog

Gui.addPreferencePage(PrintSetupDialog.SteveCADPrintPreferencesPage, "SteveCAD")
Gui.addWorkbench(SteveCADPrintWorkbench())
