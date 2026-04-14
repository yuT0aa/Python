from SRC.Mesclasses import Cercle
import math

O = [0, 0]
r = 5
cercle = Cercle(O, r)

print("Surface du cercle:", cercle.Surface())
print("Perimetre du cercle:", cercle.Perimetre())

A = [3, 4]
print(cercle.testAppartenance(A))