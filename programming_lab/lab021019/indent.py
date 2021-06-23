x = 4
"""
Test equality ==
Test greater than >
Test lesser than<
Test greater than or equal >=
Test less than or equal <=
Test different !=
"""


def foo(a):
    if a > 0:
        print("a is positive")
    elif a < 0:
        print("a is negative")
    else:
        print("a is 0")


def foo2(a):
    if a > 0:
        print("a is positive")
    else:
        if a < 0:
            print("a is negative")
        else:
            print("a is 0")


def foo3(a):
    if a > 0:
        print("a is positive")
    if a < 0:
        print("a is negative")
    else:
        print("a is 0")


foo(7)
foo(-7)
