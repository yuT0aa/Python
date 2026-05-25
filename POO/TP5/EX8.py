"""
texte = "aaabbccccddeeeeeee"
Travail demandé
1. Trouver la lettre la plus tapée.
2. Trouver la plus longue frappe consécutive.
3. Compresser le texte :
a3b2c4d2e7
4. Reconstruire le texte initial.
5. Détecter les lettres tapées une seule fois.
6. Trouver les transitions les plus fréquentes :
o exemple : a -> b
"""
texte = "aaabbccccddeeeeeee"

# 1. Trouver la lettre la plus tapée.
from collections import Counter
compteur = Counter(texte)
lettre_plus_tapee = compteur.most_common(1)[0][0]
print(f"La lettre la plus tapée est: '{lettre_plus_tapee}'")

# 2. Trouver la plus longue frappe consécutive.
max_frappe = 1
current_frappe = 1
for i in range(1, len(texte)):  
    if texte[i] == texte[i - 1]:
        current_frappe += 1
    else:
        max_frappe = max(max_frappe, current_frappe)
        current_frappe = 1
max_frappe = max(max_frappe, current_frappe)
print(f"La plus longue frappe consécutive est: {max_frappe}")

# 3. Compresser le texte : a3b2c4d2e7
texte_compresse = ""
current_char = texte[0]
current_count = 1
for i in range(1, len(texte)):
    if texte[i] == current_char:
        current_count += 1
    else:
        texte_compresse += f"{current_char}{current_count}"
        current_char = texte[i]
        current_count = 1
texte_compresse += f"{current_char}{current_count}"
print(f"Texte compressé: {texte_compresse}")    

# 4. Reconstruire le texte initial.
texte_reconstruit = ""
for i in range(0, len(texte_compresse), 2):
    char = texte_compresse[i]
    count = int(texte_compresse[i + 1])
    texte_reconstruit += char * count
print(f"Texte reconstruit: {texte_reconstruit}")    

# 5. Détecter les lettres tapées une seule fois.
lettres_une_fois = [char for char, count in compteur.items() if count == 1]
print(f"Lettres tapées une seule fois: {lettres_une_fois}") 

# 6. Trouver les transitions les plus fréquentes : exemple : a -> b
transitions = Counter()
for i in range(len(texte) - 1):
    transition = (texte[i], texte[i + 1])
    transitions[transition] += 1
transition_plus_frequente = transitions.most_common(1)[0][0]
print(f"La transition la plus fréquente est: '{transition_plus_frequente[0]}' -> '{transition_plus_frequente[1]}'")
