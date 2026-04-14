import json
import csv

bibliotheque = [ 
{"id": 1, "titre": "1984", "auteur": "George Orwell", "categorie": "Science-Fiction", "prix": 120, "quantite": 4}, 
{"id": 2, "titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "categorie": "Roman", "prix": 85, "quantite": 6}, 
{"id": 3, "titre": "L’Étranger", "auteur": "Albert Camus", "categorie": "Philosophie", "prix": 95, "quantite": 5} 
]

def ajouter_livre(bibliotheque,livre):
    ids_existants={l["id"] for l in bibliotheque}
    if livre["id"] in ids_existants:
        print("Erreur : ID déjà existant.")
    else:
        bibliotheque.append(livre) 
        print(f"livre '{livre['titre']}' ajouté avec succès.")   
        
def afficher_bibliotheque(bibliotheque):
    if not bibliotheque:
        print("la bibliotheque est vide.")
    else:
        print("\n=== liste des livres ===")
        for l in bibliotheque:
            print((l["id"],l["titre"],l["auteur"],l["categorie"],l["prix"],l["quantite"])) 
        print("=========================\n") 
        
def supprimer_livre(bibliotheque,id_livre):
    for l in bibliotheque:
        if l["id"]==id_livre:
            bibliotheque.remove(l)
            print(f"livre '{l['titre']}' supprimé avec succès.")
            return
    print(f"Aucune produit trouvé avec l'ID {id_livre}.")
    
def rechercher_par_categorie(bibliotheque,categorie):
    resultat=[l for l in bibliotheque if l["categorie"].lower()==categorie.lower()]
    if resultat:
        print(f"\nLivres de la categorie'{categorie}':")
        for l in resultat:
            print((l["id"],l["titre"],l["auteur"],l["categorie"],l["prix"],l["quantite"]))
    else:
        print(f"aucnun livre trouvé dans la categorie'{categorie}'.")
        
def calculer_valeur_totale(bibliotheque):
    valeur_totale=0
    for l in bibliotheque:
        valeur_totale+=l["prix"]*l["quantite"]
    print(f"\nValeur totale de la bibliotheque:{valeur_totale:.2f} MAD")
    return valeur_totale

def afficher_categories_uniques(bibliotheque):
    categories={l["categories"] for l in bibliotheque}
    print("\nCategories uniques dans la bibliotheque:")
    for c in categories:
        print(f"-{c}")
        
def produit_le_plus_cher(bibliotheque):
    if not bibliotheque:
        print("La bibliotheque est vide.")
        return None
    bibliotheque.sort(key=lambda l:l["prix"])
    return bibliotheque[-1]

def trier_bibliotheque_par_prix(bibliotheque):
    bibliotheque_trie=sorted(bibliotheque,key=lambda l:l["prix"])
    print("\nBibliotheque tire par prix croissant:")
    for l in bibliotheque_trie:
        print((l["id"],l["titre"],l["auteur"],l["categorie"],l["prix"],l["quantite"]))
    return bibliotheque_trie

def sauvegarder_txt(bibliotheque,nom_fichier):
    with open(nom_fichier,"w",encoding="utf-8")as f:
        for l in bibliotheque:
            ligne=f"{l['id']}, {l['titre']}, {l['auteur']}, {l['categorie']}, {l['prix']}, {l['quantite']}\n"
            f.write(ligne)
    print(f"\nBibliotheque sauvegardee dans le fichier '{nom_fichier}'.")
    
def sauvegarder_csv(bibliotheque,nom_fichier="bibliotheque.csv"):
    try:
        with open(nom_fichier,"w",newline='',encoding="utf-8")as f:
            writer=csv.DictWriter(f,fieldnames=["id","titre","auteur","categorie","prix","quantite"])
            writer.writeheader()
            writer.writerows(bibliotheque)
        print(f"Donnees sauvegardees dans {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde CSV:{e}")
        
def sauvegarder_json(bibliotheque,nom_fichier="bibliotheque.json"):
    try:
        with open(nom_fichier,"w",encoding="utf-8")as f:
            json.dump(bibliotheque,f,indent=4,ensure_ascii=False)
        print(f"Donnees sauvegardees dans {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde JSON:{e}")
        
def menu():
    print("""
          === Gestion de la Bibliotheque ===
    1. Afficher la bibliotheque
    2. Ajouter un livre    
    3. Supprimer un livre      
    4. Rechercher des livres par categorie
    5. Calculer la valeur totale de la bibliotheque
    6. Afficher les categories uniques
    7. Afficher le livre le plus cher
    8. Trier la bibliotheque par prix
    9. Sauvegarder la bibliotheque dans un fichier texte
    A. Sauvegarder la bibliotheque dans un fichier CSV
    B. Sauvegarder la bibliotheque dans un fichier JSON
    0. Quitter
    =================================================
    """)
    
def main():
    bibliotheque=[
        {"id": 1, "titre": "1984", "auteur": "George Orwell", "categorie": "Science-Fiction", "prix": 120, "quantite": 4}, 
        {"id": 2, "titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "categorie": "Roman", "prix": 85, "quantite": 6}, 
        {"id": 3, "titre": "L’Étranger", "auteur": "Albert Camus", "categorie": "Philosophie", "prix": 95, "quantite": 5}
    ]
    while True:
        menu()
        choix=input("choisissez une option:")
        if choix=="1":
            afficher_bibliotheque(bibliotheque)
        elif choix=="2":
            id=int(input("ID du livre:"))
            titre=input("Titre du livre:")
            auteur=input("auteur du livre:")
            categorie=input("Categorie:")
            prix=float(input("Prix du livre:"))
            quantite=int(input("Quanite du livre:"))
            livre={"id":id,"titre":titre,"auteur":auteur,"categorie":categorie,"prix":prix,"quantite":quantite}
            ajouter_livre(bibliotheque,livre)
        elif choix=="3":
            id=int(input("ID du livre a supprimer:"))
            supprimer_livre(bibliotheque,id)
        elif choix=="4":
            categories=input("Categorie a rechercher:")
            rechercher_par_categorie(bibliotheque,categories)
        elif choix=="5":
            calculer_valeur_totale(bibliotheque)
        elif choix=="6":    
            afficher_categories_uniques(bibliotheque)
        elif choix=="7":
            produit_le_plus_cher(bibliotheque)
        elif choix=="8":
            trier_bibliotheque_par_prix(bibliotheque)
        elif choix=="9":
            sauvegarder_txt(bibliotheque,"bibliotheque.txt")
        elif choix=="A":
            sauvegarder_csv(bibliotheque,"bibliotheque.csv")
        elif choix=="B":
            sauvegarder_json(bibliotheque,"bibliotheque.json")
        elif choix=="0":
            print("Merci d'avoir uitilise le programme!")
            break
        else:
            print("Option invalide.Veuiller reessayer.")
        input("\nAppuyez sur Entrée pour continuer...")
