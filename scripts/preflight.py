"""Offline fail-fast environment and architecture checks; no network calls."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "contracts" / "goodhart.py").read_text()
gate = (ROOT / "contracts" / "reward_gate.py").read_text()
pkg = json.loads((ROOT / "package.json").read_text())
assert pkg["devDependencies"]["genlayer"] == "0.39.1"
assert "0.40.0rc2" not in source + gate
for path in ["contracts/goodhart.py", "contracts/reward_gate.py"]:
    text = (ROOT / path).read_text()
    assert 'py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6' in text
assert "gl.vm.run_nondet_unsafe(leader, validator)" in source
assert "gl.nondet.web.get" in source
assert "gl.nondet.exec_prompt" in source
assert "def _improved(" in source and "def _decision(" in source
assert "is_rewardable" in source and "is_rewardable" in gate
assert "61997" not in (ROOT / "package.json").read_text()
assert "studionet-dev" not in (ROOT / "package.json").read_text()
assert not list(ROOT.rglob(".env"))
assert len(re.findall(r"@gl.public.write", source)) == 3
print("GOODHART: offline architecture/network pin preflight PASS (12 assertions)")
