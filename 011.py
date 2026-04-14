n=int(input("Entrez un entier n:"))
P=1
for i in [j for j in range(1,n+1)]:
    P*=i
print(f"Le produit P=1×2×3×⋯×{n} est {P}.")
