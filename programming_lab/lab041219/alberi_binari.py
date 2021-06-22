#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:21:47 2019

@author: angelo
"""


class NodoBinario:
    def __init__(self, V, SX=None, DX=None):
        self.valore = V
        self.sx = SX
        self.dx = DX

    def __str__(self, livello=0):
        risultato = ""
        if self.sx:
            risultato += "\n" + "\t" * livello + self.sx.__str__(livello + 1)
        risultato += "\n" + "\t" * livello + f"{self.valore}"
        if self.dx:
            risultato += "\n" + "\t" * livello + self.dx.__str__(livello + 1)
        return risultato


def altezza(albero):
    """Funzione che prende un albero binario e ritorna
    l'altezza dell'albero, ovvero la più lunga distanza
    di una foglia dalla radice"""

    if not albero.sx and not albero.dx:
        return 0
    alt, alt2 = 0, 0
    if albero.sx:
        alt = altezza(albero.sx)
    if albero.dx:
        alt2 = altezza(albero.dx)
    if alt > alt2:
        return alt + 1
    else:
        return alt2 + 1


def trova_massimo(albero):
    """Funzione che prende un albero binario e ritorna il
    valore massimo dell'albero"""
    if not albero.sx and not albero.dx:
        return albero.valore
    m1, m2 = albero.valore, albero.valore
    if albero.sx:
        m1 = trova_massimo(albero.sx)
    if albero.dx:
        m2 = trova_massimo(albero.dx)
    return max(m1, m2, albero.valore)
