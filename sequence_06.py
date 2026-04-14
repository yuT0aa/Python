donnees = { 
"groupes": [ 
{"nom": "G1", "etudiants": [("Sara", 14), ("Yassine", 9)]}, 
{"nom": "G2", "etudiants": [("Amine", 17), ("Nora", 15)]} 
] 
} 
"""
1. Affiche tous les noms des étudiants. 
2. Affiche le nom et la note de l’étudiant ayant la note la plus élevée. 
3. Calcule la moyenne des notes par groupe.
"""
#1
for gr in donnees["groupes"]:
    for etu in gr["etudiants"]:
        print(etu[0])
print("*"*30)        
#2
meilleure_note=0
nom_etudiants_meilleur=""
for gr in donnees["groupes"]:
    for etu in gr["etudiants"]:
        if etu[1]>meilleure_note:
            meilleure_note=etu[1]
            nom_etudiants_meilleur=etu[0]
            print(f"nom:{nom_etudiants_meilleur},note:{meilleure_note}")
print("*"*30)
#3
for gr in donnees["groupes"]:
    som=1
    for etu in gr["etudiants"]:
        som*=etu[1]
        moy=som/len(gr["etudiants"])
        print(f"gr:{gr["nom"]},moy:{moy}")
