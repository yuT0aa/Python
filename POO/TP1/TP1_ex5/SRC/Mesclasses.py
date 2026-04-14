"""
1. Défnir une classe Cercle permettant de créer un cercle C(O,r) de centre O(a,b) et de rayon
r à l&#39;aide du constructeur.
2. Défnir une méthode Surface() de la classe qui permet de calculer la surface du cercle.
3. Défnir une méthode Perimetre() de la classe qui permet de calculer le périmètre du cercle.
4. Défnir une méthode testAppartenance() de la classe qui permet de tester si un point A(x,y)
appartient ou non au cercle C(O,r).
"""
import math

class Cercle:
    def __init__(self, O, r):
        self.O = O
        self.r = r
    def Surface(self):
        return math.pi * self.r ** 2
    def Perimetre(self):
        return 2 * math.pi * self.r
    def testAppartenance(self, A):
        distance = math.sqrt((A[0] - self.O[0]) ** 2 + (A[1] - self.O[1]) ** 2)
        if distance < self.r:
            return "Le point A appartient au cercle."
        elif distance == self.r:
            return "Le point A est sur le cercle."
        else:
            return "Le point A n'appartient pas au cercle."
        