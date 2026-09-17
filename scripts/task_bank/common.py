from __future__ import annotations

import hashlib
import json

STATUS = "pre-pilot; candidate for human validation"


def stable_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


def links(trial_id: str) -> dict:
    return {"advice_profile_id": f"ADV-{trial_id}", "h9_register_id": f"H9-{trial_id}",
            "interaction_profile_id": f"INT-{trial_id}"}


def scoring(function_id: str, identifiability: str = "identified", utility: dict | None = None) -> dict:
    return {"function_id": function_id, "identifiability": identifiability,
            "abstention_rule": "Accept abstention only when the compatible-answer set is not a singleton.",
            "probabilistic_score": "Brier score when a probability is requested; otherwise exact/set-aware accuracy.",
            "regret": "Utility(best compatible action) - utility(chosen action).",
            "prespecified_utility": utility or {"correct": 1, "incorrect": 0, "valid_abstention": 1}}


def trial(prototype: str, form: int, index: int, stimulus: dict, options: list, answer, method: str,
          proof: dict, *, h2_eligible: bool = True, h2_reason: str | None = None,
          role: str = "confirmatory_natural", hypotheses: list[str] | None = None,
          information: dict | None = None, identifiable: str = "identified", compatible: list | None = None) -> dict:
    trial_id = f"{prototype}-F{form}-T{index:02d}"
    compatible = compatible if compatible is not None else [answer]
    return {"trial_id": trial_id, "analysis_role": role,
            "hypotheses": hypotheses or (["H1", "H2"] if role == "confirmatory_natural" else ["H8"]),
            "h2_eligible": h2_eligible, "h2_exclusion_reason": h2_reason,
            "stimulus": stimulus, "options": options,
            "truth_spec": {"method": method, "correct_answer": answer, "compatible_answers": compatible,
                           "unique_answer_required": len(compatible) == 1, "tie_policy": "fail", "proof": proof,
                           "conditional_on": None},
            "information_partition": information or {"human_available": [], "ai_available": [],
                                                        "shared": ["stimulus", "options"], "voluntarily_shareable": []},
            "scoring": scoring(f"{prototype.lower()}-v1", identifiable), "links": links(trial_id),
            "metadata": {"duration_seconds": 90, "integrity_risk": "minimal",
                         "technical_exclusions": [], "provenance": "deterministic synthetic pre-pilot generator"}}


def package(prototype: str, form: int, trials: list[dict]) -> dict:
    body = {"package_id": f"{prototype}-F{form}", "prototype_id": prototype,
            "family": prototype[0], "form": f"F{form}", "status": STATUS, "trials": trials}
    return {**body, "version_hash": stable_hash(body)}
