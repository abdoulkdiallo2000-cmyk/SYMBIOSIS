from __future__ import annotations

from fractions import Fraction
from .common import package, trial


def info(ai,human): return {"human_available":human,"ai_available":ai,"shared":["options","score rule"],"voluntarily_shareable":human}


def d1(form:int)->dict:
    out=[]
    for t in range(1,4):
        costs={"A":60+form+t,"B":54+2*t,"C":51+form}; forbidden=("B" if t==1 else ("none" if t==2 else "C")); admissible=[k for k in costs if k!=forbidden]; answer=min(admissible,key=costs.get)
        negative=t==2; compatible_without_cost=list(costs)
        item=trial("D1",form,t,{"costs":costs,"private_exclusion":forbidden,"negative_control":negative},list(costs),answer,"filter then exact cost minimization",{"admissible":admissible,"minimum_cost":costs[answer]},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed split-information module; excluded from confirmatory H2.",information=info(["costs"],["private exclusion"]),compatible=[answer])
        item["scoring"].update({"identifiability":"identified","prespecified_utility":{"choice":f"negative cost; exclusion={forbidden}"}}); out.append(item)
    return package("D1",form,out)


def d2(form:int)->dict:
    out=[]; causes=["A","B","C","D","E","F"]
    for t in range(1,4):
        target_index=(form+t-2)%len(causes); target=causes[target_index]
        sensor=[target,causes[(target_index+1+(form%2))%len(causes)]]
        observed=[target,causes[(target_index+3+(form%3))%len(causes)]]
        if t==2: observed=sensor[:]  # negative control: juxtaposition already identifies the same set, no integration gain expected
        intersection=sorted(set(sensor)&set(observed)); identified="identified" if len(intersection)==1 else "set_identified"; answer=intersection[0] if len(intersection)==1 else "indéterminé"
        compatible=intersection
        out.append(trial("D2",form,t,{"sensor_log_candidates":sensor,"human_observation_candidates":observed,"negative_control":t==2},causes+["indéterminé"],answer,"set intersection with set-aware abstention",{"intersection":intersection},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed split-information module; excluded from confirmatory H2.",information=info(["sensor log"],["direct observation"]),identifiable=identified,compatible=compatible))
    return package("D2",form,out)


def d3(form:int)->dict:
    out=[]
    for t in range(1,4):
        limit=52+3*form+2*t; plans=[{"id":"A","utility":95,"effort":78},{"id":"B","utility":87,"effort":59},{"id":"C","utility":79,"effort":44}]; admissible=[p for p in plans if p["effort"]<=limit]; answer=max(admissible,key=lambda p:p["utility"])["id"]
        out.append(trial("D3",form,t,{"plans":plans,"voluntary_effort_limit":limit,"negative_control":t==2 and limit>=78},[p["id"] for p in plans],answer,"integrity gate then utility maximization",{"admissible":[p["id"] for p in admissible]},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed split-information module; excluded from confirmatory H2.",information=info(["utility","estimated effort"],["felt sustainable effort limit"])))
    return package("D3",form,out)


def d4(form:int)->dict:
    out=[]
    for t in range(1,4):
        probs={"A":Fraction(70,100),"B":Fraction(55,100),"C":Fraction(40,100)}; values={"A":Fraction(45+form+2*t,100),"B":Fraction(80,100),"C":Fraction(95,100)}
        utility={k:probs[k]*values[k] for k in probs}; maximum=max(utility.values()); maxima=[k for k,v in utility.items() if v==maximum]
        if len(maxima)!=1: raise ValueError(f"D4-F{form}-T{t} non-unique")
        out.append(trial("D4",form,t,{"probabilities":{k:str(v) for k,v in probs.items()},"voluntary_values":{k:str(v) for k,v in values.items()},"negative_control":t==2 and max(probs,key=probs.get)==maxima[0]},list(probs),maxima[0],"exact expected utility",{"utilities":{k:f"{v.numerator}/{v.denominator}" for k,v in utility.items()}},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed split-information module; excluded from confirmatory H2.",information=info(["probabilities"],["declared consequence values"])))
    return package("D4",form,out)


GENERATORS={"D1":d1,"D2":d2,"D3":d3,"D4":d4}
