# v0.2.18
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""Minimal consumer of Goodhart; exact-program and action-bound one-shot gate.

No funds or private data are held. This demonstrates executable composition.
"""
from genlayer import *

from dataclasses import dataclass


@gl.contract_interface
class IGoodhart:
    class View:
        def is_rewardable(self, program_id: str, fingerprint: str) -> bool: ...
        def get_program(self, program_id: str) -> dict: ...

    class Write:
        pass


@allow_storage
@dataclass
class GateExecution:
    beneficiary: Address
    program_id: str
    fingerprint: str
    action_hash: str


class RewardGate(gl.Contract):
    registry: Address
    program_id: str
    fingerprint: str
    beneficiary: Address
    expected_action_hash: str
    executions: TreeMap[str, GateExecution]

    def __init__(self, registry: Address, program_id: str, fingerprint: str,
                 beneficiary: Address, expected_action_hash: str):
        if (not 3 <= len(program_id) <= 64 or not _hex64(fingerprint)
                or not _hex64(expected_action_hash)):
            raise gl.vm.UserError("EXPECTED: invalid binding")
        self.registry = registry
        self.program_id = program_id
        self.fingerprint = fingerprint
        self.beneficiary = beneficiary
        self.expected_action_hash = expected_action_hash

    @gl.public.write
    def execute_once(self, action_hash: str) -> None:
        if gl.message.sender_address != self.beneficiary:
            raise gl.vm.UserError("EXPECTED: only beneficiary")
        if action_hash != self.expected_action_hash:
            raise gl.vm.UserError("EXPECTED: action substitution")
        if action_hash in self.executions:
            raise gl.vm.UserError("EXPECTED: replay")
        goodhart = IGoodhart(self.registry)
        if not goodhart.view().is_rewardable(self.program_id, self.fingerprint):
            raise gl.vm.UserError("EXPECTED: underlying objective not certified")
        self.executions[action_hash] = GateExecution(
            self.beneficiary, self.program_id, self.fingerprint, action_hash)

    @gl.public.view
    def was_executed(self, action_hash: str) -> bool:
        return action_hash in self.executions


def _hex64(value: str) -> bool:
    return (isinstance(value, str) and len(value) == 64
            and all(c in "0123456789abcdef" for c in value))
