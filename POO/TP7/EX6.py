"""
Match = namedtuple(...)
Chaque match contient :
 équipe1
 équipe2
 score1
 score2
À partir d'une liste de matchs :
1. Calculer les points de chaque équipe.
2. Construire le classement.
3. Trouver le champion.
"""

from collections import namedtuple, defaultdict

Match = namedtuple("Match", ["équipe1", "équipe2", "score1", "score2"])

matches = [
    Match("TeamA", "TeamB", 2, 1),
    Match("TeamA", "TeamC", 1, 1),
    Match("TeamB", "TeamC", 0, 3),
]

# 1. Calculer les points de chaque équipe.
points = defaultdict(int)
for match in matches:
    if match.score1 > match.score2:
        points[match.équipe1] += 3
    elif match.score1 < match.score2:
        points[match.équipe2] += 3
    else:
        points[match.équipe1] += 1
        points[match.équipe2] += 1
print(points)

# 2. Construire le classement.
classement = sorted(points.items(), key=lambda x: x[1], reverse=True)
print(classement)

# 3. Trouver le champion.
champion = classement[0][0]
print(champion)