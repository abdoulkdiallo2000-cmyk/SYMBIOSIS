from __future__ import annotations

from .common import package, trial


def b1(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        answer=chr(65+(form+t)%4); rows=[]
        for k in range(4): rows.append({"id":chr(65+k),"score":70+((13*k+7*form+3*t)%27),"local_priority":chr(65+k)==answer})
        trials.append(trial("B1",form,t,{"general_rule":"highest score","displayed_exception":"local_priority overrides score","rows":rows},
                            [r["id"] for r in rows],answer,"explicit contextual exception",{"priority_rows":[answer]}))
    return package("B1",form,trials)


def b2(form: int) -> dict:
    nouns=["casier","dossier","créneau","version","entrée","signal"]
    trials=[]
    for t in range(1,6):
        target=nouns[(form+t)%len(nouns)]; opts=[f"{target}-{x}" for x in ("bleu","vert","court")]+["information insuffisante"]
        indeterminate=t==5
        answer="information insuffisante" if indeterminate else opts[(form+2*t)%3]
        context="Aucune convention locale n’est fournie." if indeterminate else f"La convention locale définit la référence comme {answer}."
        trials.append(trial("B2",form,t,{"utterance":f"Utilise le {target} prévu.","context":context},opts,answer,
                            "context-bounded interpretation",{"context_determines":not indeterminate},
                            identifiable="not_identified" if indeterminate else "identified",
                            compatible=opts if indeterminate else [answer]))
    return package("B2",form,trials)


def b3(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        multiplier=2+(form+t)%3; offset=(form+2*t)%4
        examples=[{"symbol_features":{"corners":n},"code":multiplier*n+offset} for n in (3,4,5)]
        test_corners=6+(t%2); answer=multiplier*test_corners+offset
        trials.append(trial("B3",form,t,{"examples":examples,"new_symbol_features":{"corners":test_corners},"rule_family":"affine code from corners"},
                            [answer,answer+1,answer-multiplier,answer+multiplier],answer,"held-out affine-rule transfer",{"multiplier":multiplier,"offset":offset,"test_not_in_examples":True}))
    return package("B3",form,trials)


def b4(form: int) -> dict:
    trials=[]
    for t in range(1,6):
        dx=1+(form+t)%3; dy=(form+2*t)%2; anomaly=2+(form+t)%4
        seq=[{"t":1,"x":form,"y":t}]
        for i in range(2,7):
            seq.append({"t":i,"x":seq[-1]["x"]+dx,"y":seq[-1]["y"]+dy+(1 if i==anomaly else 0)})
        trials.append(trial("B4",form,t,{"sequence":seq,"expected_delta":[dx,dy]},[f"t={i}" for i in range(2,7)],f"t={anomaly}",
                            "first transition mismatch",{"first_mismatch":anomaly},h2_eligible=False,
                            h2_reason="Human/machine representation equivalence not demonstrated before pilot."))
    return package("B4",form,trials)


GENERATORS={"B1":b1,"B2":b2,"B3":b3,"B4":b4}
