from SRC.Mesclasses import Livre

livre1 = Livre(1, "Le Petit Prince", "Antoine de Saint-Exupéry", 96, 10.99)
livre1.afficher_info()
print(f"Prix moyen par page: {livre1.prix_moyen_par_page():.2f}")
print(livre1)
Livre.modifier_bibliotheque("BiblioTech")
print(f"Bibliothèque associée au livre: {livre1.bibliotheque}")
livre2 = Livre(2, "1984", "George Orwell", 328, 15.99)
livre2.afficher_info()
print(f"Prix moyen par page: {livre2.prix_moyen_par_page():.2f}")
print(livre2)
print(f"Bibliothèque associée au livre: {livre2.bibliotheque}")
