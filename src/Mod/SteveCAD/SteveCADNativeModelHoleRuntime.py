# SPDX-License-Identifier: LGPL-2.1-or-later

"""Document-bound runtime for Design Hole and its live catalog."""

from __future__ import annotations

from typing import Any, Mapping

from SteveCADNativeArguments import strict_variant_arguments
from SteveCADNativeDesignHole import (
    create_design_hole,
    preflight_design_hole,
    prepare_design_hole,
)
from SteveCADNativeDesignResults import verify_design_operation
from SteveCADNativeImmediate import run_immediate_mutation
from SteveCADNativeModelErrors import NativeModelError
from SteveCADNativeRuntimeContext import NativeRuntimeContext
from SteveCADNativeState import NativeCallTicket


_HOLE_FIELDS = frozenset(
    {
        "label",
        "profile",
        "base_profile",
        "hole_type",
        "head",
        "depth",
        "drill_point",
        "taper",
        "reversed",
        "targets",
    }
)


class NativeModelHoleRuntime:
    def __init__(self, context: NativeRuntimeContext) -> None:
        if not isinstance(context, NativeRuntimeContext):
            raise TypeError("context must be a NativeRuntimeContext")
        self._context = context

    def mutate_hole(
        self,
        arguments: Mapping[str, Any],
        *,
        ticket: NativeCallTicket,
    ) -> dict[str, Any]:
        _operation, values = strict_variant_arguments(
            arguments,
            {"hole": _HOLE_FIELDS},
        )
        label = str(values["label"] or "").strip()
        if not label or len(label) > 160:
            raise NativeModelError("A visible Hole label must contain 1 to 160 characters.")
        prepared = prepare_design_hole(
            self._context.document_uid,
            values,
        )
        self._context.guard()
        preflight_design_hole(self._context.document, prepared)

        return run_immediate_mutation(
            self._context,
            ticket=ticket,
            transaction_name="Create Native Design Hole",
            mutate=lambda document: create_design_hole(
                document,
                label=label,
                spec=prepared,
            ),
            verify=verify_design_operation,
        )
