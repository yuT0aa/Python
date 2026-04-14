# Programme d'analyse de texte : compter les lettres et mots
# Utilise des dictionnaires pour compter et des sets pour les uniques

# Fonction pour compter combien de fois chaque lettre apparaît dans un texte
def compter_lettres(texte):
    compteur = {}
    for char in texte.lower():  # Insensible à la casse
        if char.isalpha():  # Ignorer les espaces et ponctuations
            compteur[char] = compteur.get(char, 0) + 1
    return compteur

# Fonction pour compter combien de fois chaque mot apparaît dans une phrase
def compter_mots(phrase):
    mots = phrase.lower().split()  # Diviser en mots, insensible à la casse
    compteur = {}
    for mot in mots:
        # Nettoyer la ponctuation basique (optionnel, pour simplifier)
        mot = ''.join(c for c in mot if c.isalnum())
        if mot:
            compteur[mot] = compteur.get(mot, 0) + 1
    return compteur

# Fonction pour lister les lettres ou mots uniques (avec set)
def lister_uniques(texte, type="lettres"):
    if type == "lettres":
        uniques = {char for char in texte.lower() if char.isalpha()}
        print("Lettres uniques :", uniques)
    elif type == "mots":
        mots = texte.lower().split()
        uniques = {''.join(c for c in mot if c.isalnum()) for mot in mots if mot}
        print("Mots uniques :", uniques)
    else:
        print("Type invalide. Utilisez 'lettres' ou 'mots'.")
    return uniques

# Fonction pour trouver la lettre ou le mot le plus fréquent
def plus_frequent(compteur):
    if not compteur:
        return None, 0
    max_item = max(compteur, key=compteur.get)
    return max_item, compteur[max_item]

# Fonction pour créer un dictionnaire pour stocker le nombre de voyelles et de consonnes
def compter_voyelles_consonnes(texte):
    voyelles = "aeiouy"
    compteur = {"voyelles": 0, "consonnes": 0}
    for char in texte.lower():
        if char.isalpha():
            if char in voyelles:
                compteur["voyelles"] += 1
            else:
                compteur["consonnes"] += 1
    return compteur

# Exemples d'utilisation
if __name__ == "__main__":
    texte_exemple = "Bonjour, comment allez-vous ? Bonjour est un mot répété."
    phrase_exemple = "Bonjour, comment allez-vous ? Bonjour est un mot répété."

    print("Texte exemple :", texte_exemple)
    print("\n--- Questions ---")

    # 1. Compter les lettres
    lettres = compter_lettres(texte_exemple)
    print("1. Comptage des lettres :", lettres)

    # 2. Compter les mots
    mots = compter_mots(phrase_exemple)
    print("2. Comptage des mots :", mots)

    # 3. Lister les uniques
    print("3a. Lettres uniques :")
    lister_uniques(texte_exemple, "lettres")
    print("3b. Mots uniques :")
    lister_uniques(phrase_exemple, "mots")

    # 4. Plus fréquent
    lettre_freq, count_l = plus_frequent(lettres)
    mot_freq, count_m = plus_frequent(mots)
    print(f"4. Lettre la plus fréquente : '{lettre_freq}' ({count_l} fois)")
    print(f"   Mot le plus fréquent : '{mot_freq}' ({count_m} fois)")

    # 5. Voyelles et consonnes
    vc = compter_voyelles_consonnes(texte_exemple)
    print("5. Voyelles et consonnes :", vc)
