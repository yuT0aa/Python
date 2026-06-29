"""
Soit le texte :
texte = '''
Ali a 22 ans.
Sara a 19 ans.
Omar a 31 ans.
Yasmine a 25 ans.
'''
1. Extraire tous les âges.
2. Extraire tous les prénoms.
3. Extraire tous les nombres comportant exactement 2 chiffres.
4. Extraire tous les mots commençant par une majuscule.
5. Compter le nombre total de prénoms trouvés.
"""
texte = '''
Ali a 22 ans.
Sara a 19 ans.
Omar a 31 ans.
Yasmine a 25 ans.
'''

import re

#1
ages=re.findall(r'\d+',texte)

#2
prenoms=re.findall(r'[A-Z][a-z]+',texte)

#3
n2c=re.findall(r'\b\d{2}\b',texte)

#4
n_prenoms=len(prenoms)


print(ages,prenoms,n2c,n_prenoms,sep="\n-------------------------\n")
