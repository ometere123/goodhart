"""GenVM Direct Mode integration, including native validator re-observation."""
import json

PROXY = "https://metrics.example.org/program.json"
OUT_A = "https://outcomes.example.net/primary"
OUT_B = "https://feedback.example.com/corroboration"
BASE = "2026-11-09T10:00:00+00:00"
AFTER = "2026-11-09T10:02:00+00:00"
OBJECTIVE = ("Decrease actual unresolved customer issues and repeat contacts, "
             "not merely the number of tickets marked closed in the CRM.")
INDICATOR = ("Look for material improvement in genuinely resolved cases and "
             "fewer reopened or still-unresolved issues during the observed period.")
A_PAGE = ("Independent support outcome report: reopened customer issues fell from "
          "30 percent to 11 percent and median unresolved days fell from seven to four.")
B_PAGE = ("External customer feedback: the share of customers whose issue remained "
          "unresolved dropped from 29 percent to 10 percent across the reporting period.")
A_QUOTE = "reopened customer issues fell from 30 percent to 11 percent"
B_QUOTE = "share of customers whose issue remained unresolved dropped from 29 percent to 10 percent"


def deploy(vm, deployer, beneficiary):
    vm.warp(BASE)
    goodhart = deployer("contracts/goodhart.py", sdk_version="v0.2.12")
    # The fixture is raw bytes; obtain the runtime Address after SDK loading.
    from gltest.direct import create_address
    beneficiary = create_address("alice")
    fingerprint = goodhart.register_program(
        "support42", beneficiary, "Support outcomes",
        OBJECTIVE, INDICATOR, "Tickets closed", "tickets", "UP", 20, 3000,
        PROXY, OUT_A, OUT_B, 60, 7200,
    )
    return goodhart, fingerprint


def mock(vm, a_verdict="IMPROVED", b_verdict="IMPROVED", current=80,
         audit="SAFE"):
    vm.clear_mocks()
    vm.mock_web(r"metrics\.example\.org/program.json",
                {"status": 200, "body": json.dumps({"program_id": "support42",
                    "baseline": 20, "current": current, "unit": "tickets"})})
    vm.mock_web(r"outcomes\.example\.net/primary", {"status": 200, "body": A_PAGE})
    vm.mock_web(r"feedback\.example\.com/corroboration", {"status": 200, "body": B_PAGE})
    vm.mock_llm(r"<source_name>primary</source_name>", json.dumps({
        "verdict": a_verdict, "quote": A_QUOTE if a_verdict != "UNKNOWN" else "",
        "reason": "CURRENT_EVIDENCE"}))
    vm.mock_llm(r"<source_name>corroboration</source_name>", json.dumps({
        "verdict": b_verdict, "quote": B_QUOTE if b_verdict != "UNKNOWN" else "",
        "reason": "CURRENT_EVIDENCE"}))
    vm.mock_llm(r"GOODHART adversarial", json.dumps({"audit": audit}))


def test_aligns_only_two_improvements(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    assert contract.is_rewardable("support42", fingerprint) is False
    direct_vm.warp(AFTER)
    mock(direct_vm)
    assert contract.assess("support42", fingerprint) == "REWARDABLE"
    assert contract.is_rewardable("support42", fingerprint) is True
    assert contract.is_rewardable("support42", "0" * 64) is False
    assert direct_vm.run_validator() is True
    with direct_vm.expect_revert("already terminal"):
        contract.assess("support42", fingerprint)


def test_proxy_gain_with_underlying_deterioration(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm, b_verdict="DEGRADED")
    assert contract.assess("support42", fingerprint) == "DIVERGENT"
    assert contract.is_rewardable("support42", fingerprint) is False
    assert contract.get_receipt("support42")["outcome_b"] == "DEGRADED"
    assert direct_vm.run_validator() is True


def test_proxy_not_improved_saves_llm_work(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm, current=21)
    assert contract.assess("support42", fingerprint) == "PROXY_NOT_IMPROVED"
    assert contract.is_rewardable("support42", fingerprint) is False


def test_ambiguous_evidence_blocks_reward(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm, b_verdict="UNKNOWN")
    assert contract.assess("support42", fingerprint) == "INCONCLUSIVE"
    assert contract.is_rewardable("support42", fingerprint) is False


def test_public_metric_source_failure_is_retryable(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    direct_vm.mock_web(r"metrics\.example\.org/program.json", {"status": 503, "body": ""})
    assert contract.assess("support42", fingerprint) == "RETRYABLE"
    assert contract.get_program("support42")["attempts"] == "1"
    mock(direct_vm)
    assert contract.assess("support42", fingerprint) == "REWARDABLE"


def test_retry_exhaustion_is_terminal_and_nonrewardable(direct_vm, direct_deploy,
                                                        direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    direct_vm.mock_web(r"metrics\.example\.org/program.json", {
        "status": 503, "body": "",
    })
    assert contract.assess("support42", fingerprint) == "RETRYABLE"
    assert contract.get_program("support42")["attempts"] == "1"
    direct_vm.clear_mocks()
    direct_vm.mock_web(r"metrics\.example\.org/program.json", {
        "status": 503, "body": "",
    })
    assert contract.assess("support42", fingerprint) == "INCONCLUSIVE"
    assert contract.is_rewardable("support42", fingerprint) is False
    with direct_vm.expect_revert("already terminal"):
        contract.assess("support42", fingerprint)


def test_validator_rejects_changed_source(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm)
    contract.assess("support42", fingerprint)
    mock(direct_vm, current=90)
    assert direct_vm.run_validator() is False


def test_validator_rejects_injected_decision(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm)
    contract.assess("support42", fingerprint)
    forged = {"status": "REWARDABLE", "proxy_after": 80,
              "proxy_digest": "0" * 64, "a": "IMPROVED", "b": "IMPROVED",
              "a_quote": A_QUOTE, "b_quote": B_QUOTE,
              "a_digest": "0" * 64, "b_digest": "0" * 64}
    assert direct_vm.run_validator(leader_result=forged) is False


def test_validator_rejects_extra_fields_and_hidden_positive_inconclusive(
        direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm)
    contract.assess("support42", fingerprint)
    receipt = contract.get_receipt("support42")
    forged = {
        "status": "INCONCLUSIVE", "proxy_after": int(receipt["proxy_after"]),
        "proxy_digest": receipt["proxy_digest"], "a": "IMPROVED", "b": "IMPROVED",
        "a_quote": A_QUOTE, "b_quote": B_QUOTE,
        "a_digest": receipt["outcome_a_digest"],
        "b_digest": receipt["outcome_b_digest"],
        "extra": "must be rejected",
    }
    assert direct_vm.run_validator(leader_result=forged) is False


def test_validator_rechecks_positive_witness_audit(direct_vm, direct_deploy,
                                                   direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm)
    contract.assess("support42", fingerprint)
    # Re-fetch the same pages, but make the validator's independent audit veto
    # the leader's favourable witness. The proposed positive result cannot pass.
    direct_vm.clear_mocks()
    mock(direct_vm, audit="VETO")
    assert direct_vm.run_validator() is False


def test_oversized_source_with_distant_contradiction_fails_closed(
        direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    distant_contradiction = A_QUOTE + (" harmless context" * 900) + (
        " newer update: unresolved issues materially worsened")
    direct_vm.clear_mocks()
    direct_vm.mock_web(r"metrics\.example\.org/program.json", {
        "status": 200,
        "body": json.dumps({"program_id": "support42", "baseline": 20,
                            "current": 80, "unit": "tickets"}),
    })
    direct_vm.mock_web(r"outcomes\.example\.net/primary", {
        "status": 200, "body": distant_contradiction,
    })
    direct_vm.mock_web(r"feedback\.example\.com/corroboration", {
        "status": 200, "body": B_PAGE,
    })
    direct_vm.mock_llm(r"<source_name>corroboration</source_name>", json.dumps({
        "verdict": "IMPROVED", "quote": B_QUOTE, "reason": "CURRENT_EVIDENCE",
    }))
    direct_vm.mock_llm(r"GOODHART adversarial", json.dumps({"audit": "SAFE"}))
    assert len(distant_contradiction) > 12000
    assert contract.assess("support42", fingerprint) == "INCONCLUSIVE"
    assert contract.is_rewardable("support42", fingerprint) is False
    assert contract.get_receipt("support42")["outcome_a"] == "UNKNOWN"


def test_assess_owner_only(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.warp(AFTER)
    mock(direct_vm)
    direct_vm.sender = direct_alice
    with direct_vm.expect_revert("only owner"):
        contract.assess("support42", fingerprint)


def test_cancel_is_owner_only(direct_vm, direct_deploy, direct_alice):
    contract, _ = deploy(direct_vm, direct_deploy, direct_alice)
    with direct_vm.prank(direct_alice):
        with direct_vm.expect_revert("only owner"):
            contract.cancel("support42")


def test_early_rejected(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    with direct_vm.expect_revert("outside assessment window"):
        contract.assess("support42", fingerprint)


def test_cancel_blocks_assessment(direct_vm, direct_deploy, direct_alice):
    contract, fingerprint = deploy(direct_vm, direct_deploy, direct_alice)
    contract.cancel("support42")
    assert contract.is_rewardable("support42", fingerprint) is False
    direct_vm.warp(AFTER)
    with direct_vm.expect_revert("already terminal"):
        contract.assess("support42", fingerprint)
