from __future__ import annotations
import random, csv, argparse
from pathlib import Path

ARMS=['H','H+AI','SZ']
FORMS=['F1','F2','F3','F4','F5','F6']
FAMILIES=['A','B','C','D']

def latin_square(items):
    n=len(items)
    return [[items[(i+j)%n] for j in range(n)] for i in range(n)]

def allocate(n, seed=20260914):
    rng=random.Random(seed)
    rows=[]
    blocks=[6,9]
    arm_cycle=[]
    while len(arm_cycle)<n:
        b=rng.choice(blocks)
        reps=b//3
        block=ARMS*reps
        rng.shuffle(block)
        arm_cycle.extend(block)
    form_sq=latin_square(FORMS)
    fam_sq=latin_square(FAMILIES)
    for i in range(n):
        rows.append({
            'participant_index':i+1,
            'arm':arm_cycle[i],
            'pre_form':form_sq[i%6][0],
            'natural_form_1':form_sq[i%6][1],
            'natural_form_2':form_sq[i%6][2],
            'resistance_form':form_sq[i%6][3],
            'post_immediate_form':form_sq[i%6][4],
            'post_j7_form':form_sq[i%6][5],
            'family_order':'>'.join(fam_sq[i%4]),
        })
    return rows

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--n',type=int,default=36); ap.add_argument('--seed',type=int,default=20260914); ap.add_argument('--out',default='allocation.csv')
    a=ap.parse_args(); rows=allocate(a.n,a.seed)
    with open(a.out,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f'Wrote {len(rows)} allocations to {a.out}')
