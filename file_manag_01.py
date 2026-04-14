produits=[
    {"id":1, "nom":"Clavier", "prix":120, "stock":50},
    {"id":2, "nom":"Souris", "prix":80, "stock":150},
    {"id":3, "nom":"Ecran", "prix":900, "stock":20}
]
"""
1 Lire le fichier CSV et créer une liste de dictionnaires comme ceci : 
2 Augmenter le prix de tous les produits de 10%. 
3 Trouver le produit avec le plus grand prix. 
4 Sauvegarder les données mises à jour dans un fichier produits_maj.csv.
"""
from fct import *

#1

with open("produits.csv",'x') as f:
        reader=csv.DictReader(f) #pour lire chaque ligne sous forme d'un dictionnaire 
        for r in reader:
            produits.append(r)
produits=list(map(lambda p:{'id':int(p['id']),'nom':p['nom'],'prix':float(p['prix']),'stock':int(p['stock'])}))
print(produits)