#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:25:57 2019

@author: angelo

Scrivere una funzione che prende in input un nome di file di testo e restituisce un dizionario delle frequenze delle lettere ripetute consecutivamente nelle parole. Ogni riga del file deve essere considerata come una parola unica, ovvero gli spazi che dividono i caratteri di una stessa riga devono essere ignorati.
Le chiavi del dizionario sono le lettere ripetute e i valori sono il numero di volte che la lettera è ripetuta consecutivamente nella stringa.

esempio: il file esempio.txt contiene

casa a amalfi
azione estremizzata
ripasso organizzato
eeeeeeeeeeeeeeeee ee e e e
aabaabaabaa


il dizionario risultante sarà:
    {'a':5, 'e':2, 'z':2, 's':1, 'o':1}
"""

def frequenze_ripetute(fname):
    diz = {}
    with open(fname) as f:
        for riga in f:
            ultimo = ''
            riga=riga.replace(' ','')
            for indice, carattere in enumerate(riga[:-1]):
                if carattere == riga[indice+1]:
                    if carattere != ultimo:
                        diz[carattere] = diz.get(carattere,0) + 1
                        ultimo = carattere
                else:
                    ultimo = carattere
    return diz





