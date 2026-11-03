# LAST FREE KICK

Jeu de coups francs en console, développé en Python dans le cadre du projet
personnel de BUT 1 Informatique – Outils fondamentaux.

Le joueur choisit la puissance, l'angle de frappe, la direction et l'effet.
Le programme calcule la trajectoire, vérifie le franchissement du mur,
détermine le point d'arrivée dans le but et simule l'intervention du gardien.

## Lancer le jeu

Aucune bibliothèque externe n'est nécessaire. Python 3.10 ou supérieur est conseillé.

```bash
python main.py
```

Pour lancer les expériences sur le gardien :

```bash
python experiments.py
```

Pour exécuter les tests :

```bash
python -m unittest discover -s tests -v
```

## Organisation du dépôt

- `main.py` : point d'entrée.
- `game.py` : menu, saisies et déroulement du match.
- `trajectory.py` : construction et calcul de la trajectoire.
- `polynomials.py` : évaluation de polynômes, dérivée, dichotomie et Newton.
- `matrices.py` : résolution de systèmes par pivot de Gauss.
- `geometry.py` : distances, vecteurs et appartenance à une ellipse.
- `goalkeeper.py` : zone garantie et probabilité d'arrêt.
- `arithmetic.py` : PGCD et générateur pseudo-aléatoire.
- `experiments.py` : expérience reproductible sur les arrêts du gardien.
- `constants.py` : paramètres physiques et constantes du modèle.
- `tests/` : tests automatiques.
- `docs/` : explication mathématique et pistes d'analyse.

## Notions des TP mobilisées

| TP | Notions | Utilisation |
|---|---|---|
| TP1 – Calcul numérique | Flottants, tolérances, erreurs numériques | Calculs de trajectoire et recherche de racines |
| TP2 – Arithmétique | PGCD, modulo, calcul entier | Validation et fonctionnement du générateur pseudo-aléatoire |
| TP3 – Polynômes | Horner, dérivée, Newton, dichotomie | Calcul et analyse de la trajectoire parabolique |
| TP4 – Matrices | Systèmes linéaires, pivot de Gauss | Calcul des coefficients de la parabole |
| TP6 – Géométrie | Distances, vecteurs, coordonnées, ellipse | Mur, but et zone d'intervention du gardien |

Le TP5 de synthèse n'est pas intégré au projet : le chiffrement n'apporterait
pas de fonctionnalité naturelle au jeu.

## Modèle et limites

Le jeu est une simulation pédagogique en deux dimensions. Il ne prétend pas
reproduire exactement l'aérodynamique d'un ballon réel. La vitesse est estimée
à partir de la puissance choisie ; la trajectoire verticale est parabolique.
La direction et l'effet déterminent le décalage latéral.

Le gardien possède une ellipse d'arrêt garanti. En dehors de celle-ci, la
probabilité d'arrêt diminue exponentiellement avec la distance à la zone.

Les paramètres sont volontairement accessibles dans `constants.py` afin de
pouvoir réaliser des expériences et discuter leur influence.

## Utilisation d'une IA

Une assistance par IA a été utilisée pour proposer une première architecture,
des pistes d'algorithmes, une base de code et des tests. Le fonctionnement,
les formules, les paramètres et les résultats doivent être relus, testés,
compris et éventuellement modifiés par l'étudiant avant le rendu.
