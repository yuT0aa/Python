"""
On dispose d&#39;un journal de connexions :
logs = '''
2026-01-10;Ali;SUCCESS
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Sara;SUCCESS
2026-01-10;Omar;FAILED
2026-01-10;Omar;FAILED
'''
1. Extraire les utilisateurs et le statut.
2. Compter le nombre d&#39;échecs par utilisateur.
3. Afficher les utilisateurs ayant au moins 3 échecs.
4. Déterminer l'utilisateur le plus suspect.
"""

logs = """
2026-01-10;Ali;SUCCESS
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Sara;SUCCESS
2026-01-10;Omar;FAILED
2026-01-10;Omar;FAILED
"""

#1
utilisateurs = []
statuts = []
for ligne in logs.strip().split('\n'):
    _, utilisateur, statut = ligne.split(';')
    utilisateurs.append(utilisateur)
    statuts.append(statut)

#2
from collections import Counter
echecs = Counter()
for utilisateur, statut in zip(utilisateurs, statuts):
    if statut == 'FAILED':
        echecs[utilisateur] += 1
    
#3
utilisateurs_suspects = [utilisateur for utilisateur, count in echecs.items() if count >= 3]
print("Utilisateurs ayant au moins 3 échecs :", utilisateurs_suspects)  

#4
utilisateur_suspect = max(echecs, key=echecs.get)
print("Utilisateur le plus suspect :", utilisateur_suspect)



