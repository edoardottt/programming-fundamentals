#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:39:49 2019

@author: angelo
Write utility functions on arrays. That is to say:
    - get_row (A, i)
    - get_column (A, i)
    - get_diagonal (A) if it exists (i.e. the matrix is ​​square), 0 otherwise
    example:
        [[5, 7, 2, -3], [-1, 5, 4, 0], [2, -1, 7, 3], [5,2,1,6]]

        5  7  2  -3
   A   -1  5  4  0
        2 -1  7  3
        5  2  1  6

get_row(A, 2)-> [2, -1, 7, 3]
get_column(A,2) -> [2, 4, 7, 1]
get_diagonal(A) -> [5, 5, 7, 6]

per casa:
    prod_scalare(c, A)
    ex: prod_scalare(3,A)-> [[15, 21, 6, -9], [-3, 15, 12, 0], [6, -3, 21, 9], [15,6,3,18]]

    prod_vector_matrix(v,A)
    ex: prod_vector_matrix([1,0,-1,0], A) -> [[5, 0, -2, 0], [-1, 0, -4, 0], [2, 0, -7, 0], [5, 0, -1, 0]]

    sum_matrices(A,B)
    C=A+B c[i][j] = A[i][j]+B[i][j]

    prod_matrici(A,B)
    C=A*B  c[i][j] = get_row(A,i)  get_row(B,j) -> wikipedia
"""
from check_mat import check_mat


def get_row(A, i):
    if not check_mat(A) or not (0 <= i <= len(A)):
        return 0
    return A[i]


def get_column(A, i):
    if not check_mat(A) or not (0 <= i <= len(A[0])):
        return 0
    return [A[j][i] for j in range(len(A))]


def get_diagonal(A):
    if not check_mat(A) or len(A) != len(A[0]):
        return 0
    return [A[j][j] for j in range(len(A))]
