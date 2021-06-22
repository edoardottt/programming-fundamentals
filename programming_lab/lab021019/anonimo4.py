a = float(input("inserire a"))
b = float(input("inserire b"))
c = float(input("inserire c"))


def calocolare_x1(a, b, c):
    print("id di a:", id(a))
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x1


def calcolare_x2(a, b, c):
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x2


print(x1, x2)
