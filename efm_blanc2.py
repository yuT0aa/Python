
#EX 2
"""
 Écrire un algorithme qui demande à 
l’utilisateur d’entrer deux entiers et calcule 
ensuite la somme et le produit des deux 
nombres  
 Utiliser une procédure pour informer 
l’utilisateur si le produit des deux nombres 
est positif ou bien négative  
"""

n1=int(input("N1:"))
n2=int(input("N2:"))
somme=n1+n2
produit=n1*n2
print(f"la somme de {n1} et {n2} est {somme} et le produit est {produit}")

#EX 3
"""
Écrire un algorithme qui permet d'afficher la 
table de multiplication de 5. Utilisant la 
boucle Pour
"""
for i in range(1,11):
    print(f"5 x {i} = {5*i}")
    
#EX 4
"""
Écrire un algorithme qui demande à 
l’utilisateur de remplir un tableau T de 10 
entiers puis calcule et affiche le nombre 
d’occurrence d’un nombre N
"""

T=[int(input(f" T[{i}]:")) for i in range(10)]
N=int(input("N:"))
count=0
for i in T:
    if i==N:
        count+=1
print(f"le nombre {N} apparait {count} fois")

#EX 5
"""
Écrire une fonction qui permet de calculer le 
prix TTC, cette fonction va recevoir un 
paramètre de type Réel dont le nom 
est "prixHT" et un second paramètre de type 
Réel dont le nom est "tva".  
En donnent la formule de calcul est. 
(TTC=NA*HT*(1+TVA))  
"""

def prixTTC(prixHT,tva):
    return prixHT*(1+tva)
print(prixTTC(100,0.2)) 

#EX 6
"""
Écrire un programme en Python  qui permet 
d'évaluer une note saisie au  clavier par 
l’utilisateur   (si la note est supérieure à 10 
alors il affiche valider sinon non validé  (NB : 
la note comprise entre 0 et 20 ).
"""
note=float(input("Entrez la note:"))
if 0<=note<=20:
    if note>10:
        print("Validé")
    else:
        print("Non validé")
else:
    print("Note invalide")
    
#EX 7
"""
Écrire une fonction en Python qui permet de 
calculer la moyenne de trois entiers saisis 
 par l'utilisateurs
"""
def moyenne(a,b,c):
    return (a+b+c)/3
print(moyenne(1,2,3))
