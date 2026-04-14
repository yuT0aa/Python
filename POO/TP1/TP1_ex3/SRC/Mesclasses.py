"""
1. Ecrire une classe Rectangle en langage Python, permettant de construire un rectangle
dotée d&#39;attributs longueur et largeur.
2. Créer une méthode Perimetre() permettant de calculer le périmètre du rectangle et une
méthode Surface() permettant de calculer la surface du rectangle.
"""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def Perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def Surface(self):
        return self.longueur * self.largeur
