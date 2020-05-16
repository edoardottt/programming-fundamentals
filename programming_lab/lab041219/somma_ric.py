#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:44:28 2019

@author: angelo

Scrivere una funzione ricorsiva che fa la somma di tutti i numeri di una lista

es: somma_ric([1,2,3]) -> 6

caso base: la lista ha un solo elemento ->
            somma uguale l[0] (l'unico elemento)

caso ricorsivo: la lista ha n elementi:
    ritorn il primo elemento + la somma dei restanti
    n-1 elementi (return l[0] + somma_ric(l[1:]))

"""

def somma_ric(l):
    if len(l) == 1:
        return l[0]
    return l[0] + somma_ric(l[1:])



