"""
1. Créer une classe Python nommée CompteBancaire qui représente un compte bancaire,
ayant pour attributs : numeroCompte (type numérique ) , nom (nom du propriétaire du
compte du type chaine), solde.
2. Créer un constructeur ayant comme paramètres : numeroCompte, nom, solde.
3. Créer une méthode Versement() qui gère les versements.
4. Créer une méthode Retrait() qui gère les retraits.
5. Créer une méthode Agios() permettant d&#39;appliquer les agios à un pourcentage de 5 % du
solde.
6. Créer une méthode acher() permettant d&#39;acher les détails sur le compte.
7. Donner le code complet de la classe CompteBancaire.
"""

class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def Versement(self, montant):
        self.solde += montant

    def Retrait(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Fonds insuffisants pour le retrait.")

    def Agios(self):
        agios = self.solde * 0.05
        self.solde -= agios

    def Afficher(self):
        print(f"Numéro de Compte: {self.numeroCompte}")
        print(f"Nom du Propriétaire: {self.nom}")
        print(f"Solde: {self.solde:.2f}")
