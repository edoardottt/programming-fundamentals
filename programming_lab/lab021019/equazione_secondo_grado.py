a = float(input("Dammi a: "))
b = float(input("Dammi b: "))
c = float(input("Dammi c: "))
delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)
print("La soluzione positiva dell'equazione {}x^2+{}x+{}=0 e'".format(a, b, c), x1)
print("La soluzione negativa dell'equazione {}x^2+{}x+{}=0 e'".format(a, b, c), x2)
