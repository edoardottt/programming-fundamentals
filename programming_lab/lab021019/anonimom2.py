# non entra nella funzione
def x1(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    xx1 = (-b + delta) / (2 * a)
    return xx1


def x2(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    xx2 = (-b - delta) / (2 * a)
    return xx2


print(x1(1, 5, 9))
