produits = [ 
("P01", "Stylo", 2.5), 
("P02", "Cahier", 5.0), 
("P03", "Gomme", 1.5) 
] 
"""
1. Affiche le nom et le prix de chaque produit. 
2. Augmente le prix de chaque produit de 10%. 
3. Trouve et affiche le produit le plus cher.
"""
#1
for code,nom,prix in produits:
    print(f"nom:{nom},prix:{prix}")
print("*"*30)
#2
for code,nom,prix in produits:
    prix=prix*1.1
    print(f"nom:{nom},prix:{prix}")
print("*"*30)
#3
produit_plus_cher=produits[0]
for code,nom,prix in produits:
    if prix>produit_plus_cher[2]:
        produit_plus_cher=(code,nom,prix)
print(f"nom:{produit_plus_cher[1]},prix:{produit_plus_cher[2]}")