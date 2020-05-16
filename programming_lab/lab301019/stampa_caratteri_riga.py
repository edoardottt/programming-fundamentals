#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:26:42 2019

@author: angelo
Scrivere una funzione che prende una stringa che è il nome di un file e stampa il numero di caratteri trovati in ogni riga, escluso il carattere di fine riga """

def stampa_caratteri_riga(nomefile):
    with open(nomefile) as f:
        for line in f:
            print(len(line.rstrip('\n')))


