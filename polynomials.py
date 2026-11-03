def evaluer_horner(coefficients, x):

    resultat = 0.0
    for coefficient in reversed(coefficients):
        resultat = resultat * x + coefficient
    return resultat


def derivee(coefficients):

    if len(coefficients) <= 1:
        return [0.0]
    return [i * coefficients[i] for i in range(1, len(coefficients))]


def dichotomie(coefficients, cible, gauche, droite,
               tolerance=1e-9, iterations_max=100):

    def fonction(x):
        return evaluer_horner(coefficients, x) - cible

    f_gauche = fonction(gauche)
    f_droite = fonction(droite)

    if abs(f_gauche) <= tolerance:
        return gauche, 0
    if abs(f_droite) <= tolerance:
        return droite, 0
    if f_gauche * f_droite > 0:
        return None, 0

    iterations = 0
    while iterations < iterations_max:
        milieu = (gauche + droite) / 2
        f_milieu = fonction(milieu)
        iterations += 1

        if abs(f_milieu) <= tolerance or abs(droite - gauche) <= tolerance:
            return milieu, iterations

        if f_gauche * f_milieu <= 0:
            droite = milieu
            f_droite = f_milieu
        else:
            gauche = milieu
            f_gauche = f_milieu

    return (gauche + droite) / 2, iterations


def newton(coefficients, cible, depart, tolerance=1e-9,
           iterations_max=50):

    derivee_coefficients = derivee(coefficients)
    x = float(depart)

    for iteration in range(1, iterations_max + 1):
        valeur = evaluer_horner(coefficients, x) - cible
        pente = evaluer_horner(derivee_coefficients, x)

        if abs(valeur) <= tolerance:
            return x, iteration

        if abs(pente) <= tolerance:
            return None, iteration

        suivant = x - valeur / pente

        if abs(suivant - x) <= tolerance:
            return suivant, iteration

        x = suivant

    return None, iterations_max
