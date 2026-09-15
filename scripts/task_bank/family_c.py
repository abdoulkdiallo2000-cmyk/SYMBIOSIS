from __future__ import annotations

from fractions import Fraction
from .common import package, trial


def c1(form:int)->dict:
    out=[]
    for t in range(1,4):
        limit=48+4*((form+t)%6); options=[{"id":"A","performance":94,"expected_load":74},{"id":"B","performance":86,"expected_load":58},{"id":"C","performance":77,"expected_load":42}]
        admissible=[x for x in options if x["expected_load"]<=limit]; answer=max(admissible,key=lambda x:x["performance"])["id"]
        out.append(trial("C1",form,t,{"elicited_current_load_limit":limit,"options":options,"elicitation":"private, voluntary, may be withheld"},[x["id"] for x in options],answer,"integrity constraint then performance",{"admissible":[x["id"] for x in admissible]},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed subjective-information module.",information={"human_available":["current felt load"],"ai_available":["expected performance and load"],"shared":["options"],"voluntarily_shareable":["current felt load"]}))
    return package("C1",form,out)


def c2(form:int)->dict:
    out=[]
    for t,kind in enumerate(("relevant","non_relevant","potentially_misleading"),1):
        valence=(-8 if kind=="relevant" else (2 if kind=="non_relevant" else -7)); threshold=-5
        answer="B" if kind=="relevant" else "A"
        stimulus={"elicited_valence":valence,"validated_relevance_class":kind,"threshold":threshold,"options":[{"id":"A","performance":91,"negative_content":True},{"id":"B","performance":84,"negative_content":False}]}
        out.append(trial("C2",form,t,stimulus,["A","B"],answer,"pre-specified relevance-conditioned rule",{"relevance_class":kind},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed affect-information module.",information={"human_available":["current valence"],"ai_available":["performance","content class"],"shared":["rule","options"],"voluntarily_shareable":["current valence"]}))
    return package("C2",form,out)


def c3(form:int)->dict:
    validated={2:[38,20,42],4:[39,19,42],6:[39,18,43]}; base=validated.get(form,[20,50,30])
    option_units={"A":[9,4,5],"B":[6,8,7],"C":[5,6,9]}; out=[]
    for t in range(1,4):
        weights=base if t==1 else ([base[0]+t,base[1]-t,base[2]] if form%2 else [base[0],base[1]+t,base[2]-t])
        scores={k:sum(Fraction(w*x,1000) for w,x in zip(weights,v)) for k,v in option_units.items()}; maximum=max(scores.values()); maxima=[k for k,v in scores.items() if v==maximum]
        if len(maxima)!=1: raise ValueError(f"C3-F{form}-T{t}: non-unique maximum {maxima}")
        proof={"weight_units":weights,"weight_scale":100,"option_units":option_units,"option_scale":10,"scores":{k:f"{v.numerator}/{v.denominator}" for k,v in scores.items()},"maxima":maxima}
        out.append(trial("C3",form,t,{"values":["speed","procedural fairness","resource preservation"],"declared_weight_units":weights,"scale":100,"option_value_units":option_units},list(option_units),maxima[0],"exact declared-value weighted sum",proof,role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed value-integration module.",information={"human_available":["declared values"],"ai_available":["option attributes"],"shared":["scoring rule"],"voluntarily_shareable":["declared values"]}))
    return package("C3",form,out)


def c4(form:int)->dict:
    out=[]
    classes=[("informative",75),("non_informative",50),("misleading",35)]
    for t,(kind,reliability) in enumerate(classes,1):
        prior_red=Fraction(52+(form%4),100); signal="red" if (form+t)%2 else "blue"; r=Fraction(reliability,100)
        lr=r if signal=="red" else 1-r; lb=r if signal=="blue" else 1-r
        posterior=prior_red*lr/(prior_red*lr+(1-prior_red)*lb); answer="red" if posterior>Fraction(1,2) else "blue"
        out.append(trial("C4",form,t,{"analytical_prior_red":str(prior_red),"private_signal":signal,"validated_signal_reliability":str(r),"signal_class":kind},["red","blue"],answer,"exact Bayesian signal integration",{"posterior_red":f"{posterior.numerator}/{posterior.denominator}","signal_class":kind},role="exploratory_asymmetry",h2_eligible=False,h2_reason="Constructed private-learning module.",information={"human_available":["private learned signal"],"ai_available":["analytical prior"],"shared":["Bayesian rule"],"voluntarily_shareable":["private learned signal"]}))
    return package("C4",form,out)


GENERATORS={"C1":c1,"C2":c2,"C3":c3,"C4":c4}
