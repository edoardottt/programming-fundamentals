#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:21:23 2019

@author: angelo
"""


def museo(studenti, biglietto_pieno):
    """Scrivere una funzione che dati in ingresso il costo del biglietto per visitare un museo e il numero di studenti di una classe in gita scolastica, ritorna la spesa totale, considerando che se gli studenti sono compresi fra 10 e 30 il biglietto per studente costa il 20% in meno, se sono 31 o più il 30% in meno."""
    if studenti < 10:
        totale = studenti * biglietto_pieno
    elif studenti <= 30:
        totale = (studenti * biglietto_pieno) * 0.8
    else:
        totale = (studenti * biglietto_pieno) * 0.7
    return totale
