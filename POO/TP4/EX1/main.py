from src.classes import Vehicule,Voiture,Moto

if __name__ == "__main__":
    voiture1=Voiture("Toyota",100)
    moto1=Moto("Yamaha",80)

    for vehicule in [voiture1,moto1]:
        vehicule.afficher_infos()
        vehicule.demarrer()
        print(f"Vitesse calculée: {vehicule.calculer_vitesse()}")