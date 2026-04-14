from SRC.Mesclasses import CompteBancaire

compte1 = CompteBancaire(1234, "Ana", 1000)
compte2 = CompteBancaire(5678, "Nta", 500)

compte1.Versement(200)
compte2.Retrait(100)
compte1.Agios()

compte1.Afficher()
compte2.Afficher()
