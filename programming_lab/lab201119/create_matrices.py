#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:10:59 2019

@author: angelo

"""


def create_matrix_numbers(n, m):
    """the function constructs a matrix that has all numbers from 1 to n * m ordered by line e.g.:
        create_matrix_numbers(2, 4) return
        [[1,2,3,4],[5,6,7,8]]"""

    matrix = []
    row = []
    for i in range(1, n * m + 1):
        row.append(i)
        if i % m == 0:
            matrix.append(row)
            row = []
    return matrix


def create_array_numbers2(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(i * m + j + 1)
        matrix.append(row)
    return matrix


def create_array_numbers3(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(i * m + 1, i * m + m + 1):
            row.append(j)
        matrix.append(row)
    return matrix


def create_array_numbers4(n, m):
    return [[j for j in range(i * m + 1, i * m + m + 1)] for i in range(n)]
