
#Ex 2
"""
Créer une fonction qui porte votre nom. Elle reçoit en entrée une taille et un genre et retourne le poids 
idéal (PI) selon la formule suivante : 
Pour le genre "femme" : 
PI=taille – 100 – (( taille -150 )/2) 
Pour le genre "homme" : 
PI= taille – 100 – (( taille -150 )/4)
"""
def achraf(taille,genre):
    if genre.lower()=="femme":
        pi=taille -100 -((taille -150)/2)
    elif genre.lower()=="homme":
        pi=taille -100 -((taille -150)/4)
    return pi
print(achraf(170,"homme"))
print("*"*50)

#Ex 3
"""
On souhaite gérer un tournoi de chasse visant à primer le meilleur chasseur. On stocke dans un tableau 
tournoi[10][3] les résultats du tournoi. La première colonne contient le numéro du chasseur, la 
deuxième la catégorie du chasseur et la troisième le nombre de gibiers chassés par le chasseur. 

1. Remplir le tableau tournoi sachant que la catégorie ne peut prendre que A ou B aucune autre 
valeur ne doit être acceptée. Redemander la saisie en cas d’erreur 
2. Afficher le total de gibiers chassés tout chasseur compris  
3. Afficher le nombre le plus élevé de gibiers chassés  
4. Afficher la liste des vainqueurs (numéro et catégorie de chasseurs ayant eu le nombre le plus 
élevé de gibiers (nombre retrouvé dans la question précédente))  
5. Ecrire une fonction qui reçoit en entrée une catégorie et retourne le nombre de chasseurs dans 
cette catégorie  
"""
#1
tournoi=[]
for i in range(10):
    tournoi.append({"num":i+1,"cat":input("saisir la gategories:").upper(),"nb_gibiers":int(input("saisir le nombre de gibiers:"))})
    while tournoi[i]['cat']not in ['A','B']:
        print("erreur")
        tournoi[i]['cat']=input("saisir la gategories:").upper()
print(tournoi) 

#2
total_gibiers=sum([tournoi[i]['nb_gibiers']for i in range(10)])
print("le total de gibiers chasses est:",total_gibiers)

#3
max_gibiers=max([tournoi[i]['nb_gibiers']for i in range(10)])
print("le nombre le plus eleve de gibiers chasses est:",max_gibiers)

#4
for i in range(10):
    if tournoi[i]['nb_gibiers']==max_gibiers:
        print("le vainqueur est le chasseur",tournoi[i]['num'],"de la gategories",tournoi[i]['cat'])

#5
def nb_chasseurs(cat):
    nb=0
    for i in range(10):
        if tournoi[i]['cat']==cat:
            nb+=1
    return nb
print("le nombre de chasseurs de la gategories A est:",nb_chasseurs("A"))
print("le nombre de chasseurs de la gategories B est:",nb_chasseurs("B"))
print("*"*50)



#Ex 4

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
print("*"*50)


#Ex 5
"""
Soit la liste suivante : lst = [12,35,37,45,98] 
1. Afficher : 
 Le nombre d’éléments de la liste 
 La valeur maximale 
 La somme des éléments 
 La liste des nombres supérieur à 20 
2. Ajouter un élément à la fin de la liste 
3. Supprimer le premier élément de la liste
4. Trier la liste 
"""
lst = [12,35,37,45,98]

#1
print("le nombre d'elements de la liste est:",len(lst))
print("la valeur maximale est:",max(lst))
print("la somme des elements est:",sum(lst))
print("la liste des nombres superieur a 20 est:",[i for i in lst if i>20])
print("*"*50)
#2
lst.append(int(input("saisir un element a ajouter a la fin de la liste:")))
print("la liste apres l'aout est:",lst)
print("*"*50)
#3 
lst.pop(0)
print("la liste apres suprimmer le premier element est:",lst)
print("*"*50)
#4
lst.sort()
print("la liste trier est:",lst)
print("*"*50)

#Ex 6
"""
Soit le code suivant : 
f = open("fichier.csv", "r") 
fr = csv.DictReader(f,delimiter=";") 
for ligne in fr: 
    if ligne["ville"]==villeR : 
        print(f"{ligne["nom"]}/{ligne["age"]}", end= "*") 
f.close() 
 
1. Que fait ce code  ? 
2. Quelle est la différence entre le mode d’accès au fichier en a et en w ? 
3. Générer un nombre aléatoire entre 1 et 10 ? 
"""
#1
import csv
f=open("fichier.csv","r")
fr=csv.DictReader(f,delimiter=";")
for ligne in fr:
    if ligne["ville"]=="villeR":
        print(f"{ligne["nom"]}/{ligne["age"]}",end="*")
f.close()

#2
