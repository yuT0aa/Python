"""
1. Créer une classe abstraite Pret contenant les attributs nom_utilisateur,
nb_livres_empruntes et jours_retard.
2. Ajouter dans cette classe une méthode concrète est_en_retard() qui retourne True si le
nombre de jours de retard est supérieur à 0, sinon False.
3. Déclarer les méthodes abstraites suivantes dans la classe Pret : peut_emprunter(),
calculer_penalite() et type_utilisateur().
4. Créer une classe Etudiant qui hérite de Pret.
a. Implémenter la méthode peut_emprunter() pour retourner False si le nombre de
livres empruntés est supérieur ou égal à 3 ou si le retard dépasse 5 jours, sinon
retourner True.
b. Implémenter calculer_penalite() pour calculer une pénalité égale à 2 DH multiplié
par le nombre de jours de retard, et ajouter 10 DH supplémentaires si le retard
dépasse 10 jours.
c. Implémenter type_utilisateur() pour retourner &quot;Etudiant&quot;.
5. Créer une classe Professeur qui hérite de Pret.
a. Implémenter peut_emprunter() pour refuser uniquement si le nombre de livres
empruntés est supérieur ou égal à 10.
b. Implémenter calculer_penalite() pour retourner 1 DH multiplié par le nombre de
jours de retard, et 0 si aucun retard.
c. Implémenter type_utilisateur() pour retourner &quot;Professeur&quot;.
6. Créer une classe Externe qui hérite de Pret.
a. Implémenter peut_emprunter() pour retourner False si le nombre de livres est
supérieur ou égal à 2 ou si le nombre de jours de retard est supérieur à 0.
b. Implémenter calculer_penalite() pour calculer 5 DH multiplié par le nombre de
jours de retard, et doubler cette pénalité si le retard dépasse 3 jours.
c. Implémenter type_utilisateur() pour retourner &quot;Externe&quot;.
7. Dans le programme principal, créer trois objets de types différents avec des valeurs de
test.
8. Pour chaque objet, afficher le type d’utilisateur, vérifier s’il peut emprunter, indiquer s’il
est en retard et afficher la pénalité.
9. Pourquoi est_en_retard() est dans la classe abstraite ?
"""

from abc import ABC,abstractmethod

class Pret(ABC):
    def __init__(self, nom_utilisateur, nb_livres_empruntes, jours_retard):
        self.nom_utilisateur = nom_utilisateur
        self.nb_livres_empruntes = nb_livres_empruntes
        self.jours_retard = jours_retard

    def est_en_retard(self):
        return self.jours_retard > 0

    @abstractmethod
    def peut_emprunter(self):
        pass

    @abstractmethod
    def calculer_penalite(self):
        pass

    @abstractmethod
    def type_utilisateur(self):
        pass

class Etudiant(Pret):
    def __init__(self, nom_utilisateur, nb_livres_empruntes, jours_retard):
        super().__init__(nom_utilisateur, nb_livres_empruntes, jours_retard)

    def peut_emprunter(self):
        return self.nb_livres_empruntes < 3 and self.jours_retard <= 5

    def calculer_penalite(self):
        penalite = 2 * self.jours_retard
        if self.jours_retard > 10:
            penalite += 10
        return penalite

    def type_utilisateur(self):
        return "Etudiant"

class Professeur(Pret):
    def __init__(self, nom_utilisateur, nb_livres_empruntes, jours_retard):
        super().__init__(nom_utilisateur, nb_livres_empruntes, jours_retard)

    def peut_emprunter(self):
        return self.nb_livres_empruntes < 10

    def calculer_penalite(self):
        return self.jours_retard if self.jours_retard > 0 else 0

    def type_utilisateur(self):
        return "Professeur"

class Externe(Pret):
    def __init__(self, nom_utilisateur, nb_livres_empruntes, jours_retard):
        super().__init__(nom_utilisateur, nb_livres_empruntes, jours_retard)

    def peut_emprunter(self):
        return self.nb_livres_empruntes < 2 and self.jours_retard == 0

    def calculer_penalite(self):
        penalite = 5 * self.jours_retard
        if self.jours_retard > 3:
            penalite *= 2
        return penalite

    def type_utilisateur(self):
        return "Externe"
    