notes = [[12, 14, 16], [8, 9, 11], [15, 18, 17]] 

"""
1. Moyenne de chaque étudiant. 
2. Étudiants dont toutes les notes >= 12. 
3. Vérifier si au moins un étudiant a une moyenne >= 16.
"""

#1
moyennes = [sum(etudiant)/len(etudiant) for etudiant in notes]
print(moyennes)
print("*"*30)

#2
etudiants_reussis = [etudiant for etudiant in notes if all(note >= 12 for note in etudiant)]
print(etudiants_reussis)
print("*"*30)

#3
au_moins_un_reussi = any(moyenne >= 16 for moyenne in moyennes)
print(au_moins_un_reussi)