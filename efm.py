#Q1
employer=[
    {"eid": 1, "name": "Ali","date RE": "2022-01-01", "departement": "Technology","poste": "manager","salaire":4000},
    {"eid": 2, "name": "Fatima","date RE": "2020-11-23", "departement": "informatique","poste": "developeur","salaire":2500},
    {"eid": 3, "name": "karim","date RE": "2021-05-15", "departement": "Technology","poste": "analyste","salaire":3000},
    {"eid": 4, "name": "Ahmed","date RE": "2019-07-30", "departement": "Marketing","poste": "executive","salaire":2000},
]

#Q2
def calculer_salaire_moyen(employers):
    total_salaire=sum(emp["salaire"]for emp in employers)
    salaire_moyen=total_salaire/len(employers)
    return salaire_moyen

#Q3
def employes_par_departement(employers):
    departement={}
    for emp in employers:
        dept=emp["departement"]
        if dept not in departement:
            departement[dept]=[]
        departement[dept].append(emp)
    return departement
#Q4
def enrichir_donnees_employers(employers):
    for emp in employers:
        emp["salaire_annuel"]=emp["salaire"]*12
    return employers

#Q5
def suprimer_par_critere(employers,critere):
    employers_filteres=[emp for emp in employers if emp["poste"]!=critere]
    return employers_filteres
#Q6
def sauvegarder_csv(employees_filtrees,fichier):
    import csv
    with open(fichier,"w",newline="")as csv:
        list1=("eid","name","date RE","departement","poste","salaire","salaire_annuel")
        writer=csv.dictwriter(csv,filednames=list1)
        writer.writeheader()
        writer.writerows(employees_filtrees)
print(employer)