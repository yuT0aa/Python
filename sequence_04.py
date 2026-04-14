matrice = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9] 
] 
"""
1. Affiche tous les éléments de la matrice. 
2. Affiche la somme de chaque ligne. 
3. Affiche la somme de la diagonale principale.
"""
#1
for ligne in matrice:
    for element in ligne:
        print(element)  
print("*"*30)
#2
for ligne in matrice:
    somme=0
    for element in ligne:
        somme+=element
    print(somme)  
print("*"*30)
#3
somme=0
for i in range(len(matrice)):
    somme+=matrice[i][i]
print(somme)    