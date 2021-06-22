#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:31:34 2019

@author: angelo
Scrivere una funzione ricorsiva somma_lista_pari che
ritorna la somma di tutti i numeri pari della lista

somma_pari([1,2,3,4]) = se(1=pari:1 else 0) + somma([2,3,4]) = ... se(2=pari:2 else 0) + somma([3,4])
somma([]) = 0
=
CODICE OPIS 57S6HE9N
"""


def somma_lista_pari(l):
    if l == []:
        return 0
    somma_parziale = somma_lista_pari(l[1:])
    # Modulo 2 ritorna 1 (ovvero True) se dispari
    if l[0] % 2:
        return somma_parziale
    return l[0] + somma_parziale
