# SPDX-License-Identifier: LGPL-2.1-or-later

"""Production assembly point for Native capability contracts and bindings."""

from __future__ import annotations

from SteveCADNativeAnalyzeInspectBindings import (
    register_analyze_inspect_capability_implementation,
)
from SteveCADNativeAnalyzeFaceBindings import (
    register_analyze_face_capability_implementation,
)
from SteveCADNativeAnalyzeFaceSchema import (
    register_analyze_face_capability_definition,
)
from SteveCADNativeAnalyzeFlowResultBindings import (
    register_analyze_flow_result_capability_implementation,
)
from SteveCADNativeAnalyzeFlowResultSchema import (
    register_analyze_flow_result_capability_definition,
)
from SteveCADNativeAnalyzeMechanicalResultBindings import (
    register_analyze_mechanical_result_capability_implementations,
)
from SteveCADNativeAnalyzeMechanicalResultSchema import (
    register_analyze_mechanical_result_capability_definitions,
)
from SteveCADNativeAnalyzeThermalResultBindings import (
    register_analyze_thermal_result_capability_implementations,
)
from SteveCADNativeAnalyzeThermalResultSchema import (
    register_analyze_thermal_result_capability_definitions,
)
from SteveCADNativeAnalyzeElectromagneticBindings import (
    register_analyze_electromagnetic_capability_implementation,
)
from SteveCADNativeAnalyzeElectromagneticSchema import (
    register_analyze_electromagnetic_capability_definition,
)
from SteveCADNativeAnalyzeFluidBindings import (
    register_analyze_fluid_capability_implementation,
)
from SteveCADNativeAnalyzeFluidSchema import (
    register_analyze_fluid_capability_definition,
)
from SteveCADNativeAnalyzeFluidCreateBindings import (
    register_analyze_fluid_create_capability_implementations,
)
from SteveCADNativeAnalyzeFluidCreateSchema import (
    register_analyze_fluid_create_capability_definitions,
)
from SteveCADNativeAnalyzeCfdLifecycleBindings import (
    register_analyze_cfd_lifecycle_capability_implementations,
)
from SteveCADNativeAnalyzeCfdLifecycleSchema import (
    register_analyze_cfd_lifecycle_capability_definitions,
)
from SteveCADNativeAnalyzeGeometricalBindings import (
    register_analyze_geometrical_capability_implementation,
)
from SteveCADNativeAnalyzeGeometricalSchema import (
    register_analyze_geometrical_capability_definition,
)
from SteveCADNativeAnalyzeSupportBindings import (
    register_analyze_support_capability_implementation,
)
from SteveCADNativeAnalyzeSupportSchema import (
    register_analyze_support_capability_definition,
)
from SteveCADNativeAnalyzeStructuralLifecycleBindings import (
    register_analyze_structural_lifecycle_capability_implementations,
)
from SteveCADNativeAnalyzeStructuralLifecycleSchema import (
    register_analyze_structural_lifecycle_capability_definitions,
)
from SteveCADNativeAnalyzeConnectionBindings import (
    register_analyze_connection_capability_implementation,
)
from SteveCADNativeAnalyzeConnectionSchema import (
    register_analyze_connection_capability_definition,
)
from SteveCADNativeAnalyzeLoadBindings import (
    register_analyze_load_capability_implementation,
)
from SteveCADNativeAnalyzeLoadSchema import (
    register_analyze_load_capability_definition,
)
from SteveCADNativeAnalyzeThermalBindings import (
    register_analyze_thermal_capability_implementation,
)
from SteveCADNativeAnalyzeThermalSchema import (
    register_analyze_thermal_capability_definition,
)
from SteveCADNativeAnalyzeMeshBindings import (
    register_analyze_mesh_capability_implementation,
)
from SteveCADNativeAnalyzeMeshSchema import (
    register_analyze_mesh_capability_definition,
)
from SteveCADNativeAnalyzeMeshLifecycleBindings import (
    register_analyze_mesh_lifecycle_capability_implementations,
)
from SteveCADNativeAnalyzeMeshLifecycleSchema import (
    register_analyze_mesh_lifecycle_capability_definitions,
)
from SteveCADNativeAnalyzeLocalMeshBindings import (
    register_analyze_local_mesh_capability_implementations,
)
from SteveCADNativeAnalyzeLocalMeshSchema import (
    register_analyze_local_mesh_capability_definitions,
)
from SteveCADNativeAnalyzeMeshFieldBindings import (
    register_analyze_mesh_field_capability_implementation,
)
from SteveCADNativeAnalyzeMeshFieldSchema import (
    register_analyze_mesh_field_capability_definition,
)
from SteveCADNativeAnalyzeMeshOutputBindings import (
    register_analyze_mesh_output_capability_implementation,
)
from SteveCADNativeAnalyzeMeshOutputSchema import (
    register_analyze_mesh_output_capability_definition,
)
from SteveCADNativeAnalyzeMeshRefinementBindings import (
    register_analyze_mesh_refinement_capability_implementation,
)
from SteveCADNativeAnalyzeMeshRefinementSchema import (
    register_analyze_mesh_refinement_capability_definition,
)
from SteveCADNativeAnalyzeStructuredMeshBindings import (
    register_analyze_structured_mesh_capability_implementation,
)
from SteveCADNativeAnalyzeStructuredMeshSchema import (
    register_analyze_structured_mesh_capability_definition,
)
from SteveCADNativeAnalyzeSolverBindings import (
    register_analyze_solver_capability_implementation,
)
from SteveCADNativeAnalyzeSolverSchema import (
    register_analyze_solver_capability_definition,
)
from SteveCADNativeAnalyzeSolverControlBindings import (
    register_analyze_solver_control_capability_implementation,
)
from SteveCADNativeAnalyzeSolverControlSchema import (
    register_analyze_solver_control_capability_definition,
)
from SteveCADNativeAnalyzeSolverExecutionBindings import (
    register_analyze_solver_execution_capability_implementation,
)
from SteveCADNativeAnalyzeSolverExecutionSchema import (
    register_analyze_solver_execution_capability_definition,
)
from SteveCADNativeAnalyzeRunBindings import (
    register_analyze_run_solver_capability_implementation,
)
from SteveCADNativeAnalyzeRunSchema import (
    register_analyze_run_solver_capability_definition,
)
from SteveCADNativeAnalyzeEquationBindings import (
    register_analyze_equation_capability_implementation,
)
from SteveCADNativeAnalyzeEquationSchema import (
    register_analyze_equation_capability_definition,
)
from SteveCADNativeAnalyzeResultsBindings import (
    register_analyze_results_capability_implementation,
)
from SteveCADNativeAnalyzeResultsSchema import (
    register_analyze_results_capability_definition,
)
from SteveCADNativeAnalyzePresentationBindings import (
    register_analyze_presentation_capability_implementation,
)
from SteveCADNativeAnalyzePresentationSchema import (
    register_analyze_presentation_capability_definition,
)
from SteveCADNativeAnalyzePostBindings import (
    register_analyze_post_capability_implementation,
)
from SteveCADNativeAnalyzePostSchema import (
    register_analyze_post_capability_definition,
)
from SteveCADNativeAnalyzePostFunctionBindings import (
    register_analyze_post_function_capability_implementation,
)
from SteveCADNativeAnalyzePostFunctionSchema import (
    register_analyze_post_function_capability_definition,
)
from SteveCADNativeAnalyzeVisualizationBindings import (
    register_analyze_visualization_capability_implementation,
)
from SteveCADNativeAnalyzeVisualizationSchema import (
    register_analyze_visualization_capability_definition,
)
from SteveCADNativeAnalyzeGeometryBindings import (
    register_analyze_geometry_capability_implementation,
)
from SteveCADNativeAnalyzeGeometrySchema import (
    register_analyze_geometry_capability_definition,
)
from SteveCADNativeAnalyzeInspectSchema import (
    register_analyze_inspect_capability_definition,
)
from SteveCADNativeAnalyzeAssignmentViewBindings import (
    register_analyze_assignment_view_capability_implementation,
)
from SteveCADNativeAnalyzeAssignmentViewSchema import (
    register_analyze_assignment_view_capability_definition,
)
from SteveCADNativeAnalyzeModelBindings import (
    register_analyze_model_capability_implementation,
)
from SteveCADNativeAnalyzeModelSchema import (
    register_analyze_model_capability_definition,
)
from SteveCADNativeAnalyzeSolidDomainBindings import (
    register_analyze_solid_domain_capability_implementation,
)
from SteveCADNativeAnalyzeSolidDomainSchema import (
    register_analyze_solid_domain_capability_definition,
)
from SteveCADNativeAssemblyDiagnosisBindings import (
    register_assembly_diagnosis_capability_implementation,
)
from SteveCADNativeAssemblyDiagnosisSchema import (
    register_assembly_diagnosis_capability_definition,
)
from SteveCADNativeAssemblyBomBindings import (
    register_assembly_bom_capability_implementation,
)
from SteveCADNativeAssemblyBomSchema import (
    register_assembly_bom_capability_definition,
)
from SteveCADNativeAssemblyFastenerBindings import (
    register_assembly_fastener_capability_implementation,
)
from SteveCADNativeAssemblyFastenerSchema import (
    register_assembly_fastener_capability_definition,
)
from SteveCADNativeAssemblyExportBindings import (
    register_assembly_export_capability_implementation,
)
from SteveCADNativeAssemblyExportSchema import (
    register_assembly_export_capability_definition,
)
from SteveCADNativeAssemblyInspectBindings import (
    register_assembly_connectors_capability_implementation,
    register_assembly_inspect_capability_implementation,
)
from SteveCADNativeAssemblyInspectSchema import (
    register_assembly_connectors_capability_definition,
    register_assembly_inspect_capability_definition,
)
from SteveCADNativeAssemblyJointBindings import (
    register_assembly_joint_capability_implementation,
)
from SteveCADNativeAssemblyJointSchema import (
    register_assembly_joint_capability_definition,
)
from SteveCADNativeAssemblyPlaybackBindings import (
    register_assembly_playback_capability_implementation,
)
from SteveCADNativeAssemblyPlaybackSchema import (
    register_assembly_playback_capability_definition,
)
from SteveCADNativeAssemblyStructureBindings import (
    register_assembly_structure_capability_implementation,
)
from SteveCADNativeAssemblyStructureSchema import (
    register_assembly_structure_capability_definition,
)
from SteveCADNativeCapabilityRegistry import NativeCapabilityRegistry
from SteveCADNativeParametersBindings import (
    register_parameters_capability_implementations,
)
from SteveCADNativeParametersSchema import (
    register_parameters_capability_definitions,
)
from SteveCADNativeMeshConvertBindings import (
    register_mesh_convert_capability_implementation,
)
from SteveCADNativeMeshConvertSchema import register_mesh_convert_capability_definition
from SteveCADNativeMeshBooleanBindings import (
    register_mesh_boolean_capability_implementation,
)
from SteveCADNativeMeshBooleanSchema import register_mesh_boolean_capability_definition
from SteveCADNativeMeshCutBindings import register_mesh_cut_capability_implementation
from SteveCADNativeMeshCutSchema import register_mesh_cut_capability_definition
from SteveCADNativeMeshCurvatureBindings import (
    register_mesh_curvature_capability_implementation,
)
from SteveCADNativeMeshCurvatureSchema import (
    register_mesh_curvature_capability_definition,
)
from SteveCADNativeMeshInspectBindings import (
    register_mesh_inspect_capability_implementation,
)
from SteveCADNativeMeshInspectSchema import register_mesh_inspect_capability_definition
from SteveCADNativeMeshSegmentBindings import (
    register_mesh_segment_capability_implementation,
)
from SteveCADNativeMeshSegmentSchema import register_mesh_segment_capability_definition
from SteveCADNativeMeshIOBindings import register_mesh_io_capability_implementation
from SteveCADNativeMeshIOSchema import register_mesh_io_capability_definition
from SteveCADNativeMeshModifyBindings import (
    register_mesh_modify_capability_implementation,
)
from SteveCADNativeMeshModifySchema import register_mesh_modify_capability_definition
from SteveCADNativeMeshPointsBindings import (
    register_mesh_points_capability_implementation,
)
from SteveCADNativeMeshPointsSchema import register_mesh_points_capability_definition
from SteveCADNativeMeshApproximateSchema import (
    register_mesh_approximate_capability_definition,
)
from SteveCADNativeMeshRebuildSchema import register_mesh_rebuild_capability_definition
from SteveCADNativeMeshReconstructParametricSchema import (
    register_mesh_reconstruct_parametric_capability_definition,
)
from SteveCADNativeReverseBindings import register_reverse_capability_implementations
from SteveCADNativeReconstructParametricBindings import (
    register_mesh_reconstruct_parametric_capability_implementation,
)
from SteveCADNativeMeshExportBindings import (
    register_mesh_export_capability_implementation,
)
from SteveCADNativeMeshExportSchema import register_mesh_export_capability_definition
from SteveCADNativeAeroBindings import (
    register_aero_solve_capability_implementation,
)
from SteveCADNativeAeroSchema import register_aero_solve_capability_definition
from SteveCADNativeBackgroundBindings import (
    register_native_background_capability_implementation,
)
from SteveCADNativeBackgroundSchema import (
    register_native_background_capability_definition,
)
from SteveCADNativeComponentInterfaceBindings import (
    register_component_interface_capability_implementation,
    register_component_interfaces_capability_implementation,
)
from SteveCADNativeComponentInterfaceSchema import (
    register_component_interface_capability_definition,
    register_component_interfaces_capability_definition,
)
from SteveCADNativeCommonBindings import register_common_capability_implementations
from SteveCADNativeCommonSchema import register_common_capability_definitions
from SteveCADNativeInspectionCompareBindings import (
    register_inspection_compare_capability_implementation,
)
from SteveCADNativeInspectionCompareSchema import (
    register_inspection_compare_capability_definition,
)
from SteveCADNativeWorkspaceBindings import (
    register_workspace_capability_implementation,
)
from SteveCADNativeWorkspaceSchema import register_workspace_capability_definition
from SteveCADNativeModelCatalogBindings import (
    register_model_catalog_capability_implementation,
)
from SteveCADNativeModelCatalogSchema import (
    register_model_catalog_capability_definition,
)
from SteveCADNativeModelDressupBindings import (
    register_model_dressup_capability_implementation,
)
from SteveCADNativeModelDressupSchema import (
    register_model_dressup_capability_definition,
)
from SteveCADNativeModelBooleanBindings import (
    register_model_boolean_capability_implementation,
)
from SteveCADNativeModelBooleanSchema import (
    register_model_boolean_capability_definition,
)
from SteveCADNativeModelFeatureBindings import (
    register_model_feature_capability_implementation,
)
from SteveCADNativeModelFeatureSchema import (
    register_model_feature_capability_definition,
)
from SteveCADNativeModelFastenerBindings import (
    register_model_fastener_capability_implementation,
)
from SteveCADNativeModelFastenerSchema import (
    register_model_fastener_capability_definition,
)
from SteveCADNativeModelHoleBindings import (
    register_model_hole_capability_implementations,
)
from SteveCADNativeModelHoleSchema import (
    register_model_hole_capability_definitions,
)
from SteveCADNativeModelHistoryBindings import (
    register_model_history_capability_implementations,
)
from SteveCADNativeModelHistorySchema import (
    register_model_history_capability_definitions,
)
from SteveCADNativeSheetMetalInspectBindings import register_sheetmetal_inspect
from SteveCADNativeSheetMetalViewBindings import register_sheetmetal_view
from SteveCADNativeSheetMetalEditBindings import register_sheetmetal_edit
from SteveCADNativeSheetMetalCreateBindings import register_sheetmetal_create
from SteveCADNativeSheetMetalConnectionBindings import register_sheetmetal_connection
from SteveCADNativeSheetMetalManufacturingBindings import register_sheetmetal_manufacturing
from SteveCADNativeModelJoinBindings import (
    register_model_join_capability_implementation,
)
from SteveCADNativeModelJoinSchema import register_model_join_capability_definition
from SteveCADNativeModelPartBindings import (
    register_model_part_capability_implementation,
)
from SteveCADNativeModelPartSchema import register_model_part_capability_definition
from SteveCADNativeModelSurfaceBindings import (
    register_model_surface_capability_implementation,
)
from SteveCADNativeModelSurfaceSchema import (
    register_model_surface_capability_definition,
)
from SteveCADNativeModelStructureBindings import (
    register_model_structure_capability_implementations,
)
from SteveCADNativeModelStructureSchema import (
    register_model_structure_capability_definitions,
)
from SteveCADNativeSketchSetupBindings import (
    register_sketch_setup_capability_implementation,
)
from SteveCADNativeSketchSetupSchema import (
    register_sketch_setup_capability_definition,
)
from SteveCADNativeModelTransformBindings import (
    register_model_transform_capability_implementation,
)
from SteveCADNativeModelTransformSchema import (
    register_model_transform_capability_definition,
)
from SteveCADNativeManufactureInspectBindings import (
    register_manufacture_inspect_capability_implementation,
)
from SteveCADNativeManufactureInspectSchema import (
    register_manufacture_inspect_capability_definition,
)
from SteveCADNativeManufactureFocusedInspectBindings import (
    register_manufacture_focused_inspect_capability_implementations,
)
from SteveCADNativeManufactureFocusedInspectSchema import (
    register_manufacture_focused_inspect_capability_definitions,
)
from SteveCADNativeManufactureJobBindings import (
    register_manufacture_job_capability_implementation,
)
from SteveCADNativeManufactureJobSchema import (
    register_manufacture_job_capability_definition,
)
from SteveCADNativeManufactureAreaBindings import (
    register_manufacture_area_capability_implementation,
)
from SteveCADNativeManufactureAreaSchema import (
    register_manufacture_area_capability_definition,
)
from SteveCADNativeManufactureModifyBindings import (
    register_manufacture_modify_capability_implementation,
)
from SteveCADNativeManufactureModifySchema import (
    register_manufacture_modify_capability_definition,
)
from SteveCADNativeManufactureFocusedModifyBindings import (
    register_manufacture_focused_modify_capability_implementations,
)
from SteveCADNativeManufactureFocusedModifySchema import (
    register_manufacture_focused_modify_capability_definitions,
)
from SteveCADNativeManufactureProgramBindings import (
    register_manufacture_program_capability_implementation,
)
from SteveCADNativeManufactureProgramSchema import (
    register_manufacture_program_capability_definition,
)
from SteveCADNativeManufactureProbeBindings import (
    register_manufacture_probe_capability_implementation,
)
from SteveCADNativeManufactureProbeSchema import (
    register_manufacture_probe_capability_definition,
)
from SteveCADNativeManufacturePropertyBagBindings import (
    register_manufacture_property_bag_capability_implementation,
)
from SteveCADNativeManufacturePropertyBagSchema import (
    register_manufacture_property_bag_capability_definition,
)
from SteveCADNativeManufactureOperationBindings import (
    register_manufacture_operation_capability_implementation,
)
from SteveCADNativeManufactureOperationSchema import (
    register_manufacture_operation_capability_definition,
)
from SteveCADNativeManufactureFocusedOperationBindings import (
    register_manufacture_focused_operation_capability_implementations,
)
from SteveCADNativeManufactureFocusedOperationSchema import (
    register_manufacture_focused_operation_capability_definitions,
)
from SteveCADNativeManufactureCamoticsBindings import (
    register_manufacture_camotics_capability_implementation,
)
from SteveCADNativeManufactureCamoticsSchema import (
    register_manufacture_camotics_capability_definition,
)
from SteveCADNativeManufacturePostBindings import (
    register_manufacture_post_capability_implementation,
)
from SteveCADNativeManufacturePostSchema import (
    register_manufacture_post_capability_definition,
)
from SteveCADNativeManufactureFocusedPostBindings import (
    register_manufacture_focused_post_capability_implementations,
)
from SteveCADNativeManufactureFocusedPostSchema import (
    register_manufacture_focused_post_capability_definitions,
)
from SteveCADNativeManufactureTemplateBindings import (
    register_manufacture_template_capability_implementation,
)
from SteveCADNativeManufactureTemplateSchema import (
    register_manufacture_template_capability_definition,
)
from SteveCADNativeManufactureSimulationBindings import (
    register_manufacture_simulation_capability_implementation,
)
from SteveCADNativeManufactureSimulationSchema import (
    register_manufacture_simulation_capability_definition,
)
from SteveCADNativeManufactureSimulationControlBindings import (
    register_manufacture_simulation_control_capability_implementation,
)
from SteveCADNativeManufactureSimulationControlSchema import (
    register_manufacture_simulation_control_capability_definition,
)
from SteveCADNativeManufactureSimulationResultBindings import (
    register_manufacture_simulation_result_capability_implementation,
)
from SteveCADNativeManufactureSimulationResultSchema import (
    register_manufacture_simulation_result_capability_definition,
)
from SteveCADNativeManufactureFollowUpBindings import (
    register_manufacture_follow_up_capability_implementation,
)
from SteveCADNativeManufactureFollowUpSchema import (
    register_manufacture_follow_up_capability_definition,
)
from SteveCADNativeManufactureToolBindings import (
    register_manufacture_tool_capability_implementations,
)
from SteveCADNativeManufactureFocusedToolBindings import (
    register_manufacture_focused_tool_capability_implementations,
)
from SteveCADNativeManufactureFocusedToolSchema import (
    register_manufacture_focused_tool_capability_definitions,
)
from SteveCADNativeManufactureToolSchema import (
    register_manufacture_tool_capability_definitions,
)
from SteveCADNativeManufactureToolOutputBindings import (
    register_manufacture_tool_output_capability_implementation,
)
from SteveCADNativeManufactureToolOutputSchema import (
    register_manufacture_tool_output_capability_definition,
)
from SteveCADNativeDrawingPageBindings import (
    register_drawing_page_capability_implementation,
)
from SteveCADNativeDrawingPageSchema import (
    register_drawing_page_capability_definition,
)
from SteveCADNativeDrawingActiveViewBindings import (
    register_drawing_active_view_capability_implementation,
)
from SteveCADNativeDrawingActiveViewSchema import (
    register_drawing_active_view_capability_definition,
)
from SteveCADNativeDrawingViewBindings import (
    register_drawing_view_capability_implementation,
)
from SteveCADNativeDrawingViewSchema import (
    register_drawing_view_capability_definition,
)
from SteveCADNativeDrawingSectionBindings import (
    register_drawing_section_capability_implementation,
)
from SteveCADNativeDrawingSectionSchema import (
    register_drawing_section_capability_definition,
)
from SteveCADNativeDrawingComplexSectionBindings import (
    register_drawing_complex_section_capability_implementation,
)
from SteveCADNativeDrawingComplexSectionSchema import (
    register_drawing_complex_section_capability_definition,
)
from SteveCADNativeDrawingDetailBindings import (
    register_drawing_detail_capability_implementation,
)
from SteveCADNativeDrawingDetailSchema import (
    register_drawing_detail_capability_definition,
)
from SteveCADNativeDrawingDraftBindings import (
    register_drawing_draft_capability_implementation,
)
from SteveCADNativeDrawingDraftSchema import (
    register_drawing_draft_capability_definition,
)
from SteveCADNativeDrawingClipBindings import (
    register_drawing_clip_capability_implementation,
)
from SteveCADNativeDrawingClipSchema import (
    register_drawing_clip_capability_definition,
)
from SteveCADNativeDrawingStackBindings import (
    register_drawing_stack_capability_implementation,
)
from SteveCADNativeDrawingStackSchema import (
    register_drawing_stack_capability_definition,
)
from SteveCADNativeDrawingDimensionBindings import (
    register_drawing_dimension_capability_implementation,
)
from SteveCADNativeDrawingDimensionSchema import (
    register_drawing_dimension_capability_definition,
)
from SteveCADNativeDrawingDimensionInferenceBindings import (
    register_drawing_dimension_inference_capability_implementation,
)
from SteveCADNativeDrawingDimensionInferenceSchema import (
    register_drawing_dimension_inference_capability_definition,
)
from SteveCADNativeDrawingDimensionSeriesBindings import (
    register_drawing_dimension_series_capability_implementation,
)
from SteveCADNativeDrawingDimensionSeriesSchema import (
    register_drawing_dimension_series_capability_definition,
)
from SteveCADNativeDrawingDimensionRepairBindings import (
    register_drawing_dimension_repair_capability_implementation,
)
from SteveCADNativeDrawingDimensionRepairSchema import (
    register_drawing_dimension_repair_capability_definition,
)
from SteveCADNativeDrawingLineDefaultsBindings import (
    register_drawing_line_defaults_capability_implementation,
)
from SteveCADNativeDrawingLineDefaultsSchema import (
    register_drawing_line_defaults_capability_definition,
)
from SteveCADNativeDrawingLineAttributesBindings import (
    register_drawing_line_attributes_capability_implementation,
)
from SteveCADNativeDrawingLineAttributesSchema import (
    register_drawing_line_attributes_capability_definition,
)
from SteveCADNativeDrawingLineLengthBindings import (
    register_drawing_line_length_capability_implementation,
)
from SteveCADNativeDrawingLineLengthSchema import (
    register_drawing_line_length_capability_definition,
)
from SteveCADNativeDrawingViewLockBindings import (
    register_drawing_view_lock_capability_implementation,
)
from SteveCADNativeDrawingViewLockSchema import (
    register_drawing_view_lock_capability_definition,
)
from SteveCADNativeDrawingPlacementBindings import (
    register_drawing_placement_capability_implementations,
)
from SteveCADNativeDrawingPlacementSchema import (
    register_drawing_placement_capability_definitions,
)
from SteveCADNativeDrawingSectionPositionBindings import (
    register_drawing_section_position_capability_implementation,
)
from SteveCADNativeDrawingSectionPositionSchema import (
    register_drawing_section_position_capability_definition,
)
from SteveCADNativeDrawingFormatBindings import (
    register_drawing_format_capability_implementation,
)
from SteveCADNativeDrawingFormatSchema import (
    register_drawing_format_capability_definition,
)
from SteveCADNativeDrawingDimensionTextBindings import (
    register_drawing_dimension_text_capability_implementation,
)
from SteveCADNativeDrawingDimensionTextSchema import (
    register_drawing_dimension_text_capability_definition,
)
from SteveCADNativeDrawingPresentationBindings import (
    register_drawing_presentation_capability_implementation,
)
from SteveCADNativeDrawingPresentationSchema import (
    register_drawing_presentation_capability_definition,
)
from SteveCADNativeDrawingHatchBindings import (
    register_drawing_hatch_capability_implementation,
)
from SteveCADNativeDrawingHatchSchema import (
    register_drawing_hatch_capability_definition,
)
from SteveCADNativeDrawingRichAnnotationBindings import (
    register_drawing_rich_annotation_capability_implementation,
)
from SteveCADNativeDrawingRichAnnotationSchema import (
    register_drawing_rich_annotation_capability_definition,
)
from SteveCADNativeDrawingSymbolBindings import (
    register_drawing_symbol_capability_implementation,
)
from SteveCADNativeDrawingSymbolSchema import (
    register_drawing_symbol_capability_definition,
)
from SteveCADNativeDrawingExportBindings import (
    register_drawing_export_capability_implementation,
)
from SteveCADNativeDrawingExportSchema import (
    register_drawing_export_capability_definition,
)
from SteveCADNativeDrawingLeaderBindings import (
    register_drawing_leader_capability_implementation,
)
from SteveCADNativeDrawingLeaderSchema import (
    register_drawing_leader_capability_definition,
)
from SteveCADNativeDrawingCircleCenterLineBindings import (
    register_drawing_circle_center_line_capability_implementation,
)
from SteveCADNativeDrawingCircleCenterLineSchema import (
    register_drawing_circle_center_line_capability_definition,
)
from SteveCADNativeDrawingGeneralCenterLineBindings import (
    register_drawing_general_center_line_capability_implementation,
)
from SteveCADNativeDrawingGeneralCenterLineSchema import (
    register_drawing_general_center_line_capability_definition,
)
from SteveCADNativeDrawingBoltCircleCenterLineBindings import (
    register_drawing_bolt_circle_center_line_capability_implementation,
)
from SteveCADNativeDrawingBoltCircleCenterLineSchema import (
    register_drawing_bolt_circle_center_line_capability_definition,
)
from SteveCADNativeDrawingThreadRepresentationBindings import (
    register_drawing_thread_representation_capability_implementation,
)
from SteveCADNativeDrawingThreadRepresentationSchema import (
    register_drawing_thread_representation_capability_definition,
)
from SteveCADNativeDrawingCosmeticVertexBindings import (
    register_drawing_cosmetic_vertex_capability_implementation,
)
from SteveCADNativeDrawingCosmeticVertexSchema import (
    register_drawing_cosmetic_vertex_capability_definition,
)
from SteveCADNativeDrawingCosmeticCurveBindings import (
    register_drawing_cosmetic_curve_capability_implementation,
)
from SteveCADNativeDrawingCosmeticCurveSchema import (
    register_drawing_cosmetic_curve_capability_definition,
)
from SteveCADNativeDrawingCosmeticLineBindings import (
    register_drawing_cosmetic_line_capability_implementation,
)
from SteveCADNativeDrawingCosmeticLineSchema import (
    register_drawing_cosmetic_line_capability_definition,
)
from SteveCADNativeDrawingBalloonBindings import (
    register_drawing_balloon_capability_implementation,
)
from SteveCADNativeDrawingBalloonSchema import (
    register_drawing_balloon_capability_definition,
)
from SteveCADNativeRobotSetupBindings import (
    register_robot_setup_capability_implementation,
)
from SteveCADNativeRobotSetupSchema import (
    register_robot_setup_capability_definition,
)
from SteveCADNativeRobotMotionBindings import (
    register_robot_motion_capability_implementation,
)
from SteveCADNativeRobotMotionSchema import (
    register_robot_motion_capability_definition,
)
from SteveCADNativeRobotExportBindings import (
    register_robot_export_capability_implementation,
)
from SteveCADNativeRobotExportSchema import (
    register_robot_export_capability_definition,
)
from SteveCADNativeRobotTrajectoryBindings import (
    register_robot_path_feature_capability_implementations,
    register_robot_trajectory_capability_implementation,
)
from SteveCADNativeRobotTrajectorySchema import (
    register_robot_path_feature_capability_definitions,
    register_robot_trajectory_capability_definition,
)
from SteveCADNativeSketchProviderBindings import (
    register_sketch_provider_capability_implementations,
)
from SteveCADNativeSketchProviderSchema import (
    register_sketch_provider_capability_definitions,
)


def build_native_capability_registry() -> NativeCapabilityRegistry:
    """Build a fresh fail-closed registry without document or GUI state."""

    registry = NativeCapabilityRegistry()
    register_analyze_model_capability_definition(registry)
    register_analyze_model_capability_implementation(registry)
    register_analyze_solid_domain_capability_definition(registry)
    register_analyze_solid_domain_capability_implementation(registry)
    register_analyze_inspect_capability_definition(registry)
    register_analyze_inspect_capability_implementation(registry)
    register_analyze_face_capability_definition(registry)
    register_analyze_face_capability_implementation(registry)
    register_analyze_flow_result_capability_definition(registry)
    register_analyze_flow_result_capability_implementation(registry)
    register_analyze_mechanical_result_capability_definitions(registry)
    register_analyze_mechanical_result_capability_implementations(registry)
    register_analyze_thermal_result_capability_definitions(registry)
    register_analyze_thermal_result_capability_implementations(registry)
    register_analyze_assignment_view_capability_definition(registry)
    register_analyze_assignment_view_capability_implementation(registry)
    register_analyze_geometry_capability_definition(registry)
    register_analyze_geometry_capability_implementation(registry)
    register_analyze_electromagnetic_capability_definition(registry)
    register_analyze_electromagnetic_capability_implementation(registry)
    register_analyze_fluid_capability_definition(registry)
    register_analyze_fluid_capability_implementation(registry)
    register_analyze_fluid_create_capability_definitions(registry)
    register_analyze_fluid_create_capability_implementations(registry)
    register_analyze_cfd_lifecycle_capability_definitions(registry)
    register_analyze_cfd_lifecycle_capability_implementations(registry)
    register_analyze_geometrical_capability_definition(registry)
    register_analyze_geometrical_capability_implementation(registry)
    register_analyze_support_capability_definition(registry)
    register_analyze_support_capability_implementation(registry)
    register_analyze_structural_lifecycle_capability_definitions(registry)
    register_analyze_structural_lifecycle_capability_implementations(registry)
    register_analyze_connection_capability_definition(registry)
    register_analyze_connection_capability_implementation(registry)
    register_analyze_load_capability_definition(registry)
    register_analyze_load_capability_implementation(registry)
    register_analyze_thermal_capability_definition(registry)
    register_analyze_thermal_capability_implementation(registry)
    register_analyze_mesh_capability_definition(registry)
    register_analyze_mesh_capability_implementation(registry)
    register_analyze_mesh_lifecycle_capability_definitions(registry)
    register_analyze_mesh_lifecycle_capability_implementations(registry)
    register_analyze_local_mesh_capability_definitions(registry)
    register_analyze_local_mesh_capability_implementations(registry)
    register_analyze_mesh_field_capability_definition(registry)
    register_analyze_mesh_field_capability_implementation(registry)
    register_analyze_mesh_output_capability_definition(registry)
    register_analyze_mesh_output_capability_implementation(registry)
    register_analyze_mesh_refinement_capability_definition(registry)
    register_analyze_mesh_refinement_capability_implementation(registry)
    register_analyze_structured_mesh_capability_definition(registry)
    register_analyze_structured_mesh_capability_implementation(registry)
    register_analyze_solver_capability_definition(registry)
    register_analyze_solver_capability_implementation(registry)
    register_analyze_solver_control_capability_definition(registry)
    register_analyze_solver_control_capability_implementation(registry)
    register_analyze_solver_execution_capability_definition(registry)
    register_analyze_solver_execution_capability_implementation(registry)
    register_analyze_run_solver_capability_definition(registry)
    register_analyze_run_solver_capability_implementation(registry)
    register_analyze_equation_capability_definition(registry)
    register_analyze_equation_capability_implementation(registry)
    register_analyze_results_capability_definition(registry)
    register_analyze_results_capability_implementation(registry)
    register_analyze_presentation_capability_definition(registry)
    register_analyze_presentation_capability_implementation(registry)
    register_analyze_post_capability_definition(registry)
    register_analyze_post_capability_implementation(registry)
    register_analyze_post_function_capability_definition(registry)
    register_analyze_post_function_capability_implementation(registry)
    register_analyze_visualization_capability_definition(registry)
    register_analyze_visualization_capability_implementation(registry)
    register_native_background_capability_definition(registry)
    register_native_background_capability_implementation(registry)
    register_aero_solve_capability_definition(registry)
    register_aero_solve_capability_implementation(registry)
    register_mesh_convert_capability_definition(registry)
    register_mesh_convert_capability_implementation(registry)
    register_mesh_io_capability_definition(registry)
    register_mesh_io_capability_implementation(registry)
    register_mesh_export_capability_definition(registry)
    register_mesh_export_capability_implementation(registry)
    register_mesh_modify_capability_definition(registry)
    register_mesh_modify_capability_implementation(registry)
    register_mesh_boolean_capability_definition(registry)
    register_mesh_boolean_capability_implementation(registry)
    register_mesh_cut_capability_definition(registry)
    register_mesh_cut_capability_implementation(registry)
    register_mesh_inspect_capability_definition(registry)
    register_mesh_inspect_capability_implementation(registry)
    register_mesh_curvature_capability_definition(registry)
    register_mesh_curvature_capability_implementation(registry)
    register_mesh_segment_capability_definition(registry)
    register_mesh_segment_capability_implementation(registry)
    register_mesh_points_capability_definition(registry)
    register_mesh_points_capability_implementation(registry)
    register_mesh_rebuild_capability_definition(registry)
    register_mesh_approximate_capability_definition(registry)
    register_mesh_reconstruct_parametric_capability_definition(registry)
    register_reverse_capability_implementations(registry)
    register_mesh_reconstruct_parametric_capability_implementation(registry)
    register_common_capability_definitions(registry)
    register_common_capability_implementations(registry)
    register_inspection_compare_capability_definition(registry)
    register_inspection_compare_capability_implementation(registry)
    register_workspace_capability_definition(registry)
    register_workspace_capability_implementation(registry)
    register_parameters_capability_definitions(registry)
    register_parameters_capability_implementations(registry)
    register_assembly_diagnosis_capability_definition(registry)
    register_assembly_diagnosis_capability_implementation(registry)
    register_assembly_bom_capability_definition(registry)
    register_assembly_bom_capability_implementation(registry)
    register_assembly_fastener_capability_definition(registry)
    register_assembly_fastener_capability_implementation(registry)
    register_assembly_export_capability_definition(registry)
    register_assembly_export_capability_implementation(registry)
    register_assembly_connectors_capability_definition(registry)
    register_assembly_connectors_capability_implementation(registry)
    register_assembly_inspect_capability_definition(registry)
    register_assembly_inspect_capability_implementation(registry)
    register_assembly_joint_capability_definition(registry)
    register_assembly_joint_capability_implementation(registry)
    register_assembly_playback_capability_definition(registry)
    register_assembly_playback_capability_implementation(registry)
    register_assembly_structure_capability_definition(registry)
    register_assembly_structure_capability_implementation(registry)
    register_component_interface_capability_definition(registry)
    register_component_interface_capability_implementation(registry)
    register_component_interfaces_capability_definition(registry)
    register_component_interfaces_capability_implementation(registry)
    register_model_catalog_capability_definition(registry)
    register_model_catalog_capability_implementation(registry)
    register_model_structure_capability_definitions(registry)
    register_model_structure_capability_implementations(registry)
    register_model_history_capability_definitions(registry)
    register_model_history_capability_implementations(registry)
    register_sheetmetal_inspect(registry)
    register_sheetmetal_view(registry)
    register_sheetmetal_edit(registry)
    register_sheetmetal_create(registry)
    register_sheetmetal_connection(registry)
    register_sheetmetal_manufacturing(registry)
    register_sketch_setup_capability_definition(registry)
    register_sketch_setup_capability_implementation(registry)
    register_model_boolean_capability_definition(registry)
    register_model_boolean_capability_implementation(registry)
    register_model_feature_capability_definition(registry)
    register_model_feature_capability_implementation(registry)
    register_model_fastener_capability_definition(registry)
    register_model_fastener_capability_implementation(registry)
    register_model_dressup_capability_definition(registry)
    register_model_dressup_capability_implementation(registry)
    register_model_hole_capability_definitions(registry)
    register_model_hole_capability_implementations(registry)
    register_model_join_capability_definition(registry)
    register_model_join_capability_implementation(registry)
    register_model_part_capability_definition(registry)
    register_model_part_capability_implementation(registry)
    register_model_surface_capability_definition(registry)
    register_model_surface_capability_implementation(registry)
    register_model_transform_capability_definition(registry)
    register_model_transform_capability_implementation(registry)
    register_manufacture_inspect_capability_definition(registry)
    register_manufacture_inspect_capability_implementation(registry)
    register_manufacture_focused_inspect_capability_definitions(registry)
    register_manufacture_focused_inspect_capability_implementations(registry)
    register_manufacture_job_capability_definition(registry)
    register_manufacture_job_capability_implementation(registry)
    register_manufacture_area_capability_definition(registry)
    register_manufacture_area_capability_implementation(registry)
    register_manufacture_modify_capability_definition(registry)
    register_manufacture_modify_capability_implementation(registry)
    register_manufacture_focused_modify_capability_definitions(registry)
    register_manufacture_focused_modify_capability_implementations(registry)
    register_manufacture_program_capability_definition(registry)
    register_manufacture_program_capability_implementation(registry)
    register_manufacture_probe_capability_definition(registry)
    register_manufacture_probe_capability_implementation(registry)
    register_manufacture_property_bag_capability_definition(registry)
    register_manufacture_property_bag_capability_implementation(registry)
    register_manufacture_operation_capability_definition(registry)
    register_manufacture_operation_capability_implementation(registry)
    register_manufacture_focused_operation_capability_definitions(registry)
    register_manufacture_focused_operation_capability_implementations(registry)
    register_manufacture_camotics_capability_definition(registry)
    register_manufacture_camotics_capability_implementation(registry)
    register_manufacture_post_capability_definition(registry)
    register_manufacture_post_capability_implementation(registry)
    register_manufacture_focused_post_capability_definitions(registry)
    register_manufacture_focused_post_capability_implementations(registry)
    register_manufacture_template_capability_definition(registry)
    register_manufacture_template_capability_implementation(registry)
    register_manufacture_simulation_capability_definition(registry)
    register_manufacture_simulation_capability_implementation(registry)
    register_manufacture_simulation_control_capability_definition(registry)
    register_manufacture_simulation_control_capability_implementation(registry)
    register_manufacture_simulation_result_capability_definition(registry)
    register_manufacture_simulation_result_capability_implementation(registry)
    register_manufacture_follow_up_capability_definition(registry)
    register_manufacture_follow_up_capability_implementation(registry)
    register_manufacture_tool_capability_definitions(registry)
    register_manufacture_tool_capability_implementations(registry)
    register_manufacture_focused_tool_capability_definitions(registry)
    register_manufacture_focused_tool_capability_implementations(registry)
    register_manufacture_tool_output_capability_definition(registry)
    register_manufacture_tool_output_capability_implementation(registry)
    register_drawing_page_capability_definition(registry)
    register_drawing_page_capability_implementation(registry)
    register_drawing_active_view_capability_definition(registry)
    register_drawing_active_view_capability_implementation(registry)
    register_drawing_view_capability_definition(registry)
    register_drawing_view_capability_implementation(registry)
    register_drawing_section_capability_definition(registry)
    register_drawing_section_capability_implementation(registry)
    register_drawing_complex_section_capability_definition(registry)
    register_drawing_complex_section_capability_implementation(registry)
    register_drawing_detail_capability_definition(registry)
    register_drawing_detail_capability_implementation(registry)
    register_drawing_draft_capability_definition(registry)
    register_drawing_draft_capability_implementation(registry)
    register_drawing_clip_capability_definition(registry)
    register_drawing_clip_capability_implementation(registry)
    register_drawing_stack_capability_definition(registry)
    register_drawing_stack_capability_implementation(registry)
    register_drawing_dimension_capability_definition(registry)
    register_drawing_dimension_capability_implementation(registry)
    register_drawing_dimension_inference_capability_definition(registry)
    register_drawing_dimension_inference_capability_implementation(registry)
    register_drawing_dimension_series_capability_definition(registry)
    register_drawing_dimension_series_capability_implementation(registry)
    register_drawing_dimension_repair_capability_definition(registry)
    register_drawing_dimension_repair_capability_implementation(registry)
    register_drawing_line_defaults_capability_definition(registry)
    register_drawing_line_defaults_capability_implementation(registry)
    register_drawing_line_attributes_capability_definition(registry)
    register_drawing_line_attributes_capability_implementation(registry)
    register_drawing_line_length_capability_definition(registry)
    register_drawing_line_length_capability_implementation(registry)
    register_drawing_view_lock_capability_definition(registry)
    register_drawing_view_lock_capability_implementation(registry)
    register_drawing_placement_capability_definitions(registry)
    register_drawing_placement_capability_implementations(registry)
    register_drawing_section_position_capability_definition(registry)
    register_drawing_section_position_capability_implementation(registry)
    register_drawing_format_capability_definition(registry)
    register_drawing_format_capability_implementation(registry)
    register_drawing_dimension_text_capability_definition(registry)
    register_drawing_dimension_text_capability_implementation(registry)
    register_drawing_presentation_capability_definition(registry)
    register_drawing_presentation_capability_implementation(registry)
    register_drawing_hatch_capability_definition(registry)
    register_drawing_hatch_capability_implementation(registry)
    register_drawing_rich_annotation_capability_definition(registry)
    register_drawing_rich_annotation_capability_implementation(registry)
    register_drawing_symbol_capability_definition(registry)
    register_drawing_symbol_capability_implementation(registry)
    register_drawing_export_capability_definition(registry)
    register_drawing_export_capability_implementation(registry)
    register_drawing_leader_capability_definition(registry)
    register_drawing_leader_capability_implementation(registry)
    register_drawing_circle_center_line_capability_definition(registry)
    register_drawing_circle_center_line_capability_implementation(registry)
    register_drawing_general_center_line_capability_definition(registry)
    register_drawing_general_center_line_capability_implementation(registry)
    register_drawing_bolt_circle_center_line_capability_definition(registry)
    register_drawing_bolt_circle_center_line_capability_implementation(registry)
    register_drawing_thread_representation_capability_definition(registry)
    register_drawing_thread_representation_capability_implementation(registry)
    register_drawing_cosmetic_vertex_capability_definition(registry)
    register_drawing_cosmetic_vertex_capability_implementation(registry)
    register_drawing_cosmetic_curve_capability_definition(registry)
    register_drawing_cosmetic_curve_capability_implementation(registry)
    register_drawing_cosmetic_line_capability_definition(registry)
    register_drawing_cosmetic_line_capability_implementation(registry)
    register_drawing_balloon_capability_definition(registry)
    register_drawing_balloon_capability_implementation(registry)
    register_robot_setup_capability_definition(registry)
    register_robot_setup_capability_implementation(registry)
    register_robot_motion_capability_definition(registry)
    register_robot_motion_capability_implementation(registry)
    register_robot_export_capability_definition(registry)
    register_robot_export_capability_implementation(registry)
    register_robot_trajectory_capability_definition(registry)
    register_robot_trajectory_capability_implementation(registry)
    register_robot_path_feature_capability_definitions(registry)
    register_robot_path_feature_capability_implementations(registry)
    register_sketch_provider_capability_definitions(registry)
    register_sketch_provider_capability_implementations(registry)
    return registry
