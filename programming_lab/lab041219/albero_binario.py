#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:25:58 2019

@author: angelo
Scrivere una funzione ricorsiva che conta il numero
di nodi di un albero.

"""

class Nodo:
    def __init__(self, v):
        self.valore = v
        self.sx = None
        self.dx = None

    def __str__(self, livello=0):
        risultato = ''
        if self.sx:
            risultato += '\n' + '\t'*livello + self.sx.__str__(livello+1)
        risultato += '\n' + '\t'*livello + f"{self.valore}"
        if self.dx:
            risultato += '\n' + '\t'*livello + self.dx.__str__(livello+1)
        return risultato


    def conta_nodi(self):
        if not self.sx and not self.dx:
            return 1
        c = 1
        if self.sx:
            c += self.sx.conta_nodi()
        if self.dx:
            c += self.dx.conta_nodi()
        return c


def conta_nodi(albero):
    """ caso base = None ritorn 0
        caso ricorsivo = ritorno 1 + il numero di figli di sx + il numero di figli di dx """
    if albero == None:
        return 0
    return 1 + conta_nodi(albero.sx) + conta_nodi(albero.dx)


def conta_nodi2(albero):
    """ caso base = nodo foglia -> ritorno 1
        caso ricorsivo = ritorno 1 + il numero di figli di sx + il numero di figli di dx
        """
    if not albero.sx and not albero.dx:
        return 1
    c = 1
    if albero.sx:
        c += conta_nodi(albero.sx)
    if albero.dx:
        c += conta_nodi(albero.dx)
    return c


def trova_massimo(albero):
    """ caso base: nodo foglia -> foglia.valore
        caso ricorsivo: albero con figlio sx e figlio dx
            ritorno il maggior fra foglia.valore e max(sx) e max(dx)
    """
    if not albero.sx and not albero.dx:
        return albero.valore
    m, m1, m2 = albero.valore, albero.valore, albero.valore
    if albero.sx:
        m1 = trova_massimo(albero.sx)
    if albero.dx:
        m2 = trova_massimo(albero.dx)
    return max(m, m1, m2)


def calcola_altezza(albero):
    """ La maggiore lunghezza del cammino dalla radice a una foglia

    caso base: nodo foglia: 0
    caso ricorsivo: 1 + altezza_massima fra figlio sx e figlio dx
    """
    if not albero.sx and not albero.dx:
        return 0
    m1, m2 = 0, 0
    if albero.sx:
        m1 = calcola_altezza(albero.sx)
    if albero.dx:
        m2 = calcola_altezza(albero.dx)
    return max(m1, m2) + 1





