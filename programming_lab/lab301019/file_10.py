#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:25:54 2019

@author: angelo
Scriviamo una funzione che prende come parametro il nome di un file e ci stampa dentro tutti i numeri da 0 a 9 su righe diverse. Ritorna 0.
"""


def file_10(nomefile):
    f = open(nomefile, "w")
    stringa = ""
    for i in range(10):
        stringa += str(i) + "\n"
    f.write(stringa)
    f.close()
    return 0


def file_102(nomefile):
    f = open(nomefile, "w")
    for i in range(10):
        f.write(str(i) + "\n")
    f.close()
    return 0


def file_103(nomefile):
    with open(nomefile, "w") as f:
        lista = [str(i) + "\n" for i in range(10)]
        f.writelines(lista)
    return 0
