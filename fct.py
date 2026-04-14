import csv

def AugmenterPrix(list,taux):
    return list(map(lambda p:{'id':p['id'],'nom':p['nom'],'stock':p['stock'],'prix':p['prix']+p['prix']*taux},list))

def AugmenterPrix2(list,taux):
    for p in list:
        p['prix']+=p['prix']*taux

def ReadData(path):
    produits=[]
    with open(path,'r') as f:
         reader=csv.DictReader(f) #pour lire chaque ligne sous forme d'un dictionnaire 
         for r in reader:
            produits.append(r)
    #transform list using map
    produitsV2=list(map(lambda p:{'id':int(p['id']),'nom':p['nom'],'prix':float(p['prix']),'stock':int(p['stock'])},produits))
    return produitsV2
def saveData(path,list):
    with open(path,"w",newline='') as f:
        header=["id","nom","prix","stock"]
        writer=csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        for x in list:
            writer.writerow(x)
#fonction AugmenterPrix(list,taux)=> return list
#fonction ReadData("path.csv")=> list   
#fonction saveData("newPath.csv",list )
#un module HandelCsv
#import HandelCsv dans un autre fichier .py et tester les fonctions
