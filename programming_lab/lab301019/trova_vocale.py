#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:44:03 2019

@author: angelo
Scrivere una funzione che prende un nome di un file e restituisce la vocale che si ripete il maggior numero di volte su una stessa riga nel file. Se ci sono vocali che si ripetono lo stesso numero di volte, ritorna la prima individuata.

es:
    rotto
    topo
    missili

    ritorna i
"""


def trova_vocale(filename):
    with open(filename) as f:
        maxvoc = 0
        voc = ""
        for riga in f:
            for vocale in "aeiou":
                cont = riga.count(vocale)
                if cont > maxvoc:
                    voc = vocale
                    maxvoc = cont
    return voc


trova_vocale("testa_vocali.txt")
