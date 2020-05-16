#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:49:25 2019

@author: angelo
Scrivere una funzione che prende una stringa che è il nome di un file, e ritorna la vocale che è presente più volte su una stessa riga del file

Es: se il file contiene
 buffo
 papa
 richiami

 ritorna 'i'
"""

def vocale_massima(nomefile):
    ripvoc = 0
    voc =''
    with open(nomefile) as f:
        for line in f:
            for v in 'aeiou':
                cont = line.count(v)
                if cont > ripvoc:
                    ripvoc = cont
                    voc = v
    return voc
