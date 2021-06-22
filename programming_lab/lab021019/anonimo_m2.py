# Il programma non entra nelle due funzioni definite
a = float(input("Inserisci a "))
b = float(input("Inserisci b "))
c = float(input("Inserisci c "))

# non entra nella funzione
def x1(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    xx1 = (-b + delta) / (2 * a)
    print("La soluzione positiva è", xx1)
    return xx1


def x2(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** (1 / 2)
    xx2 = (-b - delta) / (2 * a)
    print("La soluzione negativa è", xx2)
    return xx2
