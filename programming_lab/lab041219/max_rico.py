#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:46:22 2019

@author: angelo


Scrivere una funzione ricorsiva che prende una lista di numeri
e ritorna il numero maggiore

def max_rico([1,2,3,4]) -> 4

[1,2,3,4] = [1] + [2,3,4]
l = l[0] + l[1:]

max_rico(l) = l[0] > max_rico(l[1:])

max_rico(1,2,3,4) = 1 > max([2,3,4]) ?
max([2,3,4]) =      2 > max([3,4]) ?
max([3,4]) =        3 > max([4]) ?
max([4]) =          4 !!!!
"""


def max_rico(l):
    if len(l) == 1:
        return l[0]

    massimo_relativo = max_rico(l[1:])

    if l[0] > massimo_relativo:
        return l[0]
    return massimo_relativo
