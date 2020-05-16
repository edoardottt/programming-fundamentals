#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:37:03 2019

@author: angelo

Scrivere una funzione RICORSIVA che prende una lista e ritorna
la lista originaria invertita come una nuova lista

es: inverti_lista([1,2,3]) -> [3,2,1]


[1] -> [1]
[1,2] = [1]+[2]
[1,2,3] = [1] + ([2,3])
inverti([2,3]) = inverti([2]) + [3]
inverti([2]) = inverti([]) + [2]
inverti([]) = []
[1,2,3,4] = [1] + [2,3,4] -> inversione([2,3,4]) + [1]
inversione [2,3,4] = [4,3,2] + [1] -> [4,3,2,1]
inversione ([2] + [3,4]) = inversione([3,4]) + [2]

"""

def inverti_lista(l):
    if len(l) <=1:
        return l

    return inverti_lista(l[1:]) + [l[0]]







