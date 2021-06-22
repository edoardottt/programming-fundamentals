#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:30:38 2019

@author: angelo

Scrivere una funzione che prende due matrici di numeri come liste di liste e ne calcola una terza che è il prodotto righe colonne.


C = A.B

cij = ai * bj -> prodotto "vettoriale"

ovvero a*b= a1*b1+a2*b2+a3*b3...

"""


def prod_vettori(x, y):
    """x = [1,2,3] y= [0,1,2]
    prot_vettori = 0 + 2 + 6 = 8"""
    return sum([x[i] * y[i] for i in range(len(x))])


def prod_righe_colonne(A, B):
    if len(A) != len(B[0]):
        raise Exception
    mat = []
    for i in range(len(A)):
        riga = []
        for j in range(len(B[0])):
            colonna_j_B = [B[k][j] for k in range(len(B))]
            #            colonna_j_B = [rigaB[j] for rigaB in B]
            riga.append(prod_vettori(A[i], colonna_j_B))
        mat.append(riga)
    return mat


def matrice_piena(nrighe, ncolonne):
    """Questa funzione crea una matrice con nrighe e ncolonne contenente tutti i numeri da 1 a nrighe*ncolonne"""
    mat = []
    for i in range(nrighe):
        riga = []
        for j in range(ncolonne):
            riga.append(1 + j + ncolonne * i)
        mat.append(riga)
    return mat
