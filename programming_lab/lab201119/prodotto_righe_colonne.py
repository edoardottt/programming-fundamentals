#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:46:17 2019

@author: angelo
Scrivere una funzione che prende due matrici di numeri come liste di liste e ne calcola una terza che è il prodotto righe colonne.
"""

def prodotto_riga_colonna(A, i, B, j):
    riga = A[i]
    colonna = [r[j] for r in B]
    return sum([riga[i]*colonna[i] for i in range(len(riga))])


def prodotto_righe_colonne(A, B):
    if not len(A[0]) == len(B):
        raise Exception
    matrice = []
    for i in range(len(A)):
        riga = []
        for j in range(len(B[0])):
            riga.append(prodotto_riga_colonna(A, i, B, j))
        matrice.append(riga)
    return matrice