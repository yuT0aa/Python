nombres = [5, 12, 7, 20, 3, 18] 

"""
1. Trouver le plus petit nombre. 
2. Filtrer les nombres supérieurs à 10. 
3. Multiplier chaque nombre par 2. 
4. Vérifier si tous les nombres sont positifs.
"""
#1
print(min(nombres))
print("*"*30)

#2
superieurs_10=[s for s in nombres if s>10]
print(superieurs_10)
print("*"*30)

#3
multi_2=[s*2 for s in nombres]
print(multi_2)
print("*"*30)

#4
for s in nombres:
    if s>0:
        print("true")
        break