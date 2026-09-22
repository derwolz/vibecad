# SPDX-License-Identifier: LGPL-2.1-or-later

from __future__ import annotations

import ast
from pathlib import Path
import re

import pytest

from SteveCADNativeActionManifest import KNOWN_ACTIONS_BY_SURFACE
from SteveCADNativeContextManifest import (
    NATIVE_CONTEXT_ACTIONS,
    NativeContextManifestError,
    context_actions_for_surface,
    provider_context_actions_for_surface,
)


MOD_ROOT = Path(__file__).resolve().parents[2]

EXPECTED_CONTEXT_ACTION_IDS = {
    "SteveCAD_NativeSketchState",
    "SketchEditDeleteGeometry",
    "SteveCAD_AnalyzeReadAnalysis",
    "SteveCAD_AnalyzeCreateStudyFocused",
    "SteveCAD_AnalyzeConfigureStudyFocused",
    "SteveCAD_AnalyzeReadGeometrySource",
    "SteveCAD_AnalyzeCreateSolidDomain",
    "SteveCAD_AnalyzeReadAssignments",
    "SteveCAD_AnalyzeValidateAssignments",
    "SteveCAD_AnalyzeHighlightAssignment",
    "SteveCAD_AnalyzeIsolateAssignment",
    "SteveCAD_AnalyzeRestoreAssignmentView",
    "SteveCAD_AnalyzeReadMaterial",
    "SteveCAD_AnalyzeSearchMaterialCatalog",
    "SteveCAD_AnalyzeSearchMaterialCatalogFocused",
    "SteveCAD_AnalyzeReadElementDefinition",
    "SteveCAD_AnalyzeUpdateBeamSection",
    "SteveCAD_AnalyzeUpdateBeamRotation",
    "SteveCAD_AnalyzeUpdateShellThickness",
    "SteveCAD_AnalyzeUpdateFluidSection",
    "SteveCAD_AnalyzeReadElectromagneticConstraint",
    "SteveCAD_AnalyzeUpdateElectromagnetic",
    "SteveCAD_AnalyzeUpdateCurrentDensity",
    "SteveCAD_AnalyzeUpdateMagnetization",
    "SteveCAD_AnalyzeUpdateElectricChargeDensity",
    "SteveCAD_AnalyzeReadFluidConstraint",
    "SteveCAD_AnalyzeCreateInitialVelocity",
    "SteveCAD_AnalyzeCreateInitialPressure",
    "SteveCAD_AnalyzeCreateBoundaryVelocity",
    "SteveCAD_AnalyzeCreateFluidBoundary",
    "SteveCAD_AnalyzeCreateFluidMaterial",
    "SteveCAD_AnalyzeCreateSolidMaterial",
    "SteveCAD_AnalyzeCreateSolidRegionMaterial",
    "SteveCAD_AnalyzeCreateCatalogMaterial",
    "SteveCAD_AnalyzeCreateCustomMaterial",
    "SteveCAD_AnalyzeCreateFixedSupport",
    "SteveCAD_AnalyzeEditFixedSupportFocused",
    "SteveCAD_AnalyzeCreateRigidCouplingFocused",
    "SteveCAD_AnalyzeEditRigidCouplingFocused",
    "SteveCAD_AnalyzeCreateDisplacementSupportFocused",
    "SteveCAD_AnalyzeEditDisplacementSupportFocused",
    "SteveCAD_AnalyzeCreateSpringSupportFocused",
    "SteveCAD_AnalyzeEditSpringSupportFocused",
    "SteveCAD_AnalyzeCreateForce",
    "SteveCAD_AnalyzeUpdateForceFocused",
    "SteveCAD_AnalyzeCreatePressureFocused",
    "SteveCAD_AnalyzeUpdatePressureFocused",
    "SteveCAD_AnalyzeCreateGravityFocused",
    "SteveCAD_AnalyzeUpdateGravityFocused",
    "SteveCAD_AnalyzeCreateCentrifugalFocused",
    "SteveCAD_AnalyzeUpdateCentrifugalFocused",
    "SteveCAD_AnalyzeCreateOpenFOAMSolver",
    "SteveCAD_AnalyzeUpdateInitialFlowVelocity",
    "SteveCAD_AnalyzeUpdateInitialPressure",
    "SteveCAD_AnalyzeUpdateFlowVelocity",
    "SteveCAD_AnalyzeUpdateFluidBoundary",
    "SteveCAD_AnalyzeReadGeometricalFeature",
    "SteveCAD_AnalyzeUpdatePlaneRotation",
    "SteveCAD_AnalyzeUpdateSectionPrint",
    "SteveCAD_AnalyzeUpdateTransform",
    "SteveCAD_AnalyzeReadSupportCondition",
    "SteveCAD_AnalyzeUpdateFixed",
    "SteveCAD_AnalyzeUpdateRigidBody",
    "SteveCAD_AnalyzeUpdateDisplacement",
    "SteveCAD_AnalyzeUpdateSpring",
    "SteveCAD_AnalyzeReadConnection",
    "SteveCAD_AnalyzeUpdateContact",
    "SteveCAD_AnalyzeUpdateTie",
    "SteveCAD_AnalyzeReadLoad",
    "SteveCAD_AnalyzeUpdateForce",
    "SteveCAD_AnalyzeUpdatePressure",
    "SteveCAD_AnalyzeUpdateCentrifugal",
    "SteveCAD_AnalyzeUpdateGravity",
    "SteveCAD_AnalyzeReadThermalCondition",
    "SteveCAD_AnalyzeCreateConvection",
    "SteveCAD_AnalyzeCreateRadiation",
    "SteveCAD_AnalyzeCreateConcentratedHeatInput",
    "SteveCAD_AnalyzeCreateTotalBodyPower",
    "SteveCAD_AnalyzeUpdateInitialTemperature",
    "SteveCAD_AnalyzeUpdateSurfaceHeatFlux",
    "SteveCAD_AnalyzeUpdateConvection",
    "SteveCAD_AnalyzeUpdateRadiation",
    "SteveCAD_AnalyzeUpdateBoundaryTemperature",
    "SteveCAD_AnalyzeUpdateConcentratedHeatInput",
    "SteveCAD_AnalyzeUpdateMassHeatGeneration",
    "SteveCAD_AnalyzeUpdateTotalBodyPower",
    "SteveCAD_AnalyzeReadMeshDefinition",
    "SteveCAD_AnalyzeCreateGmshMesh",
    "SteveCAD_AnalyzeCreateSolidMeshFocused",
    "SteveCAD_AnalyzeCreateFlowMeshFocused",
    "SteveCAD_AnalyzeUpdateGmshMeshFocused",
    "SteveCAD_AnalyzeGenerateCurrentGmshMesh",
    "SteveCAD_AnalyzeUpdateGmshMesh",
    "SteveCAD_AnalyzeUpdateNetgenMesh",
    "SteveCAD_AnalyzeGenerateGmshMesh",
    "SteveCAD_AnalyzeGenerateNetgenMesh",
    "SteveCAD_AnalyzeReadMeshRefinement",
    "SteveCAD_AnalyzeCreateLocalMeshSizeFocused",
    "SteveCAD_AnalyzeEditLocalMeshSizeFocused",
    "SteveCAD_AnalyzeUpdateMeshRegion",
    "SteveCAD_AnalyzeUpdateMeshGroup",
    "SteveCAD_AnalyzeUpdateMeshDistance",
    "SteveCAD_AnalyzeUpdateMeshBoundaryLayer",
    "SteveCAD_AnalyzeUpdateMeshShape",
    "SteveCAD_AnalyzeCreateMeshThreshold",
    "SteveCAD_AnalyzeCreateMeshMean",
    "SteveCAD_AnalyzeCreateMeshGradient",
    "SteveCAD_AnalyzeCreateMeshCurvature",
    "SteveCAD_AnalyzeCreateMeshLaplacian",
    "SteveCAD_AnalyzeCreateMeshMathEval",
    "SteveCAD_AnalyzeCreateMeshMathEvalAniso",
    "SteveCAD_AnalyzeCreateMeshFieldDistance",
    "SteveCAD_AnalyzeCreateMeshResult",
    "SteveCAD_AnalyzeUpdateMeshRestrict",
    "SteveCAD_AnalyzeUpdateMeshThreshold",
    "SteveCAD_AnalyzeUpdateMeshMean",
    "SteveCAD_AnalyzeUpdateMeshGradient",
    "SteveCAD_AnalyzeUpdateMeshCurvature",
    "SteveCAD_AnalyzeUpdateMeshLaplacian",
    "SteveCAD_AnalyzeUpdateMeshAttractorAnisoCurve",
    "SteveCAD_AnalyzeUpdateMeshMathEval",
    "SteveCAD_AnalyzeUpdateMeshMathEvalAniso",
    "SteveCAD_AnalyzeUpdateMeshFieldDistance",
    "SteveCAD_AnalyzeUpdateMeshResult",
    "SteveCAD_AnalyzeUpdateTransfiniteCurve",
    "SteveCAD_AnalyzeUpdateTransfiniteSurface",
    "SteveCAD_AnalyzeUpdateTransfiniteVolume",
    "SteveCAD_AnalyzeReadFemMeshElements",
    "SteveCAD_AnalyzeEraseMeshElements",
    "SteveCAD_AnalyzeEraseMeshElementRanges",
    "SteveCAD_AnalyzeConvertFemMeshSurface",
    "SteveCAD_AnalyzeConvertDeformedFemMeshSurface",
    "SteveCAD_AnalyzeReadSolver",
    "SteveCAD_AnalyzeRunCurrentSolver",
    "SteveCAD_AnalyzeUpdateCalculiXSolver",
    "SteveCAD_AnalyzeUpdateElmerSolver",
    "SteveCAD_AnalyzeUpdateOpenFOAMSolver",
    "SteveCAD_AnalyzeUpdateZ88Solver",
    "SteveCAD_AnalyzeReadEquation",
    "SteveCAD_AnalyzeReadResult",
    "SteveCAD_AnalyzeReadOpenFOAMFlow",
    "SteveCAD_AnalyzeMeasureOpenFOAMFlow",
    "SteveCAD_AnalyzeCompareOpenFOAMFlow",
    "SteveCAD_AnalyzeShowOpenFOAMFlow",
    "SteveCAD_AnalyzeReadMechanicalResult",
    "SteveCAD_AnalyzeShowMechanicalResult",
    "SteveCAD_AnalyzeReadTemperatureResult",
    "SteveCAD_AnalyzeShowTemperatureResult",
    "AssemblyContextToggleActive",
    "AssemblyContextMakeFlexible",
    "AssemblyContextMakeRigid",
    "Assembly_LinkSelectLinked",
    "Assembly_ExportASMT",
    "AssemblyContextPlaySimulation",
    "AssemblySimulationSeek",
    "AssemblySimulationStep",
    "AssemblySimulationPlay",
    "AssemblySimulationPause",
    "AssemblySimulationClose",
    "SteveCAD_ManufactureReadJob",
    "SteveCAD_ManufactureReadThreadCatalog",
    "SteveCAD_ManufactureListTools",
    "SteveCAD_ManufactureReadTool",
    "SteveCAD_ManufactureUpdateController",
    "SteveCAD_ManufactureUpdateToolBit",
    "CAMSimulationClose",
    "CAM_ExportTemplate",
    "CAM_SetStartPoint",
    "CAM_ToolBitSave",
    "CAM_ToolBitSaveAs",
    "TechDrawContextEditBalloon",
    "TechDrawContextEditDimension",
    "TechDrawContextShowDrawing",
    "TechDrawContextToggleKeepUpdated",
    "TechDrawContextToggleFrames",
    "TechDrawContextToggleGrid",
    "TechDrawContextExportSVG",
    "TechDrawContextExportDXF",
    "TechDrawContextExportPDF",
    "TechDrawContextPrintAll",
    "InspectionContextAnnotation",
    "InspectionContextLeaveInfoMode",
}


def _cpp_context_ids(directory: Path, prefixes: tuple[str, ...]) -> set[str]:
    pattern = re.compile(r'setObjectName\(QStringLiteral\("([^"]+)"\)\)')
    return {
        action_id
        for path in directory.rglob("*.cpp")
        for action_id in pattern.findall(path.read_text(encoding="utf-8"))
        if action_id.startswith(prefixes)
    }


def _cam_workbench_context_commands() -> set[str]:
    source = (MOD_ROOT / "CAM" / "InitGui.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    context_method = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "ContextMenu"
    )
    return {
        value.value
        for value in ast.walk(context_method)
        if isinstance(value, ast.Constant)
        and isinstance(value.value, str)
        and value.value.startswith("CAM_")
    }


def test_context_inventory_is_complete_unique_and_small() -> None:
    assert {action.action_id for action in NATIVE_CONTEXT_ACTIONS} == (
        EXPECTED_CONTEXT_ACTION_IDS
    )
    assert len({action.action_id for action in NATIVE_CONTEXT_ACTIONS}) == len(
        NATIVE_CONTEXT_ACTIONS
    )
    assert (
        sum(action.classification.human_only for action in NATIVE_CONTEXT_ACTIONS) == 5
    )
    assert all(action.exact_target_type for action in NATIVE_CONTEXT_ACTIONS)


def test_surface_filtering_never_leaks_context_actions() -> None:
    assert len(context_actions_for_surface("drawing")) == 12
    assert len(provider_context_actions_for_surface("drawing")) == 8
    assert len(context_actions_for_surface("assemble")) == 13
    assert len(provider_context_actions_for_surface("assemble")) == 10
    assert len(context_actions_for_surface("manufacture")) == 13
    assert len(provider_context_actions_for_surface("manufacture")) == 11
    assert len(context_actions_for_surface("model")) == 2
    assert provider_context_actions_for_surface("model") == ()
    analyze = context_actions_for_surface("analyze")
    assert tuple(action.action_id for action in analyze) == (
        "SteveCAD_AnalyzeReadAnalysis",
        "SteveCAD_AnalyzeCreateStudyFocused",
        "SteveCAD_AnalyzeConfigureStudyFocused",
        "SteveCAD_AnalyzeReadGeometrySource",
        "SteveCAD_AnalyzeCreateSolidDomain",
        "SteveCAD_AnalyzeReadAssignments",
        "SteveCAD_AnalyzeValidateAssignments",
        "SteveCAD_AnalyzeHighlightAssignment",
        "SteveCAD_AnalyzeIsolateAssignment",
        "SteveCAD_AnalyzeRestoreAssignmentView",
        "SteveCAD_AnalyzeReadMaterial",
        "SteveCAD_AnalyzeSearchMaterialCatalog",
        "SteveCAD_AnalyzeSearchMaterialCatalogFocused",
        "SteveCAD_AnalyzeReadElementDefinition",
        "SteveCAD_AnalyzeUpdateBeamSection",
        "SteveCAD_AnalyzeUpdateBeamRotation",
        "SteveCAD_AnalyzeUpdateShellThickness",
        "SteveCAD_AnalyzeUpdateFluidSection",
        "SteveCAD_AnalyzeReadElectromagneticConstraint",
        "SteveCAD_AnalyzeUpdateElectromagnetic",
        "SteveCAD_AnalyzeUpdateCurrentDensity",
        "SteveCAD_AnalyzeUpdateMagnetization",
        "SteveCAD_AnalyzeUpdateElectricChargeDensity",
        "SteveCAD_AnalyzeReadFluidConstraint",
        "SteveCAD_AnalyzeCreateInitialVelocity",
        "SteveCAD_AnalyzeCreateInitialPressure",
        "SteveCAD_AnalyzeCreateBoundaryVelocity",
        "SteveCAD_AnalyzeCreateFluidBoundary",
        "SteveCAD_AnalyzeCreateFluidMaterial",
        "SteveCAD_AnalyzeCreateSolidMaterial",
        "SteveCAD_AnalyzeCreateSolidRegionMaterial",
        "SteveCAD_AnalyzeCreateCatalogMaterial",
        "SteveCAD_AnalyzeCreateCustomMaterial",
        "SteveCAD_AnalyzeCreateFixedSupport",
        "SteveCAD_AnalyzeEditFixedSupportFocused",
        "SteveCAD_AnalyzeCreateRigidCouplingFocused",
        "SteveCAD_AnalyzeEditRigidCouplingFocused",
        "SteveCAD_AnalyzeCreateDisplacementSupportFocused",
        "SteveCAD_AnalyzeEditDisplacementSupportFocused",
        "SteveCAD_AnalyzeCreateSpringSupportFocused",
        "SteveCAD_AnalyzeEditSpringSupportFocused",
        "SteveCAD_AnalyzeCreateForce",
        "SteveCAD_AnalyzeUpdateForceFocused",
        "SteveCAD_AnalyzeCreatePressureFocused",
        "SteveCAD_AnalyzeUpdatePressureFocused",
        "SteveCAD_AnalyzeCreateGravityFocused",
        "SteveCAD_AnalyzeUpdateGravityFocused",
        "SteveCAD_AnalyzeCreateCentrifugalFocused",
        "SteveCAD_AnalyzeUpdateCentrifugalFocused",
        "SteveCAD_AnalyzeCreateOpenFOAMSolver",
        "SteveCAD_AnalyzeUpdateInitialFlowVelocity",
        "SteveCAD_AnalyzeUpdateInitialPressure",
        "SteveCAD_AnalyzeUpdateFlowVelocity",
        "SteveCAD_AnalyzeUpdateFluidBoundary",
        "SteveCAD_AnalyzeReadGeometricalFeature",
        "SteveCAD_AnalyzeUpdatePlaneRotation",
        "SteveCAD_AnalyzeUpdateSectionPrint",
        "SteveCAD_AnalyzeUpdateTransform",
        "SteveCAD_AnalyzeReadSupportCondition",
        "SteveCAD_AnalyzeUpdateFixed",
        "SteveCAD_AnalyzeUpdateRigidBody",
        "SteveCAD_AnalyzeUpdateDisplacement",
        "SteveCAD_AnalyzeUpdateSpring",
        "SteveCAD_AnalyzeReadConnection",
        "SteveCAD_AnalyzeUpdateContact",
        "SteveCAD_AnalyzeUpdateTie",
        "SteveCAD_AnalyzeReadLoad",
        "SteveCAD_AnalyzeUpdateForce",
        "SteveCAD_AnalyzeUpdatePressure",
        "SteveCAD_AnalyzeUpdateCentrifugal",
        "SteveCAD_AnalyzeUpdateGravity",
        "SteveCAD_AnalyzeReadThermalCondition",
        "SteveCAD_AnalyzeCreateConvection",
        "SteveCAD_AnalyzeCreateRadiation",
        "SteveCAD_AnalyzeCreateConcentratedHeatInput",
        "SteveCAD_AnalyzeCreateTotalBodyPower",
        "SteveCAD_AnalyzeUpdateInitialTemperature",
        "SteveCAD_AnalyzeUpdateSurfaceHeatFlux",
        "SteveCAD_AnalyzeUpdateConvection",
        "SteveCAD_AnalyzeUpdateRadiation",
        "SteveCAD_AnalyzeUpdateBoundaryTemperature",
        "SteveCAD_AnalyzeUpdateConcentratedHeatInput",
        "SteveCAD_AnalyzeUpdateMassHeatGeneration",
        "SteveCAD_AnalyzeUpdateTotalBodyPower",
        "SteveCAD_AnalyzeReadMeshDefinition",
        "SteveCAD_AnalyzeCreateGmshMesh",
        "SteveCAD_AnalyzeCreateSolidMeshFocused",
        "SteveCAD_AnalyzeCreateFlowMeshFocused",
        "SteveCAD_AnalyzeUpdateGmshMeshFocused",
        "SteveCAD_AnalyzeGenerateCurrentGmshMesh",
        "SteveCAD_AnalyzeUpdateGmshMesh",
        "SteveCAD_AnalyzeUpdateNetgenMesh",
        "SteveCAD_AnalyzeGenerateGmshMesh",
        "SteveCAD_AnalyzeGenerateNetgenMesh",
        "SteveCAD_AnalyzeReadMeshRefinement",
        "SteveCAD_AnalyzeCreateLocalMeshSizeFocused",
        "SteveCAD_AnalyzeEditLocalMeshSizeFocused",
        "SteveCAD_AnalyzeUpdateMeshRegion",
        "SteveCAD_AnalyzeUpdateMeshGroup",
        "SteveCAD_AnalyzeUpdateMeshDistance",
        "SteveCAD_AnalyzeUpdateMeshBoundaryLayer",
        "SteveCAD_AnalyzeUpdateMeshShape",
        "SteveCAD_AnalyzeCreateMeshThreshold",
        "SteveCAD_AnalyzeCreateMeshMean",
        "SteveCAD_AnalyzeCreateMeshGradient",
        "SteveCAD_AnalyzeCreateMeshCurvature",
        "SteveCAD_AnalyzeCreateMeshLaplacian",
        "SteveCAD_AnalyzeCreateMeshMathEval",
        "SteveCAD_AnalyzeCreateMeshMathEvalAniso",
        "SteveCAD_AnalyzeCreateMeshFieldDistance",
        "SteveCAD_AnalyzeCreateMeshResult",
        "SteveCAD_AnalyzeUpdateMeshRestrict",
        "SteveCAD_AnalyzeUpdateMeshThreshold",
        "SteveCAD_AnalyzeUpdateMeshMean",
        "SteveCAD_AnalyzeUpdateMeshGradient",
        "SteveCAD_AnalyzeUpdateMeshCurvature",
        "SteveCAD_AnalyzeUpdateMeshLaplacian",
        "SteveCAD_AnalyzeUpdateMeshAttractorAnisoCurve",
        "SteveCAD_AnalyzeUpdateMeshMathEval",
        "SteveCAD_AnalyzeUpdateMeshMathEvalAniso",
        "SteveCAD_AnalyzeUpdateMeshFieldDistance",
        "SteveCAD_AnalyzeUpdateMeshResult",
        "SteveCAD_AnalyzeUpdateTransfiniteCurve",
        "SteveCAD_AnalyzeUpdateTransfiniteSurface",
        "SteveCAD_AnalyzeUpdateTransfiniteVolume",
        "SteveCAD_AnalyzeReadFemMeshElements",
        "SteveCAD_AnalyzeEraseMeshElements",
        "SteveCAD_AnalyzeEraseMeshElementRanges",
        "SteveCAD_AnalyzeConvertFemMeshSurface",
        "SteveCAD_AnalyzeConvertDeformedFemMeshSurface",
        "SteveCAD_AnalyzeReadSolver",
        "SteveCAD_AnalyzeRunCurrentSolver",
        "SteveCAD_AnalyzeUpdateCalculiXSolver",
        "SteveCAD_AnalyzeUpdateElmerSolver",
        "SteveCAD_AnalyzeUpdateOpenFOAMSolver",
        "SteveCAD_AnalyzeUpdateZ88Solver",
        "SteveCAD_AnalyzeReadEquation",
        "SteveCAD_AnalyzeReadResult",
        "SteveCAD_AnalyzeReadOpenFOAMFlow",
        "SteveCAD_AnalyzeMeasureOpenFOAMFlow",
        "SteveCAD_AnalyzeCompareOpenFOAMFlow",
        "SteveCAD_AnalyzeShowOpenFOAMFlow",
        "SteveCAD_AnalyzeReadMechanicalResult",
        "SteveCAD_AnalyzeShowMechanicalResult",
        "SteveCAD_AnalyzeReadTemperatureResult",
        "SteveCAD_AnalyzeShowTemperatureResult",
        "InspectionContextAnnotation",
        "InspectionContextLeaveInfoMode",
    )
    assert provider_context_actions_for_surface("analyze") == analyze[:-2]
    sketch = context_actions_for_surface("sketch.edit")
    assert tuple(action.action_id for action in sketch) == (
        "SteveCAD_NativeSketchState",
        "SketchEditDeleteGeometry",
    )
    assert provider_context_actions_for_surface("sketch.edit") == sketch


@pytest.mark.parametrize("surface_id", ("unavailable", "DraftWorkbench", ""))
def test_unknown_or_unavailable_surface_fails_closed(surface_id: str) -> None:
    with pytest.raises(NativeContextManifestError, match="Unknown Native surface"):
        context_actions_for_surface(surface_id)


def test_human_only_actions_cannot_be_misrepresented_as_provider_operations() -> None:
    human_only = [
        action for action in NATIVE_CONTEXT_ACTIONS if action.classification.human_only
    ]
    assert all(action.operation_variant is None for action in human_only)
    assert all(action.transaction_behavior == "human" for action in human_only)
    assert all(action.implementation_status == "human_only" for action in human_only)
    assert all(action.classification.interactive for action in human_only)


def test_provider_actions_have_exact_variants_and_transaction_classification() -> None:
    provider_actions = {
        action.action_id: action
        for action in NATIVE_CONTEXT_ACTIONS
        if not action.classification.human_only
    }
    assert provider_actions["AssemblyContextMakeFlexible"].operation_variant == (
        "make_flexible"
    )
    assert provider_actions["AssemblyContextMakeFlexible"].capability_family == (
        "assembly.rigidity"
    )
    assert (
        provider_actions["AssemblyContextMakeRigid"].operation_variant == "make_rigid"
    )
    assert provider_actions["AssemblyContextMakeRigid"].capability_family == (
        "assembly.rigidity"
    )
    assert provider_actions[
        "SteveCAD_ManufactureUpdateController"
    ].capability_family == "manufacture.set_controller"
    assert provider_actions[
        "SteveCAD_ManufactureUpdateToolBit"
    ].capability_family == "manufacture.update_tool"
    assert provider_actions["CAM_SetStartPoint"].capability_family == (
        "manufacture.start_point"
    )
    assert provider_actions["SteveCAD_ManufactureReadJob"].capability_family == (
        "manufacture.read_setup"
    )
    assert provider_actions[
        "SteveCAD_ManufactureReadThreadCatalog"
    ].capability_family == "manufacture.threads"
    assert provider_actions["SteveCAD_AnalyzeReadAnalysis"].operation_variant == (
        "analysis"
    )
    assert provider_actions["SteveCAD_AnalyzeReadAssignments"].operation_variant == (
        "assignments"
    )
    assert provider_actions[
        "SteveCAD_AnalyzeValidateAssignments"
    ].operation_variant == "validate_assignments"
    assert provider_actions["SteveCAD_AnalyzeReadMaterial"].operation_variant == (
        "material"
    )
    assert provider_actions["SteveCAD_AnalyzeReadResult"].operation_variant == "result"
    assert (
        provider_actions["SteveCAD_AnalyzeSearchMaterialCatalog"].operation_variant
        == "material_catalog"
    )
    assert (
        provider_actions["SteveCAD_AnalyzeReadElementDefinition"].operation_variant
        == "element_definition"
    )
    assert all(
        provider_actions[action_id].classification.read
        and provider_actions[action_id].transaction_behavior == "none"
        for action_id in {
            "SteveCAD_AnalyzeReadAnalysis",
            "SteveCAD_AnalyzeReadAssignments",
            "SteveCAD_AnalyzeValidateAssignments",
            "SteveCAD_AnalyzeReadMaterial",
            "SteveCAD_AnalyzeSearchMaterialCatalog",
            "SteveCAD_AnalyzeReadElementDefinition",
            "SteveCAD_AnalyzeReadResult",
        }
    )
    assert all(
        provider_actions[action_id].classification.view
        and provider_actions[action_id].transaction_behavior == "presentation"
        for action_id in {
            "SteveCAD_AnalyzeHighlightAssignment",
            "SteveCAD_AnalyzeIsolateAssignment",
            "SteveCAD_AnalyzeRestoreAssignmentView",
        }
    )
    assert provider_actions["CAMSimulationClose"].capability_family == (
        "manufacture.close_simulation"
    )
    assert provider_actions["CAMSimulationClose"].operation_variant == "close"
    assert provider_actions["CAMSimulationClose"].classification.view
    assert provider_actions["CAMSimulationClose"].classification.interactive
    assert provider_actions["CAMSimulationClose"].transaction_behavior == (
        "presentation"
    )
    assert {
        provider_actions[action_id].operation_variant
        for action_id in {
            "SteveCAD_AnalyzeUpdateBeamSection",
            "SteveCAD_AnalyzeUpdateBeamRotation",
            "SteveCAD_AnalyzeUpdateShellThickness",
            "SteveCAD_AnalyzeUpdateFluidSection",
        }
    } == {
        "update_beam_section",
        "update_beam_rotation",
        "update_shell_thickness",
        "update_fluid_section",
    }
    assert all(
        provider_actions[action_id].classification.mutation
        and provider_actions[action_id].transaction_behavior == "document"
        for action_id in {
            "SteveCAD_AnalyzeUpdateBeamSection",
            "SteveCAD_AnalyzeUpdateBeamRotation",
            "SteveCAD_AnalyzeUpdateShellThickness",
            "SteveCAD_AnalyzeUpdateFluidSection",
        }
    )
    assert provider_actions["Assembly_LinkSelectLinked"].operation_variant == (
        "linked_source"
    )
    assert provider_actions["Assembly_LinkSelectLinked"].classification.read
    assert provider_actions["Assembly_LinkSelectLinked"].transaction_behavior == "none"
    assert provider_actions["Assembly_LinkSelectLinked"].source_command_id == (
        "Assembly_LinkSelectLinked"
    )
    assert provider_actions["Assembly_ExportASMT"].operation_variant == "asmt"
    assert provider_actions["Assembly_ExportASMT"].classification.export
    assert provider_actions["Assembly_ExportASMT"].transaction_behavior == "output"
    assert provider_actions["Assembly_ExportASMT"].source_command_id == (
        "Assembly_ExportASMT"
    )
    assert provider_actions["AssemblyContextPlaySimulation"].operation_variant == (
        "show"
    )
    assert provider_actions["AssemblyContextPlaySimulation"].source_command_id == (
        "Assembly_EditHistoryOperation"
    )
    assert all(
        provider_actions[action_id].classification.view
        and provider_actions[action_id].classification.interactive
        and provider_actions[action_id].transaction_behavior == "presentation"
        for action_id in {
            "AssemblyContextPlaySimulation",
            "AssemblySimulationSeek",
            "AssemblySimulationStep",
            "AssemblySimulationPlay",
            "AssemblySimulationPause",
            "AssemblySimulationClose",
        }
    )
    assert provider_actions["TechDrawContextToggleKeepUpdated"].classification.mutation
    assert provider_actions[
        "TechDrawContextToggleKeepUpdated"
    ].transaction_behavior == ("document")
    assert provider_actions["TechDrawContextToggleGrid"].classification.view
    assert provider_actions["TechDrawContextToggleGrid"].transaction_behavior == (
        "presentation"
    )
    assert all(
        action.background_required
        for action_id, action in provider_actions.items()
        if action_id.startswith("TechDrawContextExport")
        or action_id == "TechDrawContextPrintAll"
    )


def test_cpp_context_action_ids_match_the_inventory_exactly() -> None:
    assembly_ids = _cpp_context_ids(MOD_ROOT / "Assembly" / "Gui", ("AssemblyContext",))
    drawing_ids = _cpp_context_ids(MOD_ROOT / "TechDraw" / "Gui", ("TechDrawContext",))
    inspection_ids = _cpp_context_ids(
        MOD_ROOT / "Inspection" / "Gui", ("InspectionContext",)
    )

    assert assembly_ids == {
        "AssemblyContextToggleActive",
        "AssemblyContextMakeFlexible",
        "AssemblyContextMakeRigid",
    }
    assert drawing_ids == {
        action_id
        for action_id in EXPECTED_CONTEXT_ACTION_IDS
        if action_id.startswith("TechDrawContext")
    }
    assert inspection_ids == {
        "InspectionContextAnnotation",
        "InspectionContextLeaveInfoMode",
    }


def test_cam_context_only_commands_match_the_inventory_exactly() -> None:
    context_commands = _cam_workbench_context_commands()
    default_ribbon_commands = set(KNOWN_ACTIONS_BY_SURFACE["manufacture"])

    assert context_commands - default_ribbon_commands == {
        "CAM_ExportTemplate",
        "CAM_SetStartPoint",
        "CAM_ToolBitSave",
        "CAM_ToolBitSaveAs",
    }
    assert context_commands <= default_ribbon_commands | {
        action.action_id
        for action in NATIVE_CONTEXT_ACTIONS
        if action.surface_ids == ("manufacture",)
    }


def test_current_stevecad_fastener_workflow_has_no_hidden_context_only_action() -> None:
    fastener_actions = {
        "SteveCAD_InsertStandardFastener",
        "SteveCAD_EditStandardFastener",
        "SteveCAD_CreateMatchingFastenerHole",
        "SteveCAD_AttachStandardFastener",
    }
    assert fastener_actions <= set(KNOWN_ACTIONS_BY_SURFACE["model"])
    assert fastener_actions & set(KNOWN_ACTIONS_BY_SURFACE["assemble"]) == {
        "SteveCAD_InsertStandardFastener",
        "SteveCAD_EditStandardFastener",
    }
    source = "\n".join(
        (MOD_ROOT / "SteveCAD" / filename).read_text(encoding="utf-8")
        for filename in ("SteveCADFasteners.py", "SteveCADFastenersGui.py")
    )
    assert "appendContextMenu" not in source


def test_context_manifest_exposes_no_activation_or_command_dispatch_api() -> None:
    import SteveCADNativeContextManifest as module

    public_names = {name for name in vars(module) if not name.startswith("_")}
    forbidden_fragments = ("activate", "switch", "dispatch", "run_command")
    assert not any(
        fragment in name.lower()
        for name in public_names
        for fragment in forbidden_fragments
    )
