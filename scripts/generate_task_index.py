from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
bank=json.loads((ROOT/'data/task_bank_v1.0.json').read_text(encoding='utf-8'))
lines=['# Index des 96 paquets de formes pré-pilotes','',
       '**Statut :** implémentation candidate à validation humaine. Les contrôles logiciels ne constituent pas une validation scientifique.','',
       '| Paquet | Famille | Essais | Rôle | H2 | Réponses de référence | Hachage |','|---|---:|---:|---|---|---|---|']
for package in bank['packages']:
    trials=package['trials']; answers=', '.join(str(t['truth_spec']['correct_answer']) for t in trials)
    eligible='oui' if all(t['h2_eligible'] for t in trials) else 'non'
    lines.append(f"| {package['package_id']} | {package['family']} | {len(trials)} | {trials[0]['analysis_role']} | {eligible} | {answers} | `{package['version_hash'][7:19]}` |")
lines += ['', 'Chaque forme complète A1–B4 contient 40 essais naturels. Les paquets C1–D4 sont des modules exploratoires séparés. B4 reste exclu de H2 tant que l’équivalence des représentations n’est pas démontrée.', '',
          'Les réponses sont recalculées par `scripts/audit_reference_truths.py`. Une vérification humaine externe demeure requise.']
(ROOT/'docs/TASK-FORMS-INDEX.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
