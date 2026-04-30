"""
Un hôpital souhaite développer une application permettant de gérer différents types de patients.
Chaque patient possède des informations communes, mais sa priorité, son traitement et le coût
associé varient selon son type.
Objectifs
 Utiliser l’héritage
 Appliquer le polymorphisme
 Redéfinir des méthodesUn hôpital souhaite développer une application permettant de gérer différents types de patients.
Chaque patient possède des informations communes, mais sa priorité, son traitement et le coût
associé varient selon son type.
Objectifs
 Utiliser l’héritage
 Appliquer le polymorphisme
 Redéfinir des méthodes
 Surcharger des opérateurs
 Manipuler des objets
1. Créer une classe Patient contenant :
 nom (chaîne de caractères)
 age (entier positif)
2. Ajouter une méthode def afficher(self), cette méthode doit afficher : Nom : X | Age : Y
3. Créer les classes suivantes héritant de Patient :
 PatientNormal
 PatientUrgent
 PatientVIP
Remarque : Ces classes ne contiennent pas d’attributs supplémentaires pour le moment.

4. Ajouter dans la classe Patient la méthode priorite(self) puis la redéfinir dans chaque classe
fille, cette méthode doit retourner un entier représentant la priorité du patient.
 PatientNormal → retourne 1 (priorité faible)
 PatientUrgent → retourne 2 (priorité élevée)
 PatientVIP → retourne 3 (priorité maximale)
5. Créer une fonction traiter_patient(patient)cette fonction doit :
 afficher les informations du patient
 afficher sa priorité sans tester son type (if type(...) interdit)

6. Créer une liste contenant plusieurs patients de types différents, parcourir la liste et appeler
traiter_patient() pour chaque patient.
7. Redéfinir l’opérateur &gt; dans la classe Patient afin de comparer deux patients selon leur
priorité. (p1 &gt; p2 doit retourner True si p1 est plus prioritaire que p2, sinon False)
8. Redéfinir la méthode __str__(self), cette méthode doit retourner une chaîne de la forme,
Nom : Ali | Age : 30 | Type : PatientUrgent
9. Ajouter la méthode cout_traitement(self), cette méthode doit retourner un coût (en DH)
selon le type :
 PatientNormal → 100 DH
 PatientUrgent → 150 DH
 PatientVIP → 200 DH
10. Créer une fonction statistiques(patients) qui retourne :
 nombre de patients par type
 patient le plus prioritaire
 coût total des traitements
 Surcharger des opérateurs
 Manipuler des objets
1. Créer une classe Patient contenant :
 nom (chaîne de caractères)
 age (entier positif)
2. Ajouter une méthode def afficher(self), cette méthode doit afficher : Nom : X | Age : Y
3. Créer les classes suivantes héritant de Patient :
 PatientNormal
 PatientUrgent
 PatientVIP
Remarque : Ces classes ne contiennent pas d’attributs supplémentaires pour le moment.

4. Ajouter dans la classe Patient la méthode priorite(self) puis la redéfinir dans chaque classe
fille, cette méthode doit retourner un entier représentant la priorité du patient.
 PatientNormal → retourne 1 (priorité faible)
 PatientUrgent → retourne 2 (priorité élevée)
 PatientVIP → retourne 3 (priorité maximale)
5. Créer une fonction traiter_patient(patient)cette fonction doit :
 afficher les informations du patient
 afficher sa priorité sans tester son type (if type(...) interdit)

6. Créer une liste contenant plusieurs patients de types différents, parcourir la liste et appeler
traiter_patient() pour chaque patient.
7. Redéfinir l’opérateur &gt; dans la classe Patient afin de comparer deux patients selon leur
priorité. (p1 &gt; p2 doit retourner True si p1 est plus prioritaire que p2, sinon False)
8. Redéfinir la méthode __str__(self), cette méthode doit retourner une chaîne de la forme,
Nom : Ali | Age : 30 | Type : PatientUrgent
9. Ajouter la méthode cout_traitement(self), cette méthode doit retourner un coût (en DH)
selon le type :
 PatientNormal → 100 DH
 PatientUrgent → 150 DH
 PatientVIP → 200 DH
10. Créer une fonction statistiques(patients) qui retourne :
 nombre de patients par type
 patient le plus prioritaire
 coût total des traitements
"""

class Patient:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher(self):
        print(f"Nom : {self.nom} | Age : {self.age}")

    def priorite(self):
        return 0  # Priorité par défaut pour la classe de base

    def cout_traitement(self):
        return 0  # Coût par défaut pour la classe de base

    def __gt__(self, other):
        return self.priorite() > other.priorite()

    def __str__(self):
        return f"Nom : {self.nom} | Age : {self.age} | Type : {self.__class__.__name__}"

class PatientNormal(Patient):
    def priorite(self):
        return 1

    def cout_traitement(self):
        return 100

class PatientUrgent(Patient):
    def priorite(self):
        return 2

    def cout_traitement(self):
        return 150

class PatientVIP(Patient):
    def priorite(self):
        return 3

    def cout_traitement(self):
        return 200

def traiter_patient(patient):
    patient.afficher()
    print(f"Priorité : {patient.priorite()}")
    print(f"Coût du traitement : {patient.cout_traitement()} DH")

def statistiques(patients):
    count_normal = sum(isinstance(p, PatientNormal) for p in patients)
    count_urgent = sum(isinstance(p, PatientUrgent) for p in patients)
    count_vip = sum(isinstance(p, PatientVIP) for p in patients)

    patient_prioritaire = max(patients, key=lambda p: p.priorite())
    cout_total = sum(p.cout_traitement() for p in patients)

    return {
        "nombre_patients": {
            "PatientNormal": count_normal,
            "PatientUrgent": count_urgent,
            "PatientVIP": count_vip
        },
        "patient_prioritaire": patient_prioritaire,
        "cout_total": cout_total
    }

