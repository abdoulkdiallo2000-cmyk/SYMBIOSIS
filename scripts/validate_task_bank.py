import json, sys
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'task_bank_v1.0.json'
d=json.loads(p.read_text(encoding='utf-8'))
recs=d['records']
assert len(recs)==96, len(recs)
ids=[r['id'] for r in recs]
assert len(ids)==len(set(ids))
for prefix in [f'{c}{i}' for c in 'ABCD' for i in range(1,5)]:
    forms=[r for r in recs if r['prototype']==prefix]
    assert len(forms)==6, (prefix,len(forms))
    for r in forms:
        assert 'correct_answer' in r and 'truth_rule' in r
print('PASS: 96 unique forms, six per prototype, truth fields present.')
