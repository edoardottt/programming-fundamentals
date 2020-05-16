#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:43:21 2019

@author: angelo

Scrivere una funzione che prende una stringa e restituisce un dizionario in cui le chiavi sono i caratteri presenti nella stringa e i valori il numero di volte che il corrispondente carattere è presente nella stringa.

es: conta_caratteri("pippo") ritorna il dizionario
{'p':3, 'i':1, 'o':1}
"""

def conta_caratteri(parola):
    d = dict()
    for carattere in parola:
        if carattere not in d:
            d[carattere] = 1
        else:
            d[carattere] += 1
    return d

def conta_caratteri2(parola):
    d = dict()
    for carattere in parola:
        conta = d.get(carattere, 0)
        d[carattere] = conta +1
    return d

def conta_caratteri3(parola):
    # Viene invocato un count per ogni carattere
    # Il costo è quadratico (ovvero len*len)
    d = dict()
    for carattere in parola:
        d[carattere] = parola.count(carattere)
    return d

# test con Beowulf (292951 caratteri):
#    %timeit conta_caratteri(a)
# 33.9 ms ± 723 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

#    %timeit conta_caratteri2(a)
# 44.1 ms ± 2.29 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

#    %timeit conta_caratteri3(a)
# 1min 42s ± 3 s per loop (mean ± std. dev. of 7 runs, 1 loop each)