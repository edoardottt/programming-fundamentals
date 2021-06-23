# The program does not enter the two defined functions
a = float(input("insert a "))
b = float(input("insert b "))
c = float(input("insert c "))

# does not enter the function
def x1(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    xx1 = (-b + delta) / (2 * a)
    print("The positive solution is", xx1)
    return xx1


def x2(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    xx2 = (-b - delta) / (2 * a)
    print("The negative solution is", xx2)
    return xx2
