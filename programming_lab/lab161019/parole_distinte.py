#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:26:08 2019

@author: angelo

Scrivere una funzione che prende una stringa di parole separate da spazi in ingresso e restituisce l'insieme delle parole distinte. La stringa deve essere anche ripulita di tutti i segni di interpunzione (ovvero virgole, punti, punti esclamativi, punti interrogativi, punti e virgola, due punti, apostrofi, virgolette)

esempio: "ciao ciao se beccamo" {"ciao","se","beccamo"}
"""


def parole_distinte(stringa):
    s = set()
    stringa = stringa.replace("'", " ")
    for parola in stringa.split():
        parola = parola.strip(",.!?;:'\"")
        s.add(parola)
    return s
