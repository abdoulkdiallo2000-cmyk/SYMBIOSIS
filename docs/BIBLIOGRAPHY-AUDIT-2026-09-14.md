# Audit bibliographique final — White Papers FR et EN

**Date :** 14 septembre 2026
**Portée :** neuf notices présentes à l'identique dans les deux White Papers. Un identifiant numérique d'objet (*Digital Object Identifier*, DOI) est contrôlé lorsqu'il existe.

## Correction principale

Le DOI `10.1038/s41583-024-00819-9` correspond à **Silva, A. B., Littlejohn, K. T., Liu, J. R., Moses, D. A., & Chang, E. F. (2024), “The speech neuroprosthesis”, Nature Reviews Neuroscience, 25, 473–492**. La notice erronée « Neurotechnology and neurorights » a été supprimée des deux langues.

## Sources de vérification

| Notice | Source primaire ou institutionnelle contrôlée | Résultat |
|---|---|---|
| Buçinca et al. (2021) | ACM DOI `10.1145/3449287` et manuscrit auteur | titre, auteurs, volume 5, CSCW1, article 188, 1–21 conformes |
| Goddard et al. (2012) | PubMed et DOI `10.1136/amiajnl-2011-000089` | titre complet, revue 19(1), 121–127 conformes |
| Hemmer et al. (2025) | Taylor & Francis DOI `10.1080/0960085X.2025.2475962` | cinq auteurs, volume 34(6), 979–1002 conformes |
| Lakens (2017) | SAGE DOI `10.1177/1948550617697177` | titre complet, volume 8(4), 355–362 conformes |
| Lee & See (2004) | PubMed/SAGE DOI `10.1518/hfes.46.1.50_30392` | titre complet, volume 46(1), 50–80 conformes |
| Silva et al. (2024) | Nature et PubMed DOI `10.1038/s41583-024-00819-9` | titre, cinq auteurs, volume 25, 473–492 corrigés |
| Tapal et al. (2017) | Frontiers/PubMed DOI `10.3389/fpsyg.2017.01552` | titre, auteurs, volume 8, article 1552 conformes |
| Vaccaro et al. (2024) | Nature DOI `10.1038/s41562-024-02024-1` | titre, auteurs, volume 8, 2293–2303 conformes |
| UNESCO (2025) | page officielle de l'instrument | titre et adoption le 11 novembre 2025 conformes ; pas de DOI indiqué |

Le script `scripts/check_bibliography.py` vérifie que les deux bibliographies restent identiques, que chaque DOI apparaît une seule fois avec les métadonnées attendues et que l'ancienne notice Silva ne réapparaît pas.

## Limite

Ce contrôle vérifie l'exactitude des métadonnées des notices utilisées. Il ne constitue pas une revue systématique de littérature, ne confirme pas que la sélection est exhaustive et ne transfère pas automatiquement la validité d'un instrument ou d'un seuil au protocole SYMBIOSIS-Zero.
