"""
1. Créer une classe Calcul ayant un constructeur par défaut (sans paramètres) permettant
d&#39;effectuer différents calculs sur les nombres entiers.
2. Créer au sein de la classe Calcul une méthode nommée Factorielle() qui permet de
calculer le factorielle d&#39;un entier. Tester la méthode en faisant une instanciation sur la
classe.
3. Créer au sein de la classe Calcul une méthode nommée Somme() permettant de calculer la
somme des n premiers entiers 1+2+3+..+n. Tester la méthode.
4. Créer une méthode tableMult() qui crée et ache la table de multiplication d&#39;un entier
donné. Créer ensuite une méthode allTablesMult() permettant d&#39;acfficher toutes les tables
de multiplications des entiers 1, 2, 3, ..., 9.
5. Créer une méthode listDiv() qui récupère tous les diviseurs d&#39;un entier donné sur une liste
Ldiv.
6. Créer une autre méthode listDivPrim() qui récupère tous les diviseurs premiers d&#39;un entier
donné.
"""
import math

class Calcul:
    def __init__(self):
        pass

    def Factorielle(self, n):   
        if n < 0:
            return "Factorielle n'est pas définie pour les nombres négatifs."
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
    def Somme(self, n):
        if n < 1:
            return "La somme n'est pas définie pour les nombres inférieurs à 1."
        else:
            return n * (n + 1) // 2
    def tableMult(self, n):
        if n < 1:
            return "La table de multiplication n'est pas définie pour les nombres inférieurs à 1."
        else:
            table = []
            for i in range(1, 11):
                table.append(f"{n} x {i} = {n * i}")
            return table
    def allTablesMult(self):
        all_tables = {}
        for n in range(1, 10):
            all_tables[n] = self.tableMult(n)
        return all_tables
    def listDiv(self, n):
        if n < 1:
            return "La liste des diviseurs n'est pas définie pour les nombres inférieurs à 1."
        else:
            Ldiv = []
            for i in range(1, n + 1):
                if n % i == 0:
                    Ldiv.append(i)
            return Ldiv
    def listDivPrim(self, n):
        if n < 1:
            return "La liste des diviseurs premiers n'est pas définie pour les nombres inférieurs à 1."
        else:
            diviseurs_prim = []
            for i in range(2, n + 1):
                if n % i == 0 and self.is_prime(i):
                    diviseurs_prim.append(i)
            return diviseurs_prim
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True