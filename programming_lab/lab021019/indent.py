x = 4
"""
Test uguaglianza ==
Test maggiore >
Test minore <
Test maggiore o uguale >=
Test minore o uguale <=
Test diverso !=
"""


def foo(a):
    if a > 0:
        print("a e' positivo")
    elif a < 0:
        print("a e' negativo")
    else:
        print("a e' 0")


def foo2(a):
    if a > 0:
        print("a e' positivo")
    else:
        if a < 0:
            print("a e' negativo")
        else:
            print("a e' 0")


def foo3(a):
    if a > 0:
        print("a e' positivo")
    if a < 0:
        print("a e' negativo")
    else:
        print("a e' 0")


foo(7)
foo(-7)
