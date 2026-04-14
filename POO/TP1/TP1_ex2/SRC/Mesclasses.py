"""
On souhaite créer une classe Livre pour gérer les livres d’une bibliothèque. Chaque livre possède
les informations suivantes :
1. id
2. titre
3. auteur
4. nombre de pages
5. prix
La bibliothèque possède également une information commune à tous les livres : nom de la
bibliothèque.
1. Créer une classe appelée Livre.
2. Ajouter une documentation de la classe expliquant son rôle.
3. Créer un attribut de classe bibliotheque initialisé avec le nom BiblioTech.
4. Créer un constructeur permettant d’initialiser : id, titre, auteur, pages, _prix (attribut
protégé).
5. Créer :
a. un getter permettant de récupérer le prix
b. un setter permettant de modifier le prix
6. Créer une méthode qui affiche les informations du livre.
7. Créer une méthode permettant de calculer le prix moyen par page.
8. Redéfinir la méthode __str__ pour afficher les informations du livre sous forme lisible.
9. Créer une méthode de classe permettant de modifier le nom de la bibliothèque.
10. Dans le programme principal :
a. créer deux objets Livre
b. afficher la documentation de la classe
c. afficher les livres
d. modifier le prix d’un livre
e. afficher le prix par page
f. modifier le nom de la bibliothèque avec la méthode de classe
g. afficher la bibliothèque associée aux livres.
"""

class Livre:
    """
    La classe Livre représente un livre dans une bibliothèque. Elle contient des informations telles que l'identifiant, le titre, l'auteur, le nombre de pages et le prix du livre. La classe permet également de calculer le prix moyen par page et de modifier le nom de la bibliothèque associée à tous les livres.
    """

    bibliotheque = "BiblioTech"

    def __init__(self, id, titre, auteur, pages, prix):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self._prix = prix

    def get_prix(self):
        return self._prix

    def set_prix(self, nouveau_prix):
        self._prix = nouveau_prix

    def afficher_info(self):
        print(f"ID: {self.id}, Titre: {self.titre}, Auteur: {self.auteur}, Pages: {self.pages}, Prix: {self._prix}")

    def prix_par_page(self):
        if self.pages > 0:
            return self._prix / self.pages
        else:
            return 0

    @classmethod
    def modifier_bibliotheque(cls, nouveau_nom):
        cls.bibliotheque = nouveau_nom

    def __str__(self):
        return f"ID: {self.id}, Titre: {self.titre}, Auteur: {self.auteur}, Pages: {self.pages}, Prix: {self._prix}"


    