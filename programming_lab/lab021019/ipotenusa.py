from math import sqrt
# import math

a = float(input("Cateto a: "))
b = float(input("Cateto b: "))
c = sqrt(a**2 + b**2)
# c = (a**2 + b**2)**0.5
# c = math.sqrt(a**2 + b**2)
print("L'ipotenusa del triangolo e' lunga:", c)
print("L'ipotenusa del triangolo e' lunga:", (a**2 + b**2)**0.5)
