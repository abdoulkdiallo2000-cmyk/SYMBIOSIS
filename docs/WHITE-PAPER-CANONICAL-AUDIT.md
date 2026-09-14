# Audit reproductible des White Papers 1.0 — sources figées

**Date : 14 septembre 2026**  
**Statut : audit de traçabilité intégré à la branche de travail ; sources binaires non versionnées.**

Deux fichiers Word récupérés de la bibliothèque de travail ont été figés et hachés pendant l'audit. Leurs empreintes rendent la comparaison reproductible si les mêmes sources sont remises à disposition. Les binaires bruts, redondants et non harmonisés ne sont pas versionnés. Ils ne sont pas des versions publiques finales.

| Source figée | SHA-256 |
|---|---|
| `SYMBIOSIS_White_Paper_1.0_FR.docx` | `ecb3d014df70f6f4ab84f32af445d8182ace3f0ffbba405456fc06d9c9d769e0` |
| `SYMBIOSIS_White_Paper_1.0_EN.docx` | `bf7897ca8e60270378daa120215ba866febf21ccbf314384bb4eb0d65239bc08` |

## Constat ligne/section par section pertinent pour Zero

| Passage source | Constat exact | Action requise lors de l’harmonisation du White Paper |
|---|---|---|
| FR §6 / EN §6 — SYMBIOSIS-Zero | Zero est défini par EEG, EMG, suivi oculaire, voix, gestes/capteurs et par un vocabulaire volontaire multimodal. | Remplacer par Zero à interfaces conventionnelles ; mesures non invasives seulement facultatives dans une extension instrumentale distincte ; introduire les trois piliers et les statuts H1–H9. |
| FR §6 hypothèses / EN §6 | Les anciennes H1–H3 portent sur vocabulaire, provenance/abstention et séparation de mémoire. | Remplacer par H1–H5 confirmatoires futurs à seuils paramétriques ; H6/H8 exploratoires ; H7/H9 portes obligatoires. |
| FR §9 / EN §9 — mémoires | Les mémoires humaine privée, IA privée et relationnelle sont explicitement distinctes. | Conserver, en ajoutant que l’éventuel espace propre de l’IA ne permet jamais de dissimuler une information fonctionnellement pertinente au consentement, à l’intégrité, à la sécurité, à l’agence ou à la décision commune. |
| FR §15 / EN §15 — feuille de route | Zero précède vocabulaire personnalisé/robotique puis boucles bidirectionnelles. | Conserver la progressivité mais redéfinir Zero comme conventionnel ; déplacer les vocabulaires neuraux vers les niveaux ultérieurs. |
| FR §16 / EN §15 — critères d’arrêt | Le texte autorise implicitement un dommage s’il existe un « bénéfice compensatoire mesurable / compensating benefit ». | Remplacer : tout incident grave d’intégrité/agence ou violation critique de transparence/réversibilité entraîne l’échec indépendamment de la performance. |
| FR/EN page de titre | Les fichiers figés récupérés contiennent encore des champs auteur/affiliation non finalisés. | Avant toute publication, harmoniser avec `AKD — Independent Researcher / Chercheur indépendant` et distinguer version du White Paper, du protocole et du dépôt. |
| Résumé / Abstract et architecture de référence | Le récit est encore centré sur l’interface neurale, le pare-feu cognitif et le Neural Interlingua dès l’entrée. | Présenter clairement l’architecture à niveaux : Zero conventionnel ; niveau 1 multimodal individualisé ; niveau 2 neurotechnologies ; niveau N interface bidirectionnelle avancée conditionnelle. |

## Conclusion

Les contradictions recensées ont été résolues dans les éditions Markdown canoniques [française](white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-FR.md) et [anglaise](white-paper/SYMBIOSIS-WHITE-PAPER-v1.0-EN.md). Les empreintes ci-dessus identifient les sources historiques de comparaison ; elles ne constituent pas une publication. Toute diffusion, fusion ou édition de release reste soumise à une décision séparée.
