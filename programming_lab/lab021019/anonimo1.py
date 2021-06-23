from math import sqrt


def positive_equation(a, b, c):
    return (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def negative_equation(a, b, c):
    return (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
