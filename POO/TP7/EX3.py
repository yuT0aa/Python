"""
liaisons = [
("A","B"),
("A","C"),
("B","D"),
("C","D"),
("D","E")
]
1. Construire le graphe avec defaultdict(list).
2. Afficher tous les voisins d'un sommet.
3. Déterminer si un chemin existe entre A et E.
"""

liaisons = [
("A","B"),
("A","C"),
("B","D"),
("C","D"),
("D","E")
]

from collections import defaultdict

# 1. Construire le graphe avec defaultdict(list).
graph = defaultdict(list)
for i, j in liaisons:
    graph[i].append(j)
    graph[j].append(i)
print(graph)

#2. Afficher tous les voisins d'un sommet.
print(graph["A"])

#3. Déterminer si un chemin existe entre A et E.
def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == target:
        return True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True
    return False

print(dfs(graph, "A", "E"))

