#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:37:38 2019

@author: angelo
Scrivere una funzione che prende un argomento e verifica se l'argomento è una matrice di numeri.

Nello specifico:
    - ha tutte le righe della stessa dimensione
    - ha tutti gli elementi numerici

"""


def check_mat(m):
    if type(m) != list:
        return False
    if len(m) == 0 or type(m[0]) != list:
        return False
    colonne = len(m[0])
    for riga in m:
        if type(riga) != list or len(riga) != colonne:
            return False
        for el in riga:
            if not isinstance(el, (int, float)):
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
