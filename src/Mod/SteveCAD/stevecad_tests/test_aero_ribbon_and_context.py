# SPDX-License-Identifier: LGPL-2.1-or-later

"""Aero is a first-class ribbon surface and turn-start assistant context."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import zipfile

from SteveCADAeroContext import document_aero_summary
from SteveCADCore import SteveCADService
from SteveCADNativeActionManifest import (
    KNOWN_ACTIONS_BY_SURFACE,
    OPTIONAL_ACTIONS_BY_SURFACE,
    classify_native_surface,
)
from SteveCADRibbonSurface import RibbonSurface, SURFACE_IDS


REPO = Path(__file__).resolve().parents[4]


def test_aero_surface_id_is_registered() -> None:
    assert "aero" in SURFACE_IDS
    assert "aero" in KNOWN_ACTIONS_BY_SURFACE
    assert "aero" in OPTIONAL_ACTIONS_BY_SURFACE
    assert set(OPTIONAL_ACTIONS_BY_SURFACE) == set(KNOWN_ACTIONS_BY_SURFACE)
    for command in (
        "SteveCADAero_Analyze",
        "SteveCADAero_Section",
        "SteveCADAero_VLM",
        "SteveCADAero_ExportJSBSim",
        "SteveCADAero_Report",
        "SteveCADAero_ProposeRepairs",
        "SteveCADAero_ApplyRepairs",
        "SteveCADAero_FlightCard",
    ):
        assert command in KNOWN_ACTIONS_BY_SURFACE["aero"]
        assert command in OPTIONAL_ACTIONS_BY_SURFACE["model"]


def test_cpp_ribbon_places_aero_tab_after_parameters() -> None:
    ribbon = (REPO / "src/Gui/SteveCADRibbon.cpp").read_text(encoding="utf-8")
    assert 'constexpr std::array<DomainDefinition, 9> domains' in ribbon
    parameters = ribbon.index(
        '{"Parameters", "SpreadsheetWorkbench", "parameters"}'
    )
    aero = ribbon.index('{"Aero", "SteveCADAeroWorkbench", "aero"}')
    drawing = ribbon.index('{"Drawing", "TechDrawWorkbench", "drawing"}')
    manufacture = ribbon.index(
        '{"Manufacture", "CAMWorkbench", "manufacture"}'
    )
    assert drawing < parameters < aero
    assert manufacture < drawing
    assert "aeroGroups" not in ribbon
    assert "SteveCADAeroWorkspaceHost" not in ribbon
    assert "isAeroTab" not in ribbon
    activate = ribbon[ribbon.index("void activateDomain(int index)") :]
    activate = activate[: activate.index("void syncDomainToWorkbench")]
    assert "activateWorkbench(workbench" in activate
    assert "isAeroTabIndex(index)" not in activate


def _aero_manifest() -> dict[str, object]:
    def action(command_id: str, label: str) -> dict[str, object]:
        return {
            "command_id": command_id,
            "kind": "command",
            "label": label,
            "available": True,
        }

    return {
        "schema_version": 1,
        "surface_id": "aero",
        "groups": [
            {
                "label": "View",
                "actions": [
                    action("Std_ViewFitAll", "Fit all"),
                    action("Std_ViewIsometric", "Isometric"),
                    action("SteveCAD_ToggleGrid", "Grid"),
                    action("SteveCAD_SectionView", "Section View"),
                ],
            },
            {
                "label": "Actions",
                "actions": [
                    action("SteveCADAero_Analyze", "Analyze"),
                    action("SteveCADAero_Section", "Section"),
                    action("SteveCADAero_VLM", "VLM"),
                    action("SteveCADAero_ExportJSBSim", "JSBSim"),
                    action("SteveCADAero_Report", "Report"),
                    action("SteveCADAero_ProposeRepairs", "Propose"),
                    action("SteveCADAero_ApplyRepairs", "Apply"),
                    action("SteveCADAero_FlightCard", "Card"),
                ],
            },
            {
                "label": "Inspect",
                "actions": [
                    action("Std_Measure", "Measure"),
                    action("Std_MassProperties", "Mass"),
                    action("Inspection_VisualInspection", "Visual"),
                    action("Inspection_InspectElement", "Element"),
                    action("Part_CheckGeometry", "Check"),
                ],
            },
        ],
    }


def test_aero_surface_classifies_without_unknown_actions() -> None:
    surface = RibbonSurface.from_manifest(_aero_manifest(), revision=1)
    plans = classify_native_surface(surface)
    assert [plan.command_id for plan in plans] == list(surface.command_ids)
    human = {
        plan.command_id
        for plan in plans
        if plan.classification.human_only
    }
    aero_tools = {
        "SteveCADAero_Analyze",
        "SteveCADAero_Section",
        "SteveCADAero_VLM",
        "SteveCADAero_ExportJSBSim",
        "SteveCADAero_Report",
        "SteveCADAero_ProposeRepairs",
        "SteveCADAero_ApplyRepairs",
        "SteveCADAero_FlightCard",
    }
    assert human.isdisjoint(aero_tools)
    variants = {
        plan.command_id: plan.operation_variant
        for plan in plans
        if plan.command_id in aero_tools
    }
    assert variants["SteveCADAero_Analyze"] == "analyze"
    assert variants["SteveCADAero_ExportJSBSim"] == "export_jsbsim"
    assert variants["SteveCADAero_FlightCard"] == "flight_card"
    assert {
        plan.capability_family
        for plan in plans
        if plan.command_id in aero_tools
    } == {"aero.solve", "aero.export", "aero.inspect"}


def test_aero_native_surface_exposes_solve_export_inspect() -> None:
    from collections import defaultdict

    from SteveCADNativeAeroBindings import register_aero_solve_capability_implementation
    from SteveCADNativeAeroRuntime import NativeAeroRuntime
    from SteveCADNativeAeroSchema import register_aero_solve_capability_definition
    from SteveCADNativeCapabilityRegistry import NativeCapabilityRegistry

    surface = RibbonSurface.from_manifest(_aero_manifest(), revision=1)
    plans = classify_native_surface(surface)
    family_classes: dict[str, set[str]] = defaultdict(set)
    for plan in plans:
        classification = plan.classification
        if classification.human_only or classification.parent_only:
            continue
        if classification.export:
            primary = "export"
        elif classification.read:
            primary = "read"
        elif classification.view:
            primary = "view"
        elif classification.mutation:
            primary = "mutation"
        else:
            primary = "none"
        family_classes[plan.capability_family].add(primary)
    mixed = {name: values for name, values in family_classes.items() if len(values) != 1}
    assert mixed == {}
    assert "aero.solve" in family_classes
    assert "aero.export" in family_classes
    assert "aero.inspect" in family_classes
    registry = NativeCapabilityRegistry()
    register_aero_solve_capability_definition(registry)
    register_aero_solve_capability_implementation(registry)
    assert registry.definition("aero.solve") is not None
    assert registry.definition("aero.export") is not None
    assert registry.definition("aero.inspect") is not None
    assert registry.implementation("aero.solve") is not None
    _ = NativeAeroRuntime


def test_python_surface_list_includes_aero() -> None:
    source = (REPO / "src/Mod/SteveCAD/SteveCADRibbonSurface.py").read_text(
        encoding="utf-8"
    )
    assert '"aero"' in source


def test_document_aero_summary_reads_report_and_config() -> None:
    report = SimpleNamespace(
        Name="AeroReport",
        Label="AeroReport",
        CL=1.516,
        CD=0.242,
        CM=0.733,
        CLalpha=7.3,
        Cmalpha=4.68,
        PitchUnstable=True,
        Re=25000.0,
        V_loaf=4.19,
        P_hover=24.2,
        P_cruise=1.51,
        Source="AeroBuildup",
        Airfoil="e63",
        GeometrySource="AeroConfig",
        JSBSimPlantPath="/tmp/jsbsim/voider.xml",
        span_mm=500.0,
        chord_mm=90.0,
        gap_c=1.4,
        stagger_c=1.15,
        decalage_deg=2.0,
        auw_g=149.6,
        alpha_deg=4.0,
        n_props=2.0,
        prop_diameter_mm=178.0,
        thrust_to_weight=1.9,
        Corrections="Grew the horizontal tail span from 150 mm to 180 mm.",
        RepairPasses=1,
    )
    config = SimpleNamespace(
        Name="AeroConfig",
        Label="AeroConfig",
        vehicle_type="tailsitter",
        airfoil="e63",
        span_mm=500.0,
        chord_mm=90.0,
        gap_c=1.4,
        stagger_c=1.15,
        decalage_deg=2.0,
        auw_g=149.6,
        alpha_deg=4.0,
        n_props=2.0,
        prop_diameter_mm=178.0,
        thrust_to_weight=1.9,
    )

    def get_object(name: str):
        return {"AeroReport": report, "AeroConfig": config}.get(name)

    doc = SimpleNamespace(
        Name="Voider",
        Objects=[config, report],
        getObject=get_object,
        JSBSimPlantPath="/tmp/jsbsim/voider.xml",
    )
    summary = document_aero_summary(doc)
    assert summary["available"] is True
    assert summary["vehicle_type"] == "tailsitter"
    assert summary["airfoil"] == "e63"
    assert summary["CL"] == 1.516
    assert summary["CD"] == 0.242
    assert summary["CM"] == 0.733
    assert summary["CLalpha"] == 7.3
    assert summary["Cmalpha"] == 4.68
    assert summary["PitchUnstable"] is True
    assert summary["Re"] == 25000.0
    assert summary["V_loaf"] == 4.19
    assert summary["P_hover"] == 24.2
    assert summary["P_cruise"] == 1.51
    assert summary["source"] == "AeroBuildup"
    assert summary["jsbsim_path"] == "/tmp/jsbsim/voider.xml"
    assert summary["geometry_source"] == "AeroConfig"
    assert summary["geometry"]["span_mm"] == 500.0
    assert summary["geometry"]["chord_mm"] == 90.0
    assert summary["RepairPasses"] == 1
    assert "Grew the horizontal tail span" in str(summary["Corrections"])
    assert "trace" not in summary
    assert "solver_log" not in summary


def test_document_aero_summary_without_solve_keeps_config_geometry() -> None:
    config = SimpleNamespace(
        Name="AeroConfig",
        Label="AeroConfig",
        vehicle_type="airplane",
        airfoil="e63",
        span_mm=800.0,
        chord_mm=120.0,
        gap_c=1.2,
        stagger_c=1.0,
        decalage_deg=1.0,
        auw_g=250.0,
        alpha_deg=3.0,
        n_props=1.0,
        prop_diameter_mm=200.0,
        thrust_to_weight=0.4,
    )
    doc = SimpleNamespace(
        Name="Plane",
        Objects=[config],
        getObject=lambda name: config if name == "AeroConfig" else None,
    )
    summary = document_aero_summary(doc)
    assert summary["available"] is False
    assert summary["vehicle_type"] == "airplane"
    assert summary["airfoil"] == "e63"
    assert summary["geometry"]["span_mm"] == 800.0
    assert summary["geometry"]["chord_mm"] == 120.0
    assert "CL" not in summary


def test_provider_context_summary_includes_aero_when_report_exists() -> None:
    report = SimpleNamespace(
        Name="AeroReport",
        Label="AeroReport",
        CL=0.77,
        CD=0.04,
        CM=-0.14,
        CLalpha=4.8,
        Cmalpha=-0.7,
        PitchUnstable=False,
        Re=40000.0,
        V_loaf=7.1,
        P_hover=17.0,
        P_cruise=3.5,
        Source="NeuralFoil",
        Airfoil="e63",
        GeometrySource="AeroConfig",
        JSBSimPlantPath="",
        span_mm=500.0,
        chord_mm=90.0,
    )
    config = SimpleNamespace(
        Name="AeroConfig",
        Label="AeroConfig",
        vehicle_type="multirotor",
        airfoil="e63",
        span_mm=500.0,
        chord_mm=90.0,
        n_props=4.0,
        prop_diameter_mm=178.0,
        thrust_to_weight=1.9,
    )
    doc = SimpleNamespace(
        Name="Drone",
        Uid="doc-aero",
        Objects=[config, report],
        getObject=lambda name: {
            "AeroReport": report,
            "AeroConfig": config,
        }.get(name),
    )
    service = object.__new__(SteveCADService)
    service.active_workbench_name = lambda: "SteveCADAeroWorkbench"
    service.modeling_engine = lambda: "vibescript"
    service._active_document = lambda: doc
    service.provider_turn_document_summary = lambda: {
        "name": "Drone",
        "uid": "doc-aero",
        "object_count": 2,
        "edit_object": None,
    }
    service.provider_turn_selection_summary = lambda: {
        "selection_count": 0,
        "selection": [],
    }
    service.view_screenshot_summary = lambda: {"captured": False}
    service.provider_reference_image_attachments = lambda: {
        "count": 0,
        "images": [],
    }

    context = service.provider_context_summary()
    assert "aero" in context
    assert context["aero"]["available"] is True
    assert context["aero"]["claim_ceiling"] == "not_airworthy"
    assert context["aero"]["vehicle_type"] == "multirotor"
    assert context["aero"]["CL"] == 0.77
    assert context["aero"]["source"] == "NeuralFoil"
    assert context["aero"]["PitchUnstable"] is False
    assert "aero" not in context["document"]
    assert set(context["document"]) == {
        "name",
        "uid",
        "object_count",
        "edit_object",
    }


def test_document_aero_summary_exposes_assistant_json_when_present() -> None:
    report = SimpleNamespace(
        Name="AeroReport",
        Label="AeroReport",
        CL=1.516,
        CD=0.242,
        CM=0.733,
        CLalpha=7.3,
        Cmalpha=4.68,
        PitchUnstable=True,
        Re=25000.0,
        V_loaf=4.19,
        P_hover=24.2,
        P_cruise=1.51,
        Source="AeroBuildup",
        Airfoil="e63",
        GeometrySource="AeroConfig",
        JSBSimPlantPath="",
        Corrections=(
            "PitchUnstable: Cmα > 0. Increase decalage, add tail volume, "
            "or move CG forward until Cmα < 0."
        ),
    )
    assistant = SimpleNamespace(
        Name="AeroAssistantJson",
        Label="AeroAssistantJson",
        Text=(
            '{"CL":1.516,"CD":0.242,"Cmalpha":4.68,"PitchUnstable":true,'
            '"corrections":["PitchUnstable: Cmα > 0. Increase decalage, '
            'add tail volume, or move CG forward until Cmα < 0."]}'
        ),
    )

    def get_object(name: str):
        return {"AeroReport": report, "AeroAssistantJson": assistant}.get(name)

    doc = SimpleNamespace(
        Name="Voider",
        Objects=[report, assistant],
        getObject=get_object,
        AeroAssistantJson=assistant.Text,
    )
    summary = document_aero_summary(doc)
    assert summary["available"] is True
    assert summary["CL"] == 1.516
    assert summary["PitchUnstable"] is True
    assert "Increase decalage" in summary["corrections"][0]
    assert summary["assistant_json"]["CL"] == 1.516
    assert summary["assistant_json"]["CD"] == 0.242
    assert summary["assistant_json"]["Cmalpha"] == 4.68
    assert summary["assistant_json"]["PitchUnstable"] is True
    assert "Increase decalage" in summary["assistant_json"]["corrections"][0]


def test_document_aero_summary_reads_freecad_named_assistant_object() -> None:
    report = SimpleNamespace(
        Name="AeroReport",
        Label="AeroReport",
        CL=0.81,
        CD=0.037,
        CM=-0.021,
        CLalpha=5.1,
        Cmalpha=-0.4,
        PitchUnstable=False,
        Re=42000.0,
        V_loaf=7.4,
        P_hover=18.2,
        P_cruise=4.1,
        Source="NeuralFoil",
        Airfoil="e63",
        GeometrySource="AeroConfig",
        JSBSimPlantPath="",
        Corrections="Pitch stable.",
    )
    assistant = SimpleNamespace(
        Name="AeroAssistantJson",
        Label="AeroAssistantJson",
        Text=(
            '{"CL":0.81,"CD":0.037,"Cmalpha":-0.4,'
            '"PitchUnstable":false,"corrections":["Pitch stable."]}'
        ),
    )

    def get_object(name: str):
        return {"AeroReport": report, "AeroAssistantJson": assistant}.get(name)

    doc = SimpleNamespace(
        Name="Voider",
        Objects=[report, assistant],
        getObject=get_object,
        AeroAssistantJson=assistant,
    )

    summary = document_aero_summary(doc)

    assert summary["assistant_json"]["CL"] == 0.81
    assert summary["assistant_json"]["CD"] == 0.037
    assert summary["assistant_json"]["Cmalpha"] == -0.4
    assert summary["assistant_json"]["PitchUnstable"] is False
    assert summary["assistant_json"]["corrections"] == ["Pitch stable."]


def test_session_and_provider_allowlists_keep_aero(monkeypatch) -> None:
    import SteveCADProvider as provider
    import SteveCADSession as session

    aero = {
        "available": True,
        "CL": 1.516,
        "CD": 0.242,
        "Cmalpha": 4.68,
        "PitchUnstable": True,
        "corrections": [
            "PitchUnstable: Cmα > 0. Increase decalage, add tail volume, "
            "or move CG forward until Cmα < 0."
        ],
        "assistant_json": {
            "CL": 1.516,
            "CD": 0.242,
            "Cmalpha": 4.68,
            "PitchUnstable": True,
        },
    }

    class _Service:
        def provider_context_summary(self):
            return {
                "document": {"name": "Voider", "uid": "doc-1", "object_count": 2},
                "selection": {"selection_count": 0, "selection": []},
                "view_screenshot": {"captured": False},
                "reference_images": {"count": 0, "images": []},
                "aero": aero,
                "cad_state": {"must": "not leak"},
            }

        def active_workbench_name(self):
            return "PartWorkbench"

        def modeling_engine(self):
            return "vibescript"

        def provider_debug_config(self):
            return {"enabled": False}

        def provider_name(self):
            return "grok"

    monkeypatch.setattr(
        session,
        "provider_tool_schemas",
        lambda *_args, **_kwargs: [
            {
                "name": "vibescript.read_source",
                "description": "Read the active VibeScript source.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
            }
        ],
    )
    monkeypatch.setattr(
        session,
        "_capture_editable_sources_for_workbench",
        lambda *_args, **_kwargs: {"sources": []},
    )
    monkeypatch.setattr(
        session,
        "provider_engine_from_service",
        lambda _service: "vibescript",
    )

    context = session._capture_context_for_provider(_Service())
    assert context["aero"]["CL"] == 1.516
    assert context["aero"]["PitchUnstable"] is True
    assert "cad_state" not in context

    visible = provider._model_visible_context(context)
    assert visible["aero"]["CL"] == 1.516
    assert visible["aero"]["CD"] == 0.242
    assert visible["aero"]["Cmalpha"] == 4.68
    assert visible["aero"]["PitchUnstable"] is True

    state = session._provider_state_payload(context)
    assert state["aero"]["corrections"][0].startswith("PitchUnstable")
    assert state["aero"]["assistant_json"]["CL"] == 1.516
    assert "aero" not in (state.get("document") or {})

    prompt = session._provider_prompt("Continue.", context)
    encoded = prompt.split("STEVECAD_CONTEXT_JSON\n", 1)[1].split(
        "\nEND_STEVECAD_CONTEXT_JSON\n", 1
    )[0]
    payload = json.loads(encoded)
    assert payload["active_state"]["aero"]["CL"] == 1.516
    assert payload["active_state"]["aero"]["PitchUnstable"] is True
    assert "aero" not in (payload["active_state"].get("document") or {})
    assert "human_steering" not in encoded


def test_aero_bindings_forward_the_exact_native_ticket(monkeypatch) -> None:
    import SteveCADNativeAeroBindings as bindings

    ticket = object()
    seen: list[tuple[str, object]] = []

    class _Runtime:
        def solve(self, arguments, *, ticket):
            seen.append((str(arguments["operation"]), ticket))
            return {"operation": arguments["operation"]}

        def export(self, arguments, *, ticket):
            seen.append(("export", ticket))
            return {"operation": "export"}

        def inspect(self, arguments, *, ticket):
            seen.append(("inspect", ticket))
            return {"operation": "inspect"}

    runtime = _Runtime()
    monkeypatch.setattr(bindings, "_require_runtime", lambda _call: runtime)
    call = SimpleNamespace(arguments={"operation": "section"}, ticket=ticket)

    bindings._solve(call)
    bindings._export(call)
    bindings._inspect(call)

    assert seen == [("section", ticket), ("export", ticket), ("inspect", ticket)]


def test_native_aero_solve_uses_guarded_mutation_runner(monkeypatch) -> None:
    import SteveCADAero
    import SteveCADNativeAeroRuntime as runtime_module
    from SteveCADNativeState import NativeCallTicket

    document = SimpleNamespace(Uid="doc-aero", Objects=[])

    class _State:
        def current_revision(self, _uid):
            return 4

    class _Context:
        def __init__(self):
            self.document = document
            self.document_uid = document.Uid
            self.state = _State()
            self.authorize_output = None

        def guard(self):
            return None

    context = _Context()
    monkeypatch.setattr(runtime_module, "NativeRuntimeContext", _Context)
    monkeypatch.setattr(
        SteveCADAero,
        "run_section",
        lambda doc: {"ok": True, "source": "test", "document": doc.Uid},
    )
    calls: list[dict] = []

    def run_mutation(ctx, **kwargs):
        calls.append(kwargs)
        draft = kwargs["mutate"](ctx.document)
        return dict(kwargs["verify"](ctx.document, draft))

    monkeypatch.setattr(
        runtime_module,
        "run_immediate_mutation",
        run_mutation,
        raising=False,
    )
    ticket = NativeCallTicket("doc-aero", "aero.solve", 4, "aero-token")
    runtime = runtime_module.NativeAeroRuntime(context)

    result = runtime.solve({"operation": "section"}, ticket=ticket)

    assert result["source"] == "test"
    assert len(calls) == 1
    assert calls[0]["ticket"] is ticket
    assert calls[0]["transaction_name"] == "Aero Section"


def test_native_aero_export_requires_human_authorization_and_writes_one_zip(
    tmp_path,
    monkeypatch,
) -> None:
    import AeroJSBSim
    import SteveCADAero
    import SteveCADNativeAeroRuntime as runtime_module
    from SteveCADNativeOutput import authorize_native_output_path
    from SteveCADNativeState import NativeCallTicket

    document = SimpleNamespace(Uid="doc-aero", Objects=[])
    requests = []

    class _State:
        def current_revision(self, _uid):
            return 2

    class _Context:
        def __init__(self):
            self.document = document
            self.document_uid = document.Uid
            self.state = _State()
            self.authorize_output = self._authorize

        def guard(self):
            return None

        def _authorize(self, request):
            requests.append(request)
            return authorize_native_output_path(
                request,
                tmp_path / "stevecad_aero_jsbsim.zip",
            )

    def fake_write(_payload, *, output_dir, load_fn=None):
        root = Path(output_dir)
        aircraft = root / "stevecad_aero"
        engine = root / "engine"
        aircraft.mkdir(parents=True)
        engine.mkdir(parents=True)
        fdm = aircraft / "stevecad_aero.xml"
        electric = engine / "electric.xml"
        direct = engine / "direct.xml"
        fdm.write_text("<fdm_config/>", encoding="utf-8")
        electric.write_text("<electric_engine/>", encoding="utf-8")
        direct.write_text("<direct/>", encoding="utf-8")
        return {
            "fdm_path": str(fdm),
            "engine_path": str(electric),
            "thruster_path": str(direct),
            "model": "stevecad_aero",
            "loaded": False,
            "boot_error": "not loaded during export",
        }

    context = _Context()
    monkeypatch.setattr(runtime_module, "NativeRuntimeContext", _Context)
    monkeypatch.setattr(
        SteveCADAero,
        "prepare_jsbsim_payload",
        lambda doc: {"source": "test", "document": doc.Uid},
        raising=False,
    )
    monkeypatch.setattr(
        SteveCADAero,
        "export_jsbsim",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("Native export must not use the unguarded public writer")
        ),
    )
    monkeypatch.setattr(AeroJSBSim, "write_plant", fake_write)
    ticket = NativeCallTicket("doc-aero", "aero.export", 2, "export-token")
    runtime = runtime_module.NativeAeroRuntime(context)

    result = runtime.export({}, ticket=ticket)

    assert len(requests) == 1
    assert requests[0].allowed_suffixes == (".zip",)
    output = tmp_path / "stevecad_aero_jsbsim.zip"
    assert output.is_file()
    with zipfile.ZipFile(output) as archive:
        assert set(archive.namelist()) == {
            "stevecad_aero/stevecad_aero.xml",
            "engine/electric.xml",
            "engine/direct.xml",
        }
    assert result["output"]["file_name"] == output.name
