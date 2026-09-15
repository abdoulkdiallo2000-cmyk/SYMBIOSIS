# Rapport de contrôle qualité du pack corrigé

Date initiale : 14 septembre 2026. Mise à jour ciblée : 15 septembre 2026.

Contrôles exécutés après les cinq corrections :

- contrôle de complétude du pack : réussi ;
- banque initiale : 96 enregistrements, désormais remplacés par les 96 paquets et 384 essais décrits dans la mise à jour ci-dessous ;
- scripts Python : compilation syntaxique réussie ;
- simulation locale de révocation STOP SYMBIOSIS : 100 scénarios sur 100 bloquent toute tentative de transmission post-STOP ;
- protocole Word rendu en PDF et inspecté visuellement sur 27 pages ;
- batterie Word rendue en PDF et inspectée visuellement sur 18 pages ;
- dossier opérationnel Word rendu en PDF et inspecté visuellement sur 15 pages ;
- aucune modification GitHub, aucun préenregistrement, aucun recrutement humain.

Limite : les tests STOP restent des tests de machine à états locale et ne remplacent pas les essais de l’interface réseau réellement déployée. Les contrôles structurels de la banque ne remplacent pas la vérification humaine indépendante de chaque vérité de référence ni le pilote.

## Passe indépendante avant mise en revue

Une seconde passe le 14 septembre 2026 a ajouté : recalcul indépendant des 96 réponses sans importer le générateur ; revue qualitative des familles C/D et des ablations ; correction de A1, C1, C2, C4 et D1 ; contrôle bibliographique FR/EN ; audit de licence ; contrôle transversal des invariants scientifiques et des formulations interdites. Les résultats détaillés figurent dans `TASK-BANK-INDEPENDENT-AUDIT-2026-09-14.md`, `BIBLIOGRAPHY-AUDIT-2026-09-14.md` et `LICENSE-AUDIT.md`.

## Mise à jour de la banque opérationnelle — 15 septembre 2026

La banque est désormais structurée en 96 paquets : six formes pour chacun des seize prototypes. Chaque paquet A1–B4 porte cinq essais naturels (40 essais naturels pour une forme complète) ; chaque paquet C1–D4 porte trois essais exploratoires. Les conseils, expositions H4, registres H9 et profils d'interaction/ablation sont séparés dans des banques versionnées et reliés par identifiants.

Les 384 vérités instanciées passent un recalcul logiciel séparé. Ce résultat atteste la cohérence interne des règles codées, pas leur validité scientifique. La vérification humaine externe, les entretiens cognitifs, l'équivalence réelle des interfaces/temps, le pilote et l'avis éthique restent ouverts.
