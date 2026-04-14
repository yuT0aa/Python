while True:
    moy=input("saisir une valeur : ")
    if '.' in moy:
        l=moy.split('.')
        if l[0].isdigit() and l[1].isdigit():
            moy=float(moy)
            if moy>=0 and moy<=20:
                break
    elif moy.isdigit():
           moy=float(moy)   
        
           if moy in range(0,21):
                break
print(moy)