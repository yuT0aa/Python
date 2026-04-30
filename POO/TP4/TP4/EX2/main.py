from src.classes import Rectangle, Triangle

if __name__ == "__main__":
    rect = Rectangle("Mon Rectangle", 5, 3)
    print(f"Aire du {rect.nom} : {rect.calculer_aire()}")
    print(f"Dessin du {rect.nom} :")
    rect.dessiner()

    tri = Triangle("Mon Triangle", 5, 4)
    print(f"Aire du {tri.nom} : {tri.calculer_aire()}")
    print(f"Dessin du {tri.nom} :")
    tri.dessiner()