import albero


def es48(tree):
    if tree == None:
        return 0
    count = es48(tree.sx) + es48(tree.dx)
    if tree.sx is not None and tree.dx is not None:
        count += 1
    return count
