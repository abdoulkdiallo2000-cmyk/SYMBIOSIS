from pathlib import Path
import json, subprocess, sys
base=Path(__file__).resolve().parents[1]
required=[
'docs/SYMBIOSIS-ZERO-EXPERIMENTAL-PROTOCOL-v1.0.md',
'docs/SYMBIOSIS-ZERO-TASK-BATTERY-v1.0.md',
'data/task_bank_v1.0.json','data/advice_bank_v1.0.json','data/h9_register_v1.0.json','data/interaction_profiles_v1.0.json','data/pilot_randomization_example.csv',
'schemas/task-bank.schema.json','schemas/advice-bank.schema.json','schemas/h9-register.schema.json','schemas/interaction-profile.schema.json',
'docs/COGNITIVE-INTERVIEW-GUIDE.md','docs/PRE-PILOT-TECHNICAL-PROTOCOL.md','docs/PILOT-PROTOCOL.md',
'docs/DATA-DICTIONARY.md','docs/ETHICS-SUBMISSION-OUTLINE.md','docs/PREREGISTRATION-DRAFT.md','docs/DECISION-REGISTER.md',
'docs/CORRECTIONS-APPLIED-2026-09-14.md','docs/WHITE-PAPER-CANONICAL-AUDIT.md','docs/GLOSSARY.md','docs/EDITORIAL-CONVENTION.md',
'docs/BIBLIOGRAPHY-AUDIT-2026-09-14.md','docs/LICENSE-AUDIT.md','docs/TASK-BANK-INDEPENDENT-AUDIT-2026-09-14.md',
'docs/white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-FR.md','docs/white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-EN.md','docs/white-paper/CONCORDANCE-FR-EN.md',
'docs/SYMBIOSIS-Zero-STOP-H7-Questionnaire.md','docs/SYMBIOSIS-Zero-H9-Transparency-Template.md',
'docs/H9-REGISTER-SCHEMA.json','docs/SYMBIOSIS-Zero-PreRegistration-Checklist-v1.0.md',
'scripts/audit_reference_truths.py','scripts/check_bibliography.py','scripts/check_scientific_invariants.py']
missing=[x for x in required if not (base/x).exists()]
if missing:
    print('MISSING:',*missing,sep='\n'); raise SystemExit(1)
d=json.loads((base/'data/task_bank_v1.0.json').read_text(encoding='utf-8'))
assert len(d['packages'])==96
print('PASS: operational pack completeness checks passed.')
