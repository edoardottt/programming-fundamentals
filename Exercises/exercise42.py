# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:04:24 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a matrix of numbers as list of lists and
it returns True if the matrix is symmetric, False otherwise.
"""
m = [[1, 2, 3], [2, 1, 2], [3, 2, 1]]


def is_symm(m):
    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        for j in range(cols):
            if m[i][j] != m[j][i]:
                return False
    return True


print(is_symm(m))
