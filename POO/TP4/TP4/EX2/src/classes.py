"""
On souhaite créer un programme qui gère des formes géométriques et les affiche à l’écran.
1. Créer une classe abstraite Forme qui contient :
a. un attribut : nom
b. deux méthodes abstraites :
i. calculer_aire()
ii. dessiner()
2. Créer les classes suivantes :
Classe Rectangle :
Attributs : longueur, largeur
Méthodes :
 calculer_aire() → longueur × largeur
 dessiner() → afficher un rectangle avec *
Classe Triangle :
Attribut : hauteur
Méthodes :
 calculer_aire() → (base × hauteur) / 2
 dessiner() → triangle avec *
"""

from abc import ABC, abstractmethod

class Forme(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def calculer_aire(self):
        pass

    @abstractmethod
    def dessiner(self):
        pass

class Rectangle(Forme):
    def __init__(self, nom, longueur, largeur):
        super().__init__(nom)
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        return self.longueur * self.largeur

    def dessiner(self):
        for i in range(self.largeur):
            print('*' * self.longueur)

class Triangle(Forme):
    def __init__(self, nom, base, hauteur):
        super().__init__(nom)
        self.base = base
        self.hauteur = hauteur

    def calculer_aire(self):
        return (self.base * self.hauteur) / 2

    def dessiner(self):
        for i in range(1, self.hauteur + 1):
            print(' ' * (self.hauteur - i) + '*' * (2 * i - 1))

