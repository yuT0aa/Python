"""
Soit :
phrase="La facture N°4587 a été validée."
Travail demandé
1. Rechercher le premier nombre présent.
2. Afficher la valeur trouvée avec group().
3. Afficher sa position de début.
4. Afficher sa position de fin.
"""

import re

phrase="La facture N°4587 a été validée."

#1
match=re.search(r'\d',phrase)

#2
if match:

    print("",match.group())

#3
    print("",match.start())

#4
    print("",match.end())