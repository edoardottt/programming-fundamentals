from math import sqrt


def equazione_positiva(a, b, c):
    return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def equazione_negativa(a, b, c):
    return (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
