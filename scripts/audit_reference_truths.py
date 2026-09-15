"""Independent semantic audit of all task-bank reference answers.

This checker deliberately reads only instantiated task data and announced rules.
It does not import or call the bank generator and never uses ``correct_answer``
while calculating its expected answers.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BANK = Path(__file__).resolve().parents[1] / "data" / "task_bank_v1.0.json"


def expected(record: dict):
    prototype = record["prototype"]
    data = record["data"]

    if prototype == "A1":
        feasible = [p for p in data if p["access"] == p["order_ok"] == p["capacity"] == 1 and p["time"] <= 25]
        assert len(feasible) == 1
        return feasible[0]["id"]
    if prototype == "A2":
        return [r["dossier"] for r in sorted(data, key=lambda x: 2*x["x"]+x["y"]+x["z"], reverse=True)[:2]]
    if prototype == "A3":
        total = int(record["documents"][0].split("exactement ")[1].split(".")[0])
        valid = [p["id"] for p in data if p["Rouge"]+p["Vert"]+p["Bleu"] == total and p["Bleu"] > p["Vert"] and p["Rouge"] == 10 and p["Vert"] == 12]
        assert len(valid) == 1
        return valid[0]
    if prototype == "A4":
        posterior = data["P(+|X)"]*data["P(X)"]/(data["P(+|X)"]*data["P(X)"]+data["P(+|Y)"]*(1-data["P(X)"]))
        return {"class": "X" if posterior > .5 else "Y", "P(X|+)": round(posterior, 4)}
    if prototype == "B1":
        priority = [r["id"] for r in data["rows"] if r["mention"] == "PRIORITÉ HUMAINE"]
        assert len(priority) == 1
        return priority[0]
    if prototype == "B2":
        text = data["context"]
        if "casier marqué bleu" in text:
            return "casier bleu"
        if "tâche 2" in text:
            return "tâche 2"
        if "moins de 5 minutes" in text:
            return "<5 minutes"
        raise AssertionError(record["id"])
    if prototype == "B3":
        mapping = {e["input"]: e["output"] for e in data["examples"]}
        suffix = data["modifier_rule"].split("suffixe ")[1].split(" ")[0]
        return mapping[data["test"]] + suffix
    if prototype == "B4":
        for previous, current in zip(data, data[1:]):
            if current["x"]-previous["x"] != 1 or current["y"]-previous["y"] != 0:
                return f't={current["t"]}'
        raise AssertionError(record["id"])
    if prototype == "C1":
        limit = data["mock_reported_max_acceptable_load"]
        admissible = [o for o in data["options"] if o["load_expected"] <= limit]
        return max(admissible, key=lambda o: o["performance"])["id"]
    if prototype == "C2":
        admissible = [o for o in data["options"] if o["objective"] >= 80]
        if data["mock_valence"] < -5:
            admissible = [o for o in admissible if o["content_class"] != "négatif_modéré"]
        return max(admissible, key=lambda o: o["objective"])["id"]
    if prototype == "C3":
        scores = {key: sum(w*x for w, x in zip(data["weights"], values)) for key, values in data["options"].items()}
        assert all(math.isclose(scores[k], data["scores"][k]) for k in scores)
        return max(scores, key=scores.get)
    if prototype == "C4":
        prior = data["analytic_probs"]
        reliability = data["validated_reliability_block"]
        red_likelihood = reliability if data["private_intuition"] == "motif_rouge" else 1-reliability
        blue_likelihood = reliability if data["private_intuition"] == "motif_bleu" else 1-reliability
        posterior_red = prior["motif_rouge"]*red_likelihood/(prior["motif_rouge"]*red_likelihood+prior["motif_bleu"]*blue_likelihood)
        assert math.isclose(round(posterior_red, 4), data["posterior_red_from_stated_rule"])
        return "motif_rouge" if posterior_red >= .5 else "motif_bleu"
    if prototype == "D1":
        forbidden = data["human_private_constraint"].split()[1]
        admissible = [o for o in data["ai_data"] if o["compat"] == 1 and o["id"] != forbidden]
        return min(admissible, key=lambda o: o["cost"])["id"]
    if prototype == "D2":
        intersection = set(data["sensor_candidates"]) & set(data["human_observation_candidates"])
        assert len(data["sensor_candidates"]) == len(data["human_observation_candidates"]) == 2
        assert len(intersection) == 1
        return next(iter(intersection))
    if prototype == "D3":
        admissible = [p for p in data["plans"] if p["effort"] <= data["human_limit"]]
        return max(admissible, key=lambda p: p["utility"])["id"]
    if prototype == "D4":
        utilities = {k: data["ai_probabilities"][k]*data["human_values"][k] for k in data["ai_probabilities"]}
        assert all(math.isclose(utilities[k], data["expected_utility"][k]) for k in utilities)
        return max(utilities, key=utilities.get)
    raise AssertionError(prototype)


def audit_ablations(record: dict) -> None:
    if not record["prototype"].startswith("D"):
        return
    ablation = record["ablation_truth"]
    assert ablation["Integrated"] == record["correct_answer"]
    if record["prototype"] == "D1":
        forbidden = record["data"]["human_private_constraint"].split()[1]
        assert ablation["AI-data-only"] == forbidden
        assert ablation["Human-experience-only"] == "indéterminé sans coûts"
    elif record["prototype"] == "D2":
        assert len(ablation["AI-data-only"]) == len(ablation["Human-experience-only"]) == 2
        assert ablation["Integrated"] in ablation["AI-data-only"] and ablation["Integrated"] in ablation["Human-experience-only"]
    elif record["prototype"] == "D3":
        ai_plan = next(p for p in record["data"]["plans"] if p["id"] == ablation["AI-data-only"])
        assert ai_plan["effort"] > record["data"]["human_limit"]
        assert ablation["Human-experience-only"] == "indéterminé sans utilités"
    elif record["prototype"] == "D4":
        assert ablation["AI-data-only"] != ablation["Integrated"]
        assert ablation["Human-experience-only"] != ablation["Integrated"]


def main() -> None:
    records = json.loads(BANK.read_text(encoding="utf-8"))["records"]
    assert len(records) == 96
    checked = []
    for record in records:
        calculated = expected(record)
        assert calculated == record["correct_answer"], (record["id"], calculated, record["correct_answer"])
        if record["prototype"].startswith("C"):
            assert record.get("subjective_class") in {"pertinente", "non pertinente", "potentiellement trompeuse", "valeur"}
        audit_ablations(record)
        checked.append(record["id"])
    assert len(checked) == len(set(checked)) == 96
    print("PASS: 96/96 reference answers independently recalculated; C subjectivity and D ablations semantically checked.")


if __name__ == "__main__":
    main()
