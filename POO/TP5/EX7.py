"""
L = [1,2,3,1,2,3,1,2,3]
Questions :
1. Détecter si une séquence se répète.
2. Trouver la taille du cycle.
3. Trouver le motif répétitif.
4. Trouver combien de répétitions existent.
"""
L = [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 1. Détecter si une séquence se répète.
def detecter_repetition(L):
    for i in range(1, len(L) // 2 + 1):
        if L[:i] * (len(L) // i) == L[:i * (len(L) // i)]:
            return True
    return False
if detecter_repetition(L):
    print("Une séquence se répète.")
else:
    print("Aucune séquence ne se répète.")

# 2. Trouver la taille du cycle.
def trouver_taille_cycle(L):
    for i in range(1, len(L) // 2 + 1):
        if L[:i] * (len(L) // i) == L[:i * (len(L) // i)]:
            return i
    return None
taille_cycle = trouver_taille_cycle(L)
if taille_cycle:
    print(f"La taille du cycle est: {taille_cycle}")
else:
    print("Aucun cycle trouvé.")

# 3. Trouver le motif répétitif.
def trouver_motif_repetitif(L):
    taille_cycle = trouver_taille_cycle(L)
    if taille_cycle:
        return L[:taille_cycle]
    return None
motif_repetitif = trouver_motif_repetitif(L)
if motif_repetitif:
    print(f"Le motif répétitif est: {motif_repetitif}")
else:
    print("Aucun motif répétitif trouvé.")

# 4. Trouver combien de répétitions existent.
def compter_repetitions(L):
    taille_cycle = trouver_taille_cycle(L)
    if taille_cycle:
        return len(L) // taille_cycle
    return 0
nombre_repetitions = compter_repetitions(L)
print(f"Le nombre de répétitions est: {nombre_repetitions}")
