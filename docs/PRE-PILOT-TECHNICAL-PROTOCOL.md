# SYMBIOSIS-Zero — Pré-pilote technique v1.0

## But

Vérifier l’implémentation avant tout recrutement : solveurs, formes parallèles, cache des réponses de l’intelligence artificielle, journaux, provenance, fiche de transparence et STOP SYMBIOSIS.

## Conditions de passage

Le pré-pilote technique doit réussir intégralement avant recrutement humain. Un échec entraîne correction puis répétition complète de la famille de tests concernée.

## Tests obligatoires

### Banque de tâches

- 16 prototypes × 6 formes = 96 formes uniques.
- Identifiant unique et vérité de référence présente pour chaque forme.
- Deux vérifications de la vérité de référence avant gel, dont une indépendante du générateur pour chaque famille.
- Aucun item réel médical, juridique ou financier.
- Aucun contenu intime réel nécessaire.

### Reproductibilité

- Graine documentée pour toute génération pseudo-aléatoire.
- Version du générateur, du solveur, des prompts et du modèle archivée.
- Les conseils de l’intelligence artificielle utilisés dans H+AI et SYMBIOSIS-Zero doivent être identiques pour une même forme lorsque le protocole l’exige.

### Journaux

Chaque essai doit enregistrer au minimum : participant pseudonyme, bras, item, forme, temps, réponse initiale, confiance, conseil artificiel, ouverture/refus, réponse finale, provenance consultée, commande de souveraineté, champs de transparence affichés et erreur technique éventuelle.

### STOP SYMBIOSIS

Exécuter au moins 100 scénarios automatisés comprenant : requête inactive, requête en attente, latence artificielle, pause, reprise, perte simulée de réseau et arrêt complet. Exiger : accusé local ≤ 1 seconde dans l’environnement de test, révocation de session, aucune nouvelle transmission après accusé, impossibilité de reprendre sans nouvelle session et journal d’événement complet.

Le script `scripts/technical_stop_test.py` est seulement un test de machine à états. Il ne remplace pas le test de l’interface et du fournisseur réellement déployés.

### Transparence fonctionnelle

Pour chaque conseil destiné à la condition SYMBIOSIS-Zero, construire un registre de vérité avec : informations utilisées, incertitudes importantes, hypothèses déterminantes, alternatives significatives, risques, limites, données manquantes et éventuelle orientation. Vérifier automatiquement que tous les champs requis sont présents, puis vérifier manuellement un échantillon de 100 % des items critiques H9.

## Critère de sortie

Créer un rapport daté avec versions, hachages, tests exécutés, échecs, corrections et preuve de réussite. Aucun recrutement tant que ce rapport n’est pas signé par le responsable humain de l’étude et relu par une personne indépendante de l’implémentation.
