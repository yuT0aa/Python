etudiants = { 
    "A01": {"nom": "Sara", "notes": [12, 14, 16]}, 
    "A02": {"nom": "Yassine", "notes": [8, 9, 10]}, 
    "A03": {"nom": "Amine", "notes": [15, 18, 17]} 
} 
"""
1. Affiche le nom et la moyenne de chaque étudiant. 
2. Ajoute un nouvel étudiant "A04" avec "nom": "Nora" et "notes": [13, 15, 14]. 
3. Trouve l’étudiant ayant la meilleure moyenne et affiche son nom. 
4. Affiche tous les étudiants dont toutes les notes sont supérieures ou égales à 12. 
"""
#1
for nom_etudiant,info in etudiants.items():
    m=sum(info["notes"])/len(info["notes"])
    print(f"nom:{info['nom']},moyenne:{m}")
print("*"*30)
#2
etudiants["A04"]={"nom":"Nora","notes":[13,15,14]}
print(etudiants)
print("*"*30)
#3
meilleure_moyenne=0
nom_etudiant_meilleur=""
for nom_etdiant,info in etudiants.items():
    m=sum(info["notes"])/len(info["notes"])
    if m>meilleure_moyenne:
        meilleure_moyenne=m
        nom_etudiant_meilleur=info["nom"]
print(f"nom:{nom_etudiant_meilleur},moyenne:{meilleure_moyenne}")
print("*"*30)
#4
for nom_etudiant,info in etudiants.items():
    if all(note>=12 for note in info["notes"]):
        print(f"nom:{info['nom']},notes:{info['notes']}")
    