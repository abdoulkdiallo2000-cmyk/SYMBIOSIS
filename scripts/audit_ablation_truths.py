"""Independent recalculation of condition-specific ablation truths."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def expected_single_source(prototype,trial,condition):
    stimulus=trial['stimulus']; options=[x for x in trial['options'] if x!='indéterminé']
    if prototype=='D1' and condition=='AI-data-only':
        costs=stimulus['costs']; compatible=set()
        for forbidden in ['none',*costs]:
            allowed={k:v for k,v in costs.items() if k!=forbidden}
            compatible.add(min(allowed,key=allowed.get))
        return sorted(compatible)
    if prototype=='D1': return [x for x in options if x!=stimulus['private_exclusion']]
    if prototype=='D2': return list(stimulus['sensor_log_candidates'] if condition=='AI-data-only' else stimulus['human_observation_candidates'])
    if prototype=='D3' and condition=='Human-experience-only': return [x['id'] for x in stimulus['plans'] if x['effort']<=stimulus['voluntary_effort_limit']]
    return options

def main():
    packages=json.loads((ROOT/'data/task_bank_v1.0.json').read_text(encoding='utf-8'))['packages']
    trials={t['trial_id']:(p['prototype_id'],t) for p in packages for t in p['trials']}
    profiles=json.loads((ROOT/'data/interaction_profiles_v1.0.json').read_text(encoding='utf-8'))['profiles']
    checked=0; negative=0
    for profile in profiles:
        comparison=profile['ablation_comparison']
        if comparison is None: continue
        trial_id=profile['interaction_profile_id'].removeprefix('INT-'); prototype,trial=trials[trial_id]
        partition=trial['information_partition']
        for condition in comparison['conditions']:
            name=condition['condition']
            if name in {'Integrated SZ','Juxtaposed H+AI'}:
                compatible=list(trial['truth_spec']['compatible_answers']); response=trial['truth_spec']['correct_answer']; identified=trial['scoring']['identifiability']
                available=partition['shared']+partition['human_available']+partition['ai_available']; masked=[]
            else:
                compatible=list(dict.fromkeys(expected_single_source(prototype,trial,name)))
                response=compatible[0] if len(compatible)==1 else 'indéterminé'
                identified='identified' if len(compatible)==1 else ('set_identified' if compatible else 'not_identified')
                available=partition['shared']+(partition['ai_available'] if name=='AI-data-only' else partition['human_available'])
                masked=partition['human_available'] if name=='AI-data-only' else partition['ai_available']
            assert condition['available_information']==available,(trial_id,name,'available')
            assert condition['masked_information']==masked,(trial_id,name,'masked')
            assert condition['compatible_answers']==compatible,(trial_id,name,'compatible')
            assert condition['conditional_correct_response']==response,(trial_id,name,'response')
            assert condition['identifiability']==identified,(trial_id,name,'identifiability')
            checked+=1
        if comparison['negative_control']:
            negative+=1
            assert comparison['negative_control_expectation']=='No integration gain under the prespecified set-aware score.'
        assert comparison['gain_computation_allowed'] is False
    assert checked==576 and negative==12,(checked,negative)
    print('PASS: 576/576 condition-specific ablation truths independently recalculated; 12 negative controls preserved; gain computation blocked while comparability is pending.')

if __name__=='__main__': main()
