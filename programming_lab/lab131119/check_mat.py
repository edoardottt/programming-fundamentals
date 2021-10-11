#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:37:38 2019

@author: angelo
Write a function that takes an argument and tests if the argument is an array of numbers.

In particular:
    - has all rows of the same size
    - has all the numerical elements

"""


def check_mat(m):
    if type(m) != list:
        return False
    if len(m) == 0 or type(m[0]) != list:
        return False
    column = len(m[0])
    for row in m:
        if type(row) != list or len(row) != column:
            return False
        for l in row:
            if not isinstance(l, (int, float)):
                return False
    return True


if __name__ == "__main__":
    A = [[5, 7, 2, -3], [-1, 5, 4, 0], [2, -1, 7, 3]]
    print(check_mat(A))

    B = [[5, 7, 2, -3], [-1, 5, 4, 0], [2, -1, 7]]
    print(check_mat(B))

    C = [[5, 7, 2, " "], [-1, 5, 4, 0], [2, -1, 7]]
    print(check_mat(C))

    print(check_mat([4, 5, 6]))
