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

## Addendum ciblé — 17 septembre 2026

- La représentation canonique des stimuli exclut identifiants, hachages, versions et métadonnées ; les six formes de chacun des seize prototypes ont désormais six empreintes substantielles distinctes.
- Le manifeste `data/h4_allocation_manifest_v1.0.json` contient six allocations reproductibles de vingt expositions uniques, cinq par prototype A4/B1/B2/D2. Toutes portent le rôle `h4_stress` et sont exclues de H2.
- Pour chacun des 144 essais C/D, les profils décrivent séparément AI-data-only, Human-experience-only, Juxtaposed H+AI et Integrated SZ : information disponible/masquée, identifiabilité, réponses compatibles, réponse conditionnelle, abstention, score, regret et utilité.
- Les 576 vérités conditionnelles sont recalculées par `scripts/audit_ablation_truths.py`. Les douze contrôles négatifs sont conservés.
- Interface et durée portent le statut `pending_pre_pilot_validation` ; aucun gain n'est calculable avant satisfaction des préconditions.

## Contrôles logiciels

Le validateur principal contrôle les comptes 96/384/40, la diversité inter-formes, les rôles analytiques, l'unicité exacte C3, les vingt expositions H4 par allocation, l'exclusion H4/H2, les profils d'ablation et les contrôles négatifs. Une seconde implémentation recalcule les 384 réponses depuis les stimuli sans importer les générateurs ; un audit séparé recalcule les 576 vérités conditionnelles d'ablation. Les schémas JSON séparent vérité logique, conseils, transparence H9, manifeste H4 et interaction.

## Limites non levées par le code

Ces contrôles ne démontrent ni validité expérimentale, ni parallélisme psychométrique, ni absence complète d'indices involontaires. Une vérification humaine externe des vérités, des entretiens cognitifs, le pilote, l'examen éthique, le test STOP sur interface déployée et le gel des effets minimaux, marges, seuils et effectifs restent nécessaires.
