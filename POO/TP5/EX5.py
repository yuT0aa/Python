"""
temperatures = {
&quot;Lundi&quot;: [18, 22, 25],
&quot;Mardi&quot;: [20, 24, 28],
&quot;Mercredi&quot;: [17, 21, 23],
&quot;Jeudi&quot;: [19, 26, 30]
}
Questions :
1. Afficher toutes les températures.
2. Calculer la température moyenne de chaque jour.
3. Trouver le jour le plus chaud.
4. Trouver la température maximale de la semaine.
5. Afficher les jours où la température dépasse 25°.
6. Ajouter une température pour Vendredi.
7. Calculer la moyenne générale de la semaine.
8. Trouver les jours ayant toutes les températures supérieures à 20°.
9. Transformer les données en :
&quot;Lundi&quot; : &quot;Froid&quot;
 moyenne &lt; 20 → Froid
 sinon → Chaud
10. Compter combien de fois la température augmente dans chaque jour.
"""

temperatures = {
    "Lundi": [18, 22, 25],
    "Mardi": [20, 24, 28],
    "Mercredi": [17, 21, 23],
    "Jeudi": [19, 26, 30]
}

# 1. Afficher toutes les températures.
print("Températures de la semaine:")
for jour, temp in temperatures.items():
    print(f"{jour}: {temp}")

# 2. Calculer la température moyenne de chaque jour.
print("\nTempérature moyenne de chaque jour:")
for jour, temp in temperatures.items():
    moyenne = sum(temp) / len(temp)
    print(f"{jour}: {moyenne:.2f}°C")
    
# 3. Trouver le jour le plus chaud.
jour_plus_chaud = max(temperatures, key=lambda x: max(temperatures[x]))
print(f"\nLe jour le plus chaud est: {jour_plus_chaud}")

# 4. Trouver la température maximale de la semaine.
temp_max = max(max(temp) for temp in temperatures.values())
print(f"\nLa température maximale de la semaine est: {temp_max}°C") 

# 5. Afficher les jours où la température dépasse 25°.
jours_temp_excede_25 = [jour for jour, temp in temperatures.items() if any(t > 25 for t in temp)]
print("\nJours où la température dépasse 25°:")
for jour in jours_temp_excede_25:
    print(jour)

# 6. Ajouter une température pour Vendredi.
temperatures["Vendredi"] = [21, 27, 29]
print("\nTempératures après ajout de Vendredi:")
for jour, temp in temperatures.items():
    print(f"{jour}: {temp}")

# 7. Calculer la moyenne générale de la semaine.
toutes_temperatures = [temp for temps in temperatures.values() for temp in temps]
moyenne_generale = sum(toutes_temperatures) / len(toutes_temperatures)
print(f"\nMoyenne générale de la semaine: {moyenne_generale:.2f}°C")

# 8. Trouver les jours ayant toutes les températures supérieures à 20°.
jours_toutes_temp_sup_20 = [jour for jour, temp in temperatures.items() if all(t > 20 for t in temp)]
print("\nJours ayant toutes les températures supérieures à 20°:")
for jour in jours_toutes_temp_sup_20:
    print(jour)

# 9. Transformer les données en : "Lundi" : "Froid" ou "Chaud"
temperatures_transformees = {jour: "Froid" if sum(temp) / len(temp) < 20 else "Chaud" for jour, temp in temperatures.items()}
print("\nTempératures transformées:")
for jour, classification in temperatures_transformees.items():
    print(f"{jour}: {classification}")

# 10. Compter combien de fois la température augmente dans chaque jour.
print("\nNombre de fois que la température augmente dans chaque jour:")
for jour, temp in temperatures.items():
    count_increase = sum(1 for i in range(1, len(temp)) if temp[i] > temp[i-1])
    print(f"{jour}: {count_increase} fois")
    