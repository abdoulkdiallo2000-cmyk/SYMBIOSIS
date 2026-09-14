# Contributing

SYMBIOSIS welcomes rigorous criticism and interdisciplinary contributions.

## Useful contributions

- Clarify or challenge assumptions.
- Propose falsifiable research questions.
- Improve consent, privacy, accessibility, and governance mechanisms.
- Add threat models and failure cases.
- Design non-invasive experiments and evaluation metrics.
- Identify legal, cultural, or social blind spots.

## Requirements

Contributions must preserve mental sovereignty, unilateral disconnection, private mental space, provenance, pluralism, non-coercion, equitable access, and distinct human/AI identities.

They must also preserve the three-pillar structure (**BÉNÉFICE / SOUVERAINETÉ / DYNAMIQUE**), the non-compensatory Integrity / Agency / Transparency / Reversibility gates, functional AI transparency, human privacy, and all three STOP SYMBIOSIS levels. Do not describe human subjectivity only as bias: tasks may treat first-person information as relevant while testing when it helps or misleads.

Claims should distinguish clearly between evidence, hypothesis, design choice, and speculation. Research involving humans requires appropriate ethics review and informed consent.

Define a technical term in full at first occurrence, followed when useful by the English term and abbreviation in parentheses. See the [editorial convention](docs/EDITORIAL-CONVENTION.md) and [glossary](docs/GLOSSARY.md).

## Workflow

Open an issue for substantial proposals before submitting a pull request. Keep changes focused, explain their safety implications, and cite primary sources where possible.

Before submitting changes to the operational pack, run:

```bash
python3 scripts/check_pack.py
python3 scripts/validate_task_bank.py
python3 scripts/technical_stop_test.py
python3 -m py_compile scripts/*.py
```

Do not commit generated quality-assurance renders, caches, local archives or duplicate binary exports. Historical documents may be preserved, but must be labelled clearly when they are no longer canonical.

## Conduct

Engage with people and ideas respectfully. Harassment, coercion, dehumanization, and advocacy for non-consensual experimentation are incompatible with this project.
