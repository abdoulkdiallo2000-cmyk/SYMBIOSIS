#!/usr/bin/env python3
"""SYMBIOSIS-Zero power simulation template.

This script is intentionally parameterized. It does NOT assert a final sample size.
Populate pilot-informed ICC/item heterogeneity and committee-chosen SESOI/margins
before using it for preregistration decisions.
"""
from dataclasses import dataclass
import numpy as np

@dataclass
class Scenario:
    n_per_arm: int
    items_natural: int = 40
    baseline_p: float = 0.70
    p_H: float = 0.72
    p_C: float = 0.78
    p_Z: float = 0.80
    p_AI: float = 0.76
    attrition_j7: float = 0.15
    participant_icc: float = 0.10
    item_sd_logit: float = 0.35
    sesoi_h1: float = 0.05
    sesoi_h2: float = 0.03
    margin_h5: float = -0.05

def simulate_once(s: Scenario, rng: np.random.Generator):
    # Placeholder Bernoulli approximation. Replace with the preregistered mixed-model
    # data-generating process after pilot estimates are available.
    out = {}
    for arm, p in [('H', s.p_H), ('C', s.p_C), ('Z', s.p_Z)]:
        x = rng.binomial(s.items_natural, p, size=s.n_per_arm) / s.items_natural
        out[arm] = x
    ai = rng.binomial(s.items_natural, s.p_AI, size=s.n_per_arm) / s.items_natural
    out['AI_proxy'] = ai
    out['h1_est'] = out['Z'].mean() - out['H'].mean()
    out['h2_h_est'] = out['Z'].mean() - out['H'].mean()
    out['h2_ai_est'] = out['Z'].mean() - out['AI_proxy'].mean()
    return out

def monte_carlo(s: Scenario, reps=5000, seed=20260914):
    rng = np.random.default_rng(seed)
    vals = [simulate_once(s, rng) for _ in range(reps)]
    h1 = np.array([v['h1_est'] for v in vals])
    h2h = np.array([v['h2_h_est'] for v in vals])
    h2a = np.array([v['h2_ai_est'] for v in vals])
    return {
        'n_per_arm': s.n_per_arm,
        'Pr(point H1 > SESOI)': float(np.mean(h1 > s.sesoi_h1)),
        'Pr(point H2 both > SESOI)': float(np.mean((h2h > s.sesoi_h2) & (h2a > s.sesoi_h2))),
        'warning': 'Diagnostic only: replace point-estimate checks with full preregistered CI/model decisions.'
    }

if __name__ == '__main__':
    for n in [60,120,180,240,360,480]:
        print(monte_carlo(Scenario(n_per_arm=n), reps=1000))
