import math

from constants import (
    GARDIEN_RAYON_HORIZONTAL,
    GARDIEN_RAYON_VERTICAL,
    GARDIEN_HAUTEUR_CENTRE,
    GARDIEN_PROBA_BORD,
    GARDIEN_DECROISSANCE
)
from geometry import point_dans_ellipse, distance_approx_ellipse


def evaluer_arret(position_ballon, position_gardien, generateur):




    centre = (position_gardien, GARDIEN_HAUTEUR_CENTRE)

    dans_zone = point_dans_ellipse(
        position_ballon,
        centre,
        GARDIEN_RAYON_HORIZONTAL,
        GARDIEN_RAYON_VERTICAL
    )

    distance_zone = distance_approx_ellipse(
        position_ballon,
        centre,
        GARDIEN_RAYON_HORIZONTAL,
        GARDIEN_RAYON_VERTICAL
    )

    if dans_zone:
        return {
            "arrete": True,
            "probabilite": 1.0,
            "distance_zone": 0.0,
            "zone_garantie": True
        }

    probabilite = GARDIEN_PROBA_BORD * math.exp(
        -GARDIEN_DECROISSANCE * distance_zone
    )
    tirage = generateur.reel()

    return {
        "arrete": tirage < probabilite,
        "probabilite": probabilite,
        "distance_zone": distance_zone,
        "zone_garantie": False
    }
