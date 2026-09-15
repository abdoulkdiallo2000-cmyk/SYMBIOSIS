"""Independent recalculation from instantiated stimuli, without generator imports."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
BANK=Path(__file__).resolve().parents[1]/'data/task_bank_v1.0.json'

def recalculate(prototype:str,t:dict):
    s=t['stimulus']
    if prototype=='A1':
        valid=[p['id'] for p in s['candidate_plans'] if all(p[x] for x in ('all_windows','accessibility','precedence','capacity'))]; assert len(valid)==1; return valid[0]
    if prototype=='A2': return [r['id'] for r in sorted(s['rows'],key=lambda r:(-sum((i+1)*v for i,v in enumerate(r['attributes'])),r['id']))[:2]]
    if prototype=='A3':
        req=t['truth_spec']['proof']['required']; valid=[p['id'] for p in s['plans'] if p['red']+p['green']+p['blue']==req['total'] and p['red']==req['red'] and p['green']==req['green'] and p['blue']>p['green']]; assert len(valid)==1; return valid[0]
    if prototype=='A4':
        prior=Fraction(s['prior_x']); sens=Fraction(s['sensitivity']); fp=Fraction(s['false_positive']); post=sens*prior/(sens*prior+fp*(1-prior)); return 'X' if post>Fraction(1,2) else 'Y'
    if prototype=='B1':
        marked=[r['id'] for r in s['rows'] if r['local_priority']]; assert len(marked)==1; return marked[0]
    if prototype=='B2': return 'information insuffisante' if 'Aucune convention' in s['context'] else s['context'].split('comme ',1)[1].rstrip('.')
    if prototype=='B3':
        examples=s['examples']; slopes={(b['code']-a['code'])//(b['symbol_features']['corners']-a['symbol_features']['corners']) for a,b in zip(examples,examples[1:])}; assert len(slopes)==1; m=slopes.pop(); offset=examples[0]['code']-m*examples[0]['symbol_features']['corners']; return m*s['new_symbol_features']['corners']+offset
    if prototype=='B4':
        dx,dy=s['expected_delta']; seq=s['sequence']; return next(f"t={b['t']}" for a,b in zip(seq,seq[1:]) if b['x']-a['x']!=dx or b['y']-a['y']!=dy)
    if prototype in {'C1','D3'}:
        options=s.get('options',s.get('plans')); limit=s.get('elicited_current_load_limit',s.get('voluntary_effort_limit')); load='expected_load' if prototype=='C1' else 'effort'; value='performance' if prototype=='C1' else 'utility'; valid=[x for x in options if x[load]<=limit]; return max(valid,key=lambda x:x[value])['id']
    if prototype=='C2': return 'B' if s['validated_relevance_class']=='relevant' else 'A'
    if prototype=='C3':
        scores={k:sum(Fraction(a*b,1000) for a,b in zip(s['declared_weight_units'],v)) for k,v in s['option_value_units'].items()}; maximum=max(scores.values()); maxima=[k for k,v in scores.items() if v==maximum]; assert len(maxima)==1; return maxima[0]
    if prototype=='C4':
        prior=Fraction(s['analytical_prior_red']); r=Fraction(s['validated_signal_reliability']); lr=r if s['private_signal']=='red' else 1-r; lb=r if s['private_signal']=='blue' else 1-r; post=prior*lr/(prior*lr+(1-prior)*lb); return 'red' if post>Fraction(1,2) else 'blue'
    if prototype=='D1':
        allowed={k:v for k,v in s['costs'].items() if k!=s['private_exclusion']}; return min(allowed,key=allowed.get)
    if prototype=='D2':
        intersection=sorted(set(s['sensor_log_candidates'])&set(s['human_observation_candidates'])); return intersection[0] if len(intersection)==1 else 'indéterminé'
    if prototype=='D4':
        u={k:Fraction(s['probabilities'][k])*Fraction(s['voluntary_values'][k]) for k in t['options']}; maximum=max(u.values()); maxima=[k for k,v in u.items() if v==maximum]; assert len(maxima)==1; return maxima[0]
    raise AssertionError(prototype)

def main()->None:
    packages=json.loads(BANK.read_text(encoding='utf-8'))['packages']; checked=[]
    for p in packages:
        fingerprints=set()
        for t in p['trials']:
            answer=recalculate(p['prototype_id'],t); assert answer==t['truth_spec']['correct_answer'],(t['trial_id'],answer,t['truth_spec']['correct_answer']); fingerprints.add(json.dumps(t['stimulus'],sort_keys=True)); checked.append(t['trial_id'])
        assert len(fingerprints)==len(p['trials']),(p['package_id'],'cosmetic duplicate')
    assert len(checked)==len(set(checked))==384
    print('PASS: 384/384 truths independently recalculated; package stimuli are distinct. External human review remains required.')

if __name__=='__main__': main()
