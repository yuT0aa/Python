from src.classes import SalleCinema

salle1=SalleCinema("salle1",100,0)
salle1.reserver(50)
print(salle1.taux_remplissage())
salle1.annuler(20)
print(salle1.taux_remplissage())