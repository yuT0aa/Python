"""
Un compte possède :
 id
 nom
 __tentatives (privé)
 __mot_de_passe (privé)

Travail demandé :
1. Créer la classe CompteSecurise
2. Initialiser :
o tentatives = 0
3. Créer une méthode verifier_mot_de_passe(mdp) :
o si correct → afficher &quot;Accès autorisé&quot;
o sinon :
 incrémenter tentatives
 si tentatives ≥ 3 → afficher &quot;Compte bloqué&quot;
4. Créer une méthode changer_mot_de_passe(ancien, nouveau) :
o vérifier ancien mot de passe
o vérifier longueur ≥ 6
5. personnaliser l’affichage de l’objet sous la forme : &quot;Compte : id - Nom : nom - Tentatives
: tentatives&quot;
6. Créer un destructeur qui affiche le message &quot;Compte supprimé&quot; lorsque l’objet n’est plus
référencé.
7. Tester avec plusieurs tentatives
"""

class CompteSecurise:

    def __init__(self,id,nom,password):
        self.id=id
        self.nom=nom
        self.__tentatives=0
        self.__mot_de_passe=password
    
    def verifier_mot_de_passe(self,password):
        if password==self.__mot_de_passe:
            print("Autorise")
        else:
            print("acces bloque")
            self.__tentatives+=1
            if self.__tentatives>=3:
                print("bloque")
    
    def changer_mot_de_passe(self,ancien_password,new_password):
        if ancien_password==self.__mot_de_passe:
            if len(new_password)>=6:
                self.__mot_de_passe=new_password
            else:
                print("faible")
        else:
            print("incorrect")
    
    def del_compte(self):
        del self
        print("compte supprime")

    