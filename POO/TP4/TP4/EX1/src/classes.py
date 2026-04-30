"""
1. Créer une classe abstraite Vehicule contenant les attributs marque et vitesse.
2. Déclarer dans cette classe une méthode abstraite demarrer() qui affiche un message
indiquant que le véhicule démarre.
3. Déclarer une deuxième méthode abstraite calculer_vitesse() qui retourne la vitesse du
véhicule.
4. Créer une méthode concrète afficher_infos() qui affiche la marque et la vitesse.
5. Créer une classe Voiture qui hérite de Vehicule.
a. Implémenter la méthode demarrer() pour afficher &quot;La voiture démarre&quot;.
b. Implémenter calculer_vitesse() pour retourner la vitesse telle quelle.
6. Créer une classe Moto qui hérite de Vehicule.
a. Implémenter la méthode demarrer() pour afficher &quot;La moto démarre&quot;.
b. Implémenter calculer_vitesse() en ajoutant 10 à la vitesse
7. Dans le programme principal, créer un objet de chaque type avec une vitesse donnée.
8. Pour chaque véhicule, afficher ses informations, le faire démarrer et afficher sa vitesse
calculée.
"""

from abc import ABC, abstractmethod

class Vehicule(ABC):

    def __init__(self,marque,vitesse):
        self.marque=marque
        self.vitesse=vitesse

    @abstractmethod
    def demarrer(self):
        pass

    @abstractmethod
    def calculer_vitesse(self):
        pass

    def afficher_infos(self):
        print(f"Marque:{self.marque},Vitesse:{self.vitesse}")
    
class Voiture(Vehicule):

    def demarrer(self):
        print("La voiture démarre")

    def calculer_vitesse(self):
        return self.vitesse

class Moto(Vehicule):

    def demarrer(self):
        print("La moto démarre")

    def calculer_vitesse(self):
        return self.vitesse + 10

