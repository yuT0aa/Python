from SRC.Mesclasses import Etudiant
#a
etudiant1 = Etudiant(1, "Alice", 20, 15.5)
#b
etudiant1.set_age(21)
#c    
print(f"ID: {etudiant1.id}")
print(f"Nom: {etudiant1.nom}")
print(f"Age: {etudiant1.get_age()}")
print(f"Moyenne: {etudiant1.moyenne}")