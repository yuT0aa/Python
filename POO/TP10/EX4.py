"""
code = '''
def calcul():
pass
def afficher():
pass
class Etudiant:
pass
class Professeur:
pass
'''
1. Extraire tous les noms de fonctions.
2. Extraire tous les noms de classes.
3. Construire un rapport :
{
"fonctions": [...],
"classes": [...]
}
4. Déterminer combien de classes et combien de fonctions existent.
"""

code = '''
def calcul():
pass
def afficher():
pass
class Etudiant:
pass
class Professeur:
pass
'''

import re

#1
fcts=re.findall(r"def (\w+)\(\):", code)

#2
classes=re.findall(r"class (\w+):", code)

#3
rapport = {
    "fonctions": fcts,
    "classes": classes
}

#4
print(f"Nombre de fonctions: {len(fcts)}")
print(f"Nombre de classes: {len(classes)}")