"""Small focused mutation checks for Goodhart's deterministic pure rules.

Each mutant is loaded in memory and exercised by the corresponding regression
assertion. A mutation check passes only when the weakened variant is killed;
this does not modify the working tree or invoke a live network.
"""

import ast
import json
import pathlib
import typing

from Crypto.Hash import keccak


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "contracts" / "goodhart.py"
NAMES = {
    "_clean_page", "_json_dict", "_proxy_json", "_improved", "_decision",
    "_classify", "_sha", "_escape", "_prompt", "_audit_prompt",
    "_acceptance_reason",
}
GATE_SOURCE = ROOT / "contracts" / "reward_gate.py"


def load_context(source: str) -> dict:
    tree = ast.parse(source)
    subset = ast.Module(
        body=[node for node in tree.body
              if isinstance(node, ast.FunctionDef) and node.name in NAMES],
        type_ignores=[],
    )
    context = {
        "typing": typing,
        "json": json,
        "Keccak256": lambda value: keccak.new(digest_bits=256, data=value),
        "IMPROVED": "IMPROVED",
        "STABLE": "STABLE",
        "DEGRADED": "DEGRADED",
        "MIXED": "MIXED",
        "UNKNOWN": "UNKNOWN",
        "OUTCOMES": ("IMPROVED", "STABLE", "DEGRADED", "MIXED", "UNKNOWN"),
        "INCONCLUSIVE": "INCONCLUSIVE",
        "REWARDABLE": "REWARDABLE",
        "DIVERGENT": "DIVERGENT",
        "UNSUPPORTED": "UNSUPPORTED",
        "PROXY_NOT_IMPROVED": "PROXY_NOT_IMPROVED",
        "MAX_PAGE": 12000,
        "MAX_PAGE_BYTES": 48000,
        "MAX_QUOTE": 200,
        "MAX_REASON": 48,
    }
    exec(compile(subset, str(SOURCE), "exec"), context)
    return context


def must_fail(label: str, mutant: str, assertion) -> None:
    try:
        assertion(load_context(mutant))
    except AssertionError:
        print(f"killed: {label}")
        return
    raise SystemExit(f"mutation escaped: {label}")


def require(condition: bool) -> None:
    if not condition:
        raise AssertionError("regression did not hold")


def load_gate_context(source: str) -> dict:
    tree = ast.parse(source)
    subset = ast.Module(
        body=[node for node in tree.body
              if isinstance(node, ast.FunctionDef)
              and node.name == "_program_binding_matches"],
        type_ignores=[],
    )
    context = {}
    exec(compile(subset, str(GATE_SOURCE), "exec"), context)
    return context


def must_fail_gate(label: str, mutant: str, assertion) -> None:
    try:
        assertion(load_gate_context(mutant))
    except AssertionError:
        print(f"killed: {label}")
        return
    raise SystemExit(f"mutation escaped: {label}")


original = SOURCE.read_text()

must_fail(
    "threshold strictness",
    original.replace("change * 10000 >= before * min_delta_bps",
                     "change * 10000 > before * min_delta_bps", 1),
    lambda ctx: require(ctx["_improved"](100, 110, "UP", 1000)),
)

must_fail(
    "distant evidence truncation",
    original.replace(
        'if not isinstance(raw, str) or len(raw) > MAX_PAGE:\n        return ""',
        'if not isinstance(raw, str):\n        return ""', 1,
    ).replace(
        'page = " ".join(raw.split())',
        'page = " ".join(raw.split())[:MAX_PAGE]', 1,
    ),
    lambda ctx: require(ctx["_clean_page"]("witness " + "x" * 12000) == ""),
)

must_fail(
    "unknown status fail closed",
    original.replace("if a == UNKNOWN or b == UNKNOWN:", "if False:", 1),
    lambda ctx: require(ctx["_decision"](True, "UNKNOWN", "IMPROVED") == "INCONCLUSIVE"),
)

must_fail(
    "strict model schema",
    original.replace(
        'if set(data) != {"verdict", "quote", "reason"}:',
        "if False:", 1,
    ),
    lambda ctx: require(ctx["_classify"]({
        "verdict": "IMPROVED",
        "quote": "objective improved materially",
        "reason": "POSITIVE",
        "extra": "forged",
    }, "objective improved materially")["verdict"] == "UNKNOWN"),
)

must_fail(
    "beneficiary acceptance authentication",
    original.replace(
        "if sender != beneficiary:", "if sender == beneficiary:", 1,
    ),
    lambda ctx: require(
        ctx["_acceptance_reason"](
            "owner", "beneficiary", 0, "f" * 64, "f" * 64, 100, 200,
        ) == "only beneficiary may accept"
    ),
)

gate_original = GATE_SOURCE.read_text()
must_fail_gate(
    "reward gate primary beneficiary binding",
    gate_original.replace(
        'program.get("beneficiary") == beneficiary',
        'program.get("beneficiary") == program_id', 1,
    ),
    lambda ctx: require(ctx["_program_binding_matches"](
        {"id": "p", "fingerprint": "a" * 64, "beneficiary": "0xworker"},
        "p", "a" * 64, "0xworker",
    )),
)

print("GOODHART: mutation checks PASS (6 weakened variants killed)")

