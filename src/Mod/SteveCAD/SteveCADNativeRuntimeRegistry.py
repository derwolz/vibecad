# SPDX-License-Identifier: LGPL-2.1-or-later

"""Production assembly point for document-bound Native runtimes."""

from __future__ import annotations

from typing import Any

from SteveCADNativeAeroBindings import aero_solve_runtime_bindings
from SteveCADNativeAeroRuntime import NativeAeroRuntime
from SteveCADNativeAnalyzeInspectBindings import analyze_inspect_runtime_bindings
from SteveCADNativeAnalyzeFaceBindings import analyze_face_runtime_bindings
from SteveCADNativeAnalyzeFlowResultBindings import (
    analyze_flow_presentation_runtime_bindings,
    analyze_flow_result_runtime_bindings,
)
from SteveCADNativeAnalyzeMechanicalResultBindings import (
    analyze_mechanical_presentation_runtime_bindings,
    analyze_mechanical_result_runtime_bindings,
)
from SteveCADNativeAnalyzeThermalResultBindings import (
    analyze_thermal_presentation_runtime_bindings,
    analyze_thermal_result_runtime_bindings,
)
from SteveCADNativeAnalyzeInspectRuntime import NativeAnalyzeInspectRuntime
from SteveCADNativeAnalyzeAssignmentViewBindings import (
    analyze_assignment_view_runtime_bindings,
)
from SteveCADNativeAnalyzeAssignmentViewRuntime import (
    NativeAnalyzeAssignmentViewRuntime,
)
from SteveCADNativeAnalyzeGeometryBindings import analyze_geometry_runtime_bindings
from SteveCADNativeAnalyzeGeometryRuntime import NativeAnalyzeGeometryRuntime
from SteveCADNativeAnalyzeElectromagneticBindings import (
    analyze_electromagnetic_runtime_bindings,
)
from SteveCADNativeAnalyzeElectromagneticRuntime import (
    NativeAnalyzeElectromagneticRuntime,
)
from SteveCADNativeAnalyzeFluidBindings import analyze_fluid_runtime_bindings
from SteveCADNativeAnalyzeFluidCreateBindings import (
    analyze_fluid_create_runtime_bindings,
)
from SteveCADNativeAnalyzeCfdLifecycleBindings import (
    analyze_cfd_lifecycle_runtime_bindings,
)
from SteveCADNativeAnalyzeFluidRuntime import NativeAnalyzeFluidRuntime
from SteveCADNativeAnalyzeGeometricalBindings import (
    analyze_geometrical_runtime_bindings,
)
from SteveCADNativeAnalyzeGeometricalRuntime import NativeAnalyzeGeometricalRuntime
from SteveCADNativeAnalyzeSupportBindings import analyze_support_runtime_bindings
from SteveCADNativeAnalyzeStructuralLifecycleBindings import (
    analyze_structural_lifecycle_runtime_bindings,
)
from SteveCADNativeAnalyzeSupportRuntime import NativeAnalyzeSupportRuntime
from SteveCADNativeAnalyzeConnectionBindings import analyze_connection_runtime_bindings
from SteveCADNativeAnalyzeConnectionRuntime import NativeAnalyzeConnectionRuntime
from SteveCADNativeAnalyzeLoadBindings import analyze_load_runtime_bindings
from SteveCADNativeAnalyzeLoadRuntime import NativeAnalyzeLoadRuntime
from SteveCADNativeAnalyzeThermalBindings import analyze_thermal_runtime_bindings
from SteveCADNativeAnalyzeThermalRuntime import NativeAnalyzeThermalRuntime
from SteveCADNativeAnalyzeMeshBindings import analyze_mesh_runtime_bindings
from SteveCADNativeAnalyzeMeshLifecycleBindings import (
    analyze_mesh_lifecycle_runtime_bindings,
)
from SteveCADNativeAnalyzeMeshRuntime import NativeAnalyzeMeshRuntime
from SteveCADNativeAnalyzeMeshFieldBindings import analyze_mesh_field_runtime_bindings
from SteveCADNativeAnalyzeMeshFieldRuntime import NativeAnalyzeMeshFieldRuntime
from SteveCADNativeAnalyzeMeshOutputBindings import analyze_mesh_output_runtime_bindings
from SteveCADNativeAnalyzeMeshOutputRuntime import NativeAnalyzeMeshOutputRuntime
from SteveCADNativeAnalyzeMeshRefinementBindings import (
    analyze_mesh_refinement_runtime_bindings,
)
from SteveCADNativeAnalyzeLocalMeshBindings import (
    analyze_local_mesh_runtime_bindings,
)
from SteveCADNativeAnalyzeMeshRefinementRuntime import (
    NativeAnalyzeMeshRefinementRuntime,
)
from SteveCADNativeAnalyzeStructuredMeshBindings import (
    analyze_structured_mesh_runtime_bindings,
)
from SteveCADNativeAnalyzeStructuredMeshRuntime import (
    NativeAnalyzeStructuredMeshRuntime,
)
from SteveCADNativeAnalyzeSolverBindings import analyze_solver_runtime_bindings
from SteveCADNativeAnalyzeSolverRuntime import NativeAnalyzeSolverRuntime
from SteveCADNativeAnalyzeSolverControlBindings import (
    analyze_solver_control_runtime_bindings,
)
from SteveCADNativeAnalyzeSolverControlRuntime import (
    NativeAnalyzeSolverControlRuntime,
)
from SteveCADNativeAnalyzeSolverExecutionBindings import (
    analyze_solver_execution_runtime_bindings,
)
from SteveCADNativeAnalyzeSolverExecutionRuntime import (
    NativeAnalyzeSolverExecutionRuntime,
)
from SteveCADNativeAnalyzeRunBindings import analyze_run_solver_runtime_bindings
from SteveCADNativeAnalyzeEquationBindings import analyze_equation_runtime_bindings
from SteveCADNativeAnalyzeEquationRuntime import NativeAnalyzeEquationRuntime
from SteveCADNativeAnalyzeResultsBindings import analyze_results_runtime_bindings
from SteveCADNativeAnalyzeResultsRuntime import NativeAnalyzeResultsRuntime
from SteveCADNativeAnalyzePresentationBindings import (
    analyze_presentation_runtime_bindings,
)
from SteveCADNativeAnalyzePresentationRuntime import (
    NativeAnalyzePresentationRuntime,
)
from SteveCADNativeAnalyzePostBindings import analyze_post_runtime_bindings
from SteveCADNativeAnalyzePostRuntime import NativeAnalyzePostRuntime
from SteveCADNativeAnalyzePostFunctionBindings import (
    analyze_post_function_runtime_bindings,
)
from SteveCADNativeAnalyzePostFunctionRuntime import NativeAnalyzePostFunctionRuntime
from SteveCADNativeAnalyzeVisualizationBindings import (
    analyze_visualization_runtime_bindings,
)
from SteveCADNativeAnalyzeVisualizationRuntime import (
    NativeAnalyzeVisualizationRuntime,
)
from SteveCADNativeAnalyzeModelBindings import analyze_model_runtime_bindings
from SteveCADNativeAnalyzeModelRuntime import NativeAnalyzeModelRuntime
from SteveCADNativeAnalyzeSolidDomainBindings import (
    analyze_solid_domain_runtime_bindings,
)
from SteveCADNativeAssemblyDiagnosisBindings import (
    assembly_diagnosis_runtime_bindings,
)
from SteveCADNativeAssemblyDiagnosisRuntime import NativeAssemblyDiagnosisRuntime
from SteveCADNativeAssemblyBomBindings import assembly_bom_runtime_bindings
from SteveCADNativeAssemblyBomRuntime import NativeAssemblyBomRuntime
from SteveCADNativeAssemblyFastenerBindings import assembly_fastener_runtime_bindings
from SteveCADNativeAssemblyFastenerRuntime import NativeAssemblyFastenerRuntime
from SteveCADNativeAssemblyExportBindings import assembly_export_runtime_bindings
from SteveCADNativeAssemblyExportRuntime import NativeAssemblyExportRuntime
from SteveCADNativeAssemblyInspectBindings import assembly_inspect_runtime_bindings
from SteveCADNativeAssemblyInspectRuntime import NativeAssemblyInspectRuntime
from SteveCADNativeAssemblyJointBindings import assembly_joint_runtime_bindings
from SteveCADNativeAssemblyJointRuntime import NativeAssemblyJointRuntime
from SteveCADNativeAssemblyPlaybackBindings import (
    assembly_playback_runtime_bindings,
)
from SteveCADNativeAssemblyPlaybackRuntime import NativeAssemblyPlaybackRuntime
from SteveCADNativeAssemblyStructureBindings import (
    assembly_structure_runtime_bindings,
)
from SteveCADNativeAssemblyStructureRuntime import NativeAssemblyStructureRuntime
from SteveCADNativeCommonBindings import common_runtime_bindings
from SteveCADNativeInspectionCompareBindings import inspection_compare_runtime_bindings
from SteveCADNativeInspectionCompareRuntime import NativeInspectionCompareRuntime
from SteveCADNativeCommonRuntime import NativeCommonRuntime
from SteveCADNativeWorkspaceBindings import workspace_runtime_bindings
from SteveCADNativeWorkspaceRuntime import NativeWorkspaceRuntime
from SteveCADNativeComponentInterfaceBindings import (
    component_interface_runtime_bindings,
)
from SteveCADNativeComponentInterfaceRuntime import NativeComponentInterfaceRuntime
from SteveCADNativeModelCatalogBindings import model_catalog_runtime_bindings
from SteveCADNativeModelCatalogRuntime import NativeModelCatalogRuntime
from SteveCADNativeModelBooleanBindings import model_boolean_runtime_bindings
from SteveCADNativeModelBooleanRuntime import NativeModelBooleanRuntime
from SteveCADNativeModelFeatureBindings import model_feature_runtime_bindings
from SteveCADNativeModelFeatureRuntime import NativeModelFeatureRuntime
from SteveCADNativeModelFastenerBindings import model_fastener_runtime_bindings
from SteveCADNativeModelFastenerRuntime import NativeModelFastenerRuntime
from SteveCADNativeModelDressupBindings import model_dressup_runtime_bindings
from SteveCADNativeModelDressupRuntime import NativeModelDressupRuntime
from SteveCADNativeModelHoleBindings import model_hole_runtime_bindings
from SteveCADNativeModelHoleRuntime import NativeModelHoleRuntime
from SteveCADNativeModelHistoryBindings import model_history_runtime_bindings
from SteveCADNativeModelHistoryRuntime import NativeModelHistoryRuntime
from SteveCADNativeSheetMetalInspectBindings import sheetmetal_inspect_runtime_bindings
from SteveCADNativeSheetMetalInspectRuntime import NativeSheetMetalInspectRuntime
from SteveCADNativeSheetMetalViewBindings import sheetmetal_view_runtime_bindings
from SteveCADNativeSheetMetalViewRuntime import NativeSheetMetalViewRuntime
from SteveCADNativeSheetMetalEditBindings import sheetmetal_edit_runtime_bindings
from SteveCADNativeSheetMetalEditRuntime import NativeSheetMetalEditRuntime
from SteveCADNativeSheetMetalCreateBindings import sheetmetal_create_runtime_bindings
from SteveCADNativeSheetMetalCreateRuntime import NativeSheetMetalCreateRuntime
from SteveCADNativeSheetMetalConnectionBindings import sheetmetal_connection_runtime_bindings
from SteveCADNativeSheetMetalConnectionRuntime import NativeSheetMetalConnectionRuntime
from SteveCADNativeSheetMetalManufacturingBindings import sheetmetal_manufacturing_runtime_bindings
from SteveCADNativeSheetMetalManufacturingRuntime import NativeSheetMetalManufacturingRuntime
from SteveCADNativeModelJoinBindings import model_join_runtime_bindings
from SteveCADNativeModelJoinRuntime import NativeModelJoinRuntime
from SteveCADNativeModelPartBindings import model_part_runtime_bindings
from SteveCADNativeModelPartRuntime import NativeModelPartRuntime
from SteveCADNativeModelSurfaceBindings import model_surface_runtime_bindings
from SteveCADNativeModelSurfaceRuntime import NativeModelSurfaceRuntime
from SteveCADNativeModelStructureBindings import model_structure_runtime_bindings
from SteveCADNativeModelStructureRuntime import NativeModelStructureRuntime
from SteveCADNativeSketchSetupBindings import sketch_setup_runtime_bindings
from SteveCADNativeSketchSetupRuntime import NativeSketchSetupRuntime
from SteveCADNativeModelTransformBindings import model_transform_runtime_bindings
from SteveCADNativeModelTransformRuntime import NativeModelTransformRuntime
from SteveCADNativeManufactureInspectBindings import (
    manufacture_inspect_runtime_bindings,
)
from SteveCADNativeManufactureFocusedInspectBindings import (
    manufacture_focused_inspect_runtime_bindings,
)
from SteveCADNativeManufactureInspectRuntime import NativeManufactureInspectRuntime
from SteveCADNativeManufactureJobBindings import manufacture_job_runtime_bindings
from SteveCADNativeManufactureJobRuntime import NativeManufactureJobRuntime
from SteveCADNativeManufactureJobSchema import MANUFACTURE_JOB_CAPABILITY_NAME
from SteveCADNativeManufactureAreaBindings import manufacture_area_runtime_bindings
from SteveCADNativeManufactureAreaRuntime import NativeManufactureAreaRuntime
from SteveCADNativeManufactureModifyBindings import (
    manufacture_modify_runtime_bindings,
)
from SteveCADNativeManufactureFocusedModifyBindings import (
    manufacture_focused_modify_runtime_bindings,
)
from SteveCADNativeManufactureModifyRuntime import NativeManufactureModifyRuntime
from SteveCADNativeManufactureProgramBindings import (
    manufacture_program_runtime_bindings,
)
from SteveCADNativeManufactureProgramRuntime import NativeManufactureProgramRuntime
from SteveCADNativeManufactureProbeBindings import manufacture_probe_runtime_bindings
from SteveCADNativeManufactureProbeRuntime import NativeManufactureProbeRuntime
from SteveCADNativeManufacturePropertyBagBindings import (
    manufacture_property_bag_runtime_bindings,
)
from SteveCADNativeManufacturePropertyBagRuntime import (
    NativeManufacturePropertyBagRuntime,
)
from SteveCADNativeManufactureOperationBindings import (
    manufacture_operation_runtime_bindings,
)
from SteveCADNativeManufactureFocusedOperationBindings import (
    manufacture_focused_operation_runtime_bindings,
)
from SteveCADNativeManufactureOperationRuntime import (
    NativeManufactureOperationRuntime,
)
from SteveCADNativeManufactureOperationGeneration import (
    start_background_operation_mutation,
)
from SteveCADNativeManufactureCamoticsBindings import (
    manufacture_camotics_runtime_bindings,
)
from SteveCADNativeManufactureCamoticsRuntime import (
    NativeManufactureCamoticsRuntime,
)
from SteveCADNativeManufacturePostBindings import manufacture_post_runtime_bindings
from SteveCADNativeManufactureFocusedPostBindings import (
    manufacture_focused_post_runtime_bindings,
)
from SteveCADNativeManufacturePostRuntime import NativeManufacturePostRuntime
from SteveCADNativeManufactureTemplateBindings import (
    manufacture_template_runtime_bindings,
)
from SteveCADNativeManufactureTemplateRuntime import (
    NativeManufactureTemplateRuntime,
)
from SteveCADNativeManufactureSimulationBindings import (
    manufacture_simulation_runtime_bindings,
)
from SteveCADNativeManufactureSimulationControlBindings import (
    manufacture_simulation_control_runtime_bindings,
)
from SteveCADNativeManufactureSimulationRuntime import (
    NativeManufactureSimulationRuntime,
)
from SteveCADNativeManufactureSimulationResultBindings import (
    manufacture_simulation_result_runtime_bindings,
)
from SteveCADNativeManufactureSimulationResultRuntime import (
    NativeManufactureSimulationResultRuntime,
)
from SteveCADNativeManufactureFollowUpBindings import (
    manufacture_follow_up_runtime_bindings,
)
from SteveCADNativeManufactureFollowUpRuntime import (
    NativeManufactureFollowUpRuntime,
)
from SteveCADNativeManufactureFollowUpSchema import (
    MANUFACTURE_FOLLOW_UP_CAPABILITY_NAME,
)
from SteveCADNativeManufactureToolBindings import manufacture_tool_runtime_bindings
from SteveCADNativeManufactureFocusedToolBindings import (
    manufacture_focused_tool_runtime_bindings,
)
from SteveCADNativeManufactureToolRuntime import (
    NativeManufactureToolCatalogRuntime,
    NativeManufactureToolRuntime,
)
from SteveCADNativeManufactureToolSchema import (
    MANUFACTURE_TOOL_CATALOG_CAPABILITY_NAME,
    MANUFACTURE_TOOL_CAPABILITY_NAME,
)
from SteveCADNativeManufactureToolOutputBindings import (
    manufacture_tool_output_runtime_bindings,
)
from SteveCADNativeManufactureToolOutputRuntime import (
    NativeManufactureToolOutputRuntime,
)
from SteveCADNativeDrawingPageBindings import drawing_page_runtime_bindings
from SteveCADNativeDrawingPageRuntime import NativeDrawingPageRuntime
from SteveCADNativeDrawingActiveViewBindings import (
    drawing_active_view_runtime_bindings,
)
from SteveCADNativeDrawingActiveViewRuntime import NativeDrawingActiveViewRuntime
from SteveCADNativeDrawingViewBindings import drawing_view_runtime_bindings
from SteveCADNativeDrawingViewRuntime import NativeDrawingViewRuntime
from SteveCADNativeDrawingSectionBindings import drawing_section_runtime_bindings
from SteveCADNativeDrawingSectionRuntime import NativeDrawingSectionRuntime
from SteveCADNativeDrawingComplexSectionBindings import (
    drawing_complex_section_runtime_bindings,
)
from SteveCADNativeDrawingComplexSectionRuntime import (
    NativeDrawingComplexSectionRuntime,
)
from SteveCADNativeDrawingDetailBindings import drawing_detail_runtime_bindings
from SteveCADNativeDrawingDetailRuntime import NativeDrawingDetailRuntime
from SteveCADNativeDrawingDraftBindings import drawing_draft_runtime_bindings
from SteveCADNativeDrawingDraftRuntime import NativeDrawingDraftRuntime
from SteveCADNativeDrawingClipBindings import drawing_clip_runtime_bindings
from SteveCADNativeDrawingClipRuntime import NativeDrawingClipRuntime
from SteveCADNativeDrawingStackBindings import drawing_stack_runtime_bindings
from SteveCADNativeDrawingStackRuntime import NativeDrawingStackRuntime
from SteveCADNativeDrawingDimensionBindings import (
    drawing_dimension_runtime_bindings,
)
from SteveCADNativeDrawingDimensionRuntime import NativeDrawingDimensionRuntime
from SteveCADNativeDrawingDimensionInferenceBindings import (
    drawing_dimension_inference_runtime_bindings,
)
from SteveCADNativeDrawingDimensionInferenceRuntime import (
    NativeDrawingDimensionInferenceRuntime,
)
from SteveCADNativeDrawingDimensionSeriesBindings import (
    drawing_dimension_series_runtime_bindings,
)
from SteveCADNativeDrawingDimensionSeriesRuntime import (
    NativeDrawingDimensionSeriesRuntime,
)
from SteveCADNativeParametersBindings import parameters_runtime_bindings
from SteveCADNativeParametersRuntime import NativeParametersRuntime
from SteveCADNativeDrawingDimensionRepairBindings import (
    drawing_dimension_repair_runtime_bindings,
)
from SteveCADNativeDrawingDimensionRepairRuntime import (
    NativeDrawingDimensionRepairRuntime,
)
from SteveCADNativeDrawingLineDefaultsBindings import (
    drawing_line_defaults_runtime_bindings,
)
from SteveCADNativeDrawingLineDefaultsRuntime import (
    NativeDrawingLineDefaultsRuntime,
)
from SteveCADNativeDrawingLineAttributesBindings import (
    drawing_line_attributes_runtime_bindings,
)
from SteveCADNativeDrawingLineAttributesRuntime import (
    NativeDrawingLineAttributesRuntime,
)
from SteveCADNativeDrawingLineLengthBindings import (
    drawing_line_length_runtime_bindings,
)
from SteveCADNativeDrawingLineLengthRuntime import (
    NativeDrawingLineLengthRuntime,
)
from SteveCADNativeDrawingViewLockBindings import (
    drawing_view_lock_runtime_bindings,
)
from SteveCADNativeDrawingViewLockRuntime import (
    NativeDrawingViewLockRuntime,
)
from SteveCADNativeDrawingPlacementBindings import (
    drawing_placement_runtime_bindings,
)
from SteveCADNativeDrawingPlacementRuntime import NativeDrawingPlacementRuntime
from SteveCADNativeDrawingSectionPositionBindings import (
    drawing_section_position_runtime_bindings,
)
from SteveCADNativeDrawingSectionPositionRuntime import (
    NativeDrawingSectionPositionRuntime,
)
from SteveCADNativeDrawingFormatBindings import (
    drawing_format_runtime_bindings,
)
from SteveCADNativeDrawingFormatRuntime import NativeDrawingFormatRuntime
from SteveCADNativeDrawingDimensionTextBindings import (
    drawing_dimension_text_runtime_bindings,
)
from SteveCADNativeDrawingDimensionTextRuntime import (
    NativeDrawingDimensionTextRuntime,
)
from SteveCADNativeDrawingPresentationBindings import (
    drawing_presentation_runtime_bindings,
)
from SteveCADNativeDrawingPresentationRuntime import (
    NativeDrawingPresentationRuntime,
)
from SteveCADNativeDrawingHatchBindings import drawing_hatch_runtime_bindings
from SteveCADNativeDrawingHatchRuntime import NativeDrawingHatchRuntime
from SteveCADNativeDrawingRichAnnotationBindings import (
    drawing_rich_annotation_runtime_bindings,
)
from SteveCADNativeDrawingRichAnnotationRuntime import (
    NativeDrawingRichAnnotationRuntime,
)
from SteveCADNativeDrawingSymbolBindings import drawing_symbol_runtime_bindings
from SteveCADNativeDrawingSymbolRuntime import NativeDrawingSymbolRuntime
from SteveCADNativeDrawingExportBindings import drawing_export_runtime_bindings
from SteveCADNativeDrawingExportRuntime import NativeDrawingExportRuntime
from SteveCADNativeDrawingLeaderBindings import drawing_leader_runtime_bindings
from SteveCADNativeDrawingLeaderRuntime import NativeDrawingLeaderRuntime
from SteveCADNativeDrawingCircleCenterLineBindings import (
    drawing_circle_center_line_runtime_bindings,
)
from SteveCADNativeDrawingCircleCenterLineRuntime import (
    NativeDrawingCircleCenterLineRuntime,
)
from SteveCADNativeDrawingGeneralCenterLineBindings import (
    drawing_general_center_line_runtime_bindings,
)
from SteveCADNativeDrawingGeneralCenterLineRuntime import (
    NativeDrawingGeneralCenterLineRuntime,
)
from SteveCADNativeDrawingBoltCircleCenterLineBindings import (
    drawing_bolt_circle_center_line_runtime_bindings,
)
from SteveCADNativeDrawingBoltCircleCenterLineRuntime import (
    NativeDrawingBoltCircleCenterLineRuntime,
)
from SteveCADNativeDrawingThreadRepresentationBindings import (
    drawing_thread_representation_runtime_bindings,
)
from SteveCADNativeDrawingThreadRepresentationRuntime import (
    NativeDrawingThreadRepresentationRuntime,
)
from SteveCADNativeDrawingCosmeticVertexBindings import (
    drawing_cosmetic_vertex_runtime_bindings,
)
from SteveCADNativeDrawingCosmeticVertexRuntime import (
    NativeDrawingCosmeticVertexRuntime,
)
from SteveCADNativeDrawingCosmeticCurveBindings import (
    drawing_cosmetic_curve_runtime_bindings,
)
from SteveCADNativeDrawingCosmeticCurveRuntime import (
    NativeDrawingCosmeticCurveRuntime,
)
from SteveCADNativeDrawingCosmeticLineBindings import (
    drawing_cosmetic_line_runtime_bindings,
)
from SteveCADNativeDrawingCosmeticLineRuntime import (
    NativeDrawingCosmeticLineRuntime,
)
from SteveCADNativeDrawingBalloonBindings import drawing_balloon_runtime_bindings
from SteveCADNativeDrawingBalloonRuntime import NativeDrawingBalloonRuntime
from SteveCADNativeRobotSetupBindings import robot_setup_runtime_bindings
from SteveCADNativeRobotSetupRuntime import NativeRobotSetupRuntime
from SteveCADNativeRobotMotionBindings import robot_motion_runtime_bindings
from SteveCADNativeRobotMotionRuntime import NativeRobotMotionRuntime
from SteveCADNativeRobotExportBindings import robot_export_runtime_bindings
from SteveCADNativeRobotExportRuntime import NativeRobotExportRuntime
from SteveCADNativeRobotTrajectoryBindings import robot_trajectory_runtime_bindings
from SteveCADNativeRobotTrajectoryRuntime import NativeRobotTrajectoryRuntime
from SteveCADNativeRuntimeContext import NativeRuntimeContext
from SteveCADNativeMeshConvertBindings import mesh_convert_runtime_bindings
from SteveCADNativeMeshConvertRuntime import NativeMeshConvertRuntime
from SteveCADNativeMeshBooleanBindings import mesh_boolean_runtime_bindings
from SteveCADNativeMeshBooleanRuntime import NativeMeshBooleanRuntime
from SteveCADNativeMeshCutBindings import mesh_cut_runtime_bindings
from SteveCADNativeMeshCutRuntime import NativeMeshCutRuntime
from SteveCADNativeMeshCurvatureBindings import mesh_curvature_runtime_bindings
from SteveCADNativeMeshCurvatureRuntime import NativeMeshCurvatureRuntime
from SteveCADNativeMeshInspectBindings import mesh_inspect_runtime_bindings
from SteveCADNativeMeshInspectRuntime import NativeMeshInspectRuntime
from SteveCADNativeMeshSegmentBindings import mesh_segment_runtime_bindings
from SteveCADNativeMeshSegmentRuntime import NativeMeshSegmentRuntime
from SteveCADNativeMeshIOBindings import mesh_io_runtime_bindings
from SteveCADNativeMeshIORuntime import NativeMeshIORuntime
from SteveCADNativeMeshModifyBindings import mesh_modify_runtime_bindings
from SteveCADNativeMeshModifyRuntime import NativeMeshModifyRuntime
from SteveCADNativeMeshPointsBindings import mesh_points_runtime_bindings
from SteveCADNativeMeshPointsRuntime import NativeMeshPointsRuntime
from SteveCADNativeReverseBindings import reverse_runtime_bindings
from SteveCADNativeReverseRuntime import NativeReverseRuntime
from SteveCADNativeReconstructParametricBindings import (
    reconstruct_parametric_runtime_bindings,
)
from SteveCADNativeReconstructParametricRuntime import NativeReconstructParametricRuntime
from SteveCADNativeMeshExportBindings import mesh_export_runtime_bindings
from SteveCADNativeMeshExportRuntime import NativeMeshExportRuntime
from SteveCADNativeBackgroundBindings import native_background_runtime_bindings
from SteveCADNativeBackgroundRuntime import NativeBackgroundRuntime
from SteveCADNativeSketchProviderBindings import sketch_provider_runtime_bindings
from SteveCADNativeSketchProviderRuntime import NativeSketchProviderRuntime


def build_native_runtime_bindings(
    context: NativeRuntimeContext,
    tool_names: tuple[str, ...],
) -> dict[str, Any]:
    """Return fresh exact runtime bindings for one Native assistant turn."""

    if not isinstance(context, NativeRuntimeContext):
        raise TypeError("context must be a NativeRuntimeContext")
    analyze_model = NativeAnalyzeModelRuntime(context)
    analyze_inspect = NativeAnalyzeInspectRuntime(context)
    analyze_assignment_view = NativeAnalyzeAssignmentViewRuntime(context)
    analyze_geometry = NativeAnalyzeGeometryRuntime(context)
    analyze_electromagnetic = NativeAnalyzeElectromagneticRuntime(context)
    analyze_fluid = NativeAnalyzeFluidRuntime(context)
    analyze_geometrical = NativeAnalyzeGeometricalRuntime(context)
    analyze_support = NativeAnalyzeSupportRuntime(context)
    analyze_connection = NativeAnalyzeConnectionRuntime(context)
    analyze_load = NativeAnalyzeLoadRuntime(context)
    analyze_thermal = NativeAnalyzeThermalRuntime(context)
    analyze_mesh = NativeAnalyzeMeshRuntime(context)
    analyze_mesh_field = NativeAnalyzeMeshFieldRuntime(context)
    analyze_mesh_output = NativeAnalyzeMeshOutputRuntime(context)
    analyze_mesh_refinement = NativeAnalyzeMeshRefinementRuntime(context)
    analyze_structured_mesh = NativeAnalyzeStructuredMeshRuntime(context)
    analyze_solver = NativeAnalyzeSolverRuntime(context)
    analyze_solver_control = NativeAnalyzeSolverControlRuntime(context)
    analyze_solver_execution = NativeAnalyzeSolverExecutionRuntime(context)
    analyze_equation = NativeAnalyzeEquationRuntime(context)
    analyze_results = NativeAnalyzeResultsRuntime(context)
    analyze_presentation = NativeAnalyzePresentationRuntime(context)
    analyze_post = NativeAnalyzePostRuntime(context)
    analyze_post_function = NativeAnalyzePostFunctionRuntime(context)
    analyze_visualization = NativeAnalyzeVisualizationRuntime(context)
    common = NativeCommonRuntime(context=context)
    inspection_compare = NativeInspectionCompareRuntime(context)
    workspace = NativeWorkspaceRuntime(context)
    background = NativeBackgroundRuntime(context)
    mesh_convert = NativeMeshConvertRuntime(context)
    mesh_io = NativeMeshIORuntime(context)
    mesh_export = NativeMeshExportRuntime(context)
    mesh_modify = NativeMeshModifyRuntime(context)
    mesh_boolean = NativeMeshBooleanRuntime(context)
    mesh_cut = NativeMeshCutRuntime(context)
    mesh_inspect = NativeMeshInspectRuntime(context)
    mesh_curvature = NativeMeshCurvatureRuntime(context)
    mesh_segment = NativeMeshSegmentRuntime(context)
    mesh_points = NativeMeshPointsRuntime(context)
    mesh_rebuild = NativeReverseRuntime(context, "mesh.rebuild")
    mesh_approximate = NativeReverseRuntime(context, "mesh.approximate")
    mesh_reconstruct_parametric = NativeReconstructParametricRuntime(context)
    assembly_diagnosis = NativeAssemblyDiagnosisRuntime(context)
    assembly_bom = NativeAssemblyBomRuntime(context)
    assembly_fastener = NativeAssemblyFastenerRuntime(context)
    assembly_export = NativeAssemblyExportRuntime(context)
    assembly_inspect = NativeAssemblyInspectRuntime(context)
    assembly_joint = NativeAssemblyJointRuntime(context)
    assembly_playback = NativeAssemblyPlaybackRuntime(context)
    assembly_structure = NativeAssemblyStructureRuntime(context)
    component_interface = NativeComponentInterfaceRuntime(context)
    model_catalog = NativeModelCatalogRuntime(context)
    model_boolean = NativeModelBooleanRuntime(context)
    model_feature = NativeModelFeatureRuntime(context)
    model_fastener = NativeModelFastenerRuntime(context)
    model_dressup = NativeModelDressupRuntime(context)
    model_hole = NativeModelHoleRuntime(context)
    model_history = NativeModelHistoryRuntime(context)
    sheetmetal_inspect = NativeSheetMetalInspectRuntime(context)
    sheetmetal_view = NativeSheetMetalViewRuntime(context)
    sheetmetal_edit = NativeSheetMetalEditRuntime(context)
    sheetmetal_create = NativeSheetMetalCreateRuntime(context)
    sheetmetal_connection = NativeSheetMetalConnectionRuntime(context)
    sheetmetal_manufacturing = NativeSheetMetalManufacturingRuntime(context)
    model_join = NativeModelJoinRuntime(context)
    model_part = NativeModelPartRuntime(context)
    model_surface = NativeModelSurfaceRuntime(context)
    model_structure = NativeModelStructureRuntime(context)
    sketch_setup = NativeSketchSetupRuntime(context)
    model_transform = NativeModelTransformRuntime(context)
    manufacture_inspect = NativeManufactureInspectRuntime(context)
    manufacture_job = (
        NativeManufactureJobRuntime(context)
        if MANUFACTURE_JOB_CAPABILITY_NAME in tool_names
        else None
    )
    manufacture_area = NativeManufactureAreaRuntime(context)
    manufacture_modify = NativeManufactureModifyRuntime(context)
    manufacture_program = NativeManufactureProgramRuntime(context)
    manufacture_probe = NativeManufactureProbeRuntime(context)
    manufacture_property_bag = NativeManufacturePropertyBagRuntime(context)
    manufacture_operation = NativeManufactureOperationRuntime(
        context,
        mutation_executor=start_background_operation_mutation,
    )
    manufacture_camotics = NativeManufactureCamoticsRuntime(context)
    manufacture_post = NativeManufacturePostRuntime(context)
    manufacture_template = NativeManufactureTemplateRuntime(context)
    manufacture_simulation = NativeManufactureSimulationRuntime(context)
    manufacture_simulation_result = NativeManufactureSimulationResultRuntime(context)
    manufacture_follow_up = (
        NativeManufactureFollowUpRuntime(context)
        if MANUFACTURE_FOLLOW_UP_CAPABILITY_NAME in tool_names
        else None
    )
    manufacture_tool_catalog = (
        NativeManufactureToolCatalogRuntime(context)
        if MANUFACTURE_TOOL_CATALOG_CAPABILITY_NAME in tool_names
        else None
    )
    manufacture_tool = NativeManufactureToolRuntime(context)
    manufacture_tool_output = NativeManufactureToolOutputRuntime(context)
    drawing_page = NativeDrawingPageRuntime(context)
    drawing_active_view = NativeDrawingActiveViewRuntime(context)
    drawing_view = NativeDrawingViewRuntime(context)
    drawing_section = NativeDrawingSectionRuntime(context)
    drawing_complex_section = NativeDrawingComplexSectionRuntime(context)
    drawing_detail = NativeDrawingDetailRuntime(context)
    drawing_draft = NativeDrawingDraftRuntime(context)
    drawing_clip = NativeDrawingClipRuntime(context)
    drawing_stack = NativeDrawingStackRuntime(context)
    drawing_dimension = NativeDrawingDimensionRuntime(context)
    drawing_dimension_inference = NativeDrawingDimensionInferenceRuntime(context)
    drawing_dimension_series = NativeDrawingDimensionSeriesRuntime(context)
    parameters = NativeParametersRuntime(context)
    drawing_dimension_repair = NativeDrawingDimensionRepairRuntime(context)
    drawing_line_defaults = NativeDrawingLineDefaultsRuntime(context)
    drawing_line_attributes = NativeDrawingLineAttributesRuntime(context)
    drawing_line_length = NativeDrawingLineLengthRuntime(context)
    drawing_view_lock = NativeDrawingViewLockRuntime(context)
    drawing_placement = NativeDrawingPlacementRuntime(context)
    drawing_section_position = NativeDrawingSectionPositionRuntime(context)
    drawing_format = NativeDrawingFormatRuntime(context)
    drawing_dimension_text = NativeDrawingDimensionTextRuntime(context)
    drawing_presentation = NativeDrawingPresentationRuntime(context)
    drawing_hatch = NativeDrawingHatchRuntime(context)
    drawing_rich_annotation = NativeDrawingRichAnnotationRuntime(context)
    drawing_symbol = NativeDrawingSymbolRuntime(context)
    drawing_export = NativeDrawingExportRuntime(context)
    drawing_leader = NativeDrawingLeaderRuntime(context)
    drawing_circle_center_line = NativeDrawingCircleCenterLineRuntime(context)
    drawing_general_center_line = NativeDrawingGeneralCenterLineRuntime(context)
    drawing_bolt_circle_center_line = NativeDrawingBoltCircleCenterLineRuntime(
        context
    )
    drawing_thread_representation = NativeDrawingThreadRepresentationRuntime(
        context
    )
    drawing_cosmetic_vertex = NativeDrawingCosmeticVertexRuntime(context)
    drawing_cosmetic_curve = NativeDrawingCosmeticCurveRuntime(context)
    drawing_cosmetic_line = NativeDrawingCosmeticLineRuntime(context)
    drawing_balloon = NativeDrawingBalloonRuntime(context)
    robot_setup = NativeRobotSetupRuntime(context)
    robot_motion = NativeRobotMotionRuntime(context)
    robot_export = NativeRobotExportRuntime(context)
    robot_trajectory = NativeRobotTrajectoryRuntime(context)
    sketch_provider = NativeSketchProviderRuntime(context)
    aero_solve = NativeAeroRuntime(context)
    available = {
        **analyze_model_runtime_bindings(analyze_model),
        **analyze_solid_domain_runtime_bindings(analyze_model),
        **analyze_inspect_runtime_bindings(analyze_inspect),
        **analyze_face_runtime_bindings(analyze_inspect),
        **analyze_flow_result_runtime_bindings(analyze_inspect),
        **analyze_mechanical_result_runtime_bindings(analyze_inspect),
        **analyze_thermal_result_runtime_bindings(analyze_inspect),
        **analyze_assignment_view_runtime_bindings(analyze_assignment_view),
        **analyze_geometry_runtime_bindings(analyze_geometry),
        **analyze_electromagnetic_runtime_bindings(analyze_electromagnetic),
        **analyze_fluid_runtime_bindings(analyze_fluid),
        **analyze_fluid_create_runtime_bindings(analyze_fluid),
        **analyze_cfd_lifecycle_runtime_bindings(analyze_model, analyze_solver),
        **analyze_geometrical_runtime_bindings(analyze_geometrical),
        **analyze_support_runtime_bindings(analyze_support),
        **analyze_structural_lifecycle_runtime_bindings(
            analyze_model,
            analyze_support,
            analyze_load,
        ),
        **analyze_connection_runtime_bindings(analyze_connection),
        **analyze_load_runtime_bindings(analyze_load),
        **analyze_thermal_runtime_bindings(analyze_thermal),
        **analyze_mesh_runtime_bindings(analyze_mesh),
        **analyze_mesh_lifecycle_runtime_bindings(analyze_mesh),
        **analyze_mesh_field_runtime_bindings(analyze_mesh_field),
        **analyze_mesh_output_runtime_bindings(analyze_mesh_output),
        **analyze_mesh_refinement_runtime_bindings(analyze_mesh_refinement),
        **analyze_local_mesh_runtime_bindings(analyze_mesh_refinement),
        **analyze_structured_mesh_runtime_bindings(analyze_structured_mesh),
        **analyze_solver_runtime_bindings(analyze_solver),
        **analyze_solver_control_runtime_bindings(analyze_solver_control),
        **analyze_solver_execution_runtime_bindings(analyze_solver_execution),
        **analyze_run_solver_runtime_bindings(analyze_solver_execution),
        **analyze_equation_runtime_bindings(analyze_equation),
        **analyze_results_runtime_bindings(analyze_results),
        **analyze_presentation_runtime_bindings(analyze_presentation),
        **analyze_flow_presentation_runtime_bindings(analyze_presentation),
        **analyze_mechanical_presentation_runtime_bindings(analyze_presentation),
        **analyze_thermal_presentation_runtime_bindings(analyze_presentation),
        **analyze_post_runtime_bindings(analyze_post),
        **analyze_post_function_runtime_bindings(analyze_post_function),
        **analyze_visualization_runtime_bindings(analyze_visualization),
        **aero_solve_runtime_bindings(aero_solve),
        **common_runtime_bindings(common),
        **inspection_compare_runtime_bindings(inspection_compare),
        **workspace_runtime_bindings(workspace),
        **native_background_runtime_bindings(background),
        **mesh_convert_runtime_bindings(mesh_convert),
        **mesh_io_runtime_bindings(mesh_io),
        **mesh_export_runtime_bindings(mesh_export),
        **mesh_modify_runtime_bindings(mesh_modify),
        **mesh_boolean_runtime_bindings(mesh_boolean),
        **mesh_cut_runtime_bindings(mesh_cut),
        **mesh_inspect_runtime_bindings(mesh_inspect),
        **mesh_curvature_runtime_bindings(mesh_curvature),
        **mesh_segment_runtime_bindings(mesh_segment),
        **mesh_points_runtime_bindings(mesh_points),
        **reverse_runtime_bindings(mesh_rebuild, mesh_approximate),
        **reconstruct_parametric_runtime_bindings(mesh_reconstruct_parametric),
        **assembly_diagnosis_runtime_bindings(assembly_diagnosis),
        **assembly_bom_runtime_bindings(assembly_bom),
        **assembly_fastener_runtime_bindings(assembly_fastener),
        **assembly_export_runtime_bindings(assembly_export),
        **assembly_inspect_runtime_bindings(assembly_inspect),
        **assembly_joint_runtime_bindings(assembly_joint),
        **assembly_playback_runtime_bindings(assembly_playback),
        **assembly_structure_runtime_bindings(assembly_structure),
        **component_interface_runtime_bindings(component_interface),
        **model_catalog_runtime_bindings(model_catalog),
        **model_boolean_runtime_bindings(model_boolean),
        **model_feature_runtime_bindings(model_feature),
        **model_fastener_runtime_bindings(model_fastener),
        **model_dressup_runtime_bindings(model_dressup),
        **model_hole_runtime_bindings(model_hole),
        **model_history_runtime_bindings(model_history),
        **sheetmetal_inspect_runtime_bindings(sheetmetal_inspect),
        **sheetmetal_view_runtime_bindings(sheetmetal_view),
        **sheetmetal_edit_runtime_bindings(sheetmetal_edit),
        **sheetmetal_create_runtime_bindings(sheetmetal_create),
        **sheetmetal_connection_runtime_bindings(sheetmetal_connection),
        **sheetmetal_manufacturing_runtime_bindings(sheetmetal_manufacturing),
        **model_join_runtime_bindings(model_join),
        **model_part_runtime_bindings(model_part),
        **model_surface_runtime_bindings(model_surface),
        **model_structure_runtime_bindings(model_structure),
        **sketch_setup_runtime_bindings(sketch_setup),
        **model_transform_runtime_bindings(model_transform),
        **manufacture_inspect_runtime_bindings(manufacture_inspect),
        **manufacture_focused_inspect_runtime_bindings(manufacture_inspect),
        **(
            manufacture_job_runtime_bindings(manufacture_job)
            if manufacture_job is not None
            else {}
        ),
        **manufacture_area_runtime_bindings(manufacture_area),
        **manufacture_modify_runtime_bindings(manufacture_modify),
        **manufacture_focused_modify_runtime_bindings(manufacture_modify),
        **manufacture_program_runtime_bindings(manufacture_program),
        **manufacture_probe_runtime_bindings(manufacture_probe),
        **manufacture_property_bag_runtime_bindings(manufacture_property_bag),
        **manufacture_operation_runtime_bindings(manufacture_operation),
        **manufacture_focused_operation_runtime_bindings(manufacture_operation),
        **manufacture_camotics_runtime_bindings(manufacture_camotics),
        **manufacture_post_runtime_bindings(manufacture_post),
        **manufacture_focused_post_runtime_bindings(manufacture_post),
        **manufacture_template_runtime_bindings(manufacture_template),
        **manufacture_simulation_runtime_bindings(manufacture_simulation),
        **manufacture_simulation_control_runtime_bindings(manufacture_simulation),
        **manufacture_simulation_result_runtime_bindings(
            manufacture_simulation_result
        ),
        **(
            manufacture_follow_up_runtime_bindings(manufacture_follow_up)
            if manufacture_follow_up is not None
            else {}
        ),
        **(
            manufacture_tool_runtime_bindings(
                manufacture_tool_catalog,
                manufacture_tool,
            )
            if manufacture_tool_catalog is not None
            else {MANUFACTURE_TOOL_CAPABILITY_NAME: manufacture_tool}
        ),
        **manufacture_focused_tool_runtime_bindings(manufacture_tool),
        **manufacture_tool_output_runtime_bindings(manufacture_tool_output),
        **drawing_page_runtime_bindings(drawing_page),
        **drawing_active_view_runtime_bindings(drawing_active_view),
        **drawing_view_runtime_bindings(drawing_view),
        **drawing_section_runtime_bindings(drawing_section),
        **drawing_complex_section_runtime_bindings(drawing_complex_section),
        **drawing_detail_runtime_bindings(drawing_detail),
        **drawing_draft_runtime_bindings(drawing_draft),
        **drawing_clip_runtime_bindings(drawing_clip),
        **drawing_stack_runtime_bindings(drawing_stack),
        **drawing_dimension_runtime_bindings(drawing_dimension),
        **drawing_dimension_inference_runtime_bindings(drawing_dimension_inference),
        **drawing_dimension_series_runtime_bindings(drawing_dimension_series),
        **parameters_runtime_bindings(parameters),
        **drawing_dimension_repair_runtime_bindings(drawing_dimension_repair),
        **drawing_line_defaults_runtime_bindings(drawing_line_defaults),
        **drawing_line_attributes_runtime_bindings(drawing_line_attributes),
        **drawing_line_length_runtime_bindings(drawing_line_length),
        **drawing_view_lock_runtime_bindings(drawing_view_lock),
        **drawing_placement_runtime_bindings(drawing_placement),
        **drawing_section_position_runtime_bindings(drawing_section_position),
        **drawing_format_runtime_bindings(drawing_format),
        **drawing_dimension_text_runtime_bindings(drawing_dimension_text),
        **drawing_presentation_runtime_bindings(drawing_presentation),
        **drawing_hatch_runtime_bindings(drawing_hatch),
        **drawing_rich_annotation_runtime_bindings(drawing_rich_annotation),
        **drawing_symbol_runtime_bindings(drawing_symbol),
        **drawing_export_runtime_bindings(drawing_export),
        **drawing_leader_runtime_bindings(drawing_leader),
        **drawing_circle_center_line_runtime_bindings(
            drawing_circle_center_line
        ),
        **drawing_general_center_line_runtime_bindings(
            drawing_general_center_line
        ),
        **drawing_bolt_circle_center_line_runtime_bindings(
            drawing_bolt_circle_center_line
        ),
        **drawing_thread_representation_runtime_bindings(
            drawing_thread_representation
        ),
        **drawing_cosmetic_vertex_runtime_bindings(drawing_cosmetic_vertex),
        **drawing_cosmetic_curve_runtime_bindings(drawing_cosmetic_curve),
        **drawing_cosmetic_line_runtime_bindings(drawing_cosmetic_line),
        **drawing_balloon_runtime_bindings(drawing_balloon),
        **robot_setup_runtime_bindings(robot_setup),
        **robot_motion_runtime_bindings(robot_motion),
        **robot_export_runtime_bindings(robot_export),
        **robot_trajectory_runtime_bindings(robot_trajectory),
        **sketch_provider_runtime_bindings(sketch_provider),
    }
    missing = sorted(set(tool_names) - set(available))
    if missing:
        raise RuntimeError(f"Native runtime bindings are missing: {missing}.")
    return {name: available[name] for name in tool_names}
