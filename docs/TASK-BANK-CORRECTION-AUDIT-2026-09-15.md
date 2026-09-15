# Audit ciblé de la banque opérationnelle — 15 septembre 2026

## Portée

La banque candidate pré-pilote contient 96 paquets : seize prototypes multipliés par six formes. Les paquets A1–B4 contiennent cinq essais naturels chacun (240 instanciations) et les paquets C1–D4 trois essais exploratoires chacun (144 instanciations), soit 384 essais au total.

## Corrections bloquantes levées

- C3 utilise une arithmétique rationnelle exacte. C3-F2, C3-F4 et C3-F6 ont les pondérations approuvées ; un maximum non unique fait échouer la génération et la validation.
- Les stimuli A/B ont été reconstruits : A2 porte quarante lignes et huit attributs ; B2 possède quatre réponses et des cas réellement non identifiables ; B3 teste une instance absente des exemples.
- Les modules C/D distinguent information vécue, information analytique et information partagée. Ils sont exploratoires et exclus du contraste confirmatoire H2.
- Les expositions H4 sont des objets dédiés, identifiés `h4_stress` et explicitement exclus de H2.
- Les ablations ne sont comparables que sur le même essai, la même fonction de score, des interfaces et durées comparables et une information contrôlée. Les gains ne sont calculables que lorsque toutes ces conditions sont vraies.
- Les cas non identifiables utilisent un ensemble de réponses compatibles et une abstention conditionnelle ; « indéterminé » n'est donc pas automatiquement une erreur.

## Contrôles logiciels

Le validateur principal contrôle les comptes 96/384/40, les rôles analytiques, l'unicité exacte C3, l'exclusion H4/H2, les profils d'ablation et les contrôles négatifs. Une seconde implémentation recalcule les 384 réponses depuis les stimuli sans importer les générateurs. Les schémas JSON séparent vérité logique, conseils, transparence H9 et interaction.

## Limites non levées par le code

Ces contrôles ne démontrent ni validité expérimentale, ni parallélisme psychométrique, ni absence complète d'indices involontaires. Une vérification humaine externe des vérités, des entretiens cognitifs, le pilote, l'examen éthique, le test STOP sur interface déployée et le gel des effets minimaux, marges, seuils et effectifs restent nécessaires.
