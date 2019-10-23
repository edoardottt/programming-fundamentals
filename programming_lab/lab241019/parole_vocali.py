#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:31:48 2019

@author: angelo
Scrivere una funzione che prende una stringa di parole separate da spazi e ritorna un dizionario in cui le chiavi sono le vocali dell'alfabeto presenti nella stringa di parole. I valori associati alle chiavi sono liste con le parole della stringa originaria che contengono quella vocale.

es: "odio et amo" {'o':['odio','amo'], 'i':['odio'], 'e':['et'], 'a':['amo']}
"""

def parole_vocali(s):
    diz = {}
    parole = s.split()
    for parola in parole:
        for vocale in 'aeiou':
            if vocale in parola:
                if vocale in diz:
                    diz[vocale].append(parola)
                else:
                    diz[vocale] = [parola]
    return diz


def parole_vocali2(s):
    diz = {}
    parole = s.split()
    for parola in parole:
        for vocale in 'aeiou':
            if vocale in parola:
                diz[vocale] = diz.get(vocale, []) + [parola]
    return diz

parole_vocali("odio et amo aaaaaaaa")


