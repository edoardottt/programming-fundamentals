def foo(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print("the positive solution of the equation {}x^2+{}x+{}=0 is:".format(a, b, c), x1)
    print("the negative solution of the equation {}x^2+{}x+{}=0 is:".format(a, b, c), x2)
    return x1, x2


foo(1, -5, 6)
