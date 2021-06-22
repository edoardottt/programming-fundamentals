#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:42:28 2019

@author: angelo
"""


def conta_vocali():
    """La funzione prende continuamente da tastiera una stringa finché l'utente non inserisce la lettera 'z' e restituisce il numero di stringhe inserite corrispondenti a vocali (indipendentemente dalle maiuscole)"""
    contatore = 0
    s = ""
    while s != "z":
        s = input("Inserisci la stringa: ")
        if s in "aeiouAEIOU" and len(s) == 1:
            contatore = contatore + 1
    return contatore
