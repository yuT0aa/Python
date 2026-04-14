n=int(input("Entrez un entier n : "))
S=0
for i in range(2,n+1,2):
    S+=i
print(f"La somme des nombres pairs de 1 à {n} est {S=}.")
