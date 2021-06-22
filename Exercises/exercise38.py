#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:53:23 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

from untitled0 import check_matrix


def get_riga(A, i):
    if check_matrix(A) and 0 < i < len(A) - 1:
        return A[i]
    else:
        return 0


def get_colonna(A, i):
    if check_matrix(A) and 0 < i < len(A[0]) - 1:
        return [A[j][i] for j in range(len(A))]
    else:
        return 0


def get_diagonale(A):
    if check_matrix(A) and (len(A) == len(A[0])):
        return [A[i][i] for i in range(len(A))]
    else:
        return 0


A = [[5, 7, 2, -3], [-1, 5, 4, 0], [2, -1, 7, 3], [5, 2, 1, 6]]

riga2 = get_riga(A, 2)
colonna2 = get_colonna(A, 2)
diagonale = get_diagonale(A)

print(riga2)
print(colonna2)
print(diagonale)
