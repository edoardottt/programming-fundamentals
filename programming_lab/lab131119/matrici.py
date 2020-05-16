#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:23:44 2019

@author: angelo

Scrivere una funzione che prende una lista e verifica se la lista può essere considerata una matrice di numeri (int oppure float).

Nello specifico: il numero di elementi di ogni riga deve essere lo stesso per ogni riga.
"""

def check_matrix(A):
    colonne = len(A[0])
    for riga in A:
        if len(riga) != colonne:
            return False
        for elemento in riga:
#            if type(elemento) != float and type(elemento) != int:
#                return False
            if not isinstance(elemento, (int, float)):
                return False
    return True

def prod_scalare(s, A):
    """ ritorna la matrice risultante dal prodotto della matrice A per lo scalare s
    es:
        s = 4
        A = [[1,2,3],[4,5,6]]

        A' = [[4,8,12],[16,20,24]]
    """
    nuova_matrice = []
    for riga in A:
        nuova_riga = [s*el for el in riga]
#        for elemento in riga:
#            nuova_riga.append(s*elemento)
        nuova_matrice.append(nuova_riga)
    return nuova_matrice

def prod_vettore_matrice(v, A):
    """ ritorna la matrice risultante dal prodotto della matrice A per lo il vettore v
    es:
        v = [4, 2, 1]
        A = [[1,2,3],[4,5,6]]

        A' = [[4,4,3],[16,10,6]]
    """
    nuova_matrice = []
    for riga in A:
        nuova_riga = [riga[i]*v[i] for i in range(len(riga))]
#        for indice in range(len(riga)):
#            nuova_riga.append(A[indice] * v[indice])
        nuova_matrice.append(nuova_riga)
    return nuova_matrice



def somma_matrici(A, B):
    """ ritorna la matrice risultante dalla somma delle matrici
    nb: l'elemento i,j sarà A[i,j]+B[i,j]

    """
    nuova_matrice = []
    for indice_riga in range(len(A)):
        nuova_riga = [A[indice_riga][i]+B[indice_riga][i] for i in range(len(A[indice_riga]))]
#        for indice_colonna in range(len(A[indice_riga])):
#            nuova_riga.append(A[indice_riga][indice_colonna] + B[indice_riga][indice_colonna])
        nuova_matrice.append(nuova_riga)
    return nuova_matrice

def prodotto_matrici (A,B):
    """ da fare a casa """

if __name__=='__main__':
    A = [[5, 6, 7], [3, 6, 1], [9, -1, -2], [1.3,5,-0.5]]
    print(check_matrix(A))

    B = [[5, 6, 7], [3, 6, 1], [9, -1, -2], [1.3,5,"-0.5"]]
    print(check_matrix(B))

    C = [[5, 6, 7], [3, 6, 1], [9, -1, -2], [1.3,5,"-0.5"],[5,6]]
    print(check_matrix(C))




