"""
Une salle possède :
 nom
 capacité
 _places_occupees

Travail demandé :
1. Créer la classe SalleCinema
2. Initialiser les attributs
3. Créer une méthode reserver(nb_places) :
o vérifier si les places sont disponibles
o sinon refuser
4. Créer une méthode annuler(nb_places) :
o ne pas dépasser le nombre réservé
5. Créer une méthode taux_remplissage() :

o retourne le pourcentage d’occupation
6. Créer une méthode afficher()
"""

class SalleCinema:

    def __init__(self,nom,cap,occ):
        self.nom=nom
        self.capacite=cap
        self._places_occupees=occ

    def reserver(self,nb_places):
        if nb_places<=self.capacite-self._places_occupees:
            print("accepter")
            self._places_occupees+=nb_places
        else:
            print("refuser")

    def annuler(self,nb_places):
        if nb_places<=self._places_occupees:
            print("accepter")
            self._places_occupees-=nb_places
        else:
            print("refuser")
    
    def taux_remplissage(self):
        return (self._places_occupees/self.capacite)*100
    
    
        