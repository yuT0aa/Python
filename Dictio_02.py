# Programme de gestion des employés
# Chaque employé est un dictionnaire avec les clés : id, nom, departement, salaire

# Liste initiale des employés
employes = [
    {"id": 1, "nom": "Alice Dupont", "departement": "Informatique", "salaire": 50000},
    {"id": 2, "nom": "Bob Martin", "departement": "Ressources Humaines", "salaire": 45000},
    {"id": 3, "nom": "Charlie Durand", "departement": "Informatique", "salaire": 55000},
    {"id": 4, "nom": "Diana Leroy", "departement": "Finance", "salaire": 60000},
]

# Fonction pour afficher tous les employés
def afficher_employes():
    if not employes:
        print("Aucun employé dans la liste.")
        return
    for employe in employes:
        print(employe)

# Fonction pour ajouter un nouvel employé
def ajouter_employe(id, nom, departement, salaire):
    # Vérifier si l'id existe déjà
    if any(e["id"] == id for e in employes):
        print(f"Erreur : Un employé avec l'id {id} existe déjà.")
        return
    nouvel_employe = {"id": id, "nom": nom, "departement": departement, "salaire": salaire}
    employes.append(nouvel_employe)
    print(f"Employé ajouté : {nouvel_employe}")

# Fonction pour modifier le département ou le salaire d’un employé
def modifier_employe(id, champ, nouvelle_valeur):
    for employe in employes:
        if employe["id"] == id:
            if champ in ["departement", "salaire"]:
                if champ == "salaire":
                    nouvelle_valeur = float(nouvelle_valeur)
                employe[champ] = nouvelle_valeur
                print(f"Employé modifié : {employe}")
                return
            else:
                print("Champ invalide. Utilisez 'departement' ou 'salaire'.")
                return
    print(f"Aucun employé trouvé avec id {id}.")

# Fonction pour supprimer un employé
def supprimer_employe(id):
    global employes
    employes = [e for e in employes if e["id"] != id]
    print(f"Employé avec id {id} supprimé (si existant).")

# Fonction pour rechercher un employé par nom
def rechercher_employe(nom):
    resultats = [e for e in employes if nom.lower() in e["nom"].lower()]
    if resultats:
        for r in resultats:
            print(r)
    else:
        print("Aucun employé trouvé.")

# Fonction pour regrouper les employés par département
def regrouper_par_departement():
    groupes = {}
    for employe in employes:
        dep = employe["departement"]
        if dep not in groupes:
            groupes[dep] = []
        groupes[dep].append(employe)
    for dep, liste in groupes.items():
        print(f"\nDépartement : {dep}")
        for emp in liste:
            print(f"  - {emp['nom']} (ID: {emp['id']}, Salaire: {emp['salaire']})")

# Fonction pour trouver l’employé le mieux rémunéré
def employe_mieux_remunere():
    if not employes:
        print("Aucun employé dans la liste.")
        return
    max_salaire = max(e["salaire"] for e in employes)
    meilleurs = [e for e in employes if e["salaire"] == max_salaire]
    print("Employé(s) le(s) mieux rémunéré(s) :")
    for emp in meilleurs:
        print(emp)

# Fonction pour lister tous les départements existants (avec set)
def lister_departements():
    departements = {e["departement"] for e in employes}
    print("Départements existants :", departements)
    return departements

# Menu interactif
if __name__ == "__main__":
    while True:
        print("\n--- Menu de gestion des employés ---")
        print("1. Afficher tous les employés")
        print("2. Ajouter un nouvel employé")
        print("3. Modifier le département ou le salaire d’un employé")
        print("4. Supprimer un employé")
        print("5. Rechercher un employé par nom")
        print("6. Regrouper les employés par département")
        print("7. Trouver l’employé le mieux rémunéré")
        print("8. Lister tous les départements existants")
        print("0. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            afficher_employes()
        elif choix == "2":
            id = int(input("ID : "))
            nom = input("Nom : ")
            departement = input("Département : ")
            salaire = float(input("Salaire : "))
            ajouter_employe(id, nom, departement, salaire)
        elif choix == "3":
            id = int(input("ID de l'employé : "))
            champ = input("Champ à modifier (departement/salaire) : ")
            nouvelle_valeur = input("Nouvelle valeur : ")
            modifier_employe(id, champ, nouvelle_valeur)
        elif choix == "4":
            id = int(input("ID à supprimer : "))
            supprimer_employe(id)
        elif choix == "5":
            nom = input("Nom à rechercher : ")
            rechercher_employe(nom)
        elif choix == "6":
            regrouper_par_departement()
        elif choix == "7":
            employe_mieux_remunere()
        elif choix == "8":
            lister_departements()
        elif choix == "0":
            break
        else:
            print("Option invalide.")

    print("\n--- Fin du programme ---")