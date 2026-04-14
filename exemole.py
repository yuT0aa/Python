"""
1. Créer une liste de dictionnaires représentant des livres. 
Chaque dictionnaire doit contenir les informations suivantes : 
• titre : Titre du livre 
• date_publication : Date de publication au format "AAAA-MM-JJ" 
• prix : Prix du livre en DH 
• categorie : Catégorie du livre (ex. "Roman", "Science", "Histoire", etc.) 
• auteur : Nom de l’auteur 
1. Créer une fonction calculer_prix_moyen(livres) qui renvoie la moyenne des prix des 
livres. 
2. Créer une fonction livres_par_categorie(livres) qui retourne un dictionnaire : 
{categorie: nombre_livres} 
3. Créer une fonction enrichir_donnees_livres(livres) qui : 
• Calcule le prix TTC pour chaque livre avec une TVA de 20 % : 
prix_ttc = prix * 1.2 
• Ajoute une classification selon le prix TTC : 
o 'Bas' si prix_ttc < 100 DH 
o 'Moyen' si 100 ≤ prix_ttc < 300 DH 
o 'Élevé' si prix_ttc ≥ 300 DH 
4. Créer une fonction supprimer_par_categorie(livres, categorie) qui supprime tous les 
livres appartenant à la catégorie passée en paramètre. 
5. Créer une fonction sauvegarder_csv(livres_filtres, fichier) qui exporte les données 
des livres dans un fichier CSV. 
"""
import csv
from datetime import datetime

def calculer_prix_moyen(livres):
    prix_total = 0
    for livre in livres:
        prix_total += livre["prix"]
    return prix_total / len(livres)
def livres_par_categorie(livres):
    categories = {}
    for livre in livres:
        categorie = livre["categorie"]
        if categorie in categories:
            categories[categorie] += 1
        else:
            categories[categorie] = 1
    return categories
def enrichir_donnees_livres(livres):
    for livre in livres:
        prix_ttc = livre["prix"] * 1.2
        livre["prix_ttc"] = prix_ttc
        if prix_ttc < 100:
            livre["classification"] = "Bas"
        elif 100 <= prix_ttc < 300:
            livre["classification"] = "Moyen"
        else:
            livre["classification"] = "Élevé"
    return livres
def supprimer_par_categorie(livres, categorie):
    return [livre for livre in livres if livre["categorie"] != categorie]
def sauvegarder_csv(livres_filtres, fichier):
    with open(fichier, "w", newline="", encoding="utf-8") as fichier_csv:
        writer = csv.DictWriter(fichier_csv, fieldnames=["titre", "date_publication", "prix", "categorie", "auteur"])
        writer.writeheader()
        for livre in livres_filtres:
            writer.writerow(livre)

