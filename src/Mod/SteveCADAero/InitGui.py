# SPDX-License-Identifier: LGPL-2.1-or-later

"""GUI bootstrap for the Aero workbench (internal name: SteveCADAero)."""


class SteveCADAeroWorkbench(Workbench):
    """First-class in-app aerodynamics workbench."""

    MenuText = "Aero"
    ToolTip = "NeuralFoil section, AeroSandbox VLM/AeroBuildup, momentum hover, JSBSim"

    def __init__(self):
        self.__class__.Icon = (
            FreeCAD.getHomePath()
            + "Mod/SteveCADAero/icons/stevecad-aero-analyze.svg"
        )

    def Initialize(self):
        import AeroCommandLoader

        AeroCommandLoader.ensure_commands_registered()
        commands = [
            "SteveCADAero_Analyze",
            "SteveCADAero_Section",
            "SteveCADAero_VLM",
            "SteveCADAero_ExportJSBSim",
            "SteveCADAero_Report",
            "SteveCADAero_ProposeRepairs",
            "SteveCADAero_ApplyRepairs",
            "SteveCADAero_FlightCard",
        ]
        self.appendToolbar("Aero", commands)
        self.appendMenu("Aero", commands)
        Log("Loading SteveCAD Aero workbench... done\n")

    def Activated(self):
        Msg("SteveCADAeroWorkbench::Activated()\n")

    def Deactivated(self):
        Msg("SteveCADAeroWorkbench::Deactivated()\n")

    def GetClassName(self):
        return "Gui::PythonWorkbench"


Gui.addWorkbench(SteveCADAeroWorkbench())
