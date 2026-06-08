"""
L = [5,8,5,8,5,8,5]
Tous les nombres apparaissent un nombre pair de fois sauf un.
Trouver ce nombre.
"""

L = [5,8,5,8,5,8,5]
from collections import Counter

# Compter les occurrences de chaque nombre
number_counts = Counter(L)  

# Trouver le nombre qui apparaît un nombre impair de fois
odd_occurrence_number = None
for number, count in number_counts.items():
    if count % 2 != 0:
        odd_occurrence_number = number
        break

print(f"Le nombre qui apparaît un nombre impair de fois est: {odd_occurrence_number}")