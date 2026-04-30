"""
Soit les classes suivantes :
1. La classe « Chaine », qui comporte un attribut : chaine_de_caracteres de type chaîne de
caractères.
2. Cette classe comporte un constructeur pour permettre d&#39;initialiser cet attribut. Elle
comporte également une méthode polymorphe « afficher() » permettant d’afficher la
chaîne de caractères.
3. La classe « Phrase », qui hérite de la classe « Chaine », avec en plus un attribut langue, un
constructeur et la redéfinition de la méthode « afficher() », qui permet d’afficher la langue
(anglaise ou française) de la phrase. Cette classe possède également la méthode « type() »
permettant de retourner le type de la phrase, qui peut être : déclaratif, interrogatif ou
exclamatif. La classe « Phrase » possède aussi la méthode « longueurMot() » servant à
retourner le mot le plus long de la phrase avec sa longueur.
4. Tester les différentes méthodes des classes précédemment définies, avec plusieurs
exemples de phrases anglaises et françaises.
"""

class Chaine:

    def __init__(self,chaine_de_caracteres):
        self.chaine_de_caracteres=chaine_de_caracteres

    def afficher(self):
        print(self.chaine_de_caracteres)

class Phrase(Chaine):

    def __init__(self,chaine_de_caracteres, langue):
        super().__init__(chaine_de_caracteres)
        self.langue=langue

    def afficher(self):
        print(f"Langue: {self.langue},Phrase: {self.chaine_de_caracteres}")

    def type(self):
        if self.chaine_de_caracteres.endswith('.'):
            return "déclaratif"
        elif self.chaine_de_caracteres.endswith('?'):
            return "interrogatif"
        elif self.chaine_de_caracteres.endswith('!'):
            return "exclamatif"
        else:
            return "inconnu"

    def longueurMot(self):
        mots=self.chaine_de_caracteres.split()
        mot_le_plus_long=max(mots,key=len)
        return mot_le_plus_long,len(mot_le_plus_long)
        