fl1 = float(input("Enter the value 1: "))
fl2 = float(input("Enter the value 2: "))
fl3 = float(input("Enter the value 3: "))


def x1x2(a, b, c):
    x1 = -fl2 + ((fl2 ** 2 - 4 * fl1 * fl3) ** (1 / 2)) / (2 * a)
    x2 = -fl2 - ((fl2 ** 2 - 4 * fl1 * fl3) ** (1 / 2)) / (2 * a)
    return x1, x2


print(x1x2(fl1, fl2, fl3))
