"""
texte = &quot;programmation python&quot;
Travail demandé :
1. Compter les lettres avec Counter.
2. Afficher :
o la lettre la plus fréquente ;
o les 3 lettres les plus fréquentes.
3. Afficher toutes les lettres triées.
4. Vérifier le nombre d’occurrences de :
o &quot;p&quot;
o &quot;z&quot;
5. Créer un deuxième compteur contenant :
o &quot;python&quot;
6. Soustraire ce compteur du premier.
7. Afficher le résultat final.
"""

from collections import Counter

# 1. Compter les lettres avec Counter
texte = "programmation python"
compteur = Counter(texte)   

# 2. Afficher la lettre la plus fréquente et les 3 lettres les plus fréquentes
lettre_plus_frequente = compteur.most_common(1)[0]
lettres_plus_frequentes = compteur.most_common(3)
print("Lettre la plus fréquente:", lettre_plus_frequente)
print("3 lettres les plus fréquentes:", lettres_plus_frequentes)

# 3. Afficher toutes les lettres triées
lettres_triees = sorted(compteur.items())
print("Lettres triées:", lettres_triees)

# 4. Vérifier le nombre d’occurrences de "p" et "z"
occurrences_p = compteur["p"]
occurrences_z = compteur["z"]
print("Occurrences de 'p':", occurrences_p)
print("Occurrences de 'z':", occurrences_z) 

# 5. Créer un deuxième compteur contenant "python"
compteur_python = Counter("python") 

# 6. Soustraire ce compteur du premier
compteur_soustrait = compteur - compteur_python

# 7. Afficher le résultat final
print("Résultat final après soustraction:", compteur_soustrait)