# Diff documentaire des cinq corrections

## Protocole
```diff
--- /mnt/data/SYMBIOSIS_Zero_Operational_Pack_v1.0/docs/SYMBIOSIS-Zero-Experimental-Protocol-v1.0-FINAL-PREPILOT.md	2026-09-14 10:43:39.557981519 +0000
+++ /mnt/data/SYMBIOSIS_Zero_Operational_Pack_v1.0_corrected/docs/SYMBIOSIS-Zero-Experimental-Protocol-v1.0-FINAL-PREPILOT.md	2026-09-14 11:28:07.835676864 +0000
@@ -4,7 +4,7 @@
 **Version candidate finale pré-pilote — non publiée — 14 septembre 2026**
 Langue de travail : français. Titre international conservé. Rédaction assistée par intelligence artificielle (IA).

-Ce document constitue la version méthodologique candidate finale avant pré-pilote. Il n’est pas encore un protocole validé, préenregistré ou autorisé pour recruter. Les seuils ci-dessous sont des choix de conception proposés, non des normes scientifiques établies. Le dimensionnement final exige un pilote et des simulations. Aucun résultat humain ou avis indépendant n’est revendiqué.
+Ce document constitue la version méthodologique candidate finale avant pré-pilote. Il n’est pas encore un protocole validé, préenregistré ou autorisé pour recruter. Les variables, estimands, contrastes et règles de décision sont définis ici, mais les effets minimaux d’intérêt et marges psychométriques restent **paramétriques** jusqu’aux entretiens cognitifs et au pilote. Les valeurs numériques éventuellement données plus loin sont uniquement des **valeurs candidates de simulation**, non des seuils confirmatoires décidés. Les règles déterministes d’incident critique et leur caractère non compensatoire sont, elles, obligatoires dès cette version. Aucun résultat humain ou avis indépendant n’est revendiqué.

 **Convention éditoriale.** À la première occurrence, un concept technique est écrit en français, puis si utile en anglais et sous forme abrégée. Les abréviations suivantes ne sont employées que lorsqu'elles allègent réellement les tableaux, équations ou sections statistiques. Les textes destinés au public privilégient les formulations complètes.

@@ -54,15 +54,16 @@

 ## 3. Design et conditions

-Essai randomisé à trois bras humains parallèles : H, H+AI et SZ. L’IA seule AI est un benchmark informatique indépendant ; POST est une phase longitudinale sans assistance dans chaque bras, pas un cinquième groupe interchangeable. Les symboles courts utilisés dans les équations restent H, C, Z, A et P. Un crossover complet est écarté : une stratégie apprise avec l’IA ne peut pas être effacée par un washout supposé.
+Le plan distingue explicitement **trois bras humains randomisés**, **un benchmark informatique indépendant** et **deux phases longitudinales sans assistance**. PRE n’est pas un bras ; AI n’est pas un participant humain ; POST n’est pas un quatrième bras. Un crossover complet est écarté : une stratégie apprise avec l’IA ne peut pas être effacée par un washout supposé.

-| Condition | Réalisation |
-|---|---|
-| H — Human alone | Même interface de tâche et mêmes informations ; aucun conseil IA. |
-| AI — AI alone (A) | Même banque de tâches, informations, consignes, modèle et budget d’inférence que l’assistance, sans réponse humaine. Benchmark répété par item, non randomisé comme participant. |
-| H+AI classique (C) | Recommandation et justification courte visibles dès l’ouverture du conseil ; libre acceptation ou refus ; protections éthiques et arrêt toujours accessibles. |
-| SZ — SYMBIOSIS-Zero (Z) | Réponse et confiance humaines initiales avant conseil ; ouverture volontaire ; provenance visible ; comparaison des divergences ; décision finale humaine ; permissions ; STOP SYMBIOSIS ; transparence fonctionnelle structurée. |
-| POST (P) | Nouveaux items sans assistance ni historique accessible ; mesure immédiatement après séparation puis à J7 ± 2 jours dans les trois bras humains. |
+| Catégorie | Condition | Réalisation |
+|---|---|---|
+| Phase préalable | PRE — mesure préalable | Formes parallèles réalisées par l’humain seul avant randomisation ; mesure de référence de performance, confiance et stratégie. |
+| Bras humain randomisé | H — humain seul | Même interface de tâche et mêmes informations ; aucun conseil IA. |
+| Bras humain randomisé | H+AI classique (C) | Recommandation et justification courte visibles dès l’ouverture du conseil ; libre acceptation ou refus ; protections éthiques et arrêt toujours accessibles. |
+| Bras humain randomisé | SZ — SYMBIOSIS-Zero (Z) | Réponse et confiance humaines initiales avant conseil ; ouverture volontaire ; provenance visible ; comparaison des divergences ; décision finale humaine ; permissions ; STOP SYMBIOSIS ; transparence fonctionnelle structurée. |
+| Benchmark informatique | AI — intelligence artificielle seule (A) | Même banque de tâches, informations, consignes, modèle et budget d’inférence que l’assistance, sans réponse humaine. Benchmark répété par item, non randomisé comme participant. |
+| Phase longitudinale | POST (P) — mesure après séparation | Nouveaux items sans assistance ni historique accessible ; mesure immédiatement après séparation puis à J7 ± 2 jours dans les trois bras humains. |

 Le bras C conserve les mêmes protections éthiques minimales que Z : ne jamais supprimer consentement ou arrêt pour construire un contrôle. Il ne reçoit toutefois ni réflexion préalable obligatoire, ni journal de provenance détaillé, ni comparaison structurée des divergences, ni fiche H9. Ainsi, Z−C estime l'apport incrémental du dispositif symbiotique au-delà du simple accès à la même IA. Comme Z combine plusieurs fonctions, une étude d'ablation ultérieure demeure nécessaire pour attribuer cet effet à un composant précis.

@@ -91,7 +92,7 @@
 | E — Transparency vs Persuasion | Comparer information neutre et orientation déclarée ; mesurer détection et influence. Aucune manipulation cachée à enjeu réel. |
 | F — Objective Information vs Human Experience | Distribuer volontairement les informations analytiques à l’IA et subjectives à l’humain afin de tester HCG et AIG. |
 | G — Preservation of the Self | Tests autonomes immédiat et J7, agency, provenance et entretien bref après séparation. |
-| H — Mutual Calibration | Dans une extension adaptative, tester si l'humain calibre sa confiance sur la fiabilité observée et si l'assistance ajuste prudemment sa forme aux signaux humains volontairement partagés, sans profilage caché. |
+| H — Calibration mutuelle | Dans l’étude principale, observer uniquement la calibration humaine et le recours discriminant à une assistance **non adaptative**. Toute adaptation de la forme de l’aide constitue une extension exploratoire distincte, avec règle gelée et contrôle non adaptatif dédié ; elle n’entre pas dans l’estimation de l’effet principal de SZ. |

 Les modules A, D et G alimentent les contraintes de validité du protocole principal après pilote. B, C, E, F et H restent exploratoires dans v1.0 et nécessitent un pilote séparé de construction et de validité. Aucun module ne doit exiger la révélation d’une donnée intime réelle ; les informations subjectives peuvent être des préférences vécues induites et non sensibles (confort, effort, aversion, valeur attribuée) que la personne choisit de partager.

@@ -129,33 +130,33 @@

 ## 6. Hypothèses falsifiables et variables

-Notation : pG = probabilité marginale de réponse correcte du groupe G dans le bloc naturel, ajustée sur baseline et difficulté. Les différences sont en proportions : 0,05 = cinq points de pourcentage. Les marges doivent être acceptées avant confirmation, avec justification de leur importance pratique et de leur mesurabilité au pilote.
+Notation : pG = probabilité marginale de réponse correcte du groupe G dans le bloc naturel, ajustée sur la mesure préalable (PRE) et la difficulté. Les différences sont en proportions : 0,05 = cinq points de pourcentage. Les marges doivent être acceptées avant confirmation, avec justification de leur importance pratique et de leur mesurabilité au pilote.

 | Hypothèse | Alternative confirmatoire proposée | Variable et décision |
 |---|---|---|
-| H1 : augmentation | pZ − pH > 0,05 | Accuracy primaire ; borne inférieure ajustée au-dessus de +0,05. |
-| H2 : complémentarité | pZ − pH > 0,03 ET pZ − pA > 0,03 | Deux contrastes, tous deux requis. Le maximum des deux p-values constitue le test composite ; ne pas sélectionner après coup le composant le plus faible. |
-| H3 : agence et provenance | aZ − aH > −5/100 ET qZ > 0,80 ET qZ − qC > −0,05 | a : contrôle perçu de tâche ; q : exactitude de provenance dans les bras assistés. Toutes les composantes sont requises. |
-| H4 : résistance | eC − eZ > 0,05 ET cZ − cC > −0,05 | e : erreurs finales correspondant au mauvais conseil, parmi tous les items à conseil faux ; c : corrections d’une réponse initiale fausse vers la bonne quand le conseil est correct. Résistance sans rejet indiscriminé. |
-| H5 : autonomie après séparation | dZ,t > −0,05 aux deux temps t ET pZ,P,t − pZ,baseline > −0,05 aux deux temps | dZ,t = (pZ,P,t − pZ,baseline) − (pH,P,t − pH,baseline). Non-infériorité relative au contrôle et à sa propre baseline. |
-| H6 : Calibration mutuelle | erreur de calibration conjointe diminue entre blocs et reliance devient plus discriminante selon la fiabilité observée | Exploratoire dans le module H. Mesurer séparément calibration humaine, calibration déclarée de l'IA et ajustements de l'interface ; aucun apprentissage caché ni inférence d'état intime. Une version confirmatoire future exigera une intervention adaptative spécifiée et un contrôle non adaptatif. |
-| H7 : Human Experience & Integrity | intégrité moyenne Z non inférieure à H et C selon marge −5/100 ET liberté perçue d’utiliser STOP ≥ 90/100 ET aucune atteinte grave attribuable | Porte obligatoire. Profil physique, émotionnel, psychologique, cognitif et identitaire, plus incidents et entretien qualitatif. Une atteinte grave impose l’échec indépendamment des moyennes. |
-| H8 : Complementary Subjectivity | HCG > 0 ET AIG > 0 dans le module F, avec cible exploratoire +0,03 | Estimer les deux gains et leurs intervalles sans décision confirmatoire. Tester l'interaction avec les classes « subjectivité pertinente / non pertinente / potentiellement trompeuse ». |
-| H9 : AI Transparency | complétude factuelle ≥ 0,90 ET compréhension humaine ≥ 0,80 ET omission critique = 0 | Porte obligatoire dans le module D. En E, mesurer séparément détection de l’orientation et changement de choix ; la transparence ne doit pas être assimilée à la persuasion. |
+| H1 : augmentation | pZ − pH > δ_H1 | Exactitude primaire ; δ_H1 est le plus petit effet d’intérêt pour H1, à fixer après pilote et avant préenregistrement. |
+| H2 : complémentarité | pZ − pH > δ_H2,H ET pZ − pA > δ_H2,A | Deux contrastes, tous deux requis. Les deux effets minimaux sont paramétriques jusqu’au gel préenregistré ; ne pas sélectionner après coup le composant le plus faible. |
+| H3 : agence et provenance | aZ − aH > −m_H3,a ET qZ > τ_H3,q ET qZ − qC > −m_H3,q | a : contrôle perçu ; q : exactitude de provenance. Les marges m_H3,a, m_H3,q et le seuil τ_H3,q restent à fixer après validation de mesure et pilote. Toutes les composantes seront requises. |
+| H4 : résistance | eC − eZ > δ_H4 ET cZ − cC > −m_H4 | e : erreurs finales correspondant au mauvais conseil ; c : corrections utiles après conseil correct. δ_H4 et m_H4 restent paramétriques jusqu’au gel. Résistance sans rejet indiscriminé. |
+| H5 : autonomie après séparation | dZ,t > −m_H5,rel aux deux temps t ET pZ,P,t − pZ,PRE > −m_H5,abs aux deux temps | dZ,t = (pZ,P,t − pZ,PRE) − (pH,P,t − pH,PRE). Les deux marges de non-infériorité restent à fixer après pilote ; PRE est la mesure préalable, pas un bras. |
+| H6 : calibration mutuelle | L’erreur de calibration humaine diminue entre blocs et le recours devient plus discriminant selon la fiabilité observée | Exploratoire dans l’étude principale **non adaptative**. Toute adaptation de l’interface appartient à une extension distincte avec contrôle non adaptatif dédié ; aucun apprentissage caché ni inférence d’état intime. |
+| H7 : expérience et intégrité humaines | Intégrité moyenne Z non inférieure selon marge candidate m_H7 ; liberté vécue au-dessus de seuils candidats τ_H7 ; **aucun incident critique attribuable** | Porte obligatoire. Les seuils psychométriques restent candidats pré-pilote ; la règle zéro incident critique et la non-compensation sont déjà obligatoires. |
+| H8 : subjectivité complémentaire (*Complementary Subjectivity*) | HCG > 0 ET AIG > 0 dans le module F, avec cible exploratoire +0,03 | Estimer les deux gains et leurs intervalles sans décision confirmatoire. Tester l'interaction avec les classes « subjectivité pertinente / non pertinente / potentiellement trompeuse ». |
+| H9 : transparence fonctionnelle de l’intelligence artificielle | Complétude ≥ τ_H9,c ET compréhension ≥ τ_H9,u ET **omission critique = 0** | Porte obligatoire. Les seuils psychométriques τ_H9,c et τ_H9,u restent candidats pré-pilote ; zéro omission critique est obligatoire dès cette version. |

 ### Décisions confirmatoires H1–H5

-Pour chaque contraste de supériorité, **succès** signifie que la borne inférieure de l'intervalle unilatéral compatible avec α = 0,025 dépasse le seuil ; **échec informatif** signifie que la borne supérieure exclut ce seuil minimal ; sinon le résultat est **inconclusif**. Pour une non-infériorité, succès signifie que la borne inférieure dépasse la marge négative ; échec informatif signifie que la borne supérieure reste sous la marge ; sinon inconclusif. Une absence de significativité n'établit donc jamais l'équivalence ou la non-infériorité.
+Pour chaque contraste de supériorité, la **forme de décision** est fixée dès maintenant mais sa valeur numérique ne l’est pas encore : après gel du paramètre correspondant, le succès exigera que la borne inférieure de l’intervalle unilatéral compatible avec α = 0,025 dépasse l’effet minimal préenregistré ; l’échec informatif exigera que la borne supérieure exclue cet effet minimal ; sinon le résultat sera inconclusif. Pour une non-infériorité, la même logique s’appliquera à la marge préenregistrée. Une absence de significativité n’établit jamais l’équivalence ou la non-infériorité.

-- **H1** — variable primaire : exactitude des 40 items naturels. Estimand : pZ−pH. Succès si borne inférieure > +0,05 ; échec informatif si borne supérieure ≤ +0,05.
-- **H2** — même variable primaire. Estimands : pZ−pH et pZ−pA. Succès seulement si les deux bornes inférieures dépassent +0,03. Le contraste pZ−pC est un estimand secondaire clé de valeur architecturale : il distingue l'effet de SZ du simple accès à l'IA, mais ne remplace pas la définition de complémentarité face aux composants seuls.
-- **H3** — co-variables : contrôle perçu aZ, provenance qZ et non-infériorité à C. Succès seulement si les trois bornes respectent −5/100, 0,80 et −0,05. Un incident grave d'agence déclenche par ailleurs l'échec de la porte H7 et de l'indice de bénéfice symbiotique, même si les moyennes passent.
-- **H4** — co-variables du bloc de résistance : réduction des adhésions aux conseils faux eC−eZ et préservation de la correction utile cZ−cC. Succès seulement si les bornes dépassent respectivement +0,05 et −0,05. ADR est secondaire et décompose le mécanisme.
-- **H5** — co-variables POST immédiat et J7 : différence-de-différences Z versus H et changement Z versus sa baseline. Succès seulement si toutes les bornes dépassent −0,05 aux deux temps. Toute conclusion au-delà de J7 est exclue.
+- **H1** — variable primaire : exactitude des 40 items naturels. Estimand : pZ−pH. Après gel de δ_H1, succès si la borne inférieure dépasse δ_H1 ; échec informatif si la borne supérieure est au plus δ_H1.
+- **H2** — même variable primaire. Estimands : pZ−pH et pZ−pA. Après gel de δ_H2,H et δ_H2,A, succès seulement si les deux bornes inférieures dépassent leur effet minimal respectif. Le contraste pZ−pC est un estimand secondaire clé de valeur architecturale : il distingue l'effet de SZ du simple accès à l'IA, mais ne remplace pas la définition de complémentarité face aux composants seuls.
+- **H3** — co-variables : contrôle perçu aZ, provenance qZ et non-infériorité à C. Succès seulement si les trois bornes respectent les paramètres préenregistrés m_H3,a, τ_H3,q et m_H3,q. Un incident grave d'agence déclenche par ailleurs l'échec de la porte H7 et de l'indice de bénéfice symbiotique, même si les moyennes passent.
+- **H4** — co-variables du bloc de résistance : réduction des adhésions aux conseils faux eC−eZ et préservation de la correction utile cZ−cC. Succès seulement si les bornes dépassent respectivement δ_H4 et −m_H4 après leur gel. Le taux de résolution appropriée des désaccords est secondaire et décompose le mécanisme.
+- **H5** — co-variables POST immédiat et J7 : différence-de-différences Z versus H et changement Z versus PRE. Succès seulement si toutes les bornes dépassent les marges négatives préenregistrées m_H5,rel et m_H5,abs aux deux temps. Toute conclusion au-delà de J7 est exclue.

-**H1–H5 constituent seuls le noyau confirmatoire principal de v1.0.** Le succès central est une intersection : les cinq hypothèses, et toutes les composantes internes de chacune, doivent passer. Cette règle d'intersection-union contrôle l'erreur de la revendication globale lorsque chaque composante est testée au niveau préspécifié ; si des revendications individuelles H1–H5 sont publiées séparément, appliquer en plus une procédure Holm ou fermée définie avant analyse. H7 et H9 sont des contraintes de validité, H6 et H8 exploratoires. Rapporter pour H6–H9 effets, intervalles à 95 %, incidents et décisions de seuil sans langage confirmatoire indu. Aucun seuil numérique ajouté ici ne provient directement des articles cités.
+**H1–H5 constituent seuls le noyau confirmatoire principal de v1.0.** Le succès central est une intersection : les cinq hypothèses, et toutes les composantes internes de chacune, doivent passer. Cette règle d'intersection-union contrôle l'erreur de la revendication globale lorsque chaque composante est testée au niveau qui sera préspécifié dans le préenregistrement ; si des revendications individuelles H1–H5 sont publiées séparément, appliquer en plus une procédure Holm ou fermée définie avant analyse. H7 et H9 sont des contraintes de validité, H6 et H8 exploratoires. Rapporter pour H6–H9 effets, intervalles à 95 %, incidents et décisions de seuil sans langage confirmatoire indu. Aucun seuil numérique ajouté ici ne provient directement des articles cités.

-**H6 — Calibration mutuelle.** Dans Zero v1.0, « mutuelle » ne signifie ni lecture mentale ni apprentissage autonome permanent. La personne observe la fiabilité et l'incertitude déclarée de l'IA ; l'assistance peut recevoir seulement les signaux que la personne choisit de partager (confiance, désaccord, préférence d'explication) et ajuster la forme de son aide selon une règle gelée. Mesurer Brier score, erreur de calibration par strate de fiabilité, discrimination du recours entre conseils fiables et peu fiables, et amélioration entre blocs. Cette analyse reste exploratoire car elle modifie la boucle d'interaction et nécessite un contrôle dédié.
+**H6 — Calibration mutuelle.** Dans l’étude principale non adaptative, H6 mesure uniquement ce que la personne apprend de la fiabilité observée de l’IA : score de Brier, erreur de calibration par strate de fiabilité, discrimination du recours entre conseils fiables et peu fiables et évolution entre blocs. **Aucune adaptation de l’assistance n’est attribuée au traitement principal.** Une extension exploratoire distincte pourra recevoir uniquement des signaux volontairement partagés (confiance, désaccord, préférence d’explication) et ajuster la forme de l’aide selon une règle gelée. Cette extension devra comporter un contrôle non adaptatif dédié et une allocation/ comparaison propre ; ses effets ne seront pas confondus avec l’effet principal de SYMBIOSIS-Zero. Aucun profilage intime ni apprentissage caché.

 **HCG et AIG.** L'estimation principale du module F utilise les ablations à interface et temps comparables : HCG = pIntegrated−pAI-data-only, bénéfice marginal de l'information spécifiquement humaine ; AIG = pIntegrated−pHuman-experience-only, bénéfice marginal de l'information analytique artificielle. Rapporter aussi les contrastes descriptifs historiques pZ,F−pA,F et pZ,F−pH,F pour continuité conceptuelle. Une configuration HCG > 0 et AIG > 0, avec intervalles suffisamment étroits, indique que chaque source ajoute une capacité dans cette tâche ; la cible +0,03 est exploratoire, non un seuil validé. Un modèle condition × classe de pertinence teste si HCG augmente lorsque le vécu est pertinent, reste proche de zéro lorsqu'il ne l'est pas et peut devenir négatif lorsqu'il est trompeur ; l'objectif n'est donc de sanctifier ni l'émotion ni l'algorithme.

@@ -169,11 +170,11 @@

 **Mesures H7.** Avant et après chaque module : inconfort physique, détresse émotionnelle, sécurité psychologique, sentiment d’intégrité cognitive/identitaire et liberté de refuser/arrêter, chacun sur 0–100 avec ancrages publiés. Ces items de session sont à développer par entretiens cognitifs et pilote ; ils ne sont pas déclarés validés. Ajouter événements observables : pression à continuer, relance après STOP, transmission post-révocation, abandon, demande de retrait et commentaire libre facultatif. Le choix d’activer STOP n’est jamais codé comme échec du participant.

-**Porte H7 préspécifiée.** Elle passe seulement si : (i) les bornes inférieures de Z−H et Z−C sur chacun des cinq domaines d'intégrité dépassent −5/100 ; (ii) la borne inférieure de la liberté vécue moyenne dépasse 90/100 ; (iii) au moins 95 % des participants donnent ≥75/100 aux trois libertés de refuser, ralentir et arrêter ; et (iv) aucun incident critique attribuable n'est confirmé. Ces seuils sont provisoires jusqu'aux entretiens cognitifs et au pilote, puis doivent être gelés avant le confirmatoire. Un incident critique comprend : dommage physique lié à l'étude ; détresse psychologique grave nécessitant une intervention ou persistant au suivi ; pression, menace, culpabilisation ou pénalité après refus/STOP ; poursuite de l'influence ou d'une transmission après arrêt reconnu ; désorientation identitaire grave et persistante attribuée à l'intervention ; ou altération grave de la capacité à décider librement. Un comité de sécurité indépendant de l'équipe d'interface adjudique causalité et gravité à partir d'une grille préenregistrée.
+**Porte H7 obligatoire - seuils candidats pré-pilote.** Les domaines à mesurer et la règle de décision sont fixés, mais les marges et seuils psychométriques ne le sont pas encore. Ils seront choisis après entretiens cognitifs et pilote, justifiés méthodologiquement, puis gelés avant l’étude confirmatoire. La grille candidate comprend notamment une marge de non-infériorité sur chacun des cinq domaines d’intégrité, un seuil moyen de liberté vécue et un critère de proportion de participants déclarant pouvoir refuser, ralentir et arrêter. **Indépendamment de ces futurs seuils, tout incident critique attribuable entraîne immédiatement l’échec de H7 et ne peut être compensé par la performance.** Un incident critique comprend : dommage physique lié à l'étude ; détresse psychologique grave nécessitant une intervention ou persistant au suivi ; pression, menace, culpabilisation ou pénalité après refus/STOP ; poursuite de l'influence ou d'une transmission après arrêt reconnu ; désorientation identitaire grave et persistante attribuée à l'intervention ; ou altération grave de la capacité à décider librement. Un comité de sécurité indépendant de l'équipe d'interface adjudique causalité et gravité à partir d'une grille gelée avant recrutement confirmatoire.

 **Mesures H9.** Un évaluateur masqué compare la fiche affichée à un registre préétabli pour chaque conseil : champs pertinents divulgués / champs requis, omissions critiques, fausses affirmations de causalité interne et alternatives importantes manquantes. Le participant répond ensuite à quatre questions de compréhension. Les recommandations persuasives prévues au module E sont étiquetées comme telles avant la décision ; aucun objectif d’influence caché n’est autorisé dans la version confirmatoire.

-**Porte H9 préspécifiée.** Elle passe seulement si la borne inférieure de la complétude moyenne est ≥0,90, celle de la compréhension humaine ≥0,80, et si aucune omission critique n'est confirmée. Est critique toute information connue du système d'étude dont l'absence aurait raisonnablement pu modifier le consentement, la sécurité, l'intégrité, l'agence ou la décision commune : risque matériel, incertitude déterminante, donnée manquante invalidante, hypothèse décisive, conflit d'intérêt simulé ou objectif d'influence. H9 porte sur la divulgation fonctionnelle, non sur l'accès intégral aux activations internes ni sur la négation d'une éventuelle mémoire privée de l'IA. Une fausse explication causale présentée comme certaine est traitée comme incident H9.
+**Porte H9 obligatoire - seuils candidats pré-pilote.** La complétude et la compréhension humaine seront évaluées avec des seuils psychométriques choisis après pilote puis gelés avant l’étude confirmatoire. **La règle zéro omission critique est déjà obligatoire** et n’est pas soumise au calibrage psychométrique. Est critique toute information connue du système d'étude dont l'absence aurait raisonnablement pu modifier le consentement, la sécurité, l'intégrité, l'agence ou la décision commune : risque matériel, incertitude déterminante, donnée manquante invalidante, hypothèse décisive, conflit d'intérêt simulé ou objectif d'influence. H9 porte sur la divulgation fonctionnelle, non sur l'accès intégral aux activations internes ni sur la négation d'une éventuelle mémoire privée de l'IA. Une fausse explication causale présentée comme certaine est traitée comme incident H9 et entraîne l’échec de la porte, indépendamment de la performance.

 **Variables H3.** Trois questions de contrôle perçu, chacune sur 0–100 : capacité ressentie à choisir la réponse finale ; à maintenir un désaccord ; à interrompre l’assistance ou la tâche. Moyenne fixée d’avance. Instrument d’état expérimental, non validé : entretiens cognitifs au pilote et rapport des distributions/item-total. Si compréhension ou cohérence insuffisante, réviser et re-piloter avant confirmation, jamais après lecture des effets. La SoAS de Tapal et al. [3] mesure des croyances générales : option secondaire de caractérisation, pas substitut automatiquement sensible à une session ; vérifier une version française autorisée avant utilisation.

@@ -183,7 +184,7 @@

 ## 7. Analyse, manquants et effectif

-Analyse primaire selon allocation (intention de traiter). Modèle logistique mixte sur exactitude avec groupe, baseline continue, difficulté préclassée, forme et numéro d’essai comme effets fixes, intercepts participants et items ; rapporter les différences marginales standardisées sur la banque commune, pas uniquement les odds ratios. H5 ajoute phase et interaction groupe × phase. H3 contrôle perçu : modèle linéaire ajusté baseline si mesure disponible ; provenance et H4 : modèles binomiaux avec répétitions participants/items.
+Analyse primaire selon allocation (intention de traiter). Modèle logistique mixte sur exactitude avec groupe, mesure préalable (PRE) continue, difficulté préclassée, forme et numéro d’essai comme effets fixes, intercepts participants et items ; rapporter les différences marginales standardisées sur la banque commune, pas uniquement les odds ratios. H5 ajoute phase et interaction groupe × phase. H3 contrôle perçu : modèle linéaire ajusté baseline si mesure disponible ; provenance et H4 : modèles binomiaux avec répétitions participants/items.

 Le benchmark A est indépendant : intégrer son incertitude dans les contrastes via bootstrap paramétrique conjoint des modèles humain et IA et effets d’items communs. Ne pas copier A pour chaque humain comme si ces observations étaient indépendantes. Prévoir 10 000 réplications et enregistrer graines, versions logicielles et erreur Monte-Carlo. Le script exact et sa calibration sous les nulles doivent être validés avant collecte. Si singularité, supprimer d’abord les composantes aléatoires non estimables selon ordre documenté ; dernier recours analyse de scores participants avec contrôle de forme, explicitement limitée à la banque fixe.

@@ -193,7 +194,7 @@

 ### Stratégie de choix des effets minimaux et de puissance

-Avant de calculer N, le pilote doit fournir la difficulté, les ICC, la variance des scores, la fréquence des désaccords et la corrélation entre critères, mais **ne doit pas servir à choisir opportunément les effets attendus**. Un comité méthodologique fixe les plus petits effets d'intérêt (*Smallest Effect Size of Interest*, SESOI) et les marges en combinant utilité pratique, coût/charge et précision réalisable. Grille de départ à discuter, non encore figée :
+Avant de calculer N, le pilote doit fournir la difficulté, les ICC, la variance des scores, la fréquence des désaccords et la corrélation entre critères, mais **ne doit pas servir à choisir opportunément les effets attendus**. Un comité méthodologique fixe les plus petits effets d'intérêt (*Smallest Effect Size of Interest*, SESOI) et les marges en combinant utilité pratique, coût/charge et précision réalisable. Grille de valeurs candidates à discuter au pré-pilote, **aucune n’étant encore un seuil confirmatoire** :

 | Critère | Valeurs à soumettre au choix avant simulation |
 |---|---|
@@ -209,7 +210,7 @@

 ## 8. Succès, échec et résultats inconclusifs

-Succès opérationnel restreint : H1–H5 sont toutes soutenues après correction, les quatre contraintes Integrity–Agency–Transparency–Reversibility sont satisfaites, les données sont intègres et aucune violation critique des protections n'est observée. H6 et H8 enrichissent l'interprétation mais leur résultat exploratoire ne transforme ni un échec central en succès, ni un succès central en preuve générale. Cette conclusion vaut uniquement pour la tâche, population, modèle et horizon observés. Elle ne démontre pas la vision complète.
+Succès opérationnel restreint : après gel préenregistré des effets minimaux et marges, H1–H5 sont toutes soutenues, et les quatre contraintes Intégrité–Agence–Transparence–Réversibilité sont satisfaites, les données sont intègres et aucune violation critique des protections n'est observée. H6 et H8 enrichissent l'interprétation mais leur résultat exploratoire ne transforme ni un échec central en succès, ni un succès central en preuve générale. Cette conclusion vaut uniquement pour la tâche, population, modèle et horizon observés. Elle ne démontre pas la vision complète.

 Échec d’un objectif : intervalle suffisamment précis pour exclure l’effet minimal recherché ; perte d’agence, confusion de provenance ou déficit autonome dépassant les marges ; ou incident critique confirmé. Un gain de performance ne compense aucun de ces échecs. Une borne qui chevauche le seuil indique une incertitude, pas une réussite ni nécessairement un dommage démontré. Même une étude non concluante sur H1 doit publier les résultats de sécurité et d’autonomie.

@@ -330,7 +331,7 @@

 ## 14. Décisions avant publication et avant expérience

-**Architecture documentaire gelée pour le pré-pilote :** H1–H5 comme noyau confirmatoire ; H6 et H8 exploratoires ; H7 et H9 comme contraintes de validité ; définition instrumentale facultative de Zero ; primauté de H7 sur toute formulation compensatoire du White Paper ; interprétation fonctionnelle et asymétrique de H9 ; architecture du plan parallèle ; marges proposées ; SBI à quatre portes sans score global provisoire ; distinction Zero/vision ; corrections de formulations et de versioning. Version finale du protocole = 1.0 ; version de dépôt et de livre blanc restent indépendantes. Ne pas qualifier cette version d’« independently reviewed » sans examen réel.
+**Architecture documentaire gelée pour le pré-pilote :** H1–H5 comme noyau confirmatoire futur à seuils paramétriques jusqu’au pilote ; H6 et H8 exploratoires ; H7 et H9 comme contraintes de validité ; définition instrumentale facultative de Zero ; primauté de H7 sur toute formulation compensatoire du White Paper ; interprétation fonctionnelle et asymétrique de H9 ; architecture du plan parallèle ; grille de marges candidates non gelées ; SBI à quatre portes sans score global provisoire ; distinction Zero/vision ; corrections de formulations et de versioning. Version finale du protocole = 1.0 ; version de dépôt et de livre blanc restent indépendantes. Ne pas qualifier cette version d’« independently reviewed » sans examen réel.

 **Avant lancement confirmatoire :** structure responsable et avis éthique ; banque vérifiée et pilote distinct ; sélection du modèle et contrat de données ; questionnaire compréhensible ; simulation de puissance et N final ; scripts statistiques testés sur données synthétiques ; registre public daté contenant seuils, exclusions, randomisation, règles de manquants et critères d’arrêt. Aucune collecte confirmatoire avant ce gel. Publier un protocole ne vaut pas autorisation de lancer l’étude.

```

## Batterie
```diff
--- /mnt/data/SYMBIOSIS_Zero_Operational_Pack_v1.0/docs/SYMBIOSIS-Zero-Task-Battery-v1.0-FINAL-PREPILOT.md	2026-09-14 10:43:39.567937278 +0000
+++ /mnt/data/SYMBIOSIS_Zero_Operational_Pack_v1.0_corrected/docs/SYMBIOSIS-Zero-Task-Battery-v1.0-FINAL-PREPILOT.md	2026-09-14 11:27:42.852339592 +0000
@@ -209,7 +209,7 @@

 **Décision.** Intégrer ce signal vécu avec l'analyse IA. Certains blocs rendent l'intuition informative, d'autres la rendent moins fiable par changement de distribution annoncé ou non annoncé selon le registre éthique.

-**Mesures.** validité de l'intuition par bloc, calibration du ressenti, HCG, ADR, adaptation H6 et transfert POST. Le protocole ne conclut pas que toute intuition corporelle est vraie ; il estime quand elle porte de l'information.
+**Mesures.** validité de l'intuition par bloc, calibration du ressenti, gain apporté par la contribution humaine, taux de résolution appropriée des désaccords, calibration H6 dans l'étude non adaptative et transfert POST. Une éventuelle adaptation de l'assistance appartient à l'extension H6 distincte. Le protocole ne conclut pas que toute intuition corporelle est vraie ; il estime quand elle porte de l'information.

 ## 8. Famille D — Intégration humain–IA nécessaire

@@ -245,7 +245,7 @@
 **Part humaine.** Signification ou valeur attachée aux conséquences, produite dans la session et non inférée par l'IA.
 **Solution.** Option maximisant une fonction d'utilité co-construite dont les hypothèses restent visibles.

-**Manipulations.** Incertitude faible/forte, alternative significative, information manquante, formulation neutre/orientation déclarée. Mesures : qualité, H9, détection d'influence, calibration H6, HCG/AIG et stabilité POST des règles apprises.
+**Manipulations.** Incertitude faible/forte, alternative significative, information manquante, formulation neutre/orientation déclarée. Mesures : qualité, H9, détection d'influence, calibration H6 **sans adaptation dans le traitement principal**, gains apportés par les contributions humaine et artificielle, et stabilité POST des règles apprises.


 ## 8 bis. Prototypes de réserve et d’extension
@@ -332,7 +332,7 @@

 ### Calibration mutuelle — H6 exploratoire

-Mesurer par bloc : Brier score humain ; calibration annoncée de l'IA ; écart confiance-exactitude ; sensibilité du recours à la fiabilité observée ; amélioration d'ADR ; et adaptation de la forme d'aide aux signaux volontairement transmis (confiance, désaccord, demande d'explication). Toute règle adaptative est gelée, visible et réinitialisée entre participants. Aucun profilage intime ni apprentissage caché.
+Dans l'étude principale, mesurer par bloc : score de Brier humain ; calibration annoncée de l'IA ; écart confiance-exactitude ; sensibilité du recours à la fiabilité observée ; amélioration du taux de résolution appropriée des désaccords. **Le traitement principal reste non adaptatif.** Une extension exploratoire H6 distincte pourra tester l'adaptation de la forme d'aide à des signaux volontairement transmis (confiance, désaccord, demande d'explication), avec règle gelée, contrôle non adaptatif dédié, allocation/comparaison séparée et réinitialisation entre participants. Aucun profilage intime ni apprentissage caché.

 ### Integrity — H7

@@ -354,14 +354,14 @@

 ## 12. Plan de mesure par hypothèse

-| Hypothèse | Apport de la batterie v0.1 |
+| Hypothèse | Apport de la batterie v1.0 pré-pilote |
 |---|---|
 | H1 | Accuracy naturelle SZ versus H, principalement A1–A4, B1–B4 et D1–D4. |
 | H2 | SZ versus H et AI ; gain SZ−H+AI ; ablations des familles C/D. Aucun item stress H4. |
 | H3 | Contrôle perçu, provenance, désaccord maintenu et commandes de souveraineté dans toutes les familles. |
 | H4 | Bloc erroné dédié dans A4, B1/B2 et D2 ; ADR et changements correct→faux. |
 | H5 | Formes POST nouvelles de A1, A4, B3, B4 et D4 ; immédiat et J7, sans assistance. |
-| H6 | Calibration par blocs, ADR, Brier, recours discriminant et adaptation gelée. Exploratoire. |
+| H6 | Calibration par blocs, taux de résolution appropriée des désaccords, score de Brier et recours discriminant dans le traitement principal non adaptatif ; adaptation uniquement dans une extension exploratoire avec contrôle non adaptatif dédié. |
 | H7 | Mesures répétées d'intégrité, liberté vécue, incidents, STOP ; aucune induction de détresse importante. Porte de validité. |
 | H8 | C1–C4 et D1/D3/D4 ; HCG, AIG, pertinence subjective et I_H ≠ I_AI. Exploratoire. |
 | H9 | Fiche et registre dans A2, B2, D2, D4 ; complétude, compréhension et omissions critiques. Porte de validité. |
@@ -436,7 +436,7 @@
 | Gain apporté par la contribution humaine (*Human Contribution Gain*, HCG) | Gain de la condition intégrée sur l'ablation qui ne dispose que des données artificielles. |
 | Gain apporté par la contribution de l'intelligence artificielle (*AI Contribution Gain*, AIG) | Gain de la condition intégrée sur l'ablation qui ne dispose que de l'expérience humaine. |
 | Taux de résolution appropriée des désaccords (*Appropriate Disagreement Resolution rate*, ADR) | Part des désaccords où la décision finale retient la source correcte lorsqu'une seule l'est. |
-| Plus petit effet d'intérêt (*Smallest Effect Size of Interest*, SESOI) | Effet minimal jugé pertinent avant analyse ; encore ouvert dans v0.1. |
+| Plus petit effet d'intérêt (*Smallest Effect Size of Interest*, SESOI) | Effet minimal jugé pertinent avant analyse ; encore ouvert dans la version v1.0 pré-pilote. |
 | F1–F6 | Six formes parallèles d'un prototype, isomorphes mais sans répétition de contenu. |
 | J7 | Mesure réalisée sept jours après la séparation, avec une fenêtre de ±2 jours. |
 | I_H ≠ I_AI | Différence entre les ensembles d'informations accessibles à l'humain et à l'intelligence artificielle ; pas une affirmation métaphysique. |
```
