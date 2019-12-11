#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:44:29 2019

@author: angelo
"""

class Nodo:
    def __init__(self, v):
        self.valore = v
        self.figli = []

def conta_nodi(albero):
    """ Caso base: foglia -> albero.figli == [] -> 1
    Caso ricorsivo:  somma(conta_nodi for figlio in figli)  +1
    """
    if albero.figli == []:
        return 1
    nodi = 1
    for figlio in albero.figli:
        nodi += conta_nodi(figlio)
    return nodi


