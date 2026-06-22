"""
Créer le fichier etudiants.csv
nom,age,note
Ali,20,15
Sara,21,18
Omar,19,9
Lina,22,14
1. Lire le fichier CSV avec pandas
2. Afficher :
 toutes les données ;
 les 3 premières lignes ;
 uniquement la colonne nom ;
 les colonnes nom et note.
3. Ajouter une colonne admis : True si note ≥ 10 False sinon
4. Modifier la note de Omar à 12
5. Trier les étudiants par note décroissante
6. Calculer :
a. la moyenne ;
b. la note maximale ;
c. la note minimale.
7. Sauvegarder le résultat dans resultat.csv
8. Créer une fonction def rechercher_etudiant(df, nom), Cette fonction doit :
a. rechercher un étudiant ;
b. afficher sa note ;
c. afficher "Étudiant introuvable" sinon.
"""

import pandas as pd
import os

print(os.getcwd())

os.chdir(r"C:\Users\Administrateur\Documents\GitHub\Python\POO\TP8\EX1")
df=pd.read_csv("etudiants.csv")
print(df)

print(df.head(3))

print(df["nom"])
print(df[["nom", "note"]])

df["admis"] = df["note"] >= 10
print(df)

df.loc[df["nom"] == "Omar", "note"] = 12
print(df)

df_sorted = df.sort_values(by="note", ascending=False)
print(df_sorted)

moyenne = df["note"].mean()
note_max = df["note"].max()

note_min = df["note"].min()
print(f"Moyenne: {moyenne}, Note maximale: {note_max}, Note minimale: {note_min}")
df.to_csv("resultat.csv", index=False)

def rechercher_etudiant(df, nom):
    etudiant = df[df["nom"] == nom]
    if not etudiant.empty:
        print(f"Note de {nom}: {etudiant['note'].values[0]}")
    else:
        print("Étudiant introuvable")
rechercher_etudiant(df, "Sara")
rechercher_etudiant(df, "Youssef")