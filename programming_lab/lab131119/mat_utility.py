#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:39:49 2019

@author: angelo
Scrivere delle funzioni di utility sulle matrici. Ovvero:
    - get_riga (A, i)
    - get_colonna (A, i)
    - get_diagonale (A) se esiste (ovvero la matrice è quadrata), 0 altrimenti
    esempio:
        [[5, 7, 2, -3], [-1, 5, 4, 0], [2, -1, 7, 3], [5,2,1,6]]

        5  7  2  -3
   A   -1  5  4  0
        2 -1  7  3
        5  2  1  6

get_riga(A, 2)-> [2, -1, 7, 3]
get_colonna(A,2) -> [2, 4, 7, 1]
get_diagonale(A) -> [5, 5, 7, 6]

per casa:
    prod_scalare(c, A)
    es: prod_scalare(3,A)-> [[15, 21, 6, -9], [-3, 15, 12, 0], [6, -3, 21, 9], [15,6,3,18]]

    prod_vettore_matrice(v,A)
    es: prod_vettore_matrice([1,0,-1,0], A) -> [[5, 0, -2, 0], [-1, 0, -4, 0], [2, 0, -7, 0], [5, 0, -1, 0]]

    somma_matrici(A,B)
    C=A+B c[i][j] = A[i][j]+B[i][j]

    prod_matrici(A,B)
    C=A*B  c[i][j] = get_riga(A,i)  get_riga(B,j) -> wikipedia
"""
from check_mat import check_mat


def get_riga(A, i):
    if not check_mat(A) or not (0 <= i <= len(A)):
        return 0
    return A[i]


def get_colonna(A, i):
    if not check_mat(A) or not (0 <= i <= len(A[0])):
        return 0
    return [A[j][i] for j in range(len(A))]


def get_diagonale(A):
    if not check_mat(A) or len(A) != len(A[0]):
        return 0
    return [A[j][j] for j in range(len(A))]
