




from arithmetic import Generateur
from goalkeeper import evaluer_arret


def mesurer_taux_arret(position, position_gardien, nombre_tirs, graine):
    generateur = Generateur(graine)
    arrets = 0

    for _ in range(nombre_tirs):
        resultat = evaluer_arret(position, position_gardien, generateur)
        if resultat["arrete"]:
            arrets += 1

    return arrets / nombre_tirs


def lancer_experiences():
    nombre_tirs = 10000
    cas = [
        ("Dans la zone garantie", (0.0, 1.2)),
        ("Juste à l'extérieur", (0.9, 1.2)),
        ("À distance moyenne", (1.8, 1.2)),
        ("Loin du gardien", (3.0, 1.2))
    ]

    print("=" * 64)
    print("ÉTUDE EXPÉRIMENTALE DU GARDIEN")
    print("=" * 64)
    print(f"Nombre de tirs par situation : {nombre_tirs}\n")

    for indice, (nom, position) in enumerate(cas):
        taux = mesurer_taux_arret(
            position, 0.0, nombre_tirs, 2026 + indice
        )
        print(f"{nom:25s} : {taux * 100:6.2f} % d'arrêts observés")


if __name__ == "__main__":
    lancer_experiences()
