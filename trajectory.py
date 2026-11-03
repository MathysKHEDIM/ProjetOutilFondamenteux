import math

from constants import GRAVITE
from matrices import coefficients_parabole
from polynomials import evaluer_horner, dichotomie, newton


def calculer_trajectoire(puissance, elevation, distance_but, hauteur_mur=1.95):





    vitesse = 8.0 + 0.14 * puissance
    angle = math.radians(elevation)

    vitesse_horizontale = vitesse * math.cos(angle)
    vitesse_verticale = vitesse * math.sin(angle)

    if vitesse_horizontale <= 0:
        raise ValueError("Vitesse horizontale invalide.")

    portee = 2 * vitesse_horizontale * vitesse_verticale / GRAVITE
    hauteur_max = vitesse_verticale ** 2 / (2 * GRAVITE)
    position_apex = portee / 2

    if portee <= 0:
        raise ValueError("La portée doit être positive.")

    points = [
        (0.0, 0.0),
        (position_apex, hauteur_max),
        (portee, 0.0)
    ]
    coefficients = coefficients_parabole(points)
    hauteur_but = evaluer_horner(coefficients, distance_but)

    racine_mur_dicho, tours_dicho = dichotomie(
        coefficients, hauteur_mur, 0.0, position_apex
    )
    racine_mur_newton, tours_newton = newton(
        coefficients, hauteur_mur, max(0.01, position_apex * 0.5)
    )

    return {
        "vitesse": vitesse,
        "portee": portee,
        "hauteur_max": hauteur_max,
        "position_apex": position_apex,
        "coefficients": coefficients,
        "hauteur_but": hauteur_but,
        "racine_mur_dicho": racine_mur_dicho,
        "tours_dicho": tours_dicho,
        "racine_mur_newton": racine_mur_newton,
        "tours_newton": tours_newton
    }
