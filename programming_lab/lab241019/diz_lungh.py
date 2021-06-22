#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:20:20 2019

@author: angelo
Scrivere una funzione che prende una stringa di parole separate da spazi e ritorna un dizionario in cui la chiave è il numero di lettere e il valore è il numero di parole della stringa che hanno un numero di lettere pari alla chiave

es: "pippo re ciao asdrubale te" {2:2, 4:1, 5:1, 9:1}
"""


def diz_lungh(s):
    diz = {}
    lista = s.split()
    for parola in lista:
        lung_parola = len(parola)
        if not lung_parola in diz:
            diz[lung_parola] = 1
        else:
            diz[lung_parola] = diz[lung_parola] + 1
    return diz


def diz_lungh2(s):
    diz = {}
    for parola in s.split():
        diz[len(parola)] = diz.get(len(parola), 0) + 1
    return diz
