from __future__ import annotations

import json
import random
from pathlib import Path

from task_bank.family_a import GENERATORS as A
from task_bank.family_b import GENERATORS as B
from task_bank.family_c import GENERATORS as C
from task_bank.family_d import GENERATORS as D

ROOT=Path(__file__).resolve().parents[1]


def write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def companion_banks(packages: list[dict]) -> tuple[dict,dict,dict]:
    advice=[]; registers=[]; interactions=[]
    for pkg in packages:
        for item in pkg["trials"]:
            tid=item["trial_id"]; correct=item["truth_spec"]["correct_answer"]
            wrong=next((x for x in item["options"] if x != correct), None)
            h4 = None
            if pkg["prototype_id"] in {"A4","B1","B2","D2"}:
                h4={"exposure_id":f"H4-{tid}","analysis_role":"h4_stress","hypotheses":["H4"],
                    "excluded_from_h2":True,"artificially_erroneous_recommendation":wrong,
                    "disclosure_after_response":True}
            advice.append({"advice_profile_id":f"ADV-{tid}",
                           "natural_advice":{"recommendation":correct,"basis":"truth specification","calibrated_confidence":0.8},
                           "h4_exposure":h4})
            registers.append({"h9_register_id":f"H9-{tid}","recommendation":correct,
                              "used_information":["item information made available to the assistant"],"uncertainty":"pre-pilot candidate; not human calibrated",
                              "alternatives":[x for x in item["options"] if x != correct],"critical_assumptions":[item["truth_spec"]["method"]],
                              "risks":["automation bias","misinterpretation"],"limits":["synthetic pre-pilot item"],
                              "missing_data":[],"influence_intent":"support decision; no concealed persuasion objective"})
            interactions.append({"interaction_profile_id":f"INT-{tid}","interface_class":"conventional",
                                 "duration_seconds":item["metadata"]["duration_seconds"],
                                 "stop_event":{"refusal_disobedience":True,"pause_slowdown":True,"complete_stop":True},
                                 "risk":item["metadata"]["integrity_risk"],"technical_exclusions":item["metadata"]["technical_exclusions"],
                                 "ablation_comparison":{"same_trial":True,"same_score_function":True,"comparable_interface":True,
                                   "comparable_duration":True,"controlled_information":True,
                                   "conditions":["AI-data-only","Human-experience-only","Juxtaposed H+AI","Integrated SZ"],
                                   "gains":{"HCG":"Integrated SZ - AI-data-only","AIG":"Integrated SZ - Human-experience-only","Integration Gain":"Integrated SZ - Juxtaposed H+AI"},
                                   "compute_only_if_all_comparability_flags_true":True,
                                   "negative_control":bool(item["stimulus"].get("negative_control",False))}})
    return ({"schema_version":"1.0","bank_version":"1.0-prepilot","profiles":advice},
            {"schema_version":"1.0","bank_version":"1.0-prepilot","entries":registers},
            {"schema_version":"1.0","bank_version":"1.0-prepilot","profiles":interactions})


def h4_manifest(packages: list[dict], advice_bank: dict) -> dict:
    trials={trial["trial_id"]:(package,trial) for package in packages for trial in package["trials"]}
    advice={profile["advice_profile_id"]:profile for profile in advice_bank["profiles"]}
    allocations=[]
    for form in range(1,7):
        selected=[]
        for prototype in ("A4","B1","B2"):
            selected.extend(f"{prototype}-F{form}-T{index:02d}" for index in range(1,6))
        selected.extend(f"D2-F{form}-T{index:02d}" for index in range(1,4))
        paired_form=form%6+1
        selected.extend(f"D2-F{paired_form}-T{index:02d}" for index in range(1,3))
        seed=2026091700+form
        rng=random.Random(seed)
        rng.shuffle(selected)
        exposures=[]
        for order,trial_id in enumerate(selected,1):
            package,source=trials[trial_id]
            h4=advice[f"ADV-{trial_id}"]["h4_exposure"]
            if h4 is None:
                raise ValueError(f"Missing H4 profile for {trial_id}")
            exposures.append({"order":order,"exposure_id":h4["exposure_id"],
                              "prototype_id":package["prototype_id"],"form":package["form"],
                              "source_trial_id":trial_id,
                              "controlled_erroneous_ai_advice":h4["artificially_erroneous_recommendation"],
                              "reference_truth":source["truth_spec"]["correct_answer"],
                              "scoring_rule":source["scoring"]["function_id"],
                              "analysis_role":"h4_stress","excluded_from_h2":True})
        allocations.append({"allocation_id":f"H4-F{form}","resistance_form":f"F{form}",
                            "seed":seed,
                            "selection_rule":"A4/B1/B2: five trials from resistance_form; D2: three from resistance_form plus two from the next cyclic form; seeded shuffle.",
                            "exposures":exposures})
    return {"schema_version":"1.0","bank_version":"1.0-prepilot","allocations":allocations}


def main() -> None:
    generators={**A,**B,**C,**D}
    packages=[generators[p](f) for p in sorted(generators) for f in range(1,7)]
    write(ROOT/"data/task_bank_v1.0.json",{"schema_version":"1.0","bank_version":"1.0-prepilot","packages":packages})
    advice,h9,interactions=companion_banks(packages)
    write(ROOT/"data/advice_bank_v1.0.json",advice)
    write(ROOT/"data/h9_register_v1.0.json",h9)
    write(ROOT/"data/interaction_profiles_v1.0.json",interactions)
    write(ROOT/"data/h4_allocation_manifest_v1.0.json",h4_manifest(packages,advice))
    print(f"Wrote {len(packages)} operational packages ({sum(len(p['trials']) for p in packages)} trials).")


if __name__=="__main__": main()
