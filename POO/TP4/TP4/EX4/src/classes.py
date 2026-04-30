"""
On souhaite développer un système capable de corriger automatiquement différents types
d’évaluations.
1. Créer une classe abstraite Correcteur, qui a comme attributs :
 reponses_etudiant : réponses fournies par l’étudiant
 correction : réponses correctes (référence)
2. Créer les méthodes abstraites suivantes au niveau de la classe Correcteur :

 est_valide() : Doit vérifier si les réponses sont exploitables, c’est-à-dire :
 complètes

 du bon type
 calculer_score() : comparer les réponses de l’étudiant avec la correction et
retourne une note numérique, cette méthode ne doit être appelée que si
est_valide() retourne True.
 afficher_resultat() :
 Score
 Valide (True/False)
3. Créer une classe CorrecteurQCM :
Données attendues :
correction = [&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;]
reponses_etudiant = [&quot;A&quot;, &quot;C&quot;, &quot;C&quot;, &quot;D&quot;]
 est_valide() : Retourne True si et seulement si :
o len(reponses_etudiant) == len(correction)
o chaque réponse appartient à : &quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;
o aucune réponse vide
 calculer_score() : Pour chaque question :
o +1 → réponse correcte
o -0.25 → réponse incorrecte
 afficher_resultat() :
 Score
 Valide (True/False)
4. Créer une classe CorrecteurCode :
Données attendues :
correction = [True, True, False, True]
reponses_etudiant = [True, False, False, True]
 est_valide() : Retourne True si et seulement si :
o len(reponses_etudiant) == len(correction)
o chaque élément de reponses_etudiant est de type bool
 calculer_score() = nombre de tests réussis
 afficher_resultat() :
o Score
o Valide (True/False)
5. Créer une classe CorrecteurRedaction :
Données attendues :
correction = [&quot;IA&quot;, &quot;données&quot;, &quot;algorithme&quot;]
reponses_etudiant = &quot;L&#39;IA utilise des algorithmes pour traiter les données&quot;
 est_valide() : Retourne True si et seulement si :
o reponses_etudiant est une chaîne de caractères
o longueur ≥ 50 caractères
o la réponse contient les mots clés spécifiés dans la correction
 calculer_score() = nombre de mots clés présents, pour chaque mot dans correction :
+1 si le mot est présent dans le texte (insensible à la casse)

 afficher_resultat() :
o Score
o Valide (True/False)

6. Teter les classes crées au niveau du programme principale
7. Ajouter un attribut dans la classe Correcteur : numero_place (position de l’étudiant en
salle)
8. Créer une fonction detection_fraude(liste_evaluations), avec liste_evaluations sont des
objets de même type, travail demandé :
 Pour chaque paire d’étudiants :
o Calculer la similarité = (nombre de réponses identiques / nombre total) ×
100
o Une fraude est détectée si : similarité ≥ 80% et étudiants assis à côté
o Résultat attendu : Fraude détectée entre étudiant place 5 et place 6
(similarité : 85%)
"""

from abc import ABC, abstractmethod

class Correcteur(ABC):
    def __init__(self, reponses_etudiant, correction, numero_place):
        self.reponses_etudiant = reponses_etudiant
        self.correction = correction
        self.numero_place = numero_place

    @abstractmethod
    def est_valide(self):
        pass

    @abstractmethod
    def calculer_score(self):
        pass

    @abstractmethod
    def afficher_resultat(self):
        pass

class CorrecteurQCM(Correcteur):
    def est_valide(self):
        if len(self.reponses_etudiant) != len(self.correction):
            return False
        for reponse in self.reponses_etudiant:
            if reponse not in ["A", "B", "C", "D"] or reponse == "":
                return False
        return True

    def calculer_score(self):
        score = 0
        for reponse, correction in zip(self.reponses_etudiant, self.correction):
            if reponse == correction:
                score += 1
            else:
                score -= 0.25
        return score

    def afficher_resultat(self):
        valide = self.est_valide()
        score = self.calculer_score() if valide else 0
        print(f"Score: {score}")
        print(f"Valide: {valide}")

class CorrecteurCode(Correcteur):
    def est_valide(self):
        if len(self.reponses_etudiant) != len(self.correction):
            return False
        for reponse in self.reponses_etudiant:
            if not isinstance(reponse, bool):
                return False
        return True

    def calculer_score(self):
        score = sum(1 for reponse, correction in zip(self.reponses_etudiant, self.correction) if reponse == correction)
        return score

    def afficher_resultat(self):
        valide = self.est_valide()
        score = self.calculer_score() if valide else 0
        print(f"Score: {score}")
        print(f"Valide: {valide}")

class CorrecteurRedaction(Correcteur):
    def est_valide(self):
        if not isinstance(self.reponses_etudiant, str) or len(self.reponses_etudiant) < 50:
            return False
        for mot in self.correction:
            if mot.lower() not in self.reponses_etudiant.lower():
                return False
        return True

    def calculer_score(self):
        score = sum(1 for mot in self.correction if mot.lower() in self.reponses_etudiant.lower())
        return score

    def afficher_resultat(self):
        valide = self.est_valide()
        score = self.calculer_score() if valide else 0
        print(f"Score: {score}")
        print(f"Valide: {valide}")

def detection_fraude(liste_evaluations):
    for i in range(len(liste_evaluations)):
        for j in range(i + 1, len(liste_evaluations)):
            eval1 = liste_evaluations[i]
            eval2 = liste_evaluations[j]
            if abs(eval1.numero_place - eval2.numero_place) == 1:
                total = len(eval1.reponses_etudiant)
                identiques = sum(1 for r1, r2 in zip(eval1.reponses_etudiant, eval2.reponses_etudiant) if r1 == r2)
                similarite = (identiques / total) * 100
                if similarite >= 80:
                    print(f"Fraude détectée entre étudiant place {eval1.numero_place} et place {eval2.numero_place} (similarité : {similarite:.2f}%)")

