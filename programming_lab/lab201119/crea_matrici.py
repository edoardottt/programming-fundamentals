#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:10:59 2019

@author: angelo

"""


def crea_matrice_numeri(n, m):
    """la funzione costruisce una matrice che ha tutti i numeri da 1 a n*m ordinati per riga
    es.:
        crea_matrice_numeri(2, 4) ritorna
        [[1,2,3,4],[5,6,7,8]]"""

    matrice = []
    riga = []
    for i in range(1, n * m + 1):
        riga.append(i)
        if i % m == 0:
            matrice.append(riga)
            riga = []
    return matrice


def crea_matrice_numeri2(n, m):
    matrice = []
    for i in range(n):
        riga = []
        for j in range(m):
            riga.append(i * m + j + 1)
        matrice.append(riga)
    return matrice


def crea_matrice_numeri3(n, m):
    matrice = []
    for i in range(n):
        riga = []
        for j in range(i * m + 1, i * m + m + 1):
            riga.append(j)
        matrice.append(riga)
    return matrice


def crea_matrice_numeri4(n, m):
    return [[j for j in range(i * m + 1, i * m + m + 1)] for i in range(n)]
