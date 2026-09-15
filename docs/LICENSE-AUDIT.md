# Audit de licence — branche opérationnelle SYMBIOSIS-Zero

**Date :** 14 septembre 2026
**Portée :** constat documentaire, pas avis juridique et pas nouveau choix de licence.

## État hérité de `main`

Les fichiers `LICENSE.md` et `CITATION.cff` de la branche de travail sont byte-à-byte identiques à ceux de `main` au commit `94314078cf582026206e05cc1c9f77859e8b4809`.

| Fichier | État actuel |
|---|---|
| `LICENSE.md` | Déclare la documentation, les diagrammes et les textes de recherche sous Creative Commons Attribution 4.0 International (CC BY 4.0), et le code source sous Apache License 2.0, sauf mention contraire. Renvoie vers les textes officiels mais ne les reproduit pas. |
| `CITATION.cff` | Contient le champ unique `license: CC-BY-4.0` pour le cadre cité ; il ne décrit pas séparément la licence Apache-2.0 annoncée pour les scripts. |
| `README.md` avant cet audit | Reformulait les deux choix de `LICENSE.md` comme état du dépôt, sans signaler l'ambiguïté du fichier de citation. |

Empreintes calculées avec l'algorithme de hachage sécurisé à 256 bits (*Secure Hash Algorithm 256-bit*, SHA-256), inchangées :

- `LICENSE.md` : `d629642a44343d08332f11c30676a890f3ed751af94101bb983584ecd113417c`
- `CITATION.cff` : `25855378543cd41bb248ec81953276e388359a66e2689f8e234c9f847309ad1e`

## Concordance et ambiguïté

Le README et `LICENSE.md` ne se contredisaient pas sur la répartition annoncée. En revanche, le champ unique de `CITATION.cff` peut être lu comme la licence de l'ensemble du travail cité et ne représente pas explicitement la double portée documentation/code. L'ajout de scripts rend cette ambiguïté concrète.

La présence de liens vers CC BY 4.0 et Apache 2.0 dans `LICENSE.md` exprime une intention existante, mais cet audit ne détermine ni la suffisance juridique de la notice, ni la titularité de tous les contenus, ni la compatibilité des éventuels éléments tiers.

## Action de cette branche

- `LICENSE.md` n'est pas modifié.
- `CITATION.cff` n'est pas modifié.
- Le README décrit ces licences comme un état hérité et renvoie au présent audit ; il ne les confirme pas comme décision juridique nouvelle.

## Décision requise avant fusion ou diffusion

Le titulaire du projet doit confirmer explicitement :

1. s'il maintient CC BY 4.0 pour la documentation et Apache 2.0 pour le code ;
2. si `CITATION.cff` doit rester limité à la documentation/cadre ou représenter plusieurs catégories de fichiers ;
3. si les textes complets, fichiers de licence normalisés ou en-têtes d'identifiant de licence de la *Software Package Data Exchange* (SPDX) doivent être ajoutés ;
4. si des éléments tiers ou générés par IA nécessitent des mentions supplémentaires.

La branche peut être soumise à revue avec cette ambiguïté signalée, mais elle ne devrait pas être fusionnée ni diffusée comme édition licenciée définitive avant décision explicite.
