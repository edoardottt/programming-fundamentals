#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:48:05 2019

@author: angelo

Scrivere una funzione che prende come argomento una stringa contenente parole separate da spazi e ritorna un dizionario in cui le chiavi sono le vocali presenti nella stringa e i valori associati ad ogni chiave sono una lista con le parole che contengono quella chiave.

es: "il lupo ulula" {'i':['il'], 'u':['lupo','ulula'], 'a':['ulula'], 'o':['lupo']}
"""

def vocali_in_parole(S):
    diz = {vocale:[] for vocale in 'aeiou'}
    for vocale in diz:
        for parola in S.split():
            if vocale in parola:
                diz[vocale].append(parola)
    l = []
    for vocale, lista in diz.items():
        if lista == []:
            l.append(vocale)
    for vocale in l:
        del diz[vocale]
    return diz

def vocali_in_parole2(S):
    diz = {}
    for vocale in 'aeiou':
        for parola in S.split():
            if vocale in parola:
                diz[vocale] = diz.get(vocale, []) + [parola]
#                if vocale not in diz:
#                    diz[vocale] = [parola]
#                else:
#                    diz[vocale].append(parola)
    return diz

vocali_in_parole2("il lupo ulula")
