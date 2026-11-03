def resoudre_systeme(matrice, second_membre, tolerance=1e-12):




    n = len(matrice)

    if n == 0 or len(second_membre) != n:
        raise ValueError("Dimensions incompatibles.")

    a = [ligne[:] + [second_membre[i]] for i, ligne in enumerate(matrice)]

    for ligne in a:
        if len(ligne) != n + 1:
            raise ValueError("Le système doit être carré.")

    for colonne in range(n):
        ligne_pivot = max(
            range(colonne, n),
            key=lambda i: abs(a[i][colonne])
        )

        if abs(a[ligne_pivot][colonne]) <= tolerance:
            raise ValueError("Système singulier ou mal conditionné.")

        a[colonne], a[ligne_pivot] = a[ligne_pivot], a[colonne]

        pivot = a[colonne][colonne]
        for j in range(colonne, n + 1):
            a[colonne][j] /= pivot

        for i in range(n):
            if i != colonne:
                facteur = a[i][colonne]
                for j in range(colonne, n + 1):
                    a[i][j] -= facteur * a[colonne][j]

    return [a[i][n] for i in range(n)]


def coefficients_parabole(points):




    if len(points) != 3:
        raise ValueError("Une parabole nécessite trois points.")

    matrice = []
    valeurs = []

    for x, y in points:
        matrice.append([x * x, x, 1.0])
        valeurs.append(y)

    a, b, c = resoudre_systeme(matrice, valeurs)
    return [c, b, a]
