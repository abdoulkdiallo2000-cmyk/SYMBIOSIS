# Seconde vérification des vérités de référence — 14 septembre 2026

## Portée et indépendance

Les 96 formes ont été recalculées par une implémentation séparée, `scripts/audit_reference_truths.py`, qui lit uniquement les données instanciées et les règles annoncées. Elle n'importe pas le générateur, n'appelle aucune de ses fonctions et n'utilise jamais `correct_answer` pour produire la réponse attendue. Une revue qualitative distincte a examiné les familles C et D, la représentation des entrées subjectives et les ablations.

Cette indépendance est **logicielle et logique**, pas une validation par une seconde personne. Une vérification humaine externe reste requise avant le pilote.

## Défauts détectés et corrigés

| Prototype | Défaut détecté | Correction |
|---|---|---|
| A1 | A et D satisfaisaient les contraintes alors que D était déclaré unique. | Le temps de A dépasse désormais la limite ; D est réellement l'unique option admissible dans les six formes. |
| C1 | La réponse dépendait d'un état de charge simulé sans relier explicitement celui-ci à la charge attendue des options. | L'entrée devient une limite maximale vécue ; la règle filtre les options par cette limite puis maximise la performance. |
| C2 | Les libellés `affective_fit` ne permettaient pas de déduire sans ambiguïté quel contenu devait être exclu. | Les contenus sont classés `négatif_modéré` ou `neutre` et la règle conditionnelle est explicitée. |
| C4 | L'intuition et l'estimation analytique favorisaient toujours le même motif ; aucune intégration ni intuition trompeuse n'était réellement testée. | Le signal privé varie, sa fiabilité entre dans une mise à jour bayésienne explicite et certaines formes exigent de suivre ou de rejeter l'intuition. |
| D1 | Dans trois formes, l'optimum IA restait admissible malgré la contrainte privée : l'intégration n'était pas nécessaire. | La contrainte humaine exclut désormais l'optimum déterminé par les seules données IA dans chacune des six formes. |
| D2–D4 | Les conséquences des ablations étaient décrites dans la batterie mais absentes du JSON. | Chaque forme porte maintenant `AI-data-only`, `Human-experience-only` et `Integrated`, avec vérifications sémantiques. |

## Résultat par famille

| Famille | Vérification | Résultat |
|---|---|---|
| A1–A4 | contraintes, scores, cohérence documentaire et théorème de Bayes recalculés | 24/24 conformes |
| B1–B4 | exception, contexte explicite, mini-grammaire et transition séquentielle recalculés | 24/24 conformes |
| C1–C4 | règles conditionnelles, pondérations, classes subjectives et mise à jour du signal privé recalculées | 24/24 conformes après corrections |
| D1–D4 | solution intégrée et insuffisance/différence des ablations vérifiées | 24/24 conformes après corrections |

## Interprétation prudente

- Les valeurs `mock_*` servent à éprouver les règles de construction. Elles doivent être remplacées par une entrée volontaire du participant en collecte.
- La subjectivité n'est ni décrétée vraie ni réduite à un biais : sa classe et sa fiabilité déterminent si elle doit influer sur la décision.
- Les tâches D créent volontairement une information scindée. Elles établissent une possibilité structurelle d'intégration, pas un succès empirique de SYMBIOSIS-Zero.
- Les ablations doivent conserver interface, durée et nombre d'étapes comparables ; cette équivalence reste à vérifier au pré-pilote.
- Les formes ne doivent pas être retenues ou retirées selon qu'elles favorisent la condition SYMBIOSIS-Zero.

## Conclusion

Le recalcul indépendant passe sur 96/96 formes. Les réponses de référence découlent désormais des règles annoncées pour les instances présentes. La difficulté, le parallélisme, la validité psychométrique, l'absence d'indices involontaires et l'équivalence pratique des ablations restent à établir par revue humaine, entretiens cognitifs et pilote.
