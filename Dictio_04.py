# Liste de dictionnaires pour les étudiants
# Chaque dictionnaire contient : 'nom' (str), 'notes' (list de float), 'groupe' (str)
etudiants = [
    {'nom': 'Alice', 'notes': [15.0, 14.5, 16.0], 'groupe': 'A'},
    {'nom': 'Bob', 'notes': [12.0, 13.5, 11.0], 'groupe': 'B'},
    {'nom': 'Charlie', 'notes': [17.0, 18.0, 16.5], 'groupe': 'A'},
    {'nom': 'Diana', 'notes': [10.0, 9.5, 11.0], 'groupe': 'C'},
    {'nom': 'Eve', 'notes': [14.0, 15.5, 13.0], 'groupe': 'B'}
]

# Fonction pour calculer la moyenne
def calculer_moyenne(notes):
    if not notes:
        return 0.0
    return sum(notes) / len(notes)

# 1. Afficher tous les étudiants avec leur moyenne
def afficher_etudiants_avec_moyenne():
    print("1. Étudiants avec leur moyenne :")
    for etudiant in etudiants:
        moyenne = calculer_moyenne(etudiant['notes'])
        print(f"  {etudiant['nom']} : Moyenne = {moyenne:.2f}")
    print()

# 2. Ajouter un nouvel étudiant avec ses notes
def ajouter_etudiant(nom, notes, groupe):
    etudiants.append({'nom': nom, 'notes': notes, 'groupe': groupe})
    print(f"2. Étudiant {nom} ajouté avec succès.\n")

# 3. Modifier une note existante
def modifier_note(nom, index_note, nouvelle_note):
    for etudiant in etudiants:
        if etudiant['nom'] == nom:
            if 0 <= index_note < len(etudiant['notes']):
                etudiant['notes'][index_note] = nouvelle_note
                print(f"3. Note modifiée pour {nom} à l'index {index_note}.\n")
                return
            else:
                print(f"3. Index de note invalide pour {nom}.\n")
                return
    print(f"3. Étudiant {nom} non trouvé.\n")

# 4. Supprimer un étudiant
def supprimer_etudiant(nom):
    for i, etudiant in enumerate(etudiants):
        if etudiant['nom'] == nom:
            del etudiants[i]
            print(f"4. Étudiant {nom} supprimé.\n")
            return
    print(f"4. Étudiant {nom} non trouvé.\n")

# 5. Trouver l’étudiant avec la meilleure moyenne
def meilleur_etudiant():
    if not etudiants:
        print("5. Aucun étudiant.\n")
        return
    meilleur = max(etudiants, key=lambda e: calculer_moyenne(e['notes']))
    moyenne = calculer_moyenne(meilleur['notes'])
    print(f"5. Meilleur étudiant : {meilleur['nom']} avec moyenne {moyenne:.2f}\n")

# 6. Lister tous les étudiants ayant une moyenne supérieure à un seuil (13)
def etudiants_au_dessus_seuil(seuil=13.0):
    print(f"6. Étudiants avec moyenne > {seuil} :")
    for etudiant in etudiants:
        moyenne = calculer_moyenne(etudiant['notes'])
        if moyenne > seuil:
            print(f"  {etudiant['nom']} : Moyenne = {moyenne:.2f}")
    print()

# 7. Regrouper les étudiants par groupe
def regrouper_par_groupe():
    groupes = {}
    for etudiant in etudiants:
        groupe = etudiant['groupe']
        if groupe not in groupes:
            groupes[groupe] = []
        groupes[groupe].append(etudiant['nom'])
    print("7. Étudiants regroupés par groupe :")
    for groupe, noms in groupes.items():
        print(f"  Groupe {groupe} : {', '.join(noms)}")
    print()

# Exécution des tâches avec exemples
afficher_etudiants_avec_moyenne()

ajouter_etudiant('Frank', [16.0, 17.5, 15.0], 'A')

modifier_note('Alice', 1, 15.0)  # Modifier la deuxième note d'Alice

supprimer_etudiant('Diana')

meilleur_etudiant()

etudiants_au_dessus_seuil(13.0)

regrouper_par_groupe()

# Affichage final de la liste mise à jour
print("Liste finale des étudiants :")
for etudiant in etudiants:
    print(etudiant)
    print()