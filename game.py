from arithmetic import Generateur
from constants import (
    BUT_LARGEUR, BUT_HAUTEUR, DEMI_BUT, DISTANCE_MUR,
    DEMI_LARGEUR_MUR, HAUTEUR_MUR
)
from trajectory import calculer_trajectoire
from goalkeeper import evaluer_arret


def lire_entier(message, minimum, maximum):
    while True:
        try:
            valeur = int(input(message))
            if minimum <= valeur <= maximum:
                return valeur
            print(f"Entre une valeur comprise entre {minimum} et {maximum}.")
        except ValueError:
            print("Saisie invalide : entre un nombre entier.")


def afficher_titre():
    print("\n" + "=" * 48)
    print("                 LAST FREE KICK")
    print("          La science du coup franc")
    print("=" * 48)


def afficher_situation(generateur, numero_tir):
    distance_but = generateur.entier(18, 31)
    gardien = generateur.entier(-90, 90) / 100
    hauteur_mur = HAUTEUR_MUR + generateur.entier(-15, 15) / 100
    return distance_but, gardien, hauteur_mur


def jouer_un_tir(generateur, numero_tir):
    afficher_titre()
    distance_but, position_gardien, hauteur_mur = afficher_situation(
        generateur, numero_tir
    )

    print(f"\nCoup franc à {distance_but} mètres du but.")
    print(f"Le mur se trouve à {DISTANCE_MUR:.2f} mètres.")
    print(f"Hauteur estimée du mur : {hauteur_mur:.2f} m.")
    print(f"Position du gardien : {position_gardien:+.2f} m par rapport au centre.")

    puissance = lire_entier("\nPuissance (40 à 100) : ", 40, 100)
    elevation = lire_entier("Angle de frappe (10 à 45 degrés) : ", 10, 45)
    direction = lire_entier("Direction (-12 gauche à +12 droite) : ", -12, 12)
    effet = lire_entier("Effet (-10 à +10) : ", -10, 10)

    trajectoire = calculer_trajectoire(puissance, elevation, distance_but, hauteur_mur)
    print("\nCalcul de la trajectoire...")
    print(f"Vitesse initiale estimée : {trajectoire['vitesse']:.2f} m/s")
    print(f"Portée théorique : {trajectoire['portee']:.2f} m")
    print(f"Hauteur maximale : {trajectoire['hauteur_max']:.2f} m")
    if trajectoire["racine_mur_dicho"] is not None:
        print(
            "Franchissement de la hauteur du mur : "
            f"x = {trajectoire['racine_mur_dicho']:.3f} m "
            f"(dichotomie, {trajectoire['tours_dicho']} itérations)"
        )
        if trajectoire["racine_mur_newton"] is not None:
            print(
                "Vérification par Newton : "
                f"x = {trajectoire['racine_mur_newton']:.3f} m "
                f"({trajectoire['tours_newton']} itérations)"
            )

    if trajectoire["portee"] < distance_but:
        print("\nLe ballon retombe avant d'atteindre le but.")
        return "rate"

    from polynomials import evaluer_horner
    hauteur_mur_ballon = evaluer_horner(
        trajectoire["coefficients"], DISTANCE_MUR
    )

    decalage_effet_mur = effet * 0.025 * DISTANCE_MUR * (
        1 - DISTANCE_MUR / distance_but
    )
    import math
    angle_direction = math.radians(direction)
    position_laterale_mur = (
        DISTANCE_MUR * math.tan(angle_direction)
        + decalage_effet_mur
    )

    if abs(position_laterale_mur) <= DEMI_LARGEUR_MUR:
        if hauteur_mur_ballon <= hauteur_mur:
            print("\nLe ballon percute le mur !")
            print(f"Hauteur du ballon au mur : {hauteur_mur_ballon:.2f} m.")
            return "mur"
        print("\nLe ballon passe au-dessus du mur !")
    else:
        print("\nLe ballon contourne le mur !")

    hauteur_but = trajectoire["hauteur_but"]
    position_laterale_but = (
        distance_but * math.tan(angle_direction)
        + effet * 0.012 * distance_but
    )

    print("\nPosition d'arrivée estimée :")
    print(f"  Décalage horizontal : {position_laterale_but:+.2f} m")
    print(f"  Hauteur : {hauteur_but:.2f} m")

    if abs(position_laterale_but) > DEMI_BUT:
        distance_poteau = abs(position_laterale_but) - DEMI_BUT
        print(f"\nLe ballon passe à {distance_poteau:.2f} m du poteau.")
        print("HORS CADRE !")
        return "hors_cadre"

    if hauteur_but > BUT_HAUTEUR:
        print("\nLe ballon passe au-dessus de la barre transversale.")
        return "hors_cadre"

    if hauteur_but < 0:
        print("\nLe ballon termine au sol avant la ligne de but.")
        return "rate"

    resultat = evaluer_arret(
        (position_laterale_but, hauteur_but),
        position_gardien,
        generateur
    )

    print(f"\nDistance à la zone d'intervention : {resultat['distance_zone']:.2f} m")
    print(f"Probabilité d'arrêt : {resultat['probabilite'] * 100:.1f} %")

    if resultat["zone_garantie"]:
        print("Le ballon entre dans la zone d'arrêt garantie.")
    if resultat["arrete"]:
        print("\nLE GARDIEN ARRÊTE LE BALLON !")
        return "arrete"

    print("\nBUT ! Le gardien ne parvient pas à détourner le ballon.")
    return "but"


def lancer_match(graine):
    generateur = Generateur(graine)
    resultats = {
        "but": 0,
        "arrete": 0,
        "mur": 0,
        "hors_cadre": 0,
        "rate": 0
    }

    print("\nTu disposes de 5 coups francs.")
    for numero in range(1, 6):
        print(f"\n------------- TIR {numero}/5 -------------")
        resultat = jouer_un_tir(generateur, numero)
        resultats[resultat] += 1
        print(f"\nBilan provisoire : {resultats['but']} but(s).")
        input("\nAppuie sur Entrée pour continuer...")

    afficher_bilan(resultats)


def afficher_bilan(resultats):
    afficher_titre()
    total = sum(resultats.values())
    print("\nBILAN DU MATCH")
    print(f"Tirs effectués : {total}")
    print(f"Buts : {resultats['but']}")
    print(f"Arrêts : {resultats['arrete']}")
    print(f"Murs touchés : {resultats['mur']}")
    print(f"Hors cadre : {resultats['hors_cadre']}")
    print(f"Tirs trop courts : {resultats['rate']}")
    print(f"Précision : {100 * resultats['but'] / total:.1f} %")


def lancer_menu():
    while True:
        afficher_titre()
        print("\n1. Jouer un match")
        print("2. Comprendre les règles mathématiques")
        print("3. Quitter")
        choix = input("\nTon choix : ").strip()

        if choix == "1":
            graine = lire_entier("Choisis une graine de match (0 à 999999) : ", 0, 999999)
            lancer_match(graine)
        elif choix == "2":
            afficher_explications()
        elif choix == "3":
            print("\nFin du jeu. À bientôt !")
            break
        else:
            print("Choix invalide.")


def afficher_explications():
    afficher_titre()
    print("""
Le ballon suit une trajectoire parabolique.
Les coefficients de cette parabole sont calculés
par résolution d'un système linéaire.

Le mur est contrôlé à sa position.
Le gardien possède une ellipse d'arrêt garanti.
En dehors de cette ellipse, la probabilité d'arrêt
diminue avec la distance.

Les situations de match sont produites par un
générateur pseudo-aléatoire congruentiel.
Les calculs sont réalisés par le programme.
""")
    input("Appuie sur Entrée pour revenir au menu...")
