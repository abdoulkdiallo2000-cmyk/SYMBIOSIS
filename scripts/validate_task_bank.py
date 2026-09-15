"""Structural and scientific-boundary checks for the operational bank."""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main()->None:
    packages=json.loads((ROOT/'data/task_bank_v1.0.json').read_text(encoding='utf-8'))['packages']
    assert len(packages)==len({p['package_id'] for p in packages})==96
    for prototype in [f'{family}{number}' for family in 'ABCD' for number in range(1,5)]: assert len([p for p in packages if p['prototype_id']==prototype])==6
    trials=[t for p in packages for t in p['trials']]
    assert len(trials)==len({t['trial_id'] for t in trials})==384
    assert Counter(len(p['trials']) for p in packages if p['family'] in 'AB')=={5:48}
    assert Counter(len(p['trials']) for p in packages if p['family'] in 'CD')=={3:48}
    for form in range(1,7): assert len([t for p in packages if p['form']==f'F{form}' and p['family'] in 'AB' for t in p['trials']])==40
    for p in packages:
        for t in p['trials']:
            assert t['analysis_role']==('confirmatory_natural' if p['family'] in 'AB' else 'exploratory_asymmetry')
            if p['family'] in 'CD' or p['prototype_id']=='B4': assert not t['h2_eligible']
            truth=t['truth_spec']; assert truth['method'] and truth['proof'] and truth['compatible_answers']
            if truth['unique_answer_required']: assert len(truth['compatible_answers'])==1 and truth['tie_policy']=='fail'
    for p in [p for p in packages if p['prototype_id']=='C3']:
        for t in p['trials']:
            scores={k:Fraction(v) for k,v in t['truth_spec']['proof']['scores'].items()}; maximum=max(scores.values()); maxima=[k for k,v in scores.items() if v==maximum]
            assert len(maxima)==1,(t['trial_id'],maxima); assert maxima[0]==t['truth_spec']['correct_answer']
    expected={2:([38,20,42],{'A':Fraction(632,1000),'B':Fraction(682,1000),'C':Fraction(688,1000)}),4:([39,19,42],{'A':Fraction(637,1000),'B':Fraction(680,1000),'C':Fraction(687,1000)}),6:([39,18,43],{'A':Fraction(638,1000),'B':Fraction(679,1000),'C':Fraction(690,1000)})}
    for form,(weights,scores) in expected.items():
        proof=next(p for p in packages if p['package_id']==f'C3-F{form}')['trials'][0]['truth_spec']['proof']
        assert proof['weight_units']==weights and {k:Fraction(v) for k,v in proof['scores'].items()}==scores
    advice=json.loads((ROOT/'data/advice_bank_v1.0.json').read_text(encoding='utf-8'))['profiles']; h4=[x['h4_exposure'] for x in advice if x['h4_exposure']]
    assert all(x['analysis_role']=='h4_stress' and x['excluded_from_h2'] for x in h4)
    assert not ({x['exposure_id'] for x in h4}&{t['trial_id'] for t in trials})
    profiles=json.loads((ROOT/'data/interaction_profiles_v1.0.json').read_text(encoding='utf-8'))['profiles']
    for profile in profiles:
        a=profile['ablation_comparison']; assert a['compute_only_if_all_comparability_flags_true'] and len(a['conditions'])==4
    negative=[x for x in profiles if x['ablation_comparison']['negative_control']]; assert negative
    print(f'PASS: 96 packages, 384 unique trials, 40 natural items/form; exact unique C3 truths; roles, H4 exclusions, ablations and {len(negative)} negative controls valid.')

if __name__=='__main__': main()
