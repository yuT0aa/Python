"""
liaisons = [
(&quot;A&quot;,&quot;B&quot;),
(&quot;A&quot;,&quot;C&quot;),
(&quot;B&quot;,&quot;D&quot;),
(&quot;C&quot;,&quot;D&quot;),
(&quot;D&quot;,&quot;E&quot;)
]
1. Construire le graphe avec defaultdict(list).
2. Afficher tous les voisins d&#39;un sommet.
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
for u, v in liaisons:
    graph[u].append(v)
    graph[v].append(u)  

# 2. Afficher tous les voisins d'un sommet.
def afficher_voisins(sommet):
    voisins = graph[sommet]
    print(f"Les voisins de {sommet} sont: {', '.join(voisins)}")

# 3. Déterminer si un chemin existe entre A et E.
def existe_chemin(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    if start == end:
        return True
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if existe_chemin(graph, neighbor, end, visited):
                return True
    return False

