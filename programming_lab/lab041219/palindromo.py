#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:00:44 2019

@author: angelo

Scrivere una funzione ricorsiva paindromo che prende in ingresso una stringa e ritorna True se è un palindromo, False altrimenti

oro anna osso aveva ossesso ottetto
itopinonavevanonipoti

caso base: una lettera -> True
           due lettere -> True se le due lettere sono uguali

caso ricorsivo: parola[0] == parola[-1] and palindromo (parola[1:-1])

codice OPIS : BGFZSJXL

"""


def palindromo(parola):
    if len(parola) <= 1:
        return True
    return parola[0] == parola[-1] and palindromo(parola[1:-1])
