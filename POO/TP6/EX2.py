"""
Une boulangerie gère les clients avec une file d’attente.
Travail demandé :
1. Créer un deque vide.
2. Ajouter :
o &quot;Ali&quot;
o &quot;Sara&quot;
o &quot;Omar&quot;
3. Ajouter un client prioritaire &quot;Police&quot; au début.
4. Afficher la file.
5. Faire sortir :
o le premier client ;
o le dernier client.
6. Afficher la file restante.
7. Vider complètement la file.
"""

from collections import deque

# 1. Créer un deque vide
file_attente = deque()

# 2. Ajouter "Ali", "Sara", "Omar"
file_attente.append("Ali")
file_attente.append("Sara")
file_attente.append("Omar")

# 3. Ajouter un client prioritaire "Police" au début
file_attente.appendleft("Police")

# 4. Afficher la file
print("File d'attente:", list(file_attente))

# 5. Faire sortir le premier client et le dernier client
premier_client = file_attente.popleft()
dernier_client = file_attente.pop()
print("Premier client sorti:", premier_client)
print("Dernier client sorti:", dernier_client)

# 6. Afficher la file restante
print("File d'attente restante:", list(file_attente))