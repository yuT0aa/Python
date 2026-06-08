"""
votes = ["Ali","Sara","Ali","Omar","Sara","Ali","Omar","Sara"]
1. Trouver le gagnant.
2. Détecter s&#39;il y a égalité.
3. Afficher tous les candidats classés par nombre de voix.
"""

votes = ["Ali","Sara","Ali","Omar","Sara","Ali","Omar","Sara"]
from collections import Counter

# 1. Trouver le gagnant.
vote_counts = Counter(votes)
winner = vote_counts.most_common(1)[0][0]
print(f"Le gagnant est: {winner}")

# 2. Détecter s'il y a égalité.
most_common = vote_counts.most_common()
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print("Il y a égalité entre:", most_common[0][0], "et", most_common[1][0])
else:
    print("Il n'y a pas d'égalité.")

# 3. Afficher tous les candidats classés par nombre de voix.
print("Candidats classés par nombre de voix:")
for candidate, count in vote_counts.most_common():
    print(f"{candidate}: {count} voix")