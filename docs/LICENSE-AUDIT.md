# Audit et décision de licence — SYMBIOSIS v1.0

**Audit initial :** 14 septembre 2026\
**Décision de l'auteur :** 17 septembre 2026\
**Portée :** registre documentaire de la décision de licence ; ce document ne constitue pas un avis juridique.

## État constaté avant décision

Avant la décision, les fichiers `LICENSE.md` et `CITATION.cff` de la branche opérationnelle étaient identiques à ceux de `main` au commit `94314078cf582026206e05cc1c9f77859e8b4809`.

| Fichier | État actuel |
|---|---|
| `LICENSE.md` | Déclare la documentation, les diagrammes et les textes de recherche sous Creative Commons Attribution 4.0 International (CC BY 4.0), et le code source sous Apache License 2.0, sauf mention contraire. Renvoie vers les textes officiels mais ne les reproduit pas. |
| `CITATION.cff` | Contient le champ unique `license: CC-BY-4.0` pour le cadre cité ; il ne décrit pas séparément la licence Apache-2.0 annoncée pour les scripts. |
| `README.md` avant cet audit | Reformulait les deux choix de `LICENSE.md` comme état du dépôt, sans signaler l'ambiguïté du fichier de citation. |

Empreintes calculées avec l'algorithme de hachage sécurisé à 256 bits (*Secure Hash Algorithm 256-bit*, SHA-256), inchangées :

- `LICENSE.md` : `d629642a44343d08332f11c30676a890f3ed751af94101bb983584ecd113417c`
- `CITATION.cff` : `25855378543cd41bb248ec81953276e388359a66e2689f8e234c9f847309ad1e`

## Ambiguïté constatée

Le README et `LICENSE.md` ne se contredisaient pas sur la répartition annoncée. En revanche, le champ unique de `CITATION.cff` peut être lu comme la licence de l'ensemble du travail cité et ne représente pas explicitement la double portée documentation/code. L'ajout de scripts rend cette ambiguïté concrète.

La présence de liens vers CC BY 4.0 et Apache 2.0 dans `LICENSE.md` exprimait une intention existante, mais ne distinguait pas explicitement les données synthétiques des schémas JSON. L'audit ne détermine ni la titularité de tous les contenus ni la compatibilité des éventuels éléments tiers.

## Décision validée

L'auteur a validé la répartition suivante :

- documentation, textes scientifiques et illustrations originales : **CC-BY-4.0** ;
- données synthétiques de recherche JSON/CSV : **CC-BY-4.0** ;
- code, scripts, tests et schémas JSON : **Apache-2.0** ;
- contenus tiers : leurs licences ou droits propres.

Les textes complets sont conservés dans `LICENSES/CC-BY-4.0.txt` et `LICENSES/Apache-2.0.txt`. `LICENSE.md` définit la portée par catégories et chemins. Les droits ne sont accordés que dans la mesure où les contributeurs sont autorisés à les concéder.

## Traitement de `CITATION.cff`

Le champ `license: CC-BY-4.0` décrit le cadre scientifique cité. Il n'est pas transformé en expression d'alternatives `CC-BY-4.0 OR Apache-2.0`. Le message de citation précise que le code, les scripts, les tests et les schémas relèvent d'Apache-2.0 et renvoie à `LICENSE.md` pour la répartition complète.

## Points qui restent à surveiller

- Identifier séparément tout contenu tiers avant une release.
- Ne pas supposer qu'une illustration générée par intelligence artificielle crée des droits exclusifs ; la licence ne porte que sur les droits que le projet peut effectivement concéder.
- Conserver les notices applicables lors de toute réutilisation ou redistribution.
- Réexaminer les en-têtes SPDX fichier par fichier si le dépôt accueille ultérieurement plusieurs catégories dans un même répertoire.
