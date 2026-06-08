"""
On veut représenter des positions GPS avec latitude et longitude.
PointGPS = namedtuple(...)
Travail demandé :
1. Créer un tuple nommé PointGPS contenant :
o latitude
o longitude
2. Créer les points suivants :
o Marrakech → (31.63, -8.00)
o Rabat → (34.02, -6.84)
3. Afficher :
o les coordonnées avec les indices ;
o les coordonnées avec les noms des champs.
4. Convertir un point en dictionnaire.
5. Modifier uniquement la longitude de Marrakech.
6. Afficher les noms des champs.
"""

from collections import namedtuple

# 1. Créer un tuple nommé PointGPS contenant latitude et longitude
PointGPS = namedtuple('PointGPS', ['latitude', 'longitude'])

# 2. Créer les points suivants : Marrakech → (31.63, -8.00) et Rabat → (34.02, -6.84)
marrakech = PointGPS(31.63, -8.00)
rabat = PointGPS(34.02, -6.84)

# 3. Afficher les coordonnées avec les indices
print("Marrakech (indices):", marrakech[0], marrakech[1])
print("Rabat (indices):", rabat[0], rabat[1])

# Afficher les coordonnées avec les noms des champs
print("Marrakech (champs):", marrakech.latitude, marrakech.longitude)
print("Rabat (champs):", rabat.latitude, rabat.longitude)

# 4. Convertir un point en dictionnaire
marrakech_dict = marrakech._asdict()
print("Marrakech (dictionnaire):", marrakech_dict)

# 5. Modifier uniquement la longitude de Marrakech
marrakech_modifie = marrakech._replace(longitude=-8.01)
print("Marrakech (modifié):", marrakech_modifie.latitude, marrakech_modifie.longitude)

# 6. Afficher les noms des champs
print("Noms des champs:", PointGPS._fields)