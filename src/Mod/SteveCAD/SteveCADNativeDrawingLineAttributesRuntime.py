# SPDX-License-Identifier: LGPL-2.1-or-later

"""Document-bound runtime for persistent Drawing line attributes."""

from __future__ import annotations

from functools import partial
from typing import Any, Mapping

from SteveCADNativeArguments import strict_variant_arguments
from SteveCADNativeDrawingLineAttributes import (
    mutate_drawing_line_attributes,
    prepare_drawing_line_attribute_change,
    read_drawing_line_attributes,
    verify_drawing_line_attributes,
)
from SteveCADNativeImmediate import run_immediate_mutation
from SteveCADNativeRuntimeContext import NativeRuntimeContext
from SteveCADNativeState import NativeCallTicket


_COMMON_FIELDS = frozenset(
    {"page", "view", "expected_inventory_state_sha256"}
)
_FIELDS = {
    "set": _COMMON_FIELDS | frozenset({"targets", "attributes"}),
    "read_view": _COMMON_FIELDS | frozenset({"offset", "page_size"}),
}


class NativeDrawingLineAttributesRuntime:
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
        context = self._context
        context.guard()
        if operation == "read_view":
            return read_drawing_line_attributes(context.document, values=values)
        prepared = prepare_drawing_line_attribute_change(
            context.document,
            values=values,
        )
        return run_immediate_mutation(
            context,
            ticket=ticket,
            transaction_name="Change Native Drawing Line Attributes",
            mutate=partial(mutate_drawing_line_attributes, prepared=prepared),
            verify=verify_drawing_line_attributes,
        )
