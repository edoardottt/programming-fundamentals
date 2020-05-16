#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:26:37 2019

@author: angelo
Scrivere una funzione che prende come argomento una stringa contenente parole separate da spazie e ritorna un dizionario in cui le chiavi sono le lunghezze delle parole e i valori quante parole di quella lunghezza sono presenti nella stringa in ingresso.

es: "tanti baci a tutti" {1:1, 4:1, 5:2}
"""
from frequenze import S

def frequenza_lunghezze(s):
    parole = s.split()
    diz = {}
    for parola in parole:
        if len(parola) not in diz:
            diz[len(parola)] = 1
        else:
            diz[len(parola)] += 1
    return diz

def frequenza_lunghezze2(s):
    parole = s.split()
    diz = {}
    for parola in parole:
        diz[len(parola)] = diz.get(len(parola), 0) + 1
    return diz

