a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
c = int(input("enter the value of c"))


def calculate_x1(a, b, c):
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x1


def calculate_x2(a, b, c):
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x2


calculate_x1(a, b, c)
calculate_x2(a, b, c)
print(x1, x2, sep=",")
