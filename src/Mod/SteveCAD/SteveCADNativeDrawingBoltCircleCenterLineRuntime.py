# SPDX-License-Identifier: LGPL-2.1-or-later

"""Document-bound runtime for exact Drawing bolt-circle centerlines."""

from __future__ import annotations

from functools import partial
from typing import Any, Mapping

from SteveCADNativeArguments import strict_variant_arguments
from SteveCADNativeDrawingBoltCircleCenterLine import (
    mutate_drawing_bolt_circle_center_lines,
    prepare_drawing_bolt_circle_center_lines,
    verify_drawing_bolt_circle_center_lines,
)
from SteveCADNativeImmediate import run_immediate_mutation
from SteveCADNativeRuntimeContext import NativeRuntimeContext
from SteveCADNativeState import NativeCallTicket


_FIELDS = {"create": frozenset({"page", "view", "holes"})}


class NativeDrawingBoltCircleCenterLineRuntime:
    def __init__(self, context: NativeRuntimeContext) -> None:
        if not isinstance(context, NativeRuntimeContext):
            raise TypeError("context must be a NativeRuntimeContext")
        self._context = context

    def execute(
        self,
        arguments: Mapping[str, Any],
        *,
        ticket: NativeCallTicket,
    ) -> dict[str, Any]:
        operation, values = strict_variant_arguments(arguments, _FIELDS)
        if operation != "create":
            raise ValueError("operation is not a bolt-circle centerline operation")
        context = self._context
        context.guard()
        prepared = prepare_drawing_bolt_circle_center_lines(
            context.document, values=values
        )
        return run_immediate_mutation(
            context,
            ticket=ticket,
            transaction_name="Create Native Drawing Bolt Circle Centerlines",
            mutate=partial(
                mutate_drawing_bolt_circle_center_lines, prepared=prepared
            ),
            verify=verify_drawing_bolt_circle_center_lines,
        )
