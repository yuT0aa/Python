"""
1. Soit la liste L=[0,1,2,3,4,5,6,7,8,9,10], créer les listes suivantes par compréhension à partir de
L.
a) L1=[0,2,4,6,8,10,12,14,16,18,20]
b) L2=[[0,0],[1,1],[2,2],[3,3,[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]]
c) L3=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
d) L4=[0,1,2,3,4,5,6,7,8,9,10, 0,1,2,3,4,5,6,7,8,9,10]
e)L5=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,
10,10,10,10,10,10,10,10]
2. Soient les listes suivantes :
a) L1= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b) L2 = [’Janvier’, ’Février’, ’Mars’, ’Avril’, ’Mai’, ’Juin’, ’Juillet’, ’Août’,
’Septembre’, ’Octobre’,’Novembre’, ’Décembre’]

Créer la liste L3 par compréhension à partir de L1 et L2 telle que : L3=
[[’Janvier’,31],[’Février’,28],[’Mars’,31],...].
"""
# 1. Création des listes par compréhension à partir de L.
L = list(range(11))
L1 = [x * 2 for x in L]
L2 = [[x, x] for x in L]
L3 = [x for x in L for _ in range(2)]
L4 = L + L
L5 = [x for x in L for _ in range(x)]
print("L1:", L1)
print("L2:", L2)
print("L3:", L3)
print("L4:", L4)
print("L5:", L5)

# 2. Création de la liste L3 par compréhension à partir de L1 et L2.
L1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
L2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
L3 = [[L2[i], L1[i]] for i in range(len(L1))]
print("\nL3:", L3)