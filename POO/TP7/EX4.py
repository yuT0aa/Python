"""
relations = [
("Ali","Sara"),
("Sara","Omar"),
("Ali","Yasmine"),
("Omar","Amine")
]
1. Construire le réseau.
2. Trouver les amis d'Ali.
3. Trouver les amis communs entre deux personnes.
4. Trouver les personnes isolées.
"""

relations = [
("Ali","Sara"),
("Sara","Omar"),
("Ali","Yasmine"),
("Omar","Amine")
]

from collections import defaultdict 

# 1. Construire le réseau.
network = defaultdict(list)
for i, j in relations:
    network[i].append(j)
    network[j].append(i)
print(network)

# 2. Trouver les amis d'Ali.
print(network["Ali"])

# 3. Trouver les amis communs entre deux personnes.
def common_friends(network, person1, person2):
    return set(network[person1]) & set(network[person2])
print(common_friends(network, "Ali", "Sara"))   

# 4. Trouver les personnes isolées.
isolated = [person for person in network if not network[person]]
print(isolated)
