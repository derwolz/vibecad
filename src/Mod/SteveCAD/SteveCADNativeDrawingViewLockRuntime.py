# SPDX-License-Identifier: LGPL-2.1-or-later

"""Document-bound runtime for exact Drawing view position locks."""

from __future__ import annotations

from functools import partial
from typing import Any, Mapping

from SteveCADNativeArguments import strict_variant_arguments
from SteveCADNativeDrawingViewLock import (
    mutate_drawing_view_locks,
    prepare_drawing_view_lock_change,
    read_drawing_view_locks,
    verify_drawing_view_locks,
)
from SteveCADNativeImmediate import run_immediate_mutation
from SteveCADNativeRuntimeContext import NativeRuntimeContext
from SteveCADNativeState import NativeCallTicket


_FIELDS = {
    "read": {"read": frozenset({"page", "offset"})},
    "set": {
        "set": frozenset({"page", "expected_inventory_state_sha256", "views"})
    },
}


class NativeDrawingViewLockRuntime:
    def __init__(self, context: NativeRuntimeContext) -> None:
        if not isinstance(context, NativeRuntimeContext):
            raise TypeError("context must be a NativeRuntimeContext")
        self._context = context

    def execute(
        self,
        arguments: Mapping[str, Any],
        *,
        ticket: NativeCallTicket,
        mode: str,
    ) -> dict[str, Any]:
        if mode not in _FIELDS:
            raise ValueError("mode is not supported")
        normalized = dict(arguments)
        if mode == "read":
            normalized.setdefault("offset", 0)
        _operation, values = strict_variant_arguments(normalized, _FIELDS[mode])
        context = self._context
        context.guard()
        if mode == "read":
            return read_drawing_view_locks(context.document, values=values)
        prepared = prepare_drawing_view_lock_change(
            context.document,
            values=values,
        )
        return run_immediate_mutation(
            context,
            ticket=ticket,
            transaction_name="Set Native Drawing View Locks",
            mutate=partial(mutate_drawing_view_locks, prepared=prepared),
            verify=verify_drawing_view_locks,
        )
