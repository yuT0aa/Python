"""
Écrire le programme python qui va résoudre le problème suivant : L’utilisateur doit saisir la
capacité en litres d’une piscine et ensuite saisir 3 types de bidons, chacun avec un volume donné
en litres, l’objectif est de savoir combien de bidons on va utiliser pour remplir cette piscine
sachant qu’il faut commencer le remplissage avec les bidons de grande taille sans pour autant
dépasser la capacité totale de la piscine.
Exemple :
 capacité de la piscine : 100 Litres
 Bidon A : 1.5 L
 Bidon B : 3 L
 Bidon C : 6 L
 Résultat : 16 Bidons C + 1 Bidon B (reste 1 L dans la piscine)
"""

# Saisie de la capacité de la piscine et des volumes des bidons
capacite_piscine = float(input("Entrez la capacité de la piscine en litres: "))
volume_bidon_A = float(input("Entrez le volume du bidon A en litres: "))
volume_bidon_B = float(input("Entrez le volume du bidon B en litres: "))
volume_bidon_C = float(input("Entrez le volume du bidon C en litres: "))

# Initialisation du nombre de bidons utilisés
nombre_bidon_C = 0
nombre_bidon_B = 0
nombre_bidon_A = 0

# Remplissage de la piscine en commençant par les bidons de grande taille
while capacite_piscine >= volume_bidon_C:
    nombre_bidon_C += 1
    capacite_piscine -= volume_bidon_C
while capacite_piscine >= volume_bidon_B:
    nombre_bidon_B += 1
    capacite_piscine -= volume_bidon_B
while capacite_piscine >= volume_bidon_A:
    nombre_bidon_A += 1
    capacite_piscine -= volume_bidon_A

# Affichage des résultats
print(f"Nombre de bidons C utilisés: {nombre_bidon_C}")
print(f"Nombre de bidons B utilisés: {nombre_bidon_B}")
print(f"Nombre de bidons A utilisés: {nombre_bidon_A}")