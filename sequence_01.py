etudiant = { 
    "nom": "Sara", 
    "prenom": "Bennani", 
    "notes": [12, 15, 14] 
} 
"""
1. Affiche le prénom de l’étudiant. 
2. Affiche la note maximale. 
3. Calcule et affiche la moyenne des notes.
"""
#1
print(etudiant["prenom"])
print("*"*30)
#2
print(max(etudiant["notes"]))
print("*"*30)
#3
m=sum(etudiant["notes"])/len(etudiant["notes"])
print(m)

