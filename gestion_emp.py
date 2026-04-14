from datetime import datetime,date

"""
{    "matricule": integerf,         # identifiant unique
    "nom": str,               # nom complet
    "departement": str,       # nom du département
    "date_naissance": date,   # date de naissance
    "date_embauche": date,    # date d’embauche
    "salaire": float          # salaire en dirhams
}

"""
dictio=[
  {
    "matricule": 12345,
    "nom": "Jean Dupont",
    "departement": "Informatique",
    "date_naissance": "1985-03-15",
    "date_embauche": "2010-06-01",
    "salaire": 45000.0
  },
  {
    "matricule": 67890,
    "nom": "Marie Lefèvre",
    "departement": "Ressources Humaines",
    "date_naissance": "1990-07-22",
    "date_embauche": "2015-09-10",
    "salaire": 38000.0
  },
  {
    "matricule": 11223,
    "nom": "Ahmed Bennani",
    "departement": "Finance",
    "date_naissance": "1982-11-05",
    "date_embauche": "2008-04-15",
    "salaire": 52000.0
  },
  {
    "matricule": 44556,
    "nom": "Sophie Martin",
    "departement": "Marketing",
    "date_naissance": "1995-01-30",
    "date_embauche": "2020-02-20",
    "salaire": 41000.0
  },
  {
    "matricule": 78901,
    "nom": "Youssef Tazi",
    "departement": "Production",
    "date_naissance": "1978-12-12",
    "date_embauche": "2005-08-05",
    "salaire": 48000.0
  }
]

#fonction addEmploye v1
def addEmploye(liste,emp):
    exist=False
    for e in liste:
        if e["matricule"]==emp.get("matricule"):
            exist=True;break
    if exist:
        print("employe existe déja !!!")
        return 
    else:
        liste.append(emp)

#fonction addEmploye v2

"""l=[1,3,5,6,10]
print(any([x for x in l if x%3==0]))
print(len([x for x in l if x%3==0])>0)"""
def addEmpV2(l,newEmp):
    if any([e for e in l if e["matricule"]==newEmp["matricule"]]):
        print("employe existe déja !!!")
        return 
    l.append(newEmp)
#fonction trouveEmp
def trouveEmp(l,mat):
    return any([e for e in  l if e["matricule"]==mat])
              
def trouveEmpV2(l,mat):
    for e in l : 
        if e["matricule"]==mat:
            return e  #break et quitter la fonction
    return None
def GetEmpByMat(l,mat):
    for e in l :
        if e["matricule"]==mat:
            return e
    return None

#fonction Moidfier 
def Modifier(l,mat,nouvellesValeurs):
    old=GetEmpByMat(l,mat)
    if old !=None:
        old["matricule"]=mat
        old["nom"]=nouvellesValeurs["nom"]
        old["departement"]=nouvellesValeurs["departement"]

#fonction supprimer 
def Supprimer(l,mat):
    e=trouveEmpV2(l,mat)
    if e!=None:
        l.remove(e)

#fonction employe_mieux_remunere(liste)   
def employe_mieux_remunere(liste):
    return max(liste,key=lambda e:e["salaire"])
def employe_mieux_remunereV2(liste):
    l=sorted(liste,key=lambda e:e["salaire"],reverse=True)
    return l[0]
def employe_mieux_remunereV3(liste):
    maxSal,pos=liste[0],0
    for i in range(1,len(liste)):
        if liste[i]["salaire"]>maxSal:
            maxSal=liste[i]["salaire"]
            pos=i
    return liste[pos]

#fonction  employe_plus_ancien(liste)
def  employe_plus_ancien(l):
    return min(l,key=lambda e: e["date_embauche"])

def  employe_plus_ancienv2(l):
    return (sorted(l,key=lambda e: e["date_embauche"]))[0]
def  employe_plus_ancienv3(l):   
    minDate,pos=l[0]["date_embauche"],0
    for i in range(1,len(l)):
        if l[i]["date_embauche"]<minDate:
            minDate,pos=l[i]["date_embauche"],i
    return l[pos]
#fonction : employe_plus_jeune(liste)
def  employe_plus_jeune(l):
    return max(l,key=lambda e: e["date_naissance"])

def  employe_plus_jeunev2(l):
    sl=sorted(l,key=lambda e: e["date_naissance"],reverse=True)
    return sl[0]
def  employe_plus_jeunev3(l):   
    maxBDate,pos=l[0]["date_naissance"],0
    for i in range(1,len(l)):
        if l[i]["date_naissance"]>maxBDate:
            maxBDate,pos=l[i]["date_naissance"],i
    return l[pos]
# fonction employes_par_annee(liste, annee)
def employes_par_annee(liste, annee):
    return [e for e in liste if e["date_embauche"].year==annee]
def employes_par_anneeV2(liste, annee):
    l=[]
    for e in liste:
        if e["date_embauche"].year==annee:
            l.append(e)
    return l
#fonction employes_par_departement(liste)

def employes_par_departement(liste):
    depts=list(set(e["departement"] for e in liste))
    myDict={}
    for d in depts:
        myDict[d]=[]
    for dept in myDict: # foreach key in myDict
        for e in liste:
            if e["departement"]==dept:
                myDict[dept].append(e)
# fonction age_employe(employe)
def age_employe(employe):
    sysDate=date.today()
    age=sysDate.year-employe["date_naissance"].year
    if employe["date_naissance"].month>sysDate.month: 
            age-=1
    if employe["date_naissance"].month==sysDate.month and employe["date_naissance"].day>sysDate.day:
            age-=1
    return age
def calculerAnc(emp):
    sysDate=date.today()
    anc=sysDate.year-emp["date_embauche"].year
    if emp["date_embauche"].month>sysDate.month: 
            anc-=1
    if emp["date_embauche"].month==sysDate.month and emp["date_embauche"].day>sysDate.day:
            anc-=1
    return anc
#fonction employes_salaire_sup(liste, seuil)
def employes_salaire_sup(liste, seuil):
    return [e for e in liste if e["salaire"]>=seuil]

#fonction employes_anciennete_sup(liste, nb_annees)
def employes_anciennete_sup(liste, nb_annees):
    l=[]
    for e in liste :
        if calculerAnc(e)>=nb_annees:
            l.append(e)
    return l
def employes_anciennete_supV2(liste, nb_annees):
    return [e for e in liste if calculerAnc(e)>=nb_annees]
#menu
def menu():
    print('''
          ************MENU************   
    1. Ajouter un employé.
    2. Modifier un employé.
    3. Supprimer un employé.
    4. Afficher la liste des employés.
    5. Rechercher un employé par nom.
    6. Rechercher un employé par departement.
    7. Rechercher un employé par salaire.
    8. Rechercher un employé par annee d'embauche.
    9. Rechercher un employé par annee de naissance.
    10. Rechercher un employé par age.
    11. Rechercher un employé par anciennete.
    0. Quitter.
************************************************
    ''')
def main():
    dictio=[
  {
    "matricule": 12345,
    "nom": "Jean Dupont",
    "departement": "Informatique",
    "date_naissance": "1985-03-15",
    "date_embauche": "2010-06-01",
    "salaire": 45000.0
  },
  {
    "matricule": 67890,
    "nom": "Marie Lefèvre",
    "departement": "Ressources Humaines",
    "date_naissance": "1990-07-22",
    "date_embauche": "2015-09-10",
    "salaire": 38000.0
  },
  {
    "matricule": 11223,
    "nom": "Ahmed Bennani",
    "departement": "Finance",
    "date_naissance": "1982-11-05",
    "date_embauche": "2008-04-15",
    "salaire": 52000.0
  },
  {
    "matricule": 44556,
    "nom": "Sophie Martin",
    "departement": "Marketing",
    "date_naissance": "1995-01-30",
    "date_embauche": "2020-02-20",
    "salaire": 41000.0
  },
  {
    "matricule": 78901,
    "nom": "Youssef Tazi",
    "departement": "Production",
    "date_naissance": "1978-12-12",
    "date_embauche": "2005-08-05",
    "salaire": 48000.0
  }
]
    while True:
        menu()
        choix=input("khtar")
        if choix=="1":
            emp=input("employe")
            addEmploye(emp)
        elif choix=="2":
            emp=input("employe")
            Modifier(l,mat,nouvellesValeurs)(emp)
        elif choix=="3":
            emp=input("employe")
            supEmploye(emp)
        elif choix=="4":
            print(dictio)
        elif choix=="0":
            break
        else:
            print("Option invalide.")
    print("Fin du programme.")