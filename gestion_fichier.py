"""
Créer un programme Python qui gère des données (une liste de dictionnaires) et permet : 
• d’ajouter, afficher, modifier et supprimer des données 
• de sauvegarder les données dans trois formats : JSON, CSV, et TXT 
• de charger les données depuis ces trois formats 
• de gérer toutes les actions via un menu interactif 
"""

donnee=[
    {"id":1,"nom":"John Doe","age":30},
    {"id":2,"nom":"Jane Smith","age":25},
    {"id":3,"nom":"Alice Johnson","age":28}    
]

def afficher_menu():
    print("""
            ----- MENU ----- 
        1. Ajouter un nouvel enregistrement 
        2. Afficher toutes les données 
        3. Modifier un enregistrement 
        4. Supprimer un enregistrement 
        5. Sauvegarder (JSON / CSV / TXT) 
        6. Charger (JSON / CSV / TXT) 
        0. Quitter 
            ----------------
    """)
    
def ajouter_donnee(liste):
    info={
        "id":int,
        "nom":str,
        "age":int
    }
    info["id"]=int(input("ID="))
    info["nom"]=input("nom=")
    info["age"]=int(input("age="))
    liste.append(info)
    print("info ajoutée avec succès.")
    
def afficher_donnes(liste):
    for info in liste:
        print(info)
        
def modifier_donnee(liste):
    while True:
        id_mod=int(input("Entrez l'ID de l'enregistrement à modifier: "))
        if id_mod.isdigit():
            id_mod=int(id_mod)
            for info in liste:
                if info["id"]==id_mod:
                    info["nom"]=input("Nouveau nom=")
                    while True:
                        age_nouv=input("Nouvel age=")
                        if age_nouv.isdigit():
                            info["age"]=int(age_nouv)
                            break
                    print("info modifiée avec succès.")
                    return
            else:
                print("ID non trouvé.")

def supprimer_donnee(liste):
    while True:
        id_sup=input("Entrez l'ID de l'enregistrement à supprimer: ")
        if id_sup.isdigit():
            id_sup=int(id_sup)
            for info in liste:
                if info["id"]==id_sup:
                    liste.remove(info)
                    print("info supprimée avec succès.")
                    return
            else:
                print("ID non trouvé.")


def save_json(liste, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(liste, f)
    print("Données sauvegardées en JSON.")

def  save_csv(liste, filename):
    import csv
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nom", "age"])
        writer.writeheader()
        writer.writerows(liste)
    print("Données sauvegardées en CSV.")
    

def save_txt(liste, filename):
    with open(filename, 'w') as f:
        for info in liste:
            f.write(f"{info['id']} - {info['nom']} - {info['age']}\n")
    print("Données sauvegardées en TXT.")

def load_json(filename):
    import json
    with open(filename, 'r') as f:
        liste = json.load(f)
    return liste

def  load_csv(filename):
    import csv
    liste = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
    return liste
    
def load_txt(filename):
    liste = []
    with open(filename, 'r') as f:
        for line in f:
            id_str, nom, age_str = line.strip().split(' - ')
            info = {
                "id": int(id_str),
                "nom": nom,
                "age": int(age_str)
            }
            liste.append(info)
    return liste

def main():
    data=[]
    while True:
        afficher_menu()
        choix=input("Choisissez une option: ")
        if choix=='1':
            ajouter_donnee(data)
        elif choix=='2':
            afficher_donnes(data)
        elif choix=='3':
            modifier_donnee(data)
        elif choix=='4':
            supprimer_donnee(data)
        elif choix=='5':
            format_sauvegarde=input("Format de sauvegarde (json/csv/txt): ").lower()
            filename=input("Nom du fichier: ")
            if format_sauvegarde=='json':
                save_json(data, filename)
            elif format_sauvegarde=='csv':
                save_csv(data, filename)
            elif format_sauvegarde=='txt':
                save_txt(data, filename)
            else:
                print("Format non supporté.")
        elif choix=='6':
            format_chargement=input("Format de chargement (json/csv/txt): ").lower()
            filename=input("Nom du fichier: ")
            if format_chargement=='json':
                data=load_json(filename)
            elif format_chargement=='csv':
                data=load_csv(filename)
            elif format_chargement=='txt':
                data=load_txt(filename)
            else:
                print("Format non supporté.")
        elif choix=='0':
            print("run again")
            break
        else:
            print("Option invalide")
main()