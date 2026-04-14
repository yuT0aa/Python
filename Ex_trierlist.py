#Question 1
mots=["Banane","Pomme","Kiwi","abricot","fraise"]
mots.sort(key=str.lower)
print(mots)
mots.sort(key=len)

#Question 2
persones=[("Ali",29),("Fatima",30),("karim",20),("Ahmed",25)]
persones.sort(key=lambda x:x[1])
persones.sort(key=lambda x:(x[0],x[1]))
print(persones)

#Question 3
etudiants=[
    {"nom":"Ali","note":15},
    {"nom":"Fatima","note":18},
    {"nom":"karim","note":12},
    {"nom":"Ahmed","note":15}
]
etudiants.sort(key=lambda x:x["note"])
etudiants.sort(key=lambda x:x["nom"])
etudiants.sort(key=lambda x:x["note"],reverse=True)
print(etudiants)
