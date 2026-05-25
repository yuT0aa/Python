"""
On donne :
evenements = {
&quot;event1&quot;: {&quot;nom&quot;: &quot;Conférence&quot;, &quot;participants&quot;: {&quot;Ali&quot;, &quot;Sara&quot;}},
&quot;event2&quot;: {&quot;nom&quot;: &quot;Atelier&quot;, &quot;participants&quot;: {&quot;Zineb&quot;, &quot;Ali&quot;}},
&quot;event3&quot;: {&quot;nom&quot;: &quot;Hackathon&quot;, &quot;participants&quot;: {&quot;Sara&quot;, &quot;Said&quot;}}
}
Questions :
1. Afficher les participants du event1
2. Ajouter le participant &quot;Omar&quot; au event2
3. Trouver les participants communs entre event1 et event2
4. Trouver tous les participants différents entre event2 et event3
5. Vérifier si event1 et event3 ont des participants en commun
6. Afficher tous les noms des événements
7. Afficher tous les événements qui contiennent le participant &quot;Ali&quot;
8. Afficher les événements ayant plus de 1 participant
9. Pour chaque événement, afficher : nom + nombre de participants
10. Afficher les participants qui participent à au moins 2 événements
"""

evenements = {  
    "event1": {"nom": "Conférence", "participants": {"Ali", "Sara"}},
    "event2": {"nom": "Atelier", "participants": {"Zineb", "Ali"}},
    "event3": {"nom": "Hackathon", "participants": {"Sara", "Said"}}
}

# 1. Afficher les participants du event1
print("Participants du event1:", evenements["event1"]["participants"])

# 2. Ajouter le participant "Omar" au event2
evenements["event2"]["participants"].add("Omar")
print("\nParticipants du event2 après ajout de Omar:", evenements["event2"]["participants"])

# 3. Trouver les participants communs entre event1 et event2
participants_communs = evenements["event1"]["participants"].intersection(evenements["event2"]["participants"])
print("\nParticipants communs entre event1 et event2:", participants_communs)

# 4. Trouver tous les participants différents entre event2 et event3
participants_differents = evenements["event2"]["participants"].symmetric_difference(evenements["event3"]["participants"])
print("\nParticipants différents entre event2 et event3:", participants_differents)

# 5. Vérifier si event1 et event3 ont des participants en commun
participants_communs_event1_event3 = evenements["event1"]["participants"].intersection(evenements["event3"]["participants"])
print("\nEvent1 et Event3 ont des participants en commun:", bool(participants_communs_event1_event3))

# 6. Afficher tous les noms des événements
noms_evenements = [evenement["nom"] for evenement in evenements.values()]
print("\nNoms des événements:", noms_evenements)

# 7. Afficher tous les événements qui contiennent le participant "Ali"
evenements_avec_ali = [evenement["nom"] for evenement in evenements.values() if "Ali" in evenement["participants"]]
print("\nÉvénements qui contiennent le participant 'Ali':", evenements_avec_ali)

# 8. Afficher les événements ayant plus de 1 participant
evenements_plus_un_participant = [evenement["nom"] for evenement in evenements.values() if len(evenement["participants"]) > 1]
print("\nÉvénements ayant plus de 1 participant:", evenements_plus_un_participant)

# 9. Pour chaque événement, afficher : nom + nombre de participants
print("\nNom et nombre de participants pour chaque événement:")
for evenement in evenements.values():
    print(f"{evenement['nom']} - Nombre de participants: {len(evenement['participants'])}")

# 10. Afficher les participants qui participent à au moins 2 événements
participants_count = {}
for evenement in evenements.values():
    for participant in evenement["participants"]:
        if participant in participants_count:
            participants_count[participant] += 1
        else:
            participants_count[participant] = 1
participants_au_moins_2_evenements = [participant for participant, count in participants_count.items() if count >= 2]
print("\nParticipants qui participent à au moins 2 événements:", participants_au_moins_2_evenements)