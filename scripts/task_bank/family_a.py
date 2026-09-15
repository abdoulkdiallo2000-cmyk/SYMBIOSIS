from __future__ import annotations

from fractions import Fraction
from .common import package, trial


def a1(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        stops=[{"id":f"S{i:02d}","window":[i+form, i+form+9],"accessible":(i+t)%5!=0} for i in range(1,13)]
        correct=(form+t)%5
        plans=[]
        for k in range(5):
            plans.append({"id":chr(65+k),"distance":65+3*k+form+t,"all_windows":k!=((correct+1)%5),
                          "accessibility":k!=((correct+2)%5),"precedence":k!=((correct+3)%5),
                          "capacity":k!=((correct+4)%5)})
        plans[correct].update(all_windows=True,accessibility=True,precedence=True,capacity=True)
        feasible=[p["id"] for p in plans if all(p[x] for x in ("all_windows","accessibility","precedence","capacity"))]
        trials.append(trial("A1",form,t,{"stops":stops,"candidate_plans":plans,"rule":"select unique feasible plan"},
                            [p["id"] for p in plans],feasible[0],"constraint conjunction",{"feasible":feasible}))
    return package("A1",form,trials)


def a2(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        rows=[]
        for i in range(40):
            attrs=[(i*(j+2)+form*7+t*11+j*j)%31 for j in range(8)]
            score=sum((j+1)*v for j,v in enumerate(attrs))
            rows.append({"id":f"R{i+1:02d}","attributes":attrs,"score":score})
        ranked=sorted(rows,key=lambda r:(-r["score"],r["id"]))
        answer=[ranked[0]["id"],ranked[1]["id"]]
        trials.append(trial("A2",form,t,{"rows":rows,"weights":list(range(1,9)),"select":2},
                            [r["id"] for r in rows],answer,"exact weighted ranking",{"top_scores":[ranked[0]["score"],ranked[1]["score"]]}))
    return package("A2",form,trials)


def a3(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        total=54+form+t; red=8+(form+t)%5; green=11+(2*form+t)%5; blue=total-red-green
        answer=chr(65+(form+2*t)%4)
        plans=[]
        for k in range(4):
            candidate={"id":chr(65+k),"red":red,"green":green,"blue":blue}
            if candidate["id"]!=answer: candidate[["red","green","blue"][k%3]]+=1+k
            plans.append(candidate)
        docs=[f"total={total}",f"red={red}",f"green={green}","blue > green"]
        trials.append(trial("A3",form,t,{"documents":docs,"plans":plans},[p["id"] for p in plans],answer,
                            "document constraint conjunction",{"required":{"total":total,"red":red,"green":green,"blue_gt_green":True}}))
    return package("A3",form,trials)


def a4(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        prior=Fraction(8+form+2*t,50); sensitivity=Fraction(65+3*((form+t)%6),100); false_positive=Fraction(10+2*((2*form+t)%6),100)
        posterior=sensitivity*prior/(sensitivity*prior+false_positive*(1-prior))
        answer="X" if posterior>Fraction(1,2) else "Y"
        trials.append(trial("A4",form,t,{"prior_x":str(prior),"sensitivity":str(sensitivity),"false_positive":str(false_positive)},
                            ["X","Y"],answer,"exact Bayes rule",{"posterior_x":f"{posterior.numerator}/{posterior.denominator}"}))
    return package("A4",form,trials)


GENERATORS={"A1":a1,"A2":a2,"A3":a3,"A4":a4}
