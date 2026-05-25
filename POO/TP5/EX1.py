"""
Une entreprise gère des commandes. Chaque commande est représentée par id_commande,
client, montant. Toutes les commandes sont stockées dans une liste.
Données
commandes = [
(1, &#39;Ali&#39;, 250),
(2, &#39;Sara&#39;, 120),
(3, &#39;Ali&#39;, 300),
(4, &#39;Lina&#39;, 80),
(5, &#39;Sara&#39;, 220),
(6, &#39;Omar&#39;, 150)
]
1. Afficher toutes les commandes sous forme : Commande 1 - Ali - 250 DH
2. Afficher uniquement les commandes dont le montant dépasse 200.
3. Afficher les clients sans répétition.
4. Calculer le montant total des commandes.
5. Calculer le montant moyen.
6. Trouver la commande avec le montant le plus élevé sans et avec max().
7. Calculer le total des achats pour chaque client. Résultat attendu :
Ali : 550
Sara : 340
...
8. Trouver le client qui a dépensé le plus.
9. Ajouter une nouvelle commande : (7, &#39;Nora&#39;, 270)
10. Supprimer toutes les commandes dont le montant est inférieur à 100.
11. Créer une nouvelle liste contenant uniquement les commandes supérieures à la moyenne.
12. Transformer la liste en : [(1, &#39;Ali&#39;, &#39;Elevé&#39;), (2, &#39;Sara&#39;, &#39;Faible&#39;), ...]
 montant ≥ 200 → &quot;Elevé&quot;
 sinon → &quot;Faible&quot;
13. Compter combien de fois un client fait une commande plus chère que la précédente.
Exemple pour Ali : 250 → 300
"""

commandes = [
    (1, 'Ali', 250),
    (2, 'Sara', 120),
    (3, 'Ali', 300),
    (4, 'Lina', 80),
    (5, 'Sara', 220),
    (6, 'Omar', 150)
]

# 1. Afficher toutes les commandes sous forme : Commande 1 - Ali - 250 DH
for commande in commandes:
    print(f"Commande {commande[0]} - {commande[1]} - {commande[2]} DH")

# 2. Afficher uniquement les commandes dont le montant dépasse 200.
print("\nCommandes dont le montant dépasse 200:")
for commande in commandes:
    if commande[2] > 200:
        print(f"Commande {commande[0]} - {commande[1]} - {commande[2]} DH")

# 3. Afficher les clients sans répétition.
clients = set()
for commande in commandes:
    clients.add(commande[1])
print("\nClients sans répétition:")
for client in clients:
    print(client)

# 4. Calculer le montant total des commandes.
total_montant = sum(commande[2] for commande in commandes)
print(f"\nMontant total des commandes: {total_montant} DH")

# 5. Calculer le montant moyen.
montant_moyen = total_montant / len(commandes)
print(f"Montant moyen des commandes: {montant_moyen:.2f} DH")

# 6. Trouver la commande avec le montant le plus élevé sans et avec max().
max_montant = max(commande[2] for commande in commandes)
print(f"\nMontant le plus élevé (sans max()): {max_montant} DH")
commande_max = max(commandes, key=lambda x: x[2])
print(f"Commande avec le montant le plus élevé (avec max()): Commande {commande_max[0]} - {commande_max[1]} - {commande_max[2]} DH")

# 7. Calculer le total des achats pour chaque client.
total_achats = {}
for commande in commandes:
    client = commande[1]
    montant = commande[2]
    if client in total_achats:
        total_achats[client] += montant
    else:
        total_achats[client] = montant

print("\nTotal des achats pour chaque client:")
for client, total in total_achats.items():
    print(f"{client} : {total} DH")

# 8. Trouver le client qui a dépensé le plus.
client_max = max(total_achats, key=total_achats.get)
print(f"\nClient qui a dépensé le plus: {client_max} avec {total_achats[client_max]} DH")

# 9. Ajouter une nouvelle commande : (7, 'Nora', 270)
commandes.append((7, 'Nora', 270))
print("\nCommandes après ajout de la nouvelle commande:")
for commande in commandes:
    print(f"Commande {commande[0]} - {commande[1]} - {commande[2]} DH")

# 10. Supprimer toutes les commandes dont le montant est inférieur à 100.
commandes = [commande for commande in commandes if commande[2] >= 100]
print("\nCommandes après suppression des commandes inférieures à 100:")
for commande in commandes:
    print(f"Commande {commande[0]} - {commande[1]} - {commande[2]} DH")

# 11. Créer une nouvelle liste contenant uniquement les commandes supérieures à la moyenne.
commandes_sup_moyenne = [commande for commande in commandes if commande[2] > montant_moyen]
print("\nCommandes supérieures à la moyenne:")
for commande in commandes_sup_moyenne:
    print(f"Commande {commande[0]} - {commande[1]} - {commande[2]} DH")

# 12. Transformer la liste en : [(1, 'Ali', 'Elevé'), (2, 'Sara', 'Faible'), ...]
commandes_transformees = [(commande[0], commande[1], 'Elevé' if commande[2] >= 200 else 'Faible') for commande in commandes]
print("\nCommandes transformées:")
for commande in commandes_transformees:
    print(commande) 

# 13. Compter combien de fois un client fait une commande plus chère que la précédente.
compte_augmentation = {}
for i in range(1, len(commandes)):
    client = commandes[i][1]
    montant_actuel = commandes[i][2]
    montant_precedent = commandes[i-1][2]
    if montant_actuel > montant_precedent:
        if client in compte_augmentation:
            compte_augmentation[client] += 1
        else:
            compte_augmentation[client] = 1
print("\nNombre de fois qu'un client fait une commande plus chère que la précédente:")
for client, compte in compte_augmentation.items():
    print(f"{client} : {compte} fois")  