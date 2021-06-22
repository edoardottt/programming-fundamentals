#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:32:19 2019

@author: angelo
"""


class Nodo:
    def __init__(self, V, figli=[]):
        self.valore = V
        if len(figli) == 0:
            self.figli = []
        else:
            self.figli = figli


def trova_massimo(albero):
    max_rel = albero.valore
    for figlio in albero.figli:
        m = trova_massimo(figlio)
        if m > max_rel:
            max_rel = m
    return max_rel
