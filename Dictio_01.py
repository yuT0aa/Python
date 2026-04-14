# Petit programme de gestion de produits pour un magasin
# Chaque produit est un dictionnaire avec les clés : id, nom, categorie, prix, quantite

# Liste initiale des produits
produits = [
    {"id": 1, "nom": "Clavier", "categorie": "Informatique", "prix": 250, "quantite": 10},
    {"id": 2, "nom": "Souris", "categorie": "Informatique", "prix": 150, "quantite": 20},
    {"id": 3, "nom": "Chaise", "categorie": "Mobilier", "prix": 500, "quantite": 5},
]

# Fonction pour afficher tous les produits
def afficher_produits():
    if not produits:
        print("Aucun produit dans la liste.")
        return
    for produit in produits:
        print(produit)

# Fonction pour ajouter un produit
def ajouter_produit(id, nom, categorie, prix, quantite):
    # Vérifier si l'id existe déjà
    if any(p["id"] == id for p in produits):
        print(f"Erreur : Un produit avec l'id {id} existe déjà.")
        return
    nouveau_produit = {"id": id, "nom": nom, "categorie": categorie, "prix": prix, "quantite": quantite}
    produits.append(nouveau_produit)
    print(f"Produit ajouté : {nouveau_produit}")

# Fonction pour supprimer un produit par id
def supprimer_produit(id):
    global produits
    produits = [p for p in produits if p["id"] != id]
    print(f"Produit avec id {id} supprimé (si existant).")

# Fonction pour modifier un produit par id
def modifier_produit(id, **kwargs):
    for produit in produits:
        if produit["id"] == id:
            for key, value in kwargs.items():
                if key in produit:
                    produit[key] = value
            print(f"Produit modifié : {produit}")
            return
    print(f"Aucun produit trouvé avec id {id}.")

# Fonction pour rechercher un produit par nom (recherche partielle)
def rechercher_produit(nom):
    resultats = [p for p in produits if nom.lower() in p["nom"].lower()]
    if resultats:
        for r in resultats:
            print(r)
    else:
        print("Aucun produit trouvé.")

# Fonction pour filtrer les produits par catégorie
def filtrer_par_categorie(categorie):
    resultats = [p for p in produits if p["categorie"].lower() == categorie.lower()]
    if resultats:
        for r in resultats:
            print(r)
    else:
        print("Aucun produit dans cette catégorie.")

# Fonction pour filtrer les produits par prix (inférieur ou égal à un montant)
def filtrer_par_prix(max_prix):
    resultats = [p for p in produits if p["prix"] <= max_prix]
    if resultats:
        for r in resultats:
            print(r)
    else:
        print("Aucun produit dans cette plage de prix.")

# Fonctions utilisant les sets
# Lister les catégories uniques
def lister_categories_uniques():
    categories = {p["categorie"] for p in produits}
    print("Catégories uniques :", categories)
    return categories

# Détecter les doublons (par id ou par nom)
def detecter_doublons(par="id"):
    if par == "id":
        ids = [p["id"] for p in produits]
        doublons = set([x for x in ids if ids.count(x) > 1])
    elif par == "nom":
        noms = [p["nom"] for p in produits]
        doublons = set([x for x in noms if noms.count(x) > 1])
    else:
        print("Paramètre invalide. Utilisez 'id' ou 'nom'.")
        return
    if doublons:
        print(f"Doublons détectés ({par}) :", doublons)
    else:
        print(f"Aucun doublon détecté ({par}).")

# Détecter les produits manquants (comparer à une autre liste)
def detecter_manquants(autre_liste):
    ids_actuels = {p["id"] for p in produits}
    ids_autres = {p["id"] for p in autre_liste}
    manquants = ids_autres - ids_actuels
    if manquants:
        print("Produits manquants (ids) :", manquants)
    else:
        print("Aucun produit manquant.")

# Comparer deux stocks (différences)
def comparer_stocks(autre_liste):
    ids_actuels = {p["id"] for p in produits}
    ids_autres = {p["id"] for p in autre_liste}
    seulement_actuels = ids_actuels - ids_autres
    seulement_autres = ids_autres - ids_actuels
    communs = ids_actuels & ids_autres
    print("Produits seulement dans le stock actuel :", seulement_actuels)
    print("Produits seulement dans l'autre stock :", seulement_autres)
    print("Produits communs :", communs)

# Exemple d'utilisation (menu simple)
if __name__ == "__main__":
    while True:
        print("\n--- Menu de gestion des produits ---")
        print("1. Afficher tous les produits")
        print("2. Ajouter un produit")
        print("3. Supprimer un produit")
        print("4. Modifier un produit")
        print("5. Rechercher un produit par nom")
        print("6. Filtrer par catégorie")
        print("7. Filtrer par prix max")
        print("8. Lister catégories uniques")
        print("9. Détecter doublons")
        print("10. Détecter produits manquants (vs autre liste)")
        print("11. Comparer deux stocks")
        print("0. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            afficher_produits()
        elif choix == "2":
            id = int(input("ID : "))
            nom = input("Nom : ")
            categorie = input("Catégorie : ")
            prix = float(input("Prix : "))
            quantite = int(input("Quantité : "))
            ajouter_produit(id, nom, categorie, prix, quantite)
        elif choix == "3":
            id = int(input("ID à supprimer : "))
            supprimer_produit(id)
        elif choix == "4":
            id = int(input("ID à modifier : "))
            champ = input("Champ à modifier (nom/categorie/prix/quantite) : ")
            valeur = input("Nouvelle valeur : ")
            if champ in ["prix", "quantite"]:
                valeur = float(valeur) if champ == "prix" else int(valeur)
            modifier_produit(id, **{champ: valeur})
        elif choix == "5":
            nom = input("Nom à rechercher : ")
            rechercher_produit(nom)
        elif choix == "6":
            categorie = input("Catégorie : ")
            filtrer_par_categorie(categorie)
        elif choix == "7":
            max_prix = float(input("Prix max : "))
            filtrer_par_prix(max_prix)
        elif choix == "8":
            lister_categories_uniques()
        elif choix == "9":
            par = input("Détecter doublons par (id/nom) : ")
            detecter_doublons(par)
        elif choix == "10":
            # Exemple d'autre liste (à adapter)
            autre_liste = [
                {"id": 1, "nom": "Clavier", "categorie": "Informatique", "prix": 250, "quantite": 10},
                {"id": 4, "nom": "Table", "categorie": "Mobilier", "prix": 300, "quantite": 2},
            ]
            detecter_manquants(autre_liste)
        elif choix == "11":
            # Exemple d'autre liste (à adapter)
            autre_liste = [
                {"id": 1, "nom": "Clavier", "categorie": "Informatique", "prix": 250, "quantite": 10},
                {"id": 4, "nom": "Table", "categorie": "Mobilier", "prix": 300, "quantite": 2},
            ]
            comparer_stocks(autre_liste)
        elif choix == "0":
            break
        else:
            print("Option invalide.")
# Note: Keep your bot token secure and do not share it publicly.