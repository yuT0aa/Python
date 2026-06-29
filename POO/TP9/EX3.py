"""
Soit :
date = "Réunion prévue le 15 Juin 2026"
Travail demandé
Créer une regex permettant d'extraire :
 le jour
 le mois
 l'année
"""

import re

date="Réunion prévue le 15 Juin 2026"

match=re.search(r'(\d{2})\s+([A-Za-z]+)\s+(\d{4})',date)

if match:

    jour=match.group(1)
    mois=match.group(2)
    annee=match.group(3)

    print(jour,mois,annee,sep="\n")