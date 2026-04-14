produits = [ 
{"nom": "Stylo", "prix": 2.5}, 
{"nom": "Cahier", "prix": 5.0}, 
{"nom": "Gomme", "prix": 1.5} 
] 

"""
1. Trouver le produit le plus cher. 
2. Filtrer les produits dont le prix > 2. 
3. Appliquer une remise de 10% à tous les produits. 
"""

#1
pro_cher=produits[0]
for p in produits:
    if p["prix"]>pro_cher["prix"]:
        pro_cher=p
print(f"nom:{pro_cher['nom']},prix:{pro_cher['prix']}")
print("*"*30)

#2
pro_filtre=[p for p in produits if p["prix"]>2]
print(pro_filtre)
print("*"*30)

#3
for p in produits:
    p["prix"]=p["prix"]*0.9
print(produits)