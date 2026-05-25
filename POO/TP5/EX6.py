"""
L = [1,1,1,2,2,5,5,5,5,3,3,8,8,8]
Questions :
1. Trouver la plus longue répétition consécutive.
2. Trouver combien de blocs différents existent.
3. Transformer la liste en :
[(1,3), (2,2), (5,4), (3,2), (8,3)]
4. Reconstruire la liste initiale à partir du résultat précédent.
"""
L = [1, 1, 1, 2, 2, 5, 5, 5, 5, 3, 3, 8, 8, 8]

# 1. Trouver la plus longue répétition consécutive.
max_repetition = 1
current_repetition = 1
for i in range(1, len(L)):
    if L[i] == L[i - 1]:
        current_repetition += 1
    else:
        max_repetition = max(max_repetition, current_repetition)
        current_repetition = 1
max_repetition = max(max_repetition, current_repetition)
print(f"La plus longue répétition consécutive est: {max_repetition}")

# 2. Trouver combien de blocs différents existent.
blocs_differents = set()
current_bloc = []
for num in L:
    if not current_bloc or num == current_bloc[-1]:
        current_bloc.append(num)
    else:
        blocs_differents.add(tuple(current_bloc))
        current_bloc = [num]
if current_bloc:
    blocs_differents.add(tuple(current_bloc))
print(f"Nombre de blocs différents: {len(blocs_differents)}")

# 3. Transformer la liste en : [(1,3), (2,2), (5,4), (3,2), (8,3)]
resultat = []
current_num = L[0]
current_count = 1
for i in range(1, len(L)):
    if L[i] == current_num:
        current_count += 1
    else:
        resultat.append((current_num, current_count))
        current_num = L[i]
        current_count = 1
resultat.append((current_num, current_count))
print("Liste transformée:", resultat)

# 4. Reconstruire la liste initiale à partir du résultat précédent.
reconstruite = []
for num, count in resultat:
    reconstruite.extend([num] * count)
print("Liste reconstruite:", reconstruite)  
