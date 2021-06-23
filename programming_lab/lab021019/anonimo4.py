a = float(input("insert a"))
b = float(input("insert b"))
c = float(input("insert c"))


def calculate_x1(a, b, c):
    print("id of a:", id(a))
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x1


def calculate_x2(a, b, c):
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return x2


print(x1, x2)
