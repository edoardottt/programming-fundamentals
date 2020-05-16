#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:49:01 2019

@author: angelo
"""

def prendi_numeri():
    """ La funzione prende continuamente da tastiera una stringa, se la stringa è un numero allora stampa a video il suo quadrato, altrimenti non fa nulla. Esce dalla funzione quando l'utente inserisce la parola "fine" e ritorna il numero di quadrati calcolati.
    """
    conta_quadrati=0
    stringa = ''
    while stringa != 'fine':
        stringa = input("Inserisci la stringa")
        if stringa.isnumeric():
            print(int(stringa)**2)
            conta_quadrati = conta_quadrati+1
    return conta_quadrati




















