#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende come argomento una stringa contenente una serie di parole (sequenze di caratteri separate da spazi bianchi, tabulazioni o a capo) e un intero e ritorna il numero di parole presenti nella stringa che hanno una lunghezza esattamente pari all'intero preso come argomento

esempio: conta_parole("a e i o u", 1) ritorna 5
         conta_parole("asd bip casa", 3) ritorna 2
         conta_parole('ciao
                  pippo



                  pluto', 4) ritorna 1
"""

def conta_parole(stringa, lunghezza):
    lista = stringa.split()
    c = 0
    for parola in lista:
        if len(parola) == lunghezza:
            c = c+1
    return c