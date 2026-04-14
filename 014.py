"""
nombre=int(input("Entrez un entier positif: "))

if nombre<0:
    print("Erreur: Le nombre doit être positif.")
else:
    somme=0
    
    temp=nombre
    while temp>0:
        chiffre=temp%10  
        somme+=chiffre     
        temp=temp//10   
    
    print(f"Somme des chiffres= {somme}")
"""


nombre = int(input("Entrez un entier positif : "))

if nombre<0:
    print("Erreur : Le nombre doit être positif.")
else:
    produit=1
    
    temp=nombre
    while temp>0:
        chiffre=temp%10  
        produit*=chiffre   
        temp=temp//10    
    
    print(f"Produit= {produit}")
