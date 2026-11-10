"""Pinned Direct Mode compatibility fixes for Windows hosts.

genlayer-test 0.29.2 replaces fd 0 with a temporary file while loading the
GenLayer SDK.  Windows cannot unlink that file until the duplicated stdin
handle is restored, whereas the upstream helper unlinks it immediately.  The
shim below preserves the upstream behavior and only defers cleanup on Windows;
Linux/macOS use the unmodified native helper.
"""

import os
import tempfile


def pytest_configure(config):
    if os.name != "nt":
        return

    from gltest.direct import loader
    from gltest.direct.vm import VMContext

    if getattr(loader, "_goodhart_windows_patch", False):
        return

    original_cleanup = VMContext._cleanup_after_deactivate

    def cleanup_after_deactivate(self):
        original_cleanup(self)
        for path in getattr(self, "_goodhart_stdin_paths", []):
            try:
                os.unlink(path)
            except FileNotFoundError:
                pass
            except PermissionError:
                # Do not hide VM cleanup errors; a later process exit can
                # reclaim a file that Windows still has open.
                pass
        self._goodhart_stdin_paths = []

    def inject_message_to_fd0(vm):
        from genlayer.py import calldata
        from genlayer.py.types import Address

        def address(value):
            return Address(value) if isinstance(value, bytes) else value

        encoded = calldata.encode({
            "contract_address": address(vm._contract_address),
            "sender_address": address(vm.sender),
            "origin_address": address(vm.origin),
            "stack": [],
            "value": vm._value,
            "datetime": vm._datetime,
            "is_init": False,
            "chain_id": vm._chain_id,
            "entry_kind": 0,
            "entry_data": b"",
            "entry_stage_data": None,
        })
        fd, path = tempfile.mkstemp()
        try:
            os.write(fd, encoded)
            os.lseek(fd, 0, os.SEEK_SET)
            original_stdin = os.dup(0)
            vm._original_stdin_fd = original_stdin
            os.dup2(fd, 0)
            paths = getattr(vm, "_goodhart_stdin_paths", [])
            paths.append(path)
            vm._goodhart_stdin_paths = paths
        finally:
            os.close(fd)
        # The duplicated fd 0 owns the file until VMContext cleanup restores
        # the original stdin.  Deletion is intentionally deferred.

    loader._inject_message_to_fd0 = inject_message_to_fd0
    VMContext._cleanup_after_deactivate = cleanup_after_deactivate
    loader._goodhart_windows_patch = True

