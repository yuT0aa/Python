from src.classes import CompteSecurise

compte=CompteSecurise(1,"achraf","10203040")

password=input("entrer le mot de passe : ")
compte.verifier_mot_de_passe(password)