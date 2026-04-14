a,b=int(input("Entrez le premier entier a:")),int(input("Entrez le deuxième entier b (avec a<b):"))

if a >= b:
    print("Erreur : a doit être strictement inférieur à b.")
else:
    somme=sum([i for i in range(a,b+1)])

    print(f"La somme des entiers de {a} à {b} est {somme}.")
