"""
Soit :
adresse = &quot;Rue 41 de la République Marrakech Maroc&quot;
Travail demandé
1. Découper la chaîne selon les espaces.
2. Découper la chaîne uniquement sur les deux premiers espaces.
3. Afficher la liste obtenue dans chaque cas.
"""

adresse = "Rue 41 de la République Marrakech Maroc"

#1
liste1 = adresse.split()
print("Découpage selon les espaces :")
print(liste1)

#2
liste2 = adresse.split(' ', 2)
print("\nDécoupage sur les deux premiers espaces :")
print(liste2)

#3
liste3 = adresse.rsplit(' ', 2)
print("\nDécoupage sur les deux derniers espaces :")
print(liste3)