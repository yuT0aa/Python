#EX 1
print("**********************EX1***************************")
"""
Un nombre est dit premier s’il n’a que deux diviseurs positifs : 1 et lui-même . 
1. Ecrire une fonction estPremier() qui prend en paramètre un entier n et retourne 1 si le 
nombre est premier ,et 0 sinon   
2. Ecrire un programme qui demande à l’utilisateur de saisir un nombre et affiche si le nombre 
est premier ou non. 
"""

#1
def estPremier(n):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    if len(lst)==2:
        return 1
    else:
        return 0
#2
while True:
    n=input("n=")
    if n.isdigit():
        break
n=int(n)
print(estPremier(n))

#EX 2
print("**********************EX2***************************")
"""
On appelle nombre Armstrong un nombre qui est égal à la somme des puissances de ses chiffres, 
chacune Arstrong() qui prend un entier n et retourne 1 si le nombre est un 
nombre Armstrong,et 0 sinon .
2. Ecrire un programme qui demande à l’utilisateur de saisir un nombre et indique s’il est 
Armstrong ou non.élevée au nombre de chiffres du nombre : (exemple : 153 = 1^3 + 5^3 +3^3 )  
1. Ecrire une fonction est
3. Ecrire un programme qui affiche tous les nombres Armstrong entre 1 et 999. 
"""

#1
def estArmstrong(n):
    lst=[int(i) for i in str(n)]
    som=0
    for i in range(len(lst)):
        som+=int(lst[i])**len(lst)
    if som==int(n):
        return 1
    else:
        return 0

#2
while True:
    n=input("n=")
    if n.isdigit():
        break 
print(estArmstrong(n))

#3
for i in range(0,1000):
    if estArmstrong(str(i)):
        print(i)

#EX 3
print("**********************EX3***************************")
"""
Un nombre est dit nombre abondant si la somme de ses diviseurs propres (sans inclure le nombre lui
même) est supérieure à ce nombre. 
1. Ecrire une fonction estAbondant() qui prend un entier n en paramètre et retourne 1 si le 
nombre est abondant, et 0 sinon . 
2. Ecrire une fonction listeAbondants() qui prend un entier m et retourne tous les nombres 
abondants inférieurs ou égaux à m. 
3. Ecrire un programme qui demande à l’utilisateur de saisir un nombre et qui affiche si ce 
nombre est abondant ou non. Le programme affiche également tous les nombres abondants 
jusqu’à ce nombre. 
"""

#1
def estAbondants(n):
    lst=[]
    for i in range(1,n):
        if n%i==0:
            lst.append(i)
    if sum(lst)>n:
        return 1
    else:
        return 0
    
#2
def listeAbondants(m):
    lst=[]
    for i in range(0,m+1):
        if estAbondants(i):
            lst.append(i)
    return lst

#3
while True:
    n=input("n=")
    if n.isdigit():
        n=int(n)
        break
print(estAbondants(n))



#EX 4

print("**********************EX4***************************")
"""
Un Employé est caractérisé par : un nom unique  , un département (ex . : ‘’Informatique’’, 
’’Ressources Humaines’’ ou ‘’Finance’’) , une date de recrutement , une date de naissance , un poste 
(ex. : ‘’Développeur’’ ,’’Analyste’’ ,’’Manager’’) , un salaire ,un champ booléen estPermanent 
indiquant si l’employé est en CDI (contrat à durée indéterminée ) ou non . 
1. Ecrire une fonction permettant d’ajouter un employé à une liste : ajouter(liste,emp) 
2. Ecrire une fonction qui retourne la liste des employés d’un département donné : 
fct2(liste,dept) 
3. Ecrire une fonction qui retourne l’employé le plus âgé. 
4. Ecrire une fonction qui retourne l’employé le plus récent  
5. Ecrire une fonction qui retourne tous les employés permanent de la liste. 
6. Ecrire une fonction qui retourne le nombre de Développeur dans l’équipe.  
7. Ecrire  une fonction qui retourne les employés dont l’âge entre 25 et 45 ans .  
8. Ecrire une fonction qui augment le salaire des employés qui ont plus de 20 ans d’expérience 
de 25%. 
"""
import datetime

employers=[]
#1
def ajouter(liste,emp):
    emp={}
    while True:
        emp["nom"]=input("nom=")
        if emp["nom"].isalpha():
            break
    while True:
        emp["departement"]=input("departement=")
        if emp["departement"].isalpha():
           break
    while True:
        emp["date_embauche"]=input("date_embauche=")
        if emp["date_embauche"].isdigit():
            break
    while True:
        emp["date_naissance"]=input("date_naissance=")
        if emp["date_naissance"].isdigit():
            break
    while True:    
        emp["poste"]=input("poste=")
        if emp["poste"].isalpha():
            break
    while True:
        emp["salaire"]=input("salaire=")
        if emp["salaire"].isdigit():
            break
    while True:    
        emp["estPermanent"]=input("estPermanent=")
        if emp["estPermanent"].isalpha():
            break
        employers.append(emp)

#2
def fct2(liste,dept):
    for emp in employers:
        if emp["departement"]==dept:
            print(emp)
        
#3
def fct3(liste):
    min=employers[0]
    for emp in employers:
        if emp["date_naissance"]<min["date_naissance"]:
            min=emp
    return min

#4
def fct4(liste):
    max=employers[0]
    for emp in employers:
        if emp["date_embauche"]>max["date_embauche"]:
            max=emp
    return max

#5
def fct5(liste):
    for emp in employers:
        if emp["estPermanent"]=="oui":
            print(emp)
            
#6
def fct6(liste):
    cpt=0
    for emp in employers:
        if emp["poste"]=="developpeur":
            cpt+=1
    return cpt

#7
def fct7(liste):
    for emp in employers:
        age=emp["date_embauche"].year-emp["date_naissance"].year
        if age>=25 and age<=45:
            print(emp)
            
#8
def fct8(liste):
    for emp in employers:
        age=emp["date_embauche"].year-emp["date_naissance"].year
        if age>20:
            emp["salaire"]+=emp["salaire"]*0.25
            
            
