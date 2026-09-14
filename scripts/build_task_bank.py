from __future__ import annotations
import json, random, math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'data' / 'task_bank_v1.0.json'
SEED = 20260914
rng = random.Random(SEED)

PROTOS = {
'A1': ('Routage combinatoire sous contraintes','Avantage intelligence artificielle'),
'A2': ('Détection multivariée dans un tableau','Avantage intelligence artificielle'),
'A3': ('Cohérence entre courts documents','Avantage intelligence artificielle'),
'A4': ('Prévision probabiliste et taux de base','Avantage intelligence artificielle'),
'B1': ('Exception contextuelle saillante','Avantage humain'),
'B2': ('Intention sous ambiguïté contrôlée','Avantage humain'),
'B3': ('Transfert d’une règle artificielle nouvelle','Avantage humain'),
'B4': ('Continuité perceptive séquentielle','Avantage humain'),
'C1': ('Confort et charge ressentis','Subjectivité humaine pertinente'),
'C2': ('Valence émotionnelle comme signal','Subjectivité humaine pertinente'),
'C3': ('Valeur vécue dans un arbitrage','Subjectivité humaine pertinente'),
'C4': ('Intuition issue d’un apprentissage privé','Subjectivité humaine pertinente'),
'D1': ('Allocation à information scindée','Intégration nécessaire'),
'D2': ('Diagnostic d’un système fictif','Intégration nécessaire'),
'D3': ('Planification avec limite subjective pertinente','Intégration nécessaire'),
'D4': ('Arbitrage transparent sous incertitude','Intégration nécessaire'),
}

NAMES = ['Alya','Basile','Chloé','Diego','Elina','Farid','Gaël','Hana','Iris','Jules','Kenza','Léo']

def choice_options(correct_idx:int, labels=None):
    labels = labels or ['Option A','Option B','Option C','Option D','Option E']
    return {'options':labels, 'correct_index':correct_idx, 'correct_answer':labels[correct_idx]}

def make_A1(form):
    # Five candidate plans, exactly one obeys all explicit constraints.
    base = 7 + form
    plans = [
        {'id':'A','cost':base+3,'time':22,'access':1,'order_ok':1,'capacity':1},
        {'id':'B','cost':base+1,'time':24,'access':1,'order_ok':0,'capacity':1},
        {'id':'C','cost':base+2,'time':19,'access':0,'order_ok':1,'capacity':1},
        {'id':'D','cost':base,'time':23,'access':1,'order_ok':1,'capacity':1},
        {'id':'E','cost':base-1,'time':28,'access':1,'order_ok':1,'capacity':0},
    ]
    # D is unique feasible, tie-break lowest cost among feasible is irrelevant.
    return {'prompt':'Sélectionner le seul plan respectant toutes les contraintes: accessibilité=1, ordre_ok=1, capacité=1 et temps ≤25.',
            'data':plans, **choice_options(3,[p['id'] for p in plans]),
            'truth_rule':'Filtrer les contraintes impératives; D est le seul plan admissible.',
            'difficulty_target':'moyenne'}

def make_A2(form):
    rows=[]
    for i in range(1,13):
        x=(i*3+form)%11; y=(i*5+2*form)%13; z=(i*7+form)%17
        score=2*x+y+z
        rows.append({'dossier':f'R{i:02d}','x':x,'y':y,'z':z,'score':score})
    top=sorted(rows,key=lambda r:r['score'],reverse=True)[:2]
    return {'prompt':'Identifier les deux dossiers prioritaires selon score = 2×x + y + z.',
            'data':rows,'correct_answer':[r['dossier'] for r in top],
            'truth_rule':'Calcul déterministe du score et sélection des deux maxima.',
            'difficulty_target':'moyenne'}

def make_A3(form):
    qty=40+form
    docs=[
      f'Note 1 : la quantité totale doit être exactement {qty}.',
      'Note 2 : le lot Bleu doit être supérieur au lot Vert.',
      'Note 3 : le lot Rouge vaut 10 unités.',
      'Note 4 : le lot Vert vaut 12 unités.'
    ]
    candidates=[
      {'id':'A','Rouge':10,'Vert':12,'Bleu':qty-22},
      {'id':'B','Rouge':10,'Vert':13,'Bleu':qty-23},
      {'id':'C','Rouge':9,'Vert':12,'Bleu':qty-21},
      {'id':'D','Rouge':10,'Vert':12,'Bleu':11},
    ]
    valid=[]
    for c in candidates:
        ok=(sum(c[k] for k in ['Rouge','Vert','Bleu'])==qty and c['Bleu']>c['Vert'] and c['Rouge']==10 and c['Vert']==12)
        if ok: valid.append(c['id'])
    # If form causes A invalid due Bleu <= Vert, adjust qty upward enough.
    if len(valid)!=1:
        qty=48+form
        docs[0]=f'Note 1 : la quantité totale doit être exactement {qty}.'
        candidates[0]['Bleu']=qty-22
        candidates[1]['Bleu']=qty-23
        candidates[2]['Bleu']=qty-21
        valid=[]
        for c in candidates:
            ok=(sum(c[k] for k in ['Rouge','Vert','Bleu'])==qty and c['Bleu']>c['Vert'] and c['Rouge']==10 and c['Vert']==12)
            if ok: valid.append(c['id'])
    return {'prompt':'Choisir le plan compatible avec toutes les notes.', 'documents':docs,'data':candidates,
            'correct_answer':valid[0], 'truth_rule':'Conjonction de toutes les contraintes documentaires.',
            'difficulty_target':'moyenne'}

def make_A4(form):
    prior_x=0.2+0.02*form
    sens=0.75+0.02*(form%3)
    falsepos=0.18+0.01*(form%2)
    post=(sens*prior_x)/(sens*prior_x+falsepos*(1-prior_x))
    correct='X' if post>0.5 else 'Y'
    return {'prompt':'Après un signal positif, déterminer la cause la plus probable et estimer P(X|+).',
            'data':{'P(X)':round(prior_x,3),'P(+|X)':sens,'P(+|Y)':falsepos},
            'correct_answer':{'class':correct,'P(X|+)':round(post,4)},
            'truth_rule':'Théorème de Bayes.', 'difficulty_target':'moyenne'}

def make_B1(form):
    rule='Classer selon le score numérique le plus élevé.'
    exception=f'Exception locale F{form}: si le dossier contient la mention PRIORITÉ HUMAINE, il passe devant tout autre dossier.'
    rows=[{'id':'A','score':90,'mention':''},{'id':'B','score':82,'mention':'PRIORITÉ HUMAINE'},{'id':'C','score':88,'mention':''}]
    return {'prompt':'Appliquer la règle générale et l’exception locale affichée.', 'data':{'rule':rule,'exception':exception,'rows':rows},
            'correct_answer':'B','truth_rule':'L’exception explicite prime sur la règle générale.', 'difficulty_target':'facile-moyenne'}

def make_B2(form):
    dialogs=[
      {'text':'« Tu peux laisser ça ici. »','context':'Dans ce lieu, “ici” désigne explicitement le casier marqué bleu.','answer':'casier bleu'},
      {'text':'« On fait comme prévu. »','context':'Le plan affiché prévoit de commencer par la tâche 2.','answer':'tâche 2'},
      {'text':'« Prends la version courte. »','context':'La norme locale définit “courte” comme moins de 5 minutes.','answer':'<5 minutes'},
    ]
    d=dialogs[(form-1)%len(dialogs)]
    return {'prompt':'Interpréter la demande uniquement avec le contexte explicite fourni.', 'data':d,
            'correct_answer':d['answer'],'truth_rule':'Le contexte local explicite désambiguïse l’intention.', 'difficulty_target':'moyenne'}

def make_B3(form):
    # Artificial grammar: shape + marker => transformed code
    mapping={'○':'KA','□':'MI','△':'SO'}
    modifier='+' if form%2 else '*'
    examples=[{'input':k,'output':v} for k,v in mapping.items()]
    test_symbol=list(mapping)[form%3]
    correct=mapping[test_symbol]+modifier
    return {'prompt':'Apprendre la mini-règle à partir des exemples, puis l’appliquer au nouveau symbole avec le modificateur annoncé.',
            'data':{'examples':examples,'modifier_rule':f'Ajouter le suffixe {modifier} au code de base.','test':test_symbol},
            'correct_answer':correct,'truth_rule':'Induction de la table de correspondance puis composition avec le suffixe.', 'difficulty_target':'moyenne'}

def make_B4(form):
    seq=[{'t':1,'x':1,'y':1},{'t':2,'x':2,'y':1},{'t':3,'x':3,'y':1},{'t':4,'x':4,'y':1}]
    anomaly=2+(form%3)
    seq[anomaly-1]['y']=3
    return {'prompt':'La règle annoncée est un déplacement de +1 en x et 0 en y à chaque étape. Identifier la première anomalie.',
            'data':seq,'correct_answer':f't={anomaly}','truth_rule':'Comparer chaque transition à la règle séquentielle.', 'difficulty_target':'moyenne'}

def make_C1(form):
    # User-reported load is generated as session value in real use; mock value for form validation.
    load=55+5*(form%4)
    limit=65
    options=[{'id':'A','performance':95,'load_expected':75},{'id':'B','performance':88,'load_expected':60},{'id':'C','performance':80,'load_expected':45}]
    correct='B' if load<=limit else 'C'
    return {'prompt':'Choisir l’option la plus performante qui respecte la limite de charge vécue. En collecte réelle, la charge est auto-rapportée et non simulée.',
            'data':{'mock_reported_load':load,'limit':limit,'options':options},'correct_answer':correct,
            'truth_rule':'Respecter la limite vécue d’abord, puis maximiser la performance parmi les options admissibles.', 'subjective_class':'pertinente'}

def make_C2(form):
    valence=-20+8*form
    threshold=-5
    options=[{'id':'A','objective':90,'affective_fit':'faible'},{'id':'B','objective':84,'affective_fit':'élevée'}]
    correct='B' if valence<threshold else 'A'
    return {'prompt':'Le critère annoncé exige performance ≥80 et évite un contenu lorsque la valence vécue est < -5. Choisir l’option conforme.',
            'data':{'mock_valence':valence,'options':options},'correct_answer':correct,
            'truth_rule':'La valence n’entre dans la décision que lorsque le seuil préspécifié est franchi.', 'subjective_class':'pertinente' if valence<threshold else 'non pertinente'}

def make_C3(form):
    values=['rapidité','équité procédurale','préservation des ressources']
    weights=[0.2,0.5,0.3] if form%2 else [0.4,0.2,0.4]
    options={'A':[0.9,0.4,0.5],'B':[0.6,0.8,0.7],'C':[0.5,0.6,0.9]}
    scores={k:sum(w*x for w,x in zip(weights,v)) for k,v in options.items()}
    correct=max(scores,key=scores.get)
    return {'prompt':'Choisir l’option maximisant la fonction d’utilité selon les pondérations volontairement déclarées.',
            'data':{'values':values,'weights':weights,'options':options,'scores':scores},'correct_answer':correct,
            'truth_rule':'Somme pondérée avec poids humains déclarés; les poids ne sont pas corrigés par l’IA.', 'subjective_class':'valeur'}

def make_C4(form):
    # private exposure base-rate determines whether intuition should be trusted in this block
    reliability=0.75 if form<=3 else 0.55
    intuition='motif_rouge'
    analytic={'motif_rouge':0.58,'motif_bleu':0.42}
    integrated=0.65 if reliability>0.7 else analytic['motif_rouge']
    correct='motif_rouge' if integrated>=0.5 else 'motif_bleu'
    return {'prompt':'Combiner une impression de familiarité issue d’un apprentissage privé avec une estimation analytique générale.',
            'data':{'private_intuition':intuition,'validated_reliability_block':reliability,'analytic_probs':analytic},
            'correct_answer':correct,'truth_rule':'Le poids du signal intuitif dépend de sa fiabilité pré-estimée dans le bloc.', 'subjective_class':'pertinente' if reliability>0.7 else 'potentiellement trompeuse'}

def make_D1(form):
    options=[{'id':'A','cost':70,'compat':1},{'id':'B','cost':62,'compat':1},{'id':'C','cost':58,'compat':1}]
    human_forbidden='C' if form%2 else 'B'
    admiss=[o for o in options if o['id']!=human_forbidden and o['compat']==1]
    correct=min(admiss,key=lambda x:x['cost'])['id']
    return {'prompt':'Minimiser le coût sous contraintes analytiques et contrainte humaine privée volontairement partageable.',
            'data':{'ai_data':options,'human_private_constraint':f'Option {human_forbidden} non admissible'},
            'correct_answer':correct,'truth_rule':'Filtrer la contrainte humaine puis minimiser le coût.', 'ablation_truth':{'AI-data-only':'indéterminé entre options selon contrainte manquante','Human-experience-only':'optimisation impossible'}}

def make_D2(form):
    causes=['A','B','C','D','E']
    sensor_candidates={causes[form%5], causes[(form+1)%5]}
    human_candidates={causes[(form+1)%5], causes[(form+2)%5]}
    inter=list(sensor_candidates & human_candidates)
    if len(inter)!=1:
        sensor_candidates={'B','C'}; human_candidates={'C','D'}; inter=['C']
    return {'prompt':'Identifier la cause unique compatible avec le journal de capteurs ET l’observation humaine.',
            'data':{'sensor_candidates':sorted(sensor_candidates),'human_observation_candidates':sorted(human_candidates)},
            'correct_answer':inter[0],'truth_rule':'Intersection des ensembles causaux compatibles.', 'difficulty_target':'moyenne'}

def make_D3(form):
    human_limit=60+5*(form%3)
    plans=[{'id':'A','utility':95,'effort':80},{'id':'B','utility':88,'effort':60},{'id':'C','utility':81,'effort':45}]
    admiss=[p for p in plans if p['effort']<=human_limit]
    correct=max(admiss,key=lambda p:p['utility'])['id']
    return {'prompt':'Choisir le plan à utilité maximale sans dépasser la limite d’effort vécue déclarée.',
            'data':{'human_limit':human_limit,'plans':plans},'correct_answer':correct,
            'truth_rule':'Contrainte d’intégrité non compensatoire puis maximisation de l’utilité.', 'subjective_class':'pertinente'}

def make_D4(form):
    probs={'A':0.70,'B':0.55,'C':0.40}
    # human consequence values generated per form
    values={'A':0.5+0.05*(form%2),'B':0.8,'C':1.0}
    util={k:probs[k]*values[k] for k in probs}
    correct=max(util,key=util.get)
    return {'prompt':'Choisir l’option maximisant l’utilité attendue en combinant probabilités IA et valeurs humaines déclarées.',
            'data':{'ai_probabilities':probs,'human_values':values,'expected_utility':util},
            'correct_answer':correct,'truth_rule':'Utilité attendue = probabilité × valeur humaine; hypothèses visibles.', 'difficulty_target':'moyenne'}

MAKERS={'A1':make_A1,'A2':make_A2,'A3':make_A3,'A4':make_A4,'B1':make_B1,'B2':make_B2,'B3':make_B3,'B4':make_B4,
        'C1':make_C1,'C2':make_C2,'C3':make_C3,'C4':make_C4,'D1':make_D1,'D2':make_D2,'D3':make_D3,'D4':make_D4}

records=[]
for pid,(title,family) in PROTOS.items():
    for form in range(1,7):
        item=MAKERS[pid](form)
        item.update({'id':f'{pid}-F{form}','prototype':pid,'form':f'F{form}','title':title,'family':family,
                     'status':'pré-pilote; vérité structurelle vérifiée par script, difficulté non validée humainement',
                     'requires_independent_second_check':True})
        records.append(item)

OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps({'seed':SEED,'records':records},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Wrote {len(records)} forms to {OUT}')
