"""
Créer un fichier matchs.txt contenant :
Ali Sara 15 12
Omar Lina 8 20
Sara Omar 14 9
Lina Ali 18 11
Format : joueur1 joueur2 score1 score2
Travail demandé :
1. Lire le fichier.
2. Afficher le gagnant de chaque match.
3. Compter :
o le nombre total de matchs ;

o le nombre de victoires de chaque joueur.
4. Générer un fichier classement.txt.
"""

f=open(r"C:\Users\Administrateur\Documents\GitHub\Python\POO\TP8\EX2\matchs.txt","r")
#print(f.readlines())

#Q2
for l in f.readlines():
    g1,g2,s1,s2=l.split()
    #print(g1,g2,s1,s2)
    s1=int(s1)
    s2=int(s2)
    if s1>s2:
        print("le gagnant est",g1)
    elif s1<s2:
        print("le gagnant est",g2)
    else:
        print("egalite")