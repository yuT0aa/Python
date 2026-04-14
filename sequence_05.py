classe = { 
"filiere": "Informatique", 
"etudiants": [ 
{"nom": "Sara", "notes": [12, 14, 16]}, 
{"nom": "Yassine", "notes": [8, 9, 10]}, 
{"nom": "Amine", "notes": [15, 18, 17]} 
] 
} 
"""
1. Affiche le nom de la filière. 
2. Affiche la moyenne de chaque étudiant. 
3. Trouve et affiche le nom de l’étudiant avec la meilleure note finale (moyenne). 
4. Ajoute un nouvel étudiant avec ses notes. 
"""
#1
print(classe["filiere"])
print("*"*30)
#2
for etudiants in classe["etudiants"]:
    m=sum(etudiants["notes"])/len(etudiants["notes"])
    print(f"nom:{etudiants['nom']},moyenne:{m}")
print("*"*30)    
#3
meilleure_moyenne=0
nom_etudiant_meilleur=""
for etudiants in classe["etudiants"]:
    m=sum(etudiants["notes"])/len(etudiants["notes"])
    if m>meilleure_moyenne:
        meilleure_moyenne=m
        nom_etudiants_meilleur=etudiants["nom"]
        print(f"nom:{nom_etudiants_meilleur},moyenne:{meilleure_moyenne}")
print("*"*30)        
#4
classe["etudiants"].append({"nom":"Nora","notes":[13,15,14]})
print(classe)