from src.classes import Etudiant,Externe

if __name__ == "__main__":
    etudiant = Etudiant("Alice", 2, 3)
    print(f"{etudiant.type_utilisateur()} {etudiant.nom_utilisateur} peut emprunter : {etudiant.peut_emprunter()}")
    print(f"Pénalité pour {etudiant.nom_utilisateur} : {etudiant.calculer_penalite()}")

    externe = Externe("Bob", 1, 4)
    print(f"{externe.type_utilisateur()} {externe.nom_utilisateur} peut emprunter : {externe.peut_emprunter()}")
    print(f"Pénalité pour {externe.nom_utilisateur} : {externe.calculer_penalite()}")