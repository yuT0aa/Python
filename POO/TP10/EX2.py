"""
reservations = '''
SalleA;08:00;10:00
SalleB;09:00;11:00
SalleA;09:30;12:00
SalleC;13:00;15:00
SalleA;14:00;16:00
'''
1. Extraire les réservations.
2. Détecter les conflits de réservation.
3. Afficher les salles concernées.
4. Afficher le nombre total de conflits.
"""

reservations = """
SalleA;08:00;10:00
SalleB;09:00;11:00 
SalleA;09:30;12:00
SalleC;13:00;15:00
SalleA;14:00;16:00
"""

#1
reservations_list = []
for ligne in reservations.strip().split('\n'):
    salle, debut, fin = ligne.split(';')
    reservations_list.append((salle, debut, fin))

#2
from collections import defaultdict
conflits = defaultdict(list)
for i in range(len(reservations_list)):
    salle_i, debut_i, fin_i = reservations_list[i]
    for j in range(i + 1, len(reservations_list)):
        salle_j, debut_j, fin_j = reservations_list[j]
        if salle_i == salle_j:
            if not (fin_i <= debut_j or fin_j <= debut_i):
                conflits[salle_i].append((debut_i, fin_i, debut_j, fin_j))

#3
salles_concernees = list(conflits.keys())
print("Salles concernées par des conflits :", salles_concernees)

#4
nombre_total_conflits = sum(len(conflits[salle]) for salle in conflits)
print("Nombre total de conflits :", nombre_total_conflits)