"""
Demander à l’utilisateur de saisir un nombre entre 1 et 10. Afficher un message d’erreur et redemander 
la saisie si ce n’est pas le cas. Afficher ensuite la table de multiplication selon le format dans l’exemple :  
Exemple avec nbr=3 : 
Table de multiplication de 3 
 3x1=3  3x2=6 
 3x3=9  3x4=12 
 3x5=15  3x6=18 
 3x7=21  3x8=24 
 3x9=27  3x10=30
"""

n=int(input("saisir un nombre entre 1 et 10:"))
while n<1 or n>10:
    print("erreur")
    n=int(input("saisir un nombre entre 1 et 10:"))
print(f"Table de multiplication de {n}")
for i in range(1,11,2):
    if i+1<=10:
        print(f"{n}x{i}={n*i} \t {n}x{i+1}={n*(i+1)}")
    else:
        print(f"{n}x{i}={n*i} ")    