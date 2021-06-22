a = float(input("Dammi a: "))
b = float(input("Dammi b: "))
c = float(input("Dammi c: "))
delta = b ** 2 - 4 * a * c


def x1(a1, b1, c1, delta1):
    xx1 = (-b + (delta ** (1 / 2))) / (2 * a)
    return xx1


def x2(a1, b1, c1, delta1):
    xx2 = (-b - (delta ** (1 / 2))) / (2 * a)
    return xx2


print(x1(a, b, c, delta), x2(a, b, c, delta))
