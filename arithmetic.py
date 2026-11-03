from constants import LCG_MODULO, LCG_MULTIPLICATEUR, LCG_INCREMENT


def pgcd(a, b):

    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def parametres_lcg_valides():




    condition_increment = pgcd(LCG_INCREMENT, LCG_MODULO) == 1
    condition_multiplicateur = (LCG_MULTIPLICATEUR - 1) % 4 == 0
    return condition_increment and condition_multiplicateur


class Generateur:


    def __init__(self, graine):
        if not parametres_lcg_valides():
            raise ValueError("Les paramètres du générateur ne sont pas valides.")
        self.etat = int(graine) % LCG_MODULO

    def entier(self, minimum, maximum):
        self.etat = (
            LCG_MULTIPLICATEUR * self.etat + LCG_INCREMENT
        ) % LCG_MODULO
        return minimum + self.etat % (maximum - minimum + 1)

    def reel(self):
        self.etat = (
            LCG_MULTIPLICATEUR * self.etat + LCG_INCREMENT
        ) % LCG_MODULO
        return self.etat / LCG_MODULO
