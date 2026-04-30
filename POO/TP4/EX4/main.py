from src.classes import Correcteur, CorrecteurCode, CorrecteurRedaction

if __name__ == "__main__":
    # Test Correcteur QCM
    qcm = Correcteur(["A", "B", "C"], ["A", "B", "D"])
    qcm.afficher_resultat()

    # Test Correcteur Code
    code = CorrecteurCode([True, False, True], [True, True, False])
    code.afficher_resultat()

    # Test Correcteur Rédaction
    redaction = CorrecteurRedaction("Ceci est une rédaction qui contient les mots clés.", ["rédaction", "mots", "clés"])
    redaction.afficher_resultat()