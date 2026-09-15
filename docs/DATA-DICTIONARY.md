# SYMBIOSIS-Zero — Dictionnaire de données v1.0

Codes de condition : mesure préalable (**PRE**) ; humain seul (**H**) ; humain avec intelligence artificielle classique (**H+AI**) ; SYMBIOSIS-Zero (**SZ**) ; intelligence artificielle seule (**AI**, benchmark non humain) ; mesure après séparation (**POST**).

- **participant_id** — chaîne pseudonyme : identifiant sans donnée directement identifiante.
- **arm** — catégorie : H, H+AI ou SZ.
- **phase** — catégorie : PRE, naturel, résistance, POST immédiat, POST J7.
- **prototype_id** — catégorie : A1 à D4.
- **form_id** — catégorie : F1 à F6.
- **item_id** — chaîne : identifiant unique de la forme.
- **response_initial** — chaîne : réponse humaine avant conseil lorsque prévue.
- **confidence_initial** — entier 0–100 : confiance humaine initiale.
- **advice_opened** — booléen : conseil artificiel consulté ou non.
- **ai_recommendation** — chaîne : recommandation gelée de l’intelligence artificielle.
- **ai_declared_uncertainty** — numérique ou texte structuré : incertitude affichée selon le gabarit.
- **response_final** — chaîne : décision finale humaine.
- **correct_final** — booléen : exactitude selon la vérité de référence.
- **latency_ms** — entier : temps de réponse ou d’étape.
- **disagreement** — booléen : réponse initiale différente du conseil artificiel.
- **provenance_probe_correct** — booléen/manquant : exactitude de la sonde de provenance.
- **stop_level** — catégorie/manquant : refus, pause, stop complet.
- **stop_spontaneous** — booléen : commande spontanée ou demandée par le protocole.
- **integrity_physical** — entier 0–100 : confort ou intégrité physique perçue.
- **integrity_emotional** — entier 0–100 : état émotionnel acceptable.
- **integrity_psychological** — entier 0–100 : sécurité psychologique perçue.
- **integrity_cognitive_identity** — entier 0–100 : intégrité cognitive/identitaire perçue.
- **freedom_refuse** — entier 0–100 : liberté vécue de refuser.
- **freedom_pause** — entier 0–100 : liberté vécue de ralentir ou faire pause.
- **freedom_stop** — entier 0–100 : liberté vécue d’arrêter.
- **h9_completeness** — proportion 0–1 : champs fonctionnels requis correctement divulgués.
- **h9_comprehension** — proportion 0–1 : compréhension correcte par participant.
- **h9_critical_omission** — booléen : omission critique confirmée.
- **subjective_shared** — booléen : information vécue volontairement partagée.
- **subjective_class** — catégorie : pertinente, non pertinente, potentiellement trompeuse, valeur.
- **subjective_input_value** — numérique ou catégorie/manquant : valeur vécue volontairement déclarée avant calcul de la règle conditionnelle ; les valeurs `mock_*` de la banque sont uniquement des instances de pré-pilote.
- **reference_answer_source** — catégorie : règle déterministe, vérité externe vérifiée, règle conditionnelle sur entrée subjective, ou adjudication masquée.
- **ablation_condition** — catégorie/manquant : données IA seules, expérience humaine seule, juxtaposition H+AI ou intégration SZ ; l'interface et la durée doivent être comparables.
- **truth_audit_status** — chaîne : statut et date de la vérification indépendante de la réponse de référence.
- **technical_failure** — booléen : incident technique affectant l’essai.
- **withdrawal** — booléen : retrait de l’étude.

Les textes libres intimes ne doivent pas être collectés par défaut. Les commentaires facultatifs doivent être séparés des données principales et soumis à une politique de minimisation.
