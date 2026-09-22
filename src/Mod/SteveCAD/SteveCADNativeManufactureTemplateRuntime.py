# SPDX-License-Identifier: LGPL-2.1-or-later

"""Document-bound runtime for exact CAM Job template output."""

from __future__ import annotations

from typing import Any, Mapping

from SteveCADNativeArguments import strict_variant_arguments
from SteveCADNativeManufactureErrors import NativeManufactureError
from SteveCADNativeManufactureTemplate import (
    export_template,
    preflight_template_output,
    require_current_template_ticket,
)
from SteveCADNativeOutput import NativeOutputError
from SteveCADNativeRuntimeContext import NativeRuntimeContext
from SteveCADNativeState import NativeCallTicket


_FIELDS = frozenset(
    {
        "job",
        "description",
        "include_postprocessing",
        "tool_controllers",
        "stock",
        "setup_sheet",
    }
)


class NativeManufactureTemplateRuntime:
    def __init__(self, context: NativeRuntimeContext) -> None:
        if not isinstance(context, NativeRuntimeContext):
            raise TypeError("context must be a NativeRuntimeContext")
        self._context = context

    def export(
        self,
        arguments: Mapping[str, Any],
        ticket: NativeCallTicket,
    ) -> dict[str, Any]:
        operation, values = strict_variant_arguments(
            arguments,
            {"export_template": _FIELDS},
        )
        if operation != "export_template":
            raise TypeError("CAM template output requires export_template")
        context = self._context
        require_current_template_ticket(context, ticket)
        prepared = preflight_template_output(
            context,
            job_target=values["job"],
            values=values,
        )
        authorizer = context.authorize_output
        if authorizer is None:
            raise NativeManufactureError(
                "Human output authorization is unavailable in this SteveCAD session.",
                error_code="NATIVE_MANUFACTURE_TEMPLATE_UNAVAILABLE",
            )
        try:
            authorization = authorizer(prepared.output_request)
        except NativeOutputError as exc:
            raise NativeManufactureError(str(exc), error_code=exc.code) from exc
        if authorization is None:
            raise NativeManufactureError(
                "The human cancelled CAM Job template output authorization.",
                error_code="NATIVE_MANUFACTURE_TEMPLATE_OUTPUT_CANCELLED",
            )
        require_current_template_ticket(context, ticket)
        return export_template(context, prepared, authorization, ticket)
