#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:30:33 2019

@author: angelo
"""

def estrai_pari(lista):
    """ Prende una lista di interi e restituisce una NUOVA lista con solo gli elementi pari della lista presa """
    nuova_lista = []
    for elemento in lista:
        if elemento % 2 == 0:
            nuova_lista.append(elemento)
    return nuova_lista

