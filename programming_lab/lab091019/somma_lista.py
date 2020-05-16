#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:14:55 2019

@author: angelo
"""

def somma_lista(lista):
    somma = 0
    for elemento in lista:
        if type(elemento)==int:
            somma += elemento
    return somma