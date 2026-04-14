"""
On souhaite créer une application simple permettant de gérer les informations d’un étudiant.
Un étudiant possède les informations suivantes :
 id
 nom
 âge
 moyenne
L’âge doit être protégé pour éviter des valeurs incorrectes.
1. Créer une classe appelée Etudiant.
2. Déclarer dans le constructeur les attributs suivants : id, nom, age (attribut privé), moyenne.
3. Initialiser ces attributs dans le constructeur.
4. Créer une méthode getter permettant de récupérer l’âge de l’étudiant.
5. Créer une méthode setter permettant de modifier l’âge avec la condition : l&#39;âge doit être supérieur
à 0.
6. Dans le programme principal :
a. créer un objet Etudiant
b. modifier l’âge
c. afficher toutes les informations de l’étudiant.
"""

#1
class Etudiant:
    def __init__(self, id, nom, age, moyenne):
        self.id = id
        self.nom = nom
        self.__age = age
        self.moyenne = moyenne
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("L'âge doit être supérieur à 0.")     


    
