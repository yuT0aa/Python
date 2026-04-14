n=int(input("Entrez un entier n:"))
somme=sum([i**2 for i in range(1,n+1)])
print(f"La somme des carrés des {n} premiers entiers est {somme}.")
