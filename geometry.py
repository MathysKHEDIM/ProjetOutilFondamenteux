import math


def vecteur(a, b):
    return b[0] - a[0], b[1] - a[1]


def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]


def norme(v):
    return math.hypot(v[0], v[1])


def distance(a, b):
    return norme(vecteur(a, b))


def distance_point_segment(point, debut, fin):

    segment = vecteur(debut, fin)
    longueur_carre = produit_scalaire(segment, segment)

    if longueur_carre == 0:
        return distance(point, debut)

    vers_point = vecteur(debut, point)
    parametre = produit_scalaire(vers_point, segment) / longueur_carre
    parametre = max(0.0, min(1.0, parametre))

    projection = (
        debut[0] + parametre * segment[0],
        debut[1] + parametre * segment[1]
    )
    return distance(point, projection)


def point_dans_ellipse(point, centre, rayon_x, rayon_y):

    if rayon_x <= 0 or rayon_y <= 0:
        return False

    x = (point[0] - centre[0]) / rayon_x
    y = (point[1] - centre[1]) / rayon_y
    return x * x + y * y <= 1.0


def distance_approx_ellipse(point, centre, rayon_x, rayon_y):




    if point_dans_ellipse(point, centre, rayon_x, rayon_y):
        return 0.0

    x = (point[0] - centre[0]) / rayon_x
    y = (point[1] - centre[1]) / rayon_y
    rayon_normalise = math.hypot(x, y)
    rayon_min = min(rayon_x, rayon_y)
    return (rayon_normalise - 1.0) * rayon_min


def determinant(u, v):
    return u[0] * v[1] - u[1] * v[0]


def segments_se_coupent(a, b, c, d, tolerance=1e-10):

    ab = vecteur(a, b)
    ac = vecteur(a, c)
    ad = vecteur(a, d)
    cd = vecteur(c, d)
    ca = vecteur(c, a)
    cb = vecteur(c, b)

    d1 = determinant(ab, ac)
    d2 = determinant(ab, ad)
    d3 = determinant(cd, ca)
    d4 = determinant(cd, cb)

    return (
        d1 * d2 <= tolerance
        and d3 * d4 <= tolerance
    )
