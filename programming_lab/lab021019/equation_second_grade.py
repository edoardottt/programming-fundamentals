a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("enter c: "))
delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)
print("The positive solution of the equation {}x^2+{}x+{}=0 is".format(a, b, c), x1)
print("The negative solution of the equation {}x^2+{}x+{}=0 is".format(a, b, c), x2)
