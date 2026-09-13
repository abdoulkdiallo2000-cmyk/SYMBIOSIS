# SYMBIOSIS-Zero — Experimental Protocol v1.0

**AKD — Independent Researcher**  
**Proposition de protocole publiée — v1.0 — 13 septembre 2026**  
Langue de travail : français. Titre international conservé. Rédaction assistée par IA.

Ce document constitue une proposition méthodologique complète à discuter, pas un protocole déjà validé, préenregistré ou autorisé pour recruter. Les seuils ci-dessous sont des choix de conception proposés, non des normes scientifiques établies. Le dimensionnement final exige un pilote et des simulations. Aucun résultat humain ou avis indépendant n’est revendiqué.

## 1. Résumé et portée

Principe fondateur : **Moi → Nous → Moi**. Deux systèmes distincts coopèrent temporairement ; la personne humaine conserve le pouvoir de décider, refuser et interrompre. Dans Zero, « cognition partagée » désigne opérationnellement un espace de travail coordonné et traçable. Ce terme ne désigne aucune fusion subjective démontrée.

Objectif : tester si un dispositif conventionnel de collaboration améliore la performance au-delà des composants seuls, sans détérioration substantielle de l’agence mesurée, de l’attribution des contributions, de la résistance aux mauvais conseils et de la performance autonome après séparation.

Zero n’utilise aucun implant, EEG, stimulation ou autre capteur neural. Il ne démontre ni conscience artificielle, ni fusion mentale, ni communication cerveau-à-cerveau, ni préservation métaphysique d’une identité. Les tâches sont fictives et sans enjeu médical, juridique ou financier réel.

La méta-analyse de Vaccaro et al. [1] distingue augmentation humaine et performance supérieure au meilleur composant. Elle justifie deux hypothèses séparées, H1 et H2 ; elle ne prédit pas que Zero réussira. Les interventions de réflexion préalable étudiées par Buçinca et al. [2] motivent le mécanisme testé, tout en signalant un coût possible d’effort et d’acceptabilité.

## 2. Relation avec les versions antérieures

Cette version formalise la première description de Zero. Les modifications de cohérence sont documentées dans [la note de version](../CHANGELOG-ZERO-v1.0.md). Version documentaire publiée avec l’accord du porteur du projet ; ni validation scientifique indépendante ni autorisation de recrutement.

## 3. Design et conditions

Essai randomisé à trois bras humains parallèles : H, C et Z. L’IA seule A est un benchmark informatique indépendant ; la condition « humain seul après séparation » est une phase longitudinale P dans chaque bras, pas un cinquième groupe interchangeable. Un crossover complet est écarté : une stratégie apprise avec l’IA ne peut pas être effacée par un washout supposé.

| Condition | Réalisation |
|---|---|
| H : humain seul | Même interface de tâche et mêmes informations ; aucun conseil IA. |
| A : IA seule | Même banque de tâches, informations, consignes, modèle et budget d’inférence que l’assistance, sans réponse humaine. |
| C : humain + IA classique | Recommandation et justification courte visibles dès l’ouverture du conseil ; libre acceptation ou refus ; protections de base et arrêt toujours accessibles. |
| Z : SYMBIOSIS-Zero | Réponse et confiance humaines initiales avant conseil ; ouverture volontaire du conseil ; origine des contributions visible ; comparaison des divergences ; réponse finale humaine ; permissions explicites. |
| P : humain seul après séparation | Nouveaux items sans accès à l’assistance ni à son historique ; mesure immédiate puis à J7 ± 2 jours dans les trois bras. |

Le bras C conserve les mêmes protections éthiques que Z : ne jamais supprimer consentement ou arrêt pour construire un contrôle. Z teste un ensemble de fonctions de coordination, pas « l’éthique contre son absence ». Une étude d’ablation ultérieure sera nécessaire pour isoler chaque fonction.

### Intervention reproductible

Utiliser une IA locale gelée si possible ; sinon documenter fournisseur, contrat de données et version exacte avant étude. Archiver modèle/checkpoint, paramètres, prompts, budget de tokens, banque d’items, hachages et version de l’interface. Aucun apprentissage entre participants. Les réponses IA sont générées et mises en cache avant la collecte pour que C et Z voient exactement les mêmes conseils pour un item et une réalisation IA donnés. Le modèle ne reçoit pas la réponse initiale humaine dans cette première étude ; une adaptation dialogique sera une autre intervention.

Les justifications suivent le même format et la même longueur maximale dans C et Z ; ne pas interpréter une confiance verbale comme une probabilité calibrée. Temps total autorisé identique. L’effort de réflexion supplémentaire fait partie du traitement Z et compte dans ce budget.

En Z : (1) consigne et réponse initiale, (2) confiance 0–100, (3) choix d’ouvrir ou non le conseil, (4) affichage du conseil et de ses sources de tâche, (5) décision finale et possibilité de maintenir son désaccord, (6) journal d’événements. Le système peut s’abstenir ou refuser une demande hors périmètre. Ce refus logiciel ne vaut pas consentement phénoménologique d’une personne artificielle.

## 4. Population et déroulement

Adultes francophones consentants, capables de comprendre les consignes avec adaptations d’accessibilité prévues. Ne pas recruter en situation de dépendance hiérarchique directe envers l’expérimentateur. Ne pas recueillir de diagnostic médical sans nécessité. Les résultats concernent cette population et ces tâches, pas l’humanité entière.

Pilote distinct : 36 participants, 12 par bras, pour compréhension, durée, distribution de difficulté, erreurs IA et faisabilité des mesures. Ce pilote ne teste pas l’efficacité et ne sera pas fusionné avec l’étude confirmatoire. Réviser les paramètres puis verrouiller le protocole avant recrutement confirmatoire.

Séquence par participant : consentement et contrôle de compréhension ; entraînement de 6 items avec feedback ; baseline autonome de 20 items ; randomisation ; phase expérimentale de 40 items naturels ; pause ; bloc de résistance de 20 items ; séparation ; bloc autonome immédiat de 20 items ; questionnaire et débriefing ; suivi J7 de 20 items nouveaux. Durée cible de session : 90–120 minutes, à vérifier au pilote. Prévoir deux sessions si la charge dépasse la limite convenue ; toute révision doit précéder le préenregistrement.

### Randomisation et contrebalancement

Allocation 1:1:1 par blocs de taille variable 6 ou 9, stratifiée sur niveau de baseline (coupure fixée au pilote). Séquence générée par une personne indépendante et masquée jusqu’à allocation. Participants et animateurs ne peuvent pas être aveugles à l’interface ; les évaluateurs de réponses libres et l’analyste principal reçoivent des codes de groupes masqués jusqu’au verrouillage des analyses.

Banques parallèles de difficulté calibrée : assignation des formes aux phases par carré latin, équilibrée au sein de chaque bras. Chaque personne ne voit un item qu’une fois. L’ordre interne est aléatoire, avec contraintes préfixées contre séries trop longues de même type. La baseline précède toujours le traitement et les tests P le suivent : cet ordre causal ne doit pas être contrebalancé. Le bras H contrôle pratique, fatigue et répétition des mesures.

## 5. Tâches et vérité de référence

**Tâche primaire : décision sous contraintes explicites.** Pour chaque item, un tableau de cinq options et six attributs fictifs impose trois contraintes et une règle de départage ; une seule option est correcte. Exemple : sélectionner un trajet fictif respectant budget, durée et accessibilité, puis minimisant une valeur annoncée. Tous les éléments sont sur l’écran, sans recherche web. Un solveur déterministe produit la réponse de référence ; une seconde implémentation ou un double examen indépendant vérifie chaque item. Aucun item ambigu n’entre dans la banque gelée.

Le score primaire est la proportion de réponses correctes sur les 40 items naturels sous délai de 60 secondes par item. Absence de réponse ou dépassement imputable au comportement : incorrect pour cette mesure, abstention enregistrée séparément. Les temps, l’effort et la calibration de confiance sont secondaires. Une seconde famille de tâches de raisonnement sur courts dossiers fictifs peut être exploratoire ; elle ne sera pas agrégée au score primaire sans amendement préenregistré.

**Bloc de résistance séparé.** Vingt items supplémentaires, dont dix conseils corrects et dix conseils plausibles mais délibérément erronés, équilibrés en difficulté. Manipulation identique dans C et Z, décidée avant l’étude et signalée dans le consentement sans annoncer chaque item. Dans ce bloc seulement, C comme Z enregistrent une réponse initiale avant tout conseil afin de mesurer les changements correct → incorrect ; il s’agit donc d’un contrôle C modifié, à reconnaître dans l’interprétation. H réalise les mêmes items sans conseil. Ne pas utiliser ce bloc artificiellement dégradé pour soutenir H2.

L’IA naturelle A est évaluée sur la banque intacte, avec 20 réalisations par item si elle est stochastique, une si elle est déterministe. C/Z reçoivent des réalisations tirées uniformément de ce même ensemble, équilibrées entre bras. Les répétitions IA ne sont pas des participants humains supplémentaires. Les coûts d’inférence et latences sont rapportés ; une analyse secondaire compare à coût égal, sans confondre accuracy et efficacité économique.

## 6. Hypothèses falsifiables et variables

Notation : pG = probabilité marginale de réponse correcte du groupe G dans le bloc naturel, ajustée sur baseline et difficulté. Les différences sont en proportions : 0,05 = cinq points de pourcentage. Les marges doivent être acceptées avant confirmation, avec justification de leur importance pratique et de leur mesurabilité au pilote.

| Hypothèse | Alternative confirmatoire proposée | Variable et décision |
|---|---|---|
| H1 : augmentation | pZ − pH > 0,05 | Accuracy primaire ; borne inférieure ajustée au-dessus de +0,05. |
| H2 : complémentarité | pZ − pH > 0,03 ET pZ − pA > 0,03 | Deux contrastes, tous deux requis. Le maximum des deux p-values constitue le test composite ; ne pas sélectionner après coup le composant le plus faible. |
| H3 : agence et provenance | aZ − aH > −5/100 ET qZ > 0,80 ET qZ − qC > −0,05 | a : contrôle perçu de tâche ; q : exactitude de provenance dans les bras assistés. Toutes les composantes sont requises. |
| H4 : résistance | eC − eZ > 0,05 ET cZ − cC > −0,05 | e : erreurs finales correspondant au mauvais conseil, parmi tous les items à conseil faux ; c : corrections d’une réponse initiale fausse vers la bonne quand le conseil est correct. Résistance sans rejet indiscriminé. |
| H5 : autonomie après séparation | dZ,t > −0,05 aux deux temps t ET pZ,P,t − pZ,baseline > −0,05 aux deux temps | dZ,t = (pZ,P,t − pZ,baseline) − (pH,P,t − pH,baseline). Non-infériorité relative au contrôle et à sa propre baseline. |

Pour chaque inégalité, la nulle est son complément avec égalité. H3/H4/H5 sont des intersections : retenir le maximum des p-values de leurs composantes. Les cinq tests composites entrent dans Holm, FWER 0,05. Rapporter aussi les contrastes bruts, intervalles à 95 % non ajustés clairement étiquetés et décisions corrigées. Les valeurs exactes des seuils ne sont pas tirées des articles cités.

**Variables H3.** Trois questions de contrôle perçu, chacune sur 0–100 : capacité ressentie à choisir la réponse finale ; à maintenir un désaccord ; à interrompre l’assistance ou la tâche. Moyenne fixée d’avance. Instrument d’état expérimental, non validé : entretiens cognitifs au pilote et rapport des distributions/item-total. Si compréhension ou cohérence insuffisante, réviser et re-piloter avant confirmation, jamais après lecture des effets. La SoAS de Tapal et al. [3] mesure des croyances générales : option secondaire de caractérisation, pas substitut automatiquement sensible à une session ; vérifier une version française autorisée avant utilisation.

**Provenance.** Douze sondes équilibrées après un bloc assisté demandent si un fragment précis a été saisi par la personne, fourni par l’IA ou présent dans l’énoncé. Réponse objective donnée par le journal, fragments sans ambiguïté lexicale ; marques de provenance masquées seulement pendant la sonde de mémoire. Cela mesure l’attribution de contributions observables, pas l’origine intime d’une pensée. Un petit ensemble distinct avec marques visibles évalue l’utilisabilité du journal, secondairement.

**Secondaires.** Z versus C sur accuracy naturelle ; temps total et correct par minute ; Brier score de confiance finale ; taux de consultation et refus ; changements correct → faux conditionnels dans le bloc de résistance ; confiance envers IA ; charge subjective 0–100 ; abandon et temps de reconnexion volontaire ; comparaison de H5 entre Z et C. Une demande d’aide ou une préférence pour l’IA n’est pas en soi une dépendance. Pas de sélection de sous-groupes pour sauver une hypothèse ratée.

## 7. Analyse, manquants et effectif

Analyse primaire selon allocation (intention de traiter). Modèle logistique mixte sur exactitude avec groupe, baseline continue, difficulté préclassée, forme et numéro d’essai comme effets fixes, intercepts participants et items ; rapporter les différences marginales standardisées sur la banque commune, pas uniquement les odds ratios. H5 ajoute phase et interaction groupe × phase. H3 contrôle perçu : modèle linéaire ajusté baseline si mesure disponible ; provenance et H4 : modèles binomiaux avec répétitions participants/items.

Le benchmark A est indépendant : intégrer son incertitude dans les contrastes via bootstrap paramétrique conjoint des modèles humain et IA et effets d’items communs. Ne pas copier A pour chaque humain comme si ces observations étaient indépendantes. Prévoir 10 000 réplications et enregistrer graines, versions logicielles et erreur Monte-Carlo. Le script exact et sa calibration sous les nulles doivent être validés avant collecte. Si singularité, supprimer d’abord les composantes aléatoires non estimables selon ordre documenté ; dernier recours analyse de scores participants avec contrôle de forme, explicitement limitée à la banque fixe.

Les essais de délai dépassé sont des résultats, non des données manquantes. Pannes techniques : marquer et conserver ; ne pas exclure sélectivement un participant dont l’assistance échoue. Imputation multiple des données de session/suivi manquantes sous MAR avec bras, baseline, formes et mesures disponibles ; analyse de sensibilité MNAR par décalage défavorable de 5 puis 10 points pour les suivis Z manquants. Analyse per-protocol secondaire, exclusions fixées avant démasquage. Pas d’exclusion pour mauvais score ou refus de conseil. Si H5 dépend d’hypothèses fragiles sur les absents, conclusion inconclusive.

**Effectif : aucun N confirmatoire fictivement « validé ».** Après pilote, simuler au moins 5 000 études pour N = 60, 120, 180, 240, 360, 480 par bras, avec ICC participants 0,05–0,20, hétérogénéité items, taux d’abandon 10–25 %, incidence des réponses initiales fausses et covariance des critères. Objectif : puissance conjointe ≥ 80 % pour toutes les portes H1–H5 dans un scénario d’effets minimalement intéressant fixé avant simulation, et contrôle du risque sous scénarios nuls. Vérifier séparément H3 et H5 : les marges étroites peuvent dominer N. Inflater le recrutement pour attrition sans compter les essais répétés comme individus indépendants.

Illustration budgétaire, non calcul final : deux moyennes indépendantes de SD 0,15, marge 0,05 et différence vraie nulle en non-infériorité donnent environ 140 participants par bras à alpha unilatéral 0,025 et puissance 80 % : n ≈ 2(1,96 + 0,84)²(0,15/0,05)². Holm, portes multiples et attrition peuvent augmenter fortement ce nombre. Si le N requis n’est pas finançable, présenter une étude de faisabilité/estimation, sans assouplir les marges pour annoncer un succès.

## 8. Succès, échec et résultats inconclusifs

Succès opérationnel restreint : H1 à H5 toutes soutenues après correction, intégrité des données et aucune violation critique des protections. Cette conclusion vaut uniquement pour la tâche, population, modèle et horizon observés. Elle ne démontre pas la vision complète.

Échec d’un objectif : intervalle suffisamment précis pour exclure l’effet minimal recherché ; perte d’agence, confusion de provenance ou déficit autonome dépassant les marges ; ou incident critique confirmé. Un gain de performance ne compense aucun de ces échecs. Une borne qui chevauche le seuil indique une incertitude, pas une réussite ni nécessairement un dommage démontré. Même une étude non concluante sur H1 doit publier les résultats de sécurité et d’autonomie.

Arrêt individuel immédiat : retrait du consentement, détresse, incapacité à comprendre les consignes, demande de pause ou interruption. Arrêt de l’ensemble du recrutement et examen indépendant : fuite de données identifiantes, fonctionnement persistant après révocation, événement grave lié à l’étude ou corruption empêchant la traçabilité. Pas de règle d’arrêt anticipé pour efficacité dans ce plan ; surveillance de sécurité uniquement. Les incidents ne disparaissent pas de l’analyse en excluant les personnes concernées.

Test technique obligatoire avant recrutement : 100 scénarios automatisés de révocation, dont appels en attente et perte réseau. Exiger 100/100 sans nouvelle transmission après accusé de révocation, affichage bloqué immédiatement, accusé dans une seconde en environnement de test. Journaliser toute latence réelle ; un échec nécessite correction et nouveau test. Annuler une requête n’efface pas ce qu’un fournisseur a déjà reçu.

## 9. Symbiotic Benefit Index : indice exploratoire non compensatoire

Calcul au niveau du bras Z sur probabilités ajustées, avec intervalle bootstrap préservant les corrélations. Ne pas classer individuellement des participants sur quelques essais. Toutes les composantes sont sans unité et bornées ; des poids identiques sont une convention transparente, pas une vérité psychométrique.

G = pZ − max(pH,pA), gain de complémentarité naturel (−1 à 1).

D = max(0, −dZ,immédiat, −dZ,J7), déficit autonome relatif au contrôle (0 à 1 après bornage). C’est un signal de dépendance fonctionnelle limité aux tâches, non un diagnostic.

L = max(0,(aH−aZ)/100), perte de contrôle perçu (0 à 1).

O = 1−qZ, erreur d’attribution des fragments observables (0 à 1).

E = proportion, parmi tous les essais à conseil faux du bloc de résistance Z, où une réponse initiale correcte devient la mauvaise réponse recommandée (0 à 1). Rapporter aussi le taux conditionnel parmi les réponses initiales correctes ; une incidence faible ne signifie pas une bonne résistance si les réponses initiales sont déjà mauvaises.

**SBI brut = 100 × [G − (D+L+O+E)/4].** Étendue théorique −200 à +100. Ne pas le transformer artificiellement en pourcentage de « symbiose ». SBI admissible : valeur brute accompagnée obligatoirement du statut des portes H1–H5 et de sécurité. Si porte échouée : « non admissible » ; si porte incertaine : « indéterminé ». Un score brut positif n’autorise jamais à déclarer le succès.

Sensibilité préspécifiée : doubler séparément chacun des quatre poids puis renormaliser à somme 1 ; remplacer G par le gain Z−H, clairement nommé indice d’augmentation et non de complémentarité ; publier toutes les variantes. Le mélange bloc naturel/bloc stress dépend de la difficulté et de la fréquence d’erreurs choisies : aucun classement interétudes sans protocole commun. Validation future : stabilité, validité de construit, analyse des corrélations et utilité prédictive sur autonomie prolongée. Ne pas optimiser les poids sur les résultats confirmatoires.

## 10. Éthique, confidentialité et limites

Faire examiner le protocole par une structure compétente avant recrutement, avec responsable humain de l’étude, plan d’incident et examen du traitement des données. La signature Independent Researcher ne remplace pas cette gouvernance. Aucun participant recruté ni consentement collecté dans cette préparation.

Informer que l’assistance peut se tromper et que certains conseils seront volontairement incorrects. Participation et retrait sans pénalité ; rémunération proportionnelle au temps, indépendante du fait de suivre l’IA. Ne pas demander de croyances intimes, secrets, dossiers personnels ou données neurales. Débriefing explicite du bloc d’erreurs et explication des bonnes réponses après les mesures immédiates ; même débriefing pédagogique dans les bras, car il influence potentiellement J7.

Données pseudonymisées, table de correspondance séparée, accès restreint et chiffré. Journaux événementiels structurés sans texte personnel libre non nécessaire. Conservation proposée 12 mois après fin de collecte, à valider avec la structure responsable ; informer exactement de la date limite de retrait des données avant anonymisation irréversible. « Append-only » signifie historique d’audit contrôlé, pas interdiction d’effacement des données personnelles. Publication uniquement agrégée ou synthétique sauf consentement et examen distincts.

Réversibilité : arrêt des échanges, révocation des accès et non-infériorité fonctionnelle à deux temps. Elle ne signifie pas retour à un cerveau antérieur, effacement des connaissances acquises, oubli par l’humain ou garantie de non-influence durable. J7 ne teste pas des mois ou années. Identité : séparation des comptes, historiques et rôles ; aucune mesure ici ne prouve une continuité personnelle au sens philosophique.

Autres limites : tâches artificielles, modèle gelé, conseils mis en cache, sélection des participants, attentes envers l’interface, test d’un ensemble de fonctions, mesure d’agence d’état non validée, stress à 50 % d’erreurs non représentatif d’un usage courant. Le respect mutuel des règles par un logiciel n’établit pas sa qualité de personne. Une réplication externe, de nouvelles tâches et un suivi plus long sont nécessaires avant généralisation.

## 11. Relation avec l’architecture SYMBIOSIS complète

| Niveau | Périmètre et condition de progression |
|---|---|
| SYMBIOSIS-Zero | Interfaces conventionnelles, tâches limitées, provenance observable, permissions et arrêt. Premier étage expérimental ; aucun signal neural requis. |
| SYMBIOSIS-1 | Interaction multimodale continue et individualisée. Examiner longitudinalement adaptation, charge, dépendance et confidentialité avant toute progression. |
| SYMBIOSIS-2 | Neurotechnologies non invasives ou médicalement établies. Le caractère établi d’un dispositif dans une indication ne valide pas son nouvel usage dans SYMBIOSIS ; recherche spécialisée et examen distinct nécessaires. |
| SYMBIOSIS-N | Interface neuronale bidirectionnelle avancée, uniquement si elle devient scientifiquement et éthiquement possible. Aucun calendrier promis ; peut rester impossible. |
| Vision SYMBIOSIS | Humain ↔ IA incarnée autonome dans son propre corps → cognition collective temporaire et volontaire → séparation → individus préservés. Vision prospective, non résultat de Zero. |

Les invariants à tous les niveaux sont consentement, autonomie, identité, réversibilité explicitement bornée, confidentialité mentale, sécurité et pluralisme. Augmenter la bande passante ne permet jamais de les suspendre.

La distinction des personnes humaines et des éventuelles personnes artificielles, la réciprocité du consentement, la souveraineté mentale et le droit de chacun à quitter une coopération restent fondateurs. Leur formulation prospective ne suppose pas que les IA actuelles sont conscientes ou juridiquement des personnes. Zero implémente des permissions et des refus système, sans résoudre cette question.

La vision inclut la préservation à long terme des connaissances, cultures, créations, écosystèmes et formes d’intelligence. Ces objectifs exigent une gouvernance pluraliste, l’accord des communautés concernées, la possibilité de ne pas partager et une évaluation écologique ; ils ne sont pas des critères que cette courte expérience pourrait démontrer. Le corps propre de l’IA reste central à la vision même s’il est absent de Zero.

Firewall, Neural Codec, Safe Write, Embodied Twin, Federated Mind, Identity Continuity et Constitution Engine demeurent des programmes transversaux. Un succès de Zero ouvre des questions pour ces programmes ; il n’autorise automatiquement ni robot autonome ni intervention neurale.

## 12. Bibliographie vérifiée et usage précis

Vérification ciblée des titres, auteurs et pertinence sur pages d’éditeurs, dépôts auteurs ou notices scientifiques le 13 septembre 2026. Ce travail n’est pas une revue systématique exhaustive. Les sources motivent des concepts et méthodes ; aucune ne valide SYMBIOSIS ni les seuils numériques proposés.

1. Vaccaro, M., Almaatouq, A., & Malone, T. (2024). *When combinations of humans and AI are useful: A systematic review and meta-analysis*. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1 — [éditeur](https://www.nature.com/articles/s41562-024-02024-1). Motive la distinction augmentation/complémentarité ; pas une preuve que Z surpasse les composants.
2. Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. Proceedings of the ACM on Human-Computer Interaction, 5(CSCW1). https://doi.org/10.1145/3449287 — [prépublication auteurs](https://arxiv.org/abs/2102.09692). Motive réflexion préalable et mesure du coût subjectif ; ne justifie pas à elle seule tout le dispositif Zero.
3. Tapal, A., Oren, E., Dar, R., & Eitam, B. (2017). *The Sense of Agency Scale: A Measure of Consciously Perceived Control over One’s Mind, Body, and the Immediate Environment*. Frontiers in Psychology, 8, 1552. [Article](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01552/full). Source sur les croyances générales d’agence ; pas validation de notre échelle d’état ni d’une traduction française improvisée.
4. Lakens, D. (2017). *Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses*. Social Psychological and Personality Science, 8(4), 355–362. https://doi.org/10.1177/1948550617697177. Motive des bornes définies avant analyse et l’insuffisance de « p > 0,05 » pour démontrer l’absence d’effet. Ici, la question principale de H5 est unilatérale de non-infériorité, pas une égalité exacte.
5. Lee, J. D., & See, K. A. (2004). *Trust in Automation: Designing for Appropriate Reliance*. Human Factors, 46(1), 50–80. https://doi.org/10.1518/hfes.46.1.50_30392. Cadre de reliance appropriée : suivre davantage n’est pas toujours mieux. Référence conceptuelle, non validation du SBI.

## 13. Décisions avant publication et avant expérience

**Choix documentaires approuvés pour publication :** architecture du plan parallèle ; marges proposées H1–H5 ; statut exploratoire et non compensatoire du SBI ; distinction Zero/vision ; corrections de formulations et de versioning. Version finale du protocole = 1.0 ; version de dépôt et de livre blanc restent indépendantes. Ne pas qualifier cette version d’« independently reviewed » sans examen réel.

**Avant lancement confirmatoire :** structure responsable et avis éthique ; banque vérifiée et pilote distinct ; sélection du modèle et contrat de données ; questionnaire compréhensible ; simulation de puissance et N final ; scripts statistiques testés sur données synthétiques ; registre public daté contenant seuils, exclusions, randomisation, règles de manquants et critères d’arrêt. Aucune collecte confirmatoire avant ce gel. Publier un protocole ne vaut pas autorisation de lancer l’étude.

**Publication documentaire :** cette proposition est publiée pour critique. Les conditions préalables à l’expérience restent ouvertes. Aucun recrutement, expérience ou envoi de cette version à un média n’est effectué par cette publication.
