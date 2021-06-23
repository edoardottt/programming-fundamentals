from math import sqrt

# import math

a = float(input("side a: "))
b = float(input("side b: "))
c = sqrt(a ** 2 + b ** 2)
# c = (a**2 + b**2)**0.5
# c = math.sqrt(a**2 + b**2)
print("The hypotenuse of the triangle is long:", c)
print("The hypotenuse of the triangle is long:", (a ** 2 + b ** 2) ** 0.5)
