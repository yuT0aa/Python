n = int(input("Entrez un entier n : "))

somme=0

for i in range(1,n+1):
    if i%3==0:
        somme+=i

print(f"La somme des entiers de 1 à {n} divisibles par 3 est {somme}.")
